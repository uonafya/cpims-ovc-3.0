import csv
import time
import collections
import zipfile
import datetime
import pandas as pd
from os.path import basename

from django.http import FileResponse
from django.db import connection

from django.http import StreamingHttpResponse
from django.forms.models import model_to_dict

from cpovc_registry.models import RegOrgUnit
from .models import Registrations
from .functions import get_lips

from django.conf import settings
from .downloads import QUERIES, QNAMES

MEDIA_ROOT = settings.MEDIA_ROOT


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def generate_output_files(request):
    """A view that streams a large CSV file."""
    rows = []
    qs = RegOrgUnit.objects.raw("SELECT * FROM reg_org_unit order by id LIMIT 10")
    for q in qs:
        rows.append(model_to_dict(q))
    pseudo_buffer = Echo()
    fields = list(rows[0].keys())
    writer = csv.DictWriter(pseudo_buffer, fieldnames=fields)   
    # writer.writeheader()
 
    header = dict(zip(fields, fields))
    all_rows = [header] + rows
    return StreamingHttpResponse(
        (writer.writerow(row) for row in all_rows),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="Dataset.csv"'},
    )


def generate_output_file(request):
    """A view that streams a large CSV file."""
    try:
        results = {}
        start_time = time.time()
        file_type = int(request.POST.get('file_type', 1))
        data_set = int(request.POST.get('data_set'))
        sel_period = int(request.POST.get('sel_period'))
        sel_year = int(request.POST.get('sel_year'))
        sel_funding = request.POST.get('sel_funding')
        sel_ip = request.POST.get('sel_ip')
        sel_lip = request.POST.get('sel_lip')
        # Queries
        dates = get_dates(sel_period, sel_year)
        start_date = dates['start_date']
        end_date = dates['end_date']
        query = QUERIES[data_set]
        query += " WHERE r_period = %d AND r_year = %d " % (sel_period, sel_year)
        # More filters
        if sel_ip:
            sel_lips = []
            lips = get_lips(sel_ip)
            for lip in lips:
                sel_lips.append(str(lip.org_unit_id))
            lip_ids = ','.join(sel_lips)
            query += " AND cbo_id IN (%s)" % lip_ids
        if sel_lip:
           query += " AND cbo_id IN (%s)" % sel_lip
        rows = []
        fields = []
        print(query)
        with connection.cursor() as cursor:
            cursor.execute(query)
            desc = cursor.description
            fields, rows = dictfetchall(cursor)
        ts = int(time.time())
        dts = QNAMES[data_set]
        fname = 'RawData.%s.%s-%s.%s' % (request.user.id, data_set, dts,ts)
        csv_file_name = '%s/csv/%s.csv' % (MEDIA_ROOT, fname)
        with open(csv_file_name, 'w', newline='') as csvfile:
            obj = csv.DictWriter(csvfile, fieldnames=fields)      
            obj.writeheader()      
            for row in rows:
                obj.writerow(row)
        rcds = '{:,}'.format(len(rows))
        end_time = time.time()
        tt = int(end_time - start_time)
        minutes, seconds = divmod(tt, 60)
        mt = '%s minutes, %s seconds' % (minutes, seconds)
        results['title'] = fname
        results['desc'] = fname
        results['rows'] = rcds
        results['records'] = len(rows)
        results['time'] = mt
    except Exception as e:
        print('Error - %s' % (str(e)))
        return {}
    else:
        return results


def get_data(request, fname, file_type='csv'):
    """Method to get data."""
    try:
        csv_file_name = '%s/csv/%s.csv' % (MEDIA_ROOT, fname)
        xls_file_name = '%s/xlsx/%s.xlsx' % (MEDIA_ROOT, fname)
        # Dataframe for writing to Excel
        df = pd.read_csv(csv_file_name, low_memory=False)

        if file_type == 'xlsx':
            df.to_excel(xls_file_name, index=None, sheet_name='Raw data')
            file_name = xls_file_name
        
        elif file_type == 'zip':
            zip_file_name = '%s/zip/%s.zip' % (MEDIA_ROOT, fname)
            file_name = zip_file_name
            with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.write(csv_file_name, basename(csv_file_name))
        else:
            file_name = csv_file_name

        response = FileResponse(open(file_name, "rb"), as_attachment=True)
        response['Accept-Ranges'] = 'bytes'

    except Exception as e:
        print('Error - %s' % (str(e)))
        return None
    else:
        return response



def get_dates(prd, yr):
    """Method to get dates based on Reporting period and FY."""
    try:
        dates = {}
        int_yr = int(yr)
        today = datetime.date.today()
        year = today.strftime('%Y')
        mwezi = today.strftime('%m')
        w_year = int(year) if int_yr == 0 else int_yr
        mwaka = (w_year + 1) if int(mwezi) > 9 else w_year
        emonth = '03' if int(prd) == 2 else '09'
        start_date = '%d-10-01' % (w_year)
        end_date = '%d-%s-30' % (mwaka, emonth)
        dates['start_date'] = start_date
        dates['end_date'] = end_date
        # Flat tables filters
        dates['r_period'] = int(prd)
        dates['r_year'] = int(yr)
    except Exception as e:
        print('Get dates error - %s' % (str(e)))
        raise e
    else:
        return dates


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return columns, rows
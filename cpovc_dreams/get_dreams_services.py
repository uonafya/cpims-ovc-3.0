import csv
import uuid
import requests

base_url = 'http://dreams.healthstrat.co.ke'
token = '969f3a31e01d6d03998bdd4d3592ea3a5e2c3a59'
headers = {'Authorization': 'Token %s' % token}


def get_dreams(dreams_id):
    """Method to login to get key details."""
    try:
        url = '%s/api/client-api/?dreams_id=%s' % (base_url, dreams_id)
        r = requests.get(url, headers=headers)
        # print(r.headers)
    except Exception as e:
        print('Error from DREAMS' % str(e))
        return []
    else:
        if r.status_code == 200:
            return r.json()
        else:
            return []


if __name__ == '__main__':
    ou_id = 7226
    # print(' _ ' * 60)
    dtts = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
        'intervention_id', 'org_unit_id', 'dreams_id', 'date_of_birth',
        'birth_certificate_no', 'county_code', 'county_name',
        'sub_county_code', 'sub_county_name',
        'ward_code', 'ward_name', 'intervention_date',
        'intervention_type_code', 'intervention_type_name',
        'hts_result', 'no_of_sessions_attended', 'pregnancy_test_result',
        'timestamp_created', 'is_void')
    print(dtts)

    # Read the csv for the IDs
    with open('csv/DREAMS_NYM.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            dreams_id = row[0]
            # dreams_id = '2/1162/3'
            payload = {"dreams_id": dreams_id}
            resp = get_dreams(dreams_id)
            # print(resp)
            ts = '2023-05-07 16:00:00+0300'
            for rp in resp:
                servs = rp['services']
                ddtt = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
                    ou_id, rp['dreams_id'], rp['date_of_birth'],
                    rp['birth_certificate_no'],
                    rp['county_of_residence']['iebc_code'],
                    rp['county_of_residence']['name'],
                    rp['sub_county']['iebc_code'],
                    rp['sub_county']['name'], rp['ward']['iebc_code'],
                    rp['ward']['name'])
                for serv in servs:
                    uid = uuid.uuid4()
                    hts = serv['hts_result'] if serv['hts_result'] else ''
                    sess = serv['no_of_sessions_attended'] if serv['no_of_sessions_attended'] else ''
                    prg = serv['pregnancy_test_result'] if serv['pregnancy_test_result'] else ''
                    ddsv = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
                        uid, ddtt, serv['intervention_date'],
                        serv['intervention_type']['code'],
                        serv['intervention_type']['name'],
                        hts, sess, prg, ts, 'FALSE')
                    print(ddsv)
                # print(ddtt)

"""This proves that MS Access is single-threaded. If you use multiple
Python threads, you must synchronize them by closing their Connections
in order. In the example code, because we do not explicitly close the
first connection before starting the second thread, the data written
in the second thread is not reflected in the dataset of the first thread.


If Access allowed threads properly, the output would be:

Attempt: 0 Object1 Mod1 Mod1
Attempt: 1 Object1 Mod1 Mod1
Attempt: 2 Object1 Mod1 Mod1

Instead, it's:

Attempt: 0 Object1 Mod1 Object1
Attempt: 1 Object1 Mod1 Object1
Attempt: 2 Object1 Mod1 Mod1

"""

import time
import win32com.client
import pywintypes
import threading
import os

def get_conn():
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    conn.Open(c)
    return conn

c = "PROVIDER=MICROSOFT.JET.OLEDB.4.0;DATA SOURCE=test.mdb;"

def update_record():
    conn = get_conn()
    conn.Execute('UPDATE test SET Name = "Mod1" WHERE ID = 1;')
    print_table(conn)
    if attempt == 1:
        conn.Close()

def print_table(conn):
    res = win32com.client.Dispatch(r'ADODB.Recordset')
    res.Open("SELECT * FROM test;", conn)
    data = []
    if not (res.EOF and res.BOF):
        data = res.GetRows()
    res.Close()
    print data[0][0],

def main_thread():
    print "\nAttempt: %s" % attempt,
    
    try:
        cat = win32com.client.Dispatch(r'ADOX.Catalog')
        cat.Create(c)
        cat.ActiveConnection.Close()
    except pywintypes.com_error:
        pass
    cat = None
    
    conn = get_conn()
    conn.Execute('CREATE TABLE test (Name VARCHAR(255), ID INTEGER);')
    conn.Execute('INSERT INTO test VALUES ("Object1", 1);')
    print_table(conn)
    
    t = threading.Thread(target=update_record)
    t.start()
    t.join()
    
    if attempt == 2:
        # 5 seconds seems to be the lower limit.
        # Anything less, and we get the old data.
        time.sleep(5)
    if attempt == 3:
        conn = get_conn()
    
    print_table(conn)
    conn.Close()

if __name__ == '__main__':
    for attempt in range(4):
        try:
            main_thread()
        finally:
            try:
                os.remove("test.mdb")
            except OSError:
                pass


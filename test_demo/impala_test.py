from krbcontext import krbcontext
from impala.dbapi import connect

try:
    keytab_file = '/tmp/hangsi_dev.keytab'
    user = 'hangsi_dev'
    with krbcontext(using_keytab=True, principal=user, keytab_file=keytab_file):
        conn = connect(host='10.202.42.4', port=21050, auth_mechanism='GSSAPI', kerberos_service_name='impala')
        cursor = conn.cursor()
        cursor.execute('show databases')
        column_names = cursor.fetchall()
        print(column_names)
        print(123)
except Exception as e:
    print(e)
    print(345)
    raise e


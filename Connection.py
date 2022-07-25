import psycopg2

class Connection(object):
    _db = None

    def __init__(self, mhost, mport, db, usr, pwd):
        self._db = psycopg2.connect(host=mhost, port=mport, database=db, user=usr,  password=pwd)

    def change(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return False
        return True

    def query(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
        except:
            return None
        return rs

    def close(self):
        self._db.close()
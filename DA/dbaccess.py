import sqlite3
#import MySQLdb

class DbAccess():

    def __init__(self, dbtype='sqlite3'):
        if dbtype=='sqlite3':
            self.conn = sqlite3.connect('test.db')
        #if dbtype=='mysql':
        #    self.conn = MySQLdb.connect("localhost", "root", "123123", "test", charset='utf8' )

    def close(self):
        self.conn.close()

    def findAll(self, sql, params):
        #try:
        cursor = self.conn.cursor()
        list = cursor.execute(sql, params).fetchall()
        cursor.close()
        return list
        #except:
        #    print('catch a error when excute sql')
         #   return []
       # finally:
       #     cursor.close()

    def findOne(self, sql, params):
        try:
            cursor = self.conn.cursor()
            one = cursor.execute(sql, params).fetchone()
            return one
        except:
            print('catch a error when excute sql')
            return []
        finally:
            cursor.close()

    def findMany(self, sql, params, size):
        try:
            cursor = self.conn.cursor()
            list = cursor.execute(sql, params).fetchmany(size)
            return list
        except:
            print('catch a error when excute sql')
            return []
        finally:
            cursor.close()

    def insert(self, sql, params):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            return cursor.rowcount
        except:
            print('catch a error when excute sql')
            return 0
        finally:
            self.conn.commit()
            cursor.close()

    def update(self, sql, params):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            self.conn.commit()
            return cursor.rowcount
        except:
            print('catch a error when excute sql')
            return 0
        finally:
            cursor.close()

    def delete(self, sql, params):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            self.conn.commit()
            return cursor.rowcount
        except:
            print('catch a error when excute sql')
            return 0
        finally:
            cursor.close()

if __name__ == '__main__':
    a = DbAccess('sqlite3')
    l = a.findAll('select * from user where id=?',['1'])
    print(l)
#{ year: "2021", month: "ocak", consume: "23", price: "33", billof: "elektrik", billoftype: "none" }

import sqlite3


class Db_Engine:

    def __init__(self):
        self.db=sqlite3.connect('db_bill.db')
        print('db oluşturuldu')
        self.db_connect()
        self.db_create_table()

    def db_connect(self):
        self.db_cursor=self.db.cursor()
        print('db cursor oluşturuldu')


    def db_create_table(self):
        sql_query="""CREATE TABLE IF NOT EXISTS BILL (id INTEGER PRIMARY KEY AUTOINCREMENT,
        yil INTEGER,
	    ay	VARCHAR, 
	    tuketim_miktari	INTEGER,
	    fatura_tutari	INTEGER,
	    fatura_tipi	VARCHAR,
	    alt_fatura_tipi	VARCHAR
)"""
        # db_column=(id,'yil','ay','tuketim_miktari','fatura_tutari','fatura_tipi','alt_fatura_tipi')
        # sql_number=25
        # sql_boolean=True
        # sql_array=[]
        # sql_sozluk={'name':'ugur'}
        # sql_tuple=('ugur','okur','test')
        self.db_cursor.execute(sql_query)
    def db_insert_values(self,year,month,tuketim,fatura_mik,fatura_tip,alt_fatura):
        db_sql_insert_query=f"""INSERT INTO BILL VALUES(?, ?, ?,?,?,?)"""
        db_sql_insert_values=(year,month,tuketim,fatura_mik,fatura_tip,alt_fatura)
        self.db_cursor.execute(db_sql_insert_query,db_sql_insert_values)
        self.db.commit()


if __name__=='__main__':
    db_engine=Db_Engine()
    # db_engine.db_connect()
    # db_engine.db_create_table()
    # { year: "2021", month: "ocak", consume: "23", price: "33", billof: "elektrik", billoftype: "none" }
    db_engine.db_insert_values(int("2022"),"ocak",int('44'),int('45'),'elektrik','none')


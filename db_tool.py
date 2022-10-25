#{ year: "2021", month: "ocak", consume: "23", price: "33", billof: "elektrik", billoftype: "none" }
import random
import sqlite3


class Db_Engine:

    def __init__(self):
        self.db=sqlite3.connect('db_bill.db')
        print('db oluşturuldu')
        self.db_connect()
        self.db_create_table()
        # return 'db create successfuly'


    def db_connect(self):
        self.db_cursor=self.db.cursor()
        # print('db cursor oluşturuldu')
        # return 'cursor create successfuly'


    def db_create_table(self):
        ''' year:str     month:str      consume:str     price:str     billof:str     billoftype:str'''

        sql_query="""CREATE TABLE IF NOT EXISTS BILL (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year VARCHAR,
        month VARCHAR,
        consume	VARCHAR,
        price	VARCHAR,
        billof	VARCHAR,
        billoftype	VARCHAR)
        """
        self.db_cursor.execute(sql_query)
        return 'success'


    # def db_insert_values(self,year,month,tuketim,fatura_mik,fatura_tip,alt_fatura):
    #     db_sql_insert_query="""
    #     INSERT INTO BILL(yil,ay,tuketim_miktari,fatura_tutari,fatura_tipi,alt_fatura_tipi)
    #     VALUES (?, ?, ?,?,?,?)
    #     """
    #     db_sql_insert_values=(year,month,tuketim,fatura_mik,fatura_tip,alt_fatura)
    #     self.db_cursor.execute(db_sql_insert_query,db_sql_insert_values)
    #     self.db.commit()
    #     return 'success'

    def db_insert_values(self,bill_dict):
        print(bill_dict)
        db_sql_insert_query="""
        INSERT INTO BILL(year,month,consume,price,billof,billoftype) 
        VALUES (?, ?, ?,?,?,?)
        """
        # db_sql_insert_values=(bill_dict['year'],bill_dict['month'],bill_dict['consume'],bill_dict['price'],bill_dict['billof'],bill_dict['billoftype'])
        db_sql_insert_values=(bill_dict.year,bill_dict.month,bill_dict.consume,bill_dict.price,bill_dict.billof,bill_dict.billoftype)
        self.db_cursor.execute(db_sql_insert_query,db_sql_insert_values)
        self.db.commit()
        return 'success'

    def db_getvalues(self,fatura_tipi,yil):
        #select_query=f"""SELECT tuketim_miktari,fatura_tutari,alt_fatura_tipi FROM BILL WHERE(yil={yil} and fatura_tipi='{fatura_tipi}')"""
        select_query=f"""SELECT month,consume,price,billoftype FROM BILL WHERE(year=? and billof=?) order by month asc """
        # select_query=f"""SELECT * FROM BILL """
        self.db_cursor.execute(select_query,(yil,fatura_tipi))
        values=self.db_cursor.fetchall()
        # print(values)
        return_value={}
        for i in range(len(values)):
            return_value[i]={'ay':values[i][0],
                'tuketim_miktari':values[i][1],
                      'fatura_tutari':values[i][2],
                      'alt_fatura_tipi':values[i][3]
                      }

        return return_value

    @property
    def db_last_row_id(self):
        last_row=self.db_cursor.lastrowid
        print(last_row)
        return last_row

    @property
    def db_close(self):
        self.db.close()





if __name__=='__main__':
    db_engine=Db_Engine()
    # db_engine.db_connect()
    # db_engine.db_create_table()
    # { year: "2021", month: "ocak", consume: "23", price: "33", billof: "elektrik", billoftype: "none" }
    # db_engine.db_insert_values(int("2024"),"ocak",int('44'),int('45'),'elektrik','none')
    def add_some_values():
#         month = [1,
                    # 2,
                    # 3,
                    # 4,
                    # 5,
                    # 6,
                    # 7,
                    # 8,
                    # 9,
                    # 10,
                    # 11,12]
        bill_type = ["elektrik", "su", "gaz", "telekominikasyon"]
        bill_type_of = ["cable", "mobile"]
        # print(random.choice(month))
        for i in range(30):
            bill_of_type = random.choice(bill_type)
            if bill_of_type == 'telekominikasyon':
                val={   "year": "2018",  "month": "1",   "consume": "1",  "price": "11",  "billof": "elektrik",  "billoftype": "none" }
                insert_values={'year':random.randint(2018, 2023),'month':random.randint(1, 12),'consume':random.randint(1, 100),'price':random.randint(1, 100),
                               'billof':'telekominikasyon','billoftype':random.choice(bill_type_of)}
                # print(insert_values)
                db_engine.db_insert_values(insert_values)
            else:
                insert_values = {'year': random.randint(2018, 2023), 'month': random.randint(1, 12),
                                 'consume': random.randint(1, 100), 'price': random.randint(1, 100),
                                 'billof': bill_of_type, 'billoftype': 'none'}
                db_engine.db_insert_values(insert_values)
    add_some_values()

    # db_engine.db_getvalues('su',2022)
    # db_engine.db_last_row_id
    db_engine.db_close


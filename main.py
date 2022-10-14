from fastapi import FastAPI
from db_tool import Db_Engine
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app=FastAPI()
db_engine = Db_Engine()



@app.get('/')
async def index():
    return {'message':'success'}

@app.get('/elektrik/{year}')
async def get_elektrik_bills(year:int):
    if year>=2020:
        values=db_engine.db_getvalues('elektrik',year)
        return values
    return {'message':f'year must be grather than {year} '}

@app.get('/su/{year}')
async def get_elektrik_bills(year:int):
    if year>=2020:
        values=db_engine.db_getvalues('su',year)
        return values
    return {'message':f'year must be grather than {year} '}

@app.get('/gaz/{year}')
async def get_elektrik_bills(year:int):
    if year>=2020:
        values=db_engine.db_getvalues('gaz',year)
        return values
    return {'message':f'year must be grather than {year} '}

@app.get('/telekominikasyon/{year}')
async def get_elektrik_bills(year:int):
    if year>=2020:
        values=db_engine.db_getvalues('telekominikasyon',year)
        return values
    return {'message':f'year must be grather than 2020'}

@app.post('/add_new_bill')
async def add_bill(year,month,tuketim,fatura_tutarı,fatura_tipi,alt_fatura_tipi):
    db_engine.db_insert_values(year,month,tuketim,fatura_tutarı,fatura_tipi,alt_fatura_tipi)
    return {'message':'entry added succesfuly'}






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

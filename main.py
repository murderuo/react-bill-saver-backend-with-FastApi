from fastapi import FastAPI
from pydantic import BaseModel
from db_tool import Db_Engine
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app=FastAPI()
db_engine = Db_Engine()

# command = 'Hello, World!'
# match command:
#     case 'Hello, World!':
#         print('Hello to you too!')
#     case 'Goodbye, World!':
#         print('See you later')
#     case other:
#         print('No match found')

class Bill(BaseModel):
    year:str
    month:str
    consume:int
    price:int
    billof:str
    billoftype:str



@app.get('/')
async def index():
    return {'message':'success'}


@app.get('/{billtype}/{year}')
async def match_func(billtype,year:int):
    match billtype:
        case 'elektrik':
            if year >= 2020 and year<2025:
                values = db_engine.db_getvalues(billtype, year)
                return values
            return {'message': f'year must be grather than 2020 '}
        case 'su':
            if year >= 2020 and year<2025:
                values = db_engine.db_getvalues(billtype, year)
                return values
            return {'message':f'year must be grather than 2020 '}
        case 'gaz':
            if year >= 2020 and year<2025:
                values = db_engine.db_getvalues(billtype, year)
                return values
            return {'message': f'year must be grather than 2020 '}
        case 'telekominikasyon':
            if year >= 2020 and year<2025:
                values = db_engine.db_getvalues(billtype, year)
                return values
            return {'message': f'year must be grather than 2020 '}

        case other:
            return {'message':'invalid adress'}





# @app.get('/elektrik/{year}')
# async def get_elektrik_bills(year:int):
#     if year>=2020:
#         values=db_engine.db_getvalues('elektrik',year)
#         return values
#     return {'message':f'year must be grather than {year} '}
#
# @app.get('/su/{year}')
# async def get_elektrik_bills(year:int):
#     if year>=2020 and year<2025:
#         values=db_engine.db_getvalues('su',year)
#         return values
#     return {'message':f'year must be grather than {year} '}
#
# @app.get('/gaz/{year}')
# async def get_elektrik_bills(year:int):
#     if year>=2020 and year<2025:
#         values=db_engine.db_getvalues('gaz',year)
#         return values
#     return {'message':f'year must be grather than {year} '}
#
# @app.get('/telekominikasyon/{year}')
# async def get_elektrik_bills(year:int):
#     if year>=2020 and year<2025:
#         values=db_engine.db_getvalues('telekominikasyon',year)
#         return values
#     return {'message':f'year must be grather than 2020'}

@app.post('/add_new_bill')
async def add_bill(bill:Bill):
    # db_engine.db_insert_values(year,month,tuketim,fatura_tutari,fatura_tipi,alt_fatura_tipi)
    # print(bill)
    messsage=db_engine.db_insert_values(bill)
    return {'message':f'{messsage}'}






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

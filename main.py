from fastapi import FastAPI
from db_tool import file_opener
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app=FastAPI()
data=file_opener()

@app.get('/')
async def index():
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

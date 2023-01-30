import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

Json = "./valiant-airlock-368605-b41043dbf16a.json"
Url = ["https://spreadsheets.google.com/feeds"]
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
# Sheet = GoogleSheets.open_by_key("表單網址d/後面的KEY")

Sheet = GoogleSheets.open_by_key('1NToliV1I1Ypzaw6zvTLLH5GecPQseQ20j7EFJpfBDvQ')

Sheets = Sheet.sheet1



Sheet2 = GoogleSheets.open_by_key('1NToliV1I1Ypzaw6zvTLLH5GecPQseQ20j7EFJpfBDvQ')

# 讀取第二個sheet
# Sheets2 = Sheet2.worksheets()[1]
# Sheets2 = Sheet2.get_worksheet(1)


# 讀取id為932602527的sheet
Sheets2 = Sheet2.get_worksheet_by_id(932602527)



print(Sheets.get_all_values())
print(Sheets2.get_all_values())

# ----- fast api -----
app = FastAPI()
@app.get("/sheet1")
def getAllData():
    return Sheets.get_all_records()
class Info(BaseModel):
    id: int
    data: list

@app.get("/sheet2")
def getAllData():
    return Sheets2.get_all_records()
class Info(BaseModel):
    id: int
    data: list

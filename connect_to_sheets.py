import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json",scope)

client = gspread.authorize(creds)

sheet = client.open("PythonSheet").sheet1

### accessing data
#print(sheet.get_all_records())
#print(sheet.row_values(2))
#print(sheet.cell(2,1).value) #(row,col)

### inserting data
#sheet.insert_row(["NewData1", "NewData2","NewData3","NewData4"],2) #Shifts all rows down

### deleting data
##sheet.delete_row(4) #Will shift all rows below it up to fill in the gap

### update cell
#sheet.update_cell(3,1,"New value")

### find first instance
#cell = sheet.find("New value")
#print(cell.value)
#print(cell.row)
#print(cell.col)

### find multiple instance
#cell_list = sheet.findall("1300")
#for cell in cell_list:
#	print(cell.value)
#	print(cell.row)
#	print(cell.col)


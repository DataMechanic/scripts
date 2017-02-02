
# read excel with openpyxl to numpy
import openpyxl
import numpy as np

wb = openpyxl.load_workbook(filename='d://scripts//table_example.xlsx', read_only=True) #use read_only for big files
ws = wb['table_1'] # sheet name
arr = []
for i in ws.rows:
    row = []
    for j in i:
        row.append(j.value)
    arr.append(row)

tbl = np.array(arr)
print(tbl)


import random
from openpyxl import load_workbook
flag=True
i=0
path='Excel.xlsx'
sheet_name='result'
while flag:
    i=i+1
    sd=random.random()+2.3
    ss18=True
    cs=1
    wz=1
    while ss18:
        gl=random.random()
        if gl<0.093 and cs<6:
            cs=cs+1
            cz=random.random()*0.6+2.4
            sd=sd+cz
            if cs==6:
                try:
                    wb=load_workbook(path)
                    ws=wb.active
                    ws.title = sheet_name
                    ws.append([sd,i])
                    wb.save(path)
                    print("xlsx格式表格写入数据成功！")
                except:
                    print("xlsx格式表格写入数据失败！")
                i=0
        else:
            ss18=False

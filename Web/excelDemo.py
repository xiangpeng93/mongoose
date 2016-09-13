# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd

#import xml module
from xml.dom import minidom

import codecs 

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    print sys.argv[1]
    if sys.argv[1] != "":
        file = sys.argv[1]
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数

    list=[]
    for rownum in range(5,nrows):
         row = table.row_values(rownum)
         if row:
             list.append(row)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def generatorXmlReport(tables):
    doc = minidom.Document()
    testElement = doc.appendChild(doc.createElement("table"))
    f = codecs.open("test.xml","w",'utf-8')
    for row in tables:
        print row[0]
        print row[6]
        tr = doc.createElement("tr")
        td1 = doc.createElement("td")
        td2 = doc.createElement("td")
        
        keyWord = row[0];
        keyValue = row[6];
        td1.appendChild(doc.createTextNode(keyWord))
        
        td2.appendChild(doc.createTextNode(keyValue))

        tr.appendChild(td1)
        tr.appendChild(td2)
        
        testElement.appendChild(tr)
        #element.appendChild(doc.createTextNode(row[6]))
    
    doc.writexml(f)
    

def main():
   tables = excel_table_byindex()
   generatorXmlReport(tables)
   for row in tables:
       #for rowContext in row:
       print row[0]
       print row[6]
   # = excel_table_byname()
   #for row in tables:
   #    print row

if __name__=="__main__":
    main()

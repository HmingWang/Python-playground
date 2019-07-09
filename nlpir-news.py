import pymysql
import pynlpir
import openpyxl

pynlpir.open()

conn = pymysql.connect(host='47.112.111.139', user='whaim', passwd='1122', db='newsdb')

cur = pymysql.cursors.SSCursor(conn)
cur.execute("select concat(ifnull(title_pre,''),ifnull(title,''),ifnull(title_sub,'')) as title , content from news ")


book = openpyxl.Workbook()
sheet = book.active
sheet.append(['标题','内容'])
count=0
while True:
    row = cur.fetchone()
    count=count+1
    if not row:
        break

    title=''
    content=''
    nlp_title = pynlpir.segment(row[0])
    for i in nlp_title:
        title=title+i[0]+' '
    nlp_content = pynlpir.segment(row[1])

    for i in nlp_content:
        content=content+i[0]+' '

    sheet.append([title,content])
    print(count)


    if count%500==0:
        book.save(r'e:\test1.xlsx')

book.save(r'e:\test1.xlsx')
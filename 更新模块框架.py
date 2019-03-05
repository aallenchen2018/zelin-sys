#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')

while 1:
    cho1=input('是否需要修改基本信息？(Y,N)')
    if cho1=='Y' or 'y':
        uname=input('请输入你的名字： >>>按Q返回')
        if uname=='Q' or 'q':
            continue
        else:
            cur=conn.cursor()
            cur.execute('select sname,college,tel,sex from student where sname="%s"'%uname)
            data=cur.fetchall()
            for i in data:
                print(i)


    # elif cho1=='N' or 'n':
    #     cho2==input('是否需要修改详细信息？(Y,N)')
    #     if 




# cur=conn.cursor()
# cur.execute('l')
cur.close()			#关闭游标
conn.close()   			#关闭数据库连接，释放数据库资源
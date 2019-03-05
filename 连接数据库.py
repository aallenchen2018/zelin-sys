#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')

cur=conn.cursor()
cur.execute('select * from student')
data=cur.fetchall()
for i in data:
    print(i)

# cur=conn.cursor()     #获取一个游标
# cur.execute('create view va as select study.sname from study,hopping where study.sname=hopping.sname and  study.sname="chenyou"')  


# data=cur.fetchall()		#获取语句的执行结果

# cur1=conn.cursor()
# cur1.execute('select * from va')
# data1=cur1.fetchall()

# cur2=conn.cursor()
# cur2.execute('create view  vb as select study.sname,class.rname,hopping.newcompany from study,class,hopping where study.cname=class.cname and study.sname=hopping.sname')
# data2=cur2.fetchall()




# for con in data3:
#     print('ok,abc')

cur.close()			#关闭游标
conn.close()   			#关闭数据库连接，释放数据库资源
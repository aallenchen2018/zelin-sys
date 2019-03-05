#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='text',db='zelin',port=3306,charset='utf8')



# cur=conn.cursor()     #获取一个游标
# cur.execute('create view va as select study.sname from study,hopping where study.sname=hopping.sname and  study.sname="chenyou"')  


# data=cur.fetchall()		#获取语句的执行结果

# cur1=conn.cursor()
# cur1.execute('select * from va')
# data1=cur1.fetchall()

#cur2=conn.cursor()
#cur2.execute('create view  vb as select study.sname,class.rname,hopping.newcompany from study,class,hopping where study.cname=class.cname and study.sname=hopping.sname')
#data2=cur2.fetchall()

#listb=[]
aa=input('查询名字')
cur4=conn.cursor()
cur4.execute('select * from student where sname="%s"'%aa)
data4=cur4.fetchall()
if len(data4)==0:
	print('无')
else:
	cur3=conn.cursor()
	cur3.execute('select * from vb where sname="%s"'%aa)
	data3=cur3.fetchall()
	for i in data3:
		print(i)
1

cur4.close()
cur3.close()			#关闭游标
conn.close()   			#关闭数据库连接，释放数据库资源

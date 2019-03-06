#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='test',db='zelin',port=3306,charset='utf8')
a=input('欢迎来到删除系统,输入1开始删除程序,输入其他退出本系统')
while 1:
	if a=='1':
		b=input('请输入你要删除的名字')
		c=input('请输入与上边名字对应的电话')
		cur=conn.cursor()
		cur.execute("select * from student where sname='%s' and tel='%s'"%(b,c))
		data=cur.fetchall()
		if len(data)==0:
			i=input('名字不存在,请重新输入,输入q退出')
			if i=='q':
				break
		else:	
			cur=conn.cursor()
			cur.execute("delete from student where sname='%s' and tel='%s'"%(b,c))
			cur=conn.cursor()
			cur.execute("delete from study where sname in(select sname from student where tel='%s')"%c)
			cur=conn.cursor()
			cur.execute("delete from job where sname in(select sname from student where tel='%s')"%c)
			cur=conn.cursor()
			cur.execute("delete from hopping where sname in(select sname from student where tel='%s')"%c)
			d=input('是否真的要删除该名字所有相关信息,继续请输入yes,输入其他退出')
			if d=='yes':
				e=input('由于删除后无法恢复数据,请输入confirm作为最后确认,输入其他退出')
				if e=='confirm':
					conn.commit()
					print('删除成功')
			else:
				continue
	else:
		break

import pymysql

conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')
cur=conn.cursor()
def cha1(a):#查询学员信息
#	checkname=input('请输入需要查询的姓名: ')	#判断名字是否存在
	cur.execute('select * from student where sname="%s"'%a)
	data=cur.fetchall()
	if len(data)==0:
		print('无此学员信息')
		return data
	else:
		for i in data:
			print('姓  名: ',i[1],'性  别:',i[4],'毕业学校: ',i[2],'联系方式:',i[3])	#查询学生部分信息
		return data

def cha2(b):
	cur.execute('select * from study where sname="%s"'%b)
	data2=cur.fetchall()
	if len(data2)==0:
		print('暂无学习信息')
	else:
		for i in data2:
			print('课程名称:',i[2],'考试成绩:',i[3], '迟到次数:',i[4],'违纪次数:',i[5])
		return data2
def cha3(c):#查询就业信息
#	checkname=input('请输入需要查询的姓名: ')	#判断名字是否存在
	cur.execute('select * from job where sname="%s"'%c)
	data=cur.fetchall()
	if len(data)==0:
		print('无此就业信息')
		return data
	else:
		for i in data:
			print('毕业时间: ',i[2],'就业时间: ',i[3],'就业薪资:',i[4],'就业公司:',i[5])	#查询学生部分信息
			return data

def cha4(d):
	cur.execute('select * from hopping where sname="%s"'%d)
	data2=cur.fetchall()
	if len(data2)==0:
		print('暂无跳槽信息')
	else:
		for i in data2:
			print('跳槽公司:',i[2], '跳槽薪资',i[3],' 跳槽时间',i[4])
def cha5(e):
	cur.execute('select c.cname,c.rname,c.lesson from class c,study s where s.cname=c.cname and s.sname="%s"'%e)
	data5=cur.fetchall()
	if len(data5)==0:
		print('无课程信息')
	else:
		for i in data5:
			print('教室名称:',i[0],' 教室名称',i[1], ' 课程名称',i[2])


while 1:
	cho=input('查询全部信息请按1,查询学生部分信息请按2,查询学生就业信息请按3,退出请按q')
	if cho=='1':
		chall=input('请选择您需要查询的方式:a.通过名字查询 b.通过号码查询 ')
		if chall=='a':
			checkname=input('请输入需要查询的姓名: ')
			if len(cha1(checkname))==0:
				print('请输入正确的姓名:')
				continue
			else:
				cha2(checkname)
				cha5(checkname)
				cha3(checkname)
				cha4(checkname)
				
	elif cho=='2':
		while 1:
			cho1=input('请选择您的查询方式:a.通过名字查询 b.通过号码查询  q.退出')#选项,通过名字查a还是号码查b退出q	
			if cho1=='a':
				checkname=input('请输入需要查询的姓名: ')
				if len(cha1(checkname))==0:
					print('请输入正确的姓名:')
					continue
				else:
					cha2(checkname)
					cha5(checkname)
			elif cho1=='b':
				checktel=input('请输入需要查询的电话: ')
				cur.execute('select sname from student where tel="%s"'%checktel)
				data=cur.fetchall()
				if len(data)==0:
					print('暂无该学员的学习信息!')
				else:
					for i in data:
						a=i[0]
						cha1(a)
						cha2(a)
			elif cho1=='q':
				break
			else:
				print('输入有误请重新输入!')
				print('_______________________')
	elif cho=='3':
		while 1:
			cho1=input('请选择您的查询方式:a.通过名字查询 b.通过号码查询  q.退出')#选项,通过名字查a还是号码查b退出q	
			if cho1=='a':
				checkname=input('请输入需要查询的姓名: ')
				if len(cha3(checkname))==0:
					print('请输入正确的姓名:')
					continue
				else:
					cha4(checkname)
			elif cho1=='b':
				checktel=input('请输入需要查询的电话: ')
				cur.execute('select sname from student where tel="%s"'%checktel)
				data=cur.fetchall()
				if len(data)==0:
					print('输入有误!')
				else:
					for i in data:
						a=i[0]
						cha1(a)
						cha2(a)
			elif cho1=='q':
				break
			else:
				print('输入有误,请重新输入')
				print('_______________________')


	elif cho=='q':
		break
	else:
		print('请正确选择需要办理的业务!')


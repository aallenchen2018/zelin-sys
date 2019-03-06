#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')
while 1:
	print('*'*70,'\n',)
	a=input('请输入需要更新信息的名字')
	cur=conn.cursor()
	cur.execute('select * from student where sname="%s"'%a)
	data=cur.fetchall()
	for i in data:
		print('*'*70,'\n',"SID: %d>>>,名字： %s>>>学校：  %s>>>tel:  %s>>>性别：  %s"%(i[0],i[1],i[2],i[3],i[4]))
	
	if len(data)==0:
		print('*'*70,'\n',)
		print('需要更新信息的名字不存在,请重新输入')
	else:
		print('*'*70,'\n',)
		b=input('1.修改单个信息2.修改大部分信息;按Q返回')
		if b=='1':
			print('*'*70,'\n',)
			print('你要修改单个信息>>>')
			pass
			c=input('1.学习系统2.工作系统')
			if c=='1':
				print('*'*70,'\n',)
				d=input('''请选择学习系统中要修改的单个信息
				1.sname			6.degree       
				2.tel			7.lagtime
				3.college		8.lapsetimes
				4.ssex			9.rname
				5.cname			10.lesson
				''')
				if d=='1':
					while 1:
						try:
							print('*'*70,'\n',)
							newname=input('修改后的名字（输入Q返回）')
							if newname=='Q' or 'q':
								break
							else:
								print('你输入的名字是 %s'%newname)
								cur=conn.cursor()
								cur.execute('update student set sname="%s" where sname="%s"'%(newname,a))
								cur.execute('update hopping set sname="%s" where sname="%s"'%(newname,a))
								cur.execute('update job set sname="%s" where sname="%s"'%(newname,a))
								cur.execute('update study set sname="%s" where sname="%s"'%(newname,a))
								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								# check="""select * from student"""
								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%newname)
								cur1.execute("select * from study where sname='%s'"%newname)
								cur2.execute("select * from job where sname='%s'"%newname)
								cur3.execute("select * from hopping where sname='%s'"%newname)
								
								data=cur.fetchall()
								for i in data:
									print('*'*70,'\n',"SID:>>> %d,名字：>>>%s,学校>>>%s,tel:>>>%s,性别>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
								data1=cur1.fetchall()
								for l in data1:
									print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
								data2=cur2.fetchall()
								for l in data2:
									print("毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽时间：>>>%s"%(l[1],l[2],l[3]))
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break
						
					
					
						


					

				# elif d=='2':
					

	# 			elif d=='3':
	# 			elif d=='4':
	# 			elif d=='5':
	# 			elif d=='6':
	# 			elif d=='7':
	# 			elif d=='8':
	# 			elif d=='9':
	# 			elif d=='10':
	# 			else:
				

			# elif c=='2':

	# 			e=input('''请选择工作系统中要修改的单个信息
	# 			1.sname
	# 			2.graduatetime
	# 			3.salary
	# 			4.company
	# 			5.newsalary
	# 			6.hoppingtime
	# 			''')
				
	# 			if e=='1':
	# 			elif e=='2':
	# 			elif e=='3':
	# 			elif e=='4':
	# 			elif e=='5':
	# 			elif e=='6':
	# 			else:
			# elif 
	# 		else:
	# 			print('该信息不在系统中,请重新输入')	
		elif b=='2':
			print('*'*70,'\n',)
			print('你要修改所有的信息')
			# f=input('请输入关键字以修改所有信息')
		elif b=='Q' or 'q':
			continue
		else:	
			print('输入有误,请重新输入')


cur.close()			#关闭游标
conn.close()   			#关闭数据库连接，释放数据库资源
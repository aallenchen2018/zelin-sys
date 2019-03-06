#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')
cur=conn.cursor()

while 1:
	print('*'*70,'\n',)
	cho1=input('注册学生基本信息按1\n完善信息按2\n新增班级按3\n退出请按q\n')
	if cho1=='1':
		while 1:
			print('*'*70,'\n',)
			type1=input('输入需要注册的学生姓名: ')
			cur.execute('select sname from student where sname="%s"'%type1)
			data=cur.fetchall()
			if len(data)==0:
				type2=input('请输入学生性别: ')
				print('*'*70,'\n',)
				type3=input('请输入学生大学: ')
				print('*'*70,'\n',)
				type4=input('请输入学生电话: ')
				print('*'*70,'\n',)
				typec=input('请输入学生班级: ')
				print('*'*70,'\n',)
				cur.execute("insert into student values(null,'%s','%s','%s','%s')"%(type1,type2,type3,type4))
				cur.execute("insert into study (sid,sname,cname) values ((select sid from student where sname='%s'),'%s','%s')"%(type1,type1,typec))
				cur.execute("insert into job (sid,sname) values ((select sid from student where sname='%s'),'%s')"%(type1,type1))
				cur.execute("insert into hopping (sid,sname) values ((select sid from student where sname='%s'),'%s')"%(type1,type1))
				print('注册成功')
				conn.commit()
				break
			else:
				print('*'*70,'\n',)
				cho=input('名字已存在,任意键重输,q键退出')
				if cho=='q':
					break	
				else:
					continue

	elif cho1=='2':
		print('*'*70,'\n',)
		cho3=input('完善毕业信息请按a\n完善跳槽信息请按b\n退出请按q键\n')
		if cho3=='a':
			#完善job表
			while 1:
				print('*'*70,'\n',)
				cho4=input('通过学生姓名完善请按a\n通过学生号码完善请按b\n退出请按q\n')
				if cho4=='a':
					print('*'*70,'\n',)
					sname=input(('请输入需要完善的学生姓名: '))
					cur.execute('select * from student where sname="%s"'%sname)
					data=cur.fetchall()
					if len(data)==0:
						print('*'*70,'\n',)
						chot=input('需要完善信息的名字不存在\n任意键重新输入\n退出请按q\n')
						if chot=='q':
							break
						else:
							continue
					else:
						print('*'*70,'\n',)
						type5=input('毕业时间: ')
						type6=input('就业薪资: ')
						type7=input('就业公司: ')
						typej1=input('就业时间: ')	
						cur.execute('update job set graduatetime="%s",salary="%s",company="%s",getjobtime="%s" where sname="%s"'%(type5,type6,type7,typej1,sname))
						conn.commit()
						print('*'*70,'\n',)
						print('完善成功')
						break
				elif cho4=='b':
					print('*'*70,'\n',)
					tel=input(('请输入需要完善的学生号码: '))
					cur.execute('select * from student where tel="%s"'%tel)
					data=cur.fetchall()
					if len(data)==0:
						print('*'*70,'\n',)
						chot=input('需要完善信息的号码不存在\n任意键重新输入\n退出请按q\n')
						if chot=='q':
							break
						else:
							continue
					else:
						print('*'*70,'\n',)
						type5=input('毕业时间: ')
						type6=input('就业薪资: ')
						type7=input('就业公司: ')
						typej1=input('就业时间: ')
						cur.execute('update job set graduatetime="%s",salary="%s",company="%s",getjobtime="%s" where sname=(select sname from student where tel="%s")'%(type5,type6,type7,typej1,tel))
						conn.commit()
						print('完善成功')
						break

				elif cho4=='q':
						break
				else:
					print('输入有误')

		if cho3=='b':
			#完善hopping表
			while 1:
				#选项,通过名字查a还是号码查b退出q
				print('*'*70,'\n',)
				cho6=input('通过学生姓名完善请按a\n通过学生号码完善请按b\n退出请按q\n')
				if cho6=='a':
					print('*'*70,'\n',)
					sname=input(('请输入需要完善的学生姓名'))
					cur.execute('select * from student where sname="%s"'%sname)
					data=cur.fetchall()
					if len(data)==0:
						print('*'*70,'\n',)
						chot=input('需要完善信息的名字不存在\n任意键重新输入\n退出请按q\n')
						if chot=='q':
							break
						else:
							continue
					else:
						print('*'*70,'\n',)
						type8=input('跳槽后公司: ')
						type9=int(input('跳槽后薪资: '))
						type10=input('跳槽时间: ')
						cur.execute('update hopping set newcompany="%s",newsalary="%d",hoppingtime="%s" where sname="%s"'%(type8,type9,type10,sname))
						conn.commit()
						print('完善成功')
						break

				elif cho6=='b':
					print('*'*70,'\n',)
					tel=input(('请输入需要完善的学生号码'))
					cur.execute('select * from student where tel="%s"'%tel)
					data=cur.fetchall()
					if len(data)==0:
						chot=input('需要完善信息的号码不存在\n任意键重新输入\n退出请按q\n')
						if chot=='q':
							break
						else:
							continue
					else:
						print('*'*70,'\n',)
						type8=input('跳槽后公司: ')
						type9=input('跳槽后薪资: ')
						type10=input('跳槽时间: ')
						cur.execute('update hopping set newcompany="%s",newsalary="%s",hoppingtime="%s" where sname=(select sname from student where tel="%s")'%(type8,type9,type10,tel))
						conn.commit()
						print('完善成功')
						break
				elif cho6=='q':
					break
				else:
					print('*'*70,'\n',)
					print('输入有误,请重新输入')

	elif cho1=='3':
		print('*'*70,'\n',)
		typec1=input('新增班级名称')
		typec2=input('新增教室地点')
		typec3=input('新增课程类型')
		cur.execute("insert into class (cname,rname,lesson) values ('%s','%s','%s')"%(typec1,typec2,typec3))
		conn.commit()
		print('新增成功')	
	elif cho1=='q':
		break
	else:
		print('*'*70,'\n',)
		print('输入有误,请重新输入')






cur.close()
conn.close()

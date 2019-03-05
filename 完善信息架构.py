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
							if newname=='Q':
								print('你需要返回')
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break
						
					
				elif d=='2':
					while 1:
						try:
							print('*'*70,'\n',)
							newtel=input('修改后的电话（输入Q返回）')
							if newtel=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的电话是 %s'%newtel)
								cur=conn.cursor()
								cur.execute('update student set tel="%s" where sname="%s"'%(newtel,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a
								

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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break
				
				elif d=='3':
					while 1:
						try:
							print('*'*70,'\n',)
							newuni=input('修改后的大学（输入Q返回）')
							if newuni=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的大学是 %s'%newuni)
								cur=conn.cursor()
								cur.execute('update student set college="%s" where sname="%s"'%(newuni,a))

								conn.commit()
										#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

								print(a)
								cur.execute("select * from student where sname='%s'"%a)
								cur1.execute("select * from study where sname='%s'"%a)
								cur2.execute("select * from job where sname='%s'"%a)
								cur3.execute("select * from hopping where sname='%s'"%a)
								
								data=cur.fetchall()
								for i in data:
									print('*'*70,'\n',"SID:>>> %d,名字：>>>%s,学校>>>%s,tel:>>>%s,性别>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
								data1=cur1.fetchall()
								for l in data1:
									print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
								data2=cur2.fetchall()
								for l in data2:
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))								
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif d=='4':
					while 1:
						try:
							print('*'*70,'\n',)
							newsex=input('修改后的性别（输入Q返回）')
							if newsex=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的性别是 %s'%newsex)
								cur=conn.cursor()
								cur.execute('update student set sex="%s" where sname="%s"'%(newsex,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break								


				elif d=='5':
					while 1:
						try:
							print('*'*70,'\n',)
							newcla=input('修改后的班级（输入Q返回）')
							if newcla=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的班级是 %s'%newcla)
								cur=conn.cursor()
								cur.execute('update study set cname="%s" where sname="%s"'%(newcla,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif d=='6':
					while 1:
						try:
							print('*'*70,'\n',)
							newdegree=int(input('修改后的成绩（输入Q返回）'))
							if newdegree=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的成绩是 %s'%newdegree)
								cur=conn.cursor()
								cur.execute('update study set degree="%d" where sname="%s"'%(newdegree,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))
								
															
						except Exception as result:
							print('请输入正确的格式,数字')
						finally:
							break	

				elif d=='7':
					while 1:
						try:
							print('*'*70,'\n',)
							newlagt=int(input('修改后的迟到次数（输入Q返回）'))
							if newlagt=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的迟到次数是 %s'%newlagt)
								cur=conn.cursor()
								cur.execute('update study set lagtime="%d" where sname="%s"'%(newlagt,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif d=='8':
					while 1:
						try:
							print('*'*70,'\n',)
							newlags=int(input('修改后的违纪次数（输入Q返回）'))
							if newlags=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的违纪次数是 %d'%newlags)
								cur=conn.cursor()
								cur.execute('update study set lapsetimes="%d" where sname="%s"'%(newlags,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif d=='9':
					print('*'*70,'\n',)
					print('你所更新的教室将会在其他状态下更新！！')
					

				elif d=='10':
					print('*'*70,'\n',)
					print('你的课程名将会在其他信息内更新！！')


				else:
					print('*'*70,'\n',)
					print('请输入正确的选择。')
				

			elif c=='2':
				print('*'*70,'\n',)
				e=input('''请选择工作系统中要修改的单个信息
				1.sname
				2.gradeuatetime
				3.salary
				4.company
				5.newsalary
				6.newcompany
				7.hoppingtime
				''')
				
				if e=='1':
					while 1:
						try:
							print('*'*70,'\n',)
							newname=input('修改后的名字（输入Q返回）')
							if newname=='Q':
								print('你需要返回')
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break
					
				elif e=='2':
					while 1:
						try:
							print('*'*70,'\n',)
							newgra=input('修改后的毕业时间（输入Q返回）')
							if newgra=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的毕业是 %s'%newgra)
								cur=conn.cursor()
								cur.execute('update job set graduatetime="%s" where sname="%s"'%(newgra,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif e=='3':
					while 1:
						try:
							print('*'*70,'\n',)
							newsal=input('修改后的工资（输入Q返回）')
							if newsal=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的工资是 %s'%newsal)
								cur=conn.cursor()
								cur.execute('update job set salary="%s" where sname="%s"'%(newsal,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	


				elif e=='4':
					while 1:
						try:
							print('*'*70,'\n',)
							newcom=input('修改后的公司（输入Q返回）')
							if newcom=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的公司是 %s'%newcom)
								cur=conn.cursor()
								cur.execute('update job set company="%s" where sname="%s"'%(newcom,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif e=='5':
					while 1:
						try:
							print('*'*70,'\n',)
							newnsal=int(input('修改后的最新工资（输入Q返回）'))
							if newnsal=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的最新工资是 %s'%newnsal)
								cur=conn.cursor()
								cur.execute('update hopping set newsalary="%s" where sname="%s"'%(newnsal,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif e=='6':
					while 1:
						try:
							print('*'*70,'\n',)
							newncom=input('修改后的新公司（输入Q返回）')
							if newncom=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的新公司是 %s'%newncom)
								cur=conn.cursor()
								cur.execute('update hopping set newcompany="%s" where sname="%s"'%(newncom,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	

				elif e=='7':
					while 1:
						try:
							print('*'*70,'\n',)
							newnhtime=input('修改后的跳槽时间（输入Q返回）')
							if newnhtime=='Q':
								print('你正在返回')
								break
							else:
								print('你输入的跳槽时间是 %s'%newnhtime)
								cur=conn.cursor()
								cur.execute('update hopping set hoppingtime="%s" where sname="%s"'%(newnhtime,a))

								conn.commit()
								cur.close()			#关闭游标
								
								print('你已经修改成功！！！')
								print('*'*70,'\n',)
								print('更新后的数值为：')
								print('\n')
								
								newname=a

								cur=conn.cursor()
								cur1=conn.cursor()
								cur2=conn.cursor()
								cur3=conn.cursor()
								
								cur.execute("select * from student where sname='%s'"%a)
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
									print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
								data3=cur3.fetchall()
								for l in data3:
									print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))

															
						except Exception as result:
							print('请输入正确的格式')
						finally:
							break	


				else:
					print('*'*70,'\n',)
					print('请输入正确的选择！！')

			else:
				print('*'*70,'\n',)
				print('该信息不在系统中,请重新输入')	
		elif b=='2':
			print('*'*70,'\n',)
			print('你要修改所有的信息')
			print('*'*70,'\n',)
			while 1:
			
				try:

					
					newname=input('输入名字（输入Q返回）')
					if newname=='Q':
						print('你需要返回')
						break
					else:
						newtel=input('输入电话 （Q退出）')
						if newtel=='Q':
							print('你需要返回')
							break
						else:
							college=input('输入学校 （Q退出）')
							if college=='Q':
								print('你需要返回')
								break
							else:
								sex=input('输入性别 （Q退出）')
								if sex=='Q':
									print('你需要返回')
									break
								else:
								
									print('你输入的是 %s>>>%s>>>%s'%(newname,newtel,college))

									cur=conn.cursor()
									cur.execute('update student set sname="%s" where sname="%s"'%(newname,a))
									cur.execute('update hopping set sname="%s" where sname="%s"'%(newname,a))
									cur.execute('update job set sname="%s" where sname="%s"'%(newname,a))
									cur.execute('update study set sname="%s" where sname="%s"'%(newname,a))
									cur.execute('update student set tel="%s" where sname="%s"'%(newtel,newname))
									cur.execute('update student set college="%s" where sname="%s"'%(college,newname))
									cur.execute('update student set sex="%s" where sname="%s"'%(sex,newname))
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
										print("毕业实际:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4]))
									data3=cur3.fetchall()
									for l in data3:
										print("新公司:>>>%s,新薪水：>>>%s,跳槽实际：>>>%s"%(l[1],l[2],l[3]))
				except Exception as result:
					print('请输入正确的格式')
				finally:
					break
				

			
		elif b=='Q' or 'q':
			continue
		else:	
			print('输入有误,请重新输入')



cur.close()			#关闭游标
conn.close()   			#关闭数据库连接，释放数据库资源
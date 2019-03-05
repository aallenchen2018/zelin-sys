#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='text',db='zelin',port=3306,charset='utf8')
cur=conn.cursor()

while 1:
	cho=input('新增学生基本信息按1,完善信息按2,退出请按q')
	if cho1=='1':
		while 1:
		
			#新增代码
			sanme=input('名字')
			#判断是否存在
			
			if #不存在:
				college=input('大学')			
				tel=int(input('电话'))
				#新增student表
				#新增study表
				#新增job表sid,sname
				#新增hopping表sid,sname
				print('注册成功')
				break
			else:#存在
			#	退出按q,任意键重新输入
				if 'q':
					break	
				else:
					continue
	elif cho2=='2':
		cho3=input(完善job表按a,完善hopping表按b)
		if cho3=='a':
			while 1:
				#选项,通过名字查a还是号码查b退出q
				if cho16=='a':
					#判断名字是否存在
					if #不存在
						#报错
					else:
						graduatetime=input('毕业时间')
						salary=input('工资')
						company=input('公司')
						#新增
						print('完善成功')
						break
				elif cho1=='b':
					#判断号码是否存在
					if #不存在
						#报错
					else:
						graduatetime=input('毕业时间')
						salary=input('工资')
						company=input('公司')
						#新增
						print('完善成功')
						break
				elif cho1=='q':
					break
				else:
					#输入有误
				
		if cho3=='b':
			#完善hopping表
			while 1:
				#选项,通过名字查a还是号码查b退出q
				if cho1=='a':
					#判断名字是否存在
					if #不存在
						#报错
					else:
						newcompany=input('新公司')
						newsalary=input('新工资')
						hoppingtime=input('跳槽时间')
						#新增
						print('完善成功')
						break
				elif cho1=='b':
					#判断号码是否存在
					if #不存在
						#报错
					else:
						newcompany=input('新公司')
						newsalary=input('新工资')
						hoppingtime=input('跳槽时间')
						#新增
						print('完善成功')
						break
				elif cho1=='q':
					break
				else:
					#输入有误
						
	elif cho2=='q':		
		break
	else:
		#输入错误重输








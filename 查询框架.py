#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='text',db='zelin',port=3306,charset='utf8')
cur=conn.cursor()


while 1:
	cho=input('查询全部信息请按1,查询学生部分信息请按2,查询学生就业信息请按3,退出请按q')
	if cho==1:
		#查询全部信息
	elif cho==2:
		while 1:
			#选项,通过名字查a还是号码查b退出q	
			if cho1=='a':
				#判断名字是否存在
				if #不存在
					#报错
				else:
					#查询学生部分信息
			elif cho1=='b':
				#判断号码是否存在
				if #不存在
					#报错
				else:
					#查询学习部分信息
			elif cho1=='q':
				break
			else:
				#报错循环
	elif cho==3:
		while 1:
			#选项,通过名字查a还是号码查b退出q	
			if cho1=='a':
				#判断名字是否存在
				if #不存在
					#报错
				else:
					#查询学生就业信息
			elif cho1=='b':
				#判断号码是否存在
				if #不存在
					#报错
				else:
					#查询学习就业信息
			elif cho1=='q':
				break
			else:
				#报错循环

	elif cho=='q':
		break
	else:
		#输入有误






cur.close()
conn.close()






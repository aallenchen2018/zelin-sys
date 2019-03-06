import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='1',db='zelin',port=3306,charset='utf8')


def 增添():
    cur=conn.cursor()
    while 1:
        cho1=input('注册学生基本信息按1\n完善信息按2\n新增班级按3\n退出请按q\n')
        if cho1=='1':
            while 1:
                type1=input('输入需要注册的学生姓名: ')
                cur.execute('select sname from student where sname="%s"'%type1)
                data=cur.fetchall()
                if len(data)==0:
                    type2=input('请输入学生性别: ')
                    type3=input('请输入学生大学: ')
                    type4=input('请输入学生电话: ')
                    typec=input('请输入学生班级: ')
                    cur.execute('select cname from class where cname="%s"'%typec)
                    data1=cur.fetchall()
                    if len(data1)==0:
                        cho=input('无该班级')
                        break
                    else:
                        cur.execute("insert into student values(null,'%s','%s','%s','%s')"%(type1,type2,type3,type4))
                        cur.execute("insert into study (sid,sname,cname) values ((select sid from student where sname='%s'),'%s','%s')"%(type1,type1,typec))
                        cur.execute("insert into job (sid,sname) values ((select sid from student where sname='%s'),'%s')"%(type1,type1))
                        cur.execute("insert into hopping (sid,sname) values ((select sid from student where sname='%s'),'%s')"%(type1,type1))
                        print('注册成功')
                        conn.commit()
                        break
                else:
                    cho=input('名字已存在,任意键重输,q键退出')
                    if cho=='q':
                        break	
                    else:
                        continue

        elif cho1=='2':
            cho3=input('完善毕业信息请按a\n完善跳槽信息请按b\n退出请按q键\n')
            if cho3=='a':
                #完善job表
                while 1:
                    cho4=input('通过学生姓名完善请按a\n通过学生号码完善请按b\n退出请按q\n')
                    if cho4=='a':
                        sname=input(('请输入需要完善的学生姓名: '))
                        cur.execute('select * from student where sname="%s"'%sname)
                        data=cur.fetchall()
                        if len(data)==0:
                            chot=input('需要完善信息的名字不存在\n任意键重新输入\n退出请按q\n')
                            if chot=='q':
                                break
                            else:
                                continue
                        else:
                            try:
                                type5=input('毕业时间: ')
                                type6=input('就业薪资: ')
                                type7=input('就业公司: ')
                                typej1=input('就业时间: ')	
                                cur.execute('update job set graduatetime="%s",salary="%s",company="%s",getjobtime="%s" where sname="%s"'%(type5,type6,type7,typej1,sname))
                                conn.commit()
                                print('完善成功')
                                break
                            except Exception as e:
                                print('请输入正确的格式')
                            finally:
                                break
                    elif cho4=='b':
                        tel=input(('请输入需要完善的学生号码: '))
                        cur.execute('select * from student where tel="%s"'%tel)
                        data=cur.fetchall()
                        if len(data)==0:
                            chot=input('需要完善信息的号码不存在\n任意键重新输入\n退出请按q\n')
                            if chot=='q':
                                break
                            else:
                                continue
                        else:
                            try:
                                type5=input('毕业时间: ')
                                type6=input('就业薪资: ')
                                type7=input('就业公司: ')
                                typej1=input('就业时间: ')
                                cur.execute('update job set graduatetime="%s",salary="%s",company="%s",getjobtime="%s" where sname=(select sname from student where tel="%s")'%(type5,type6,type7,typej1,tel))
                                conn.commit()
                                print('完善成功')
                                break
                            except Exception as e:
                                print('请输入正确的格式')
                            finally:
                                break

                    elif cho4=='q':
                            break
                    else:
                        print('输入有误')

            if cho3=='b':
                #完善hopping表
                while 1:
                    #选项,通过名字查a还是号码查b退出q
                    cho6=input('通过学生姓名完善请按a\n通过学生号码完善请按b\n退出请按q\n')
                    if cho6=='a':
                        sname=input(('请输入需要完善的学生姓名'))
                        cur.execute('select * from student where sname="%s"'%sname)
                        data=cur.fetchall()
                        if len(data)==0:
                            chot=input('需要完善信息的名字不存在\n任意键重新输入\n退出请按q\n')
                            if chot=='q':
                                break
                            else:
                                continue
                        else:
                            try:
                                type8=input('跳槽后公司: ')
                                type9=int(input('跳槽后薪资: '))
                                type10=input('跳槽时间: ')
                                cur.execute('update hopping set newcompany="%s",newsalary="%d",hoppingtime="%s" where sname="%s"'%(type8,type9,type10,sname))
                                conn.commit()
                                print('完善成功')
                                break
                            except Exception as e:
                                print('请输入正确的格式')
                            finally:
                                break

                    elif cho6=='b':
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
                            try:
                                type8=input('跳槽后公司: ')
                                type9=input('跳槽后薪资: ')
                                type10=input('跳槽时间: ')
                                cur.execute('update hopping set newcompany="%s",newsalary="%s",hoppingtime="%s" where sname=(select sname from student where tel="%s")'%(type8,type9,type10,tel))
                                conn.commit()
                                print('完善成功')
                                break
                            except Exception as e:
                                print('请输入正确的格式')
                            finally:
                                break
                    elif cho6=='q':
                        break
                    else:
                        print('输入有误,请重新输入')

        elif cho1=='3':
            typec1=input('新增班级名称')
            typec2=input('新增教室地点')
            typec3=input('新增课程类型')
            cur.execute("insert into class (cname,rname,lesson) values ('%s','%s','%s')"%(typec1,typec2,typec3))
            conn.commit()
            print('新增成功')	
        elif cho1=='q':
            break
        else:
            print('输入有误,请重新输入')
        
        cur.close()

def 查询():
    while 1:

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
            print('*'*70)
            cho=input('''	   	   
        查询学生所有信息请输入:1
        查询学生部分信息请输入:2
        查询学生就业信息请输入:3
        查询班级学生信息请输入:4
        模糊检索学生姓名请输入:5
        退出请按输入:q  
                                ''')
            if cho=='1':
            
                print('*'*70)
                chall=input('请选择您需要查询的方式:a.通过名字查询 b.通过号码查询 ')
                if chall=='a':
                    while 1:
                        checkname=input('请输入需要查询的姓名: ')
                        if len(cha1(checkname))==0:
                            print('请输入正确的姓名!')
                            continue
                        else:
                    
                            print('*'*70)
                            cha2(checkname)
                            cha5(checkname)
                            cha3(checkname)
                            cha4(checkname)
                            break
                elif chall=='b':
                    
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
                            cha5(a)
                            cha3(a)
                            cha4(a)
                else:
                    print('输入有误,请重新输入')
            elif cho=='2':
                while 1:
                    
                    print('*'*70)
                    cho1=input('请选择您的查询方式:a.通过名字查询 b.通过号码查询  q.退出')#选项,通过名字查a还是号码查b退出q	
                    if cho1=='a':
                        while 1:
                            checkname=input('请输入需要查询的姓名: ')
                            if len(cha1(checkname))==0:
                                print('请输入正确的姓名!')
                                continue
                            else:
                                cha2(checkname)
                                cha5(checkname)
                                break
                    elif cho1=='b':
                        
                        print('*'*70)
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
                        print('')
            elif cho=='3':
                while 1:
                    
                    
                    print('*'*70)
                    cho1=input('请选择您的查询方式:a.通过名字查询 b.通过号码查询  q.退出')#选项,通过名字查a还是号码查b退出q	
                    if cho1=='a':
                        while 1:
                            checkname=input('请输入需要查询的姓名: ')
                            if len(cha3(checkname))==0:
                                print('请输入正确的姓名!')
                                continue
                            else:
                                cha4(checkname)
                                break
                    elif cho1=='b':
                        while 1:
                            checktel=input('请输入需要查询的电话: ')
                            cur.execute('select sname from student where tel="%s"'%checktel)
                            data=cur.fetchall()
                            if len(data)==0:
                                print('输入有误!')
                                continue
                            else:
                                for i in data:
                                    a=i[0]
                                    cha1(a)
                                    cha2(a)
                                    break
                    elif cho1=='q':
                        break
                    else:
                        print('输入有误,请重新输入')
                        
                        
                
            elif cho=='4':
                while 1:
                    
                    print('*'*70)
                    cho4=input('请输入您需要查询的班级,输入q退出')
                    if cho4=='q':
                        break
                    else:
                        cur.execute('select * from study where cname="%s"'%cho4)
                        data=cur.fetchall()
                        if len(data)==0:
                            print('无此班级!')
                        else:
                            for i in data:
                                print('姓  名:',i[1],'班级名称:',i[2],'考试成绩',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
                        
            elif cho=='5':
                while 1:
                
                    print('*'*70)
                    a=input('请输入要查询名字,输入quit退出')
                    if a=='quit':
                        break
                    else:
                        p=a+'%'
                        cur.execute('select * from student where sname like "%s"'%p)
                        data=cur.fetchall()
                        if len(data)==0:
                            print('无此类似学员姓名信息')
                            continue
                        else:
                            for i in data:
                                print('姓  名: ',i[1],'性  别:',i[4],'毕业学校: ',i[2],'联系方式:',i[3])	#查询学生部分信息
                                break
            elif cho=='q':
                break
            else:
                print('请正确选择需要办理的业务!')
            break
        break

        

def 修改():
    while 1:
        print('*'*70,'\n',)
        a=input('请输入需要更新信息的名字 (Q退出）')
        if a=='Q':
            break
        else:
            cur=conn.cursor()
            cur.execute('select * from student where sname="%s"'%a)
            data=cur.fetchall()
            for i in data:
                print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
            
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
                        1.sname名字			6.degree成绩       
                        2.tel电话			7.lagtime迟到次数
                        3.college大学			8.lapsetimes违纪次数
                        4.ssex性别			9.rname教室名称
                        5.cname课程名字			10.lesson课程    


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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))
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
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                        print(a)
                                        cur.execute("select * from student where sname='%s'"%a)
                                        cur1.execute("select * from study where sname='%s'"%a)
                                        cur2.execute("select * from job where sname='%s'"%a)
                                        cur3.execute("select * from hopping where sname='%s'"%a)
                                        
                                        data=cur.fetchall()
                                        for i in data:
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))							
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                            
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))
                                        
                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                        data1=cur1.fetchall()
                                        for l in data1:
                                            print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data2=cur2.fetchall()
                                        for l in data2:
                                            print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                        data3=cur3.fetchall()
                                        for l in data3:
                                            print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))

                                                                    
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
                                            print('原名字： ',a)
                                            print('新改的名字： ',newname)
                                            cur=conn.cursor()
                                            cur.execute('update student set sname="%s" where sname="%s"'%(newname,a))
                                            conn.commit()
                                            cur.execute('update hopping set sname="%s" where sname="%s"'%(newname,a))
                                            conn.commit()
                                            cur.execute('update job set sname="%s" where sname="%s"'%(newname,a))
                                            conn.commit()
                                            cur.execute('update study set sname="%s" where sname="%s"'%(newname,a))
                                            conn.commit()
                                            cur.execute('update student set tel="%s" wher1e sname="%s"'%(newtel,newname))
                                            conn.commit()
                                            cur.execute('update student set college="%s" where sname="%s"'%(college,newname))
                                            conn.commit()
                                            cur.execute('update student set ssex="%s" where sname="%s"'%(sex,newname))
                                            conn.commit()
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
                                                print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                                            data1=cur1.fetchall()
                                            for l in data1:
                                                print("班级名字:>>>%s,成绩：>>>%s,迟到次数：>>>%s,违纪次数：>>>%s"%(l[2],l[3],l[4],l[5]))
                                            data2=cur2.fetchall()
                                            for l in data2:
                                                print("参加工作时间：>>>%s;毕业时间:>>>%s,工资：>>>%s,公司：>>>%s"%(l[2],l[3],l[4],l[5]))
                                            data3=cur3.fetchall()
                                            for l in data3:
                                                print("新公司:>>>%s,跳槽后薪水：>>>%s,跳槽时间：>>>%s"%(l[2],l[3],l[4]))
                        except Exception as result:
                            print('请输入正确的格式')
                        finally:
                            break
                        

                    
                elif b=='Q' or 'q':
                    continue
                else:	
                    print('输入有误,请重新输入')
        



        cur.close()		

def 删除():
    cur=conn.cursor()
    a=input('欢迎来到删除系统,输入1开始删除程序,输入其他退出本系统')
    while 1:
        if a=='1':
            y=input('请查询你要删除的名字(可能有多个名字,先查询>>>输入Q退出)')
            if y=='Q':
                break
            else:
                p=y+'%'
                
                cur.execute("select * from student where sname like'%s'"%p)
                data=cur.fetchall()
                for i in data:
                    print('*'*70,'\n',"SID:>>>%d;名字:>>>%s;性别:>>>%s;学校:>>>%s ;tel:>>>%s"%(i[0],i[1],i[2],i[3],i[4]))
                b=input('请输入你要删除的名字')
                c=input('请输入与上边名字对应的电话')
                cur=conn.cursor()
                cur.execute("select * from student where sname='%s' and tel='%s'"%(b,c))
                data=cur.fetchall()
                if len(data)==0:
                    print('输入信息不存在,请重新输入')
                    continue
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
                            break
                
                        

                    else:
                        continue
                
        else:
            break
    cur.close()


while 1:

    userinput=input('请选择你所需要的功能： 1>查询; 2>增添 ;3>修改 ;4>删除 ;任意键>>>退出 ')
    if userinput=='1':
        查询()

    elif userinput=='2':
        增添()

    elif userinput=='3':
        修改()

    elif userinput=='4':

        删除()
    
    else:
        break





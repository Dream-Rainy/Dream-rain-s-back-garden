import pymysql
import random
#外部数据读入(MySQL)(摇号)
#region
yaohaoAttributes=[]
yaohaoall=[]
yaohaoboy=[]
yaohaogirl=[]
flagChinesedictation='True'
updatedatabase=''
jg=''
sx=0
temp=''
yaohaoallfrequency=-1
yaohaoboyfrequency=-1
yaohaogirlfrequency=-1
#打开数据库连接
db=pymysql.connect(host='localhost',user='root',password='200310.28',database='ssdq')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#使用 execute()  方法执行 SQL 查询 
sql='SELECT * FROM yaohao'
try:
    #执行SQL语句
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        if row[0]==0:
            Rounds=row[1]
        else:
            yaohaoall.append(row[0])
            yaohaoAttributes.append(row[1])
            yaohaoallfrequency=yaohaoallfrequency+1
            if row[2]=='男':
                yaohaoboy.append(row[0])
                yaohaoboyfrequency=yaohaoboyfrequency+1
            else:
                yaohaogirl.append(row[0])
                yaohaogirlfrequency=yaohaogirlfrequency+1
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
#endregion
def jgsc():
    global jg
    global sx
    global temp
    global updatedatabase
    if sx==0:
        temp=str(yaohaoall[random.randint(0,yaohaoallfrequency)])
    elif sx==1:
        temp=str(yaohaoboy[random.randint(0,yaohaoboyfrequency)])
    else:
        temp=str(yaohaogirl[random.randint(0,yaohaogirlfrequency)])
    temp=cc()
    temp=gsh()
    return(temp)
def gsh():
    global temp
    k=temp
    for j in range(0,3-len(temp)):
        k=k+' '
    return k
def cc():
    global jg
    global temp
    global flagChinesedictation
    global jieguo
    k1=''
    if jieguo==1:
        while yaohaoAttributes[int(temp)-1]==9999 or flagChinesedictation=='True' and yaohaoAttributes[int(temp)-1]==9998 or flagChinesedictation=='True' and yaohaoAttributes[int(temp)-1]==Rounds+1:
            temp=jgsc()
    for i in range(1,len(jg)+1):
        k2=jg[i-1:i]
        if k2!=' ':
            k1=k1+k2
        elif k1!='':
            while k1==temp or yaohaoAttributes[int(temp)-1]==9999 or flagChinesedictation=='True' and yaohaoAttributes[int(temp)-1]==9998 or flagChinesedictation=='True' and yaohaoAttributes[int(temp)-1]==Rounds:
                temp=jgsc()
            k1=''
    return temp
jg=''
updatedatabase=input('请输入是否更新数据库')
print(updatedatabase)
sx1=input('tiaojian')
sx=int(sx1)
rs1=input('shumu')
rs=int(rs1)
for jieguo in range(1,rs+1):
    jg+=jgsc()
    if yaohaoAttributes[int(temp)-1]!=9998 and updatedatabase=="true":
        yaohaoAttributes[int(temp)-1]=yaohaoAttributes[int(temp)-1]+1
print(jg)
if updatedatabase=="true":
    #打开数据库连接
    db=pymysql.connect(host='localhost',user='root',password='200310.28',database='ssdq')
    #使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    xuehao=1
    for yaohaoAttributesupdate in yaohaoAttributes:
        update_sql = "UPDATE yaohao SET 属性="+str(yaohaoAttributesupdate)+" WHERE 学号="+str(xuehao)
        try:
            #执行SQL语句
            cursor.execute(update_sql)
            #提交到数据库执行
            db.commit()#数据的改变需要执行这个命令
            xuehao=xuehao+1
        except:
            jg="数据库更新失败！"
            #发生错误时回滚
            db.rollback()
    #更新Rounds
    flagupdate=False
    for i in yaohaoAttributes:
        if i==Rounds:
            flagupdate=True
            break
    if flagupdate==False:
        Rounds=Rounds+1
        update_sql = "UPDATE yaohao SET 属性="+str(Rounds)+" WHERE 学号=0"
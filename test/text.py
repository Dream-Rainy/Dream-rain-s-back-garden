from email.policy import default
import random
from re import MULTILINE
import time
import pymysql
verify=''
id='DreamRain'
password1='200310.28'
flagcz=False
verify1=''
millis1=''
for i in range(1,9): #八位验证码
    randomstr = random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
    verify += randomstr
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
# 发信方的信息：发信邮箱，腾讯免费企业邮授权码
from_addr = 'no-reply@ckmnq.xyz'
password = 'rfWMha93aAuKM5bc'
# 收信方邮箱
to_addr = 'www.2289533715@qq.com'
# 发信服务器
smtp_server = 'smtp.exmail.qq.com'
"""标题"""
head="邮箱验证码"
"""正文"""
text=f'【阴阳师工具小站】您的验证码：{verify}，该验证码5分钟内有效，请勿泄漏于他人！'
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(text,'html','utf-8')
# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header(head)
# 开启发信服务，这里使用的是加密传输
#server = smtplib.SMTP_SSL()
server=smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
try:
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('邮件发送成功！')
except Exception as ex :
    print ("Error: 无法发送邮件",ex)
# 关闭服务器
server.quit()
millis = int(round(time.time()))
#mysql数据存入
db=pymysql.connect(host='localhost',user='root',password='200310.28',database='ssdq')
cursor=db.cursor()
query_sql="SELECT * FROM account"
try:
    cursor.execute(query_sql)
    #获取所有数据
    results = cursor.fetchall()
    #获得属性名称和长度（list）
    fields = cursor.description
    n = len(fields)#
    for row in results:
        if row[0]==id:
            flagcz=True
            break
except:
    print("获取数据失败")
if flagcz==False:
    try:
        sql = "INSERT INTO account(id, \
       touxiang, email, yzm, time ,password) \
       VALUES ('%s', '%s',  '%s',  '%s',  '%s', '%s')" % \
       (id, '/static/moren.png', to_addr, verify, millis , password1)
        cursor.execute(sql)
        db.commit()
    except:
        print("插入失败")
        db.rollback()
else:
    update_sql = "UPDATE account SET yzm='"+verify+"'"+" WHERE id='"+id+"'"
    print(update_sql)
    try:
        #执行SQL语句
        cursor.execute(update_sql)
        #提交到数据库执行
        db.commit()#数据的改变需要执行这个命令
    except:
        print("更新失败！")
        #发生错误时回滚
        db.rollback()
    update_sql = "UPDATE account SET time='"+str(millis)+"'"+" WHERE id='"+id+"'"
    print(update_sql)
    try:
        #执行SQL语句
        cursor.execute(update_sql)
        #提交到数据库执行
        db.commit()#数据的改变需要执行这个命令
    except:
        print("更新失败！")
        #发生错误时回滚
        db.rollback()
flag=True
sycs=3
while flag and int(round(time.time()))-millis<=300 and sycs!=0:
    yzmsr=input("请输入验证码")
    if len(yzmsr)!=8:
        print("验证码位数不正确！")
    elif yzmsr==verify:
        print('验证成功！')
        flag=False
    else:
        if int(round(time.time()))-millis>300:
            print('该验证码已经失效，请尝试重新注册！')
            break
        else:
            sycs=sycs-1
            print('验证失败！请重试！剩余次数：'+str(sycs)+"次")
if sycs==0:
    print("剩余次数耗尽！请尝试重新注册！")
if flag==True and flagcz==False:
    delete_sql = "DELETE FROM account WHERE id='"+id+"'"
    try:
        cursor.execute(delete_sql)
        db.commit()#提交数据库执行删除
    except:
        print("删除数据失败！")
        db.rollback()#有错误时进行回滚
db.close
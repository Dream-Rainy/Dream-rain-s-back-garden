#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#模块导入
#region
import json
from operator import length_hint
import re
import os
import random
import datetime
import pymysql
from flask import Flask,request,render_template,jsonify,send_from_directory, template_rendered
import time
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
#endregion
#列表定义
#region
flagChinesedictation=''
updatedatabase=''
jg=''
sx=0
temp=''
rmc=[]
srmc=[]
ssrmc=[]
spmc=[]
specialname=['桔梗碎片','犬夜叉碎片','杀生丸碎片']
specialSkinmc=[]
flagspecialSkin=[]
flagwsl=False
flagpiece=True
activityname='寒祭灼魂，心火永明'
app = Flask(__name__, static_folder='static') 
#endregion
#外部数据读入(MySQL)(式神)
#region
#打开数据库连接
db=pymysql.connect(host='localhost',user='',password='',database='')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#使用 execute()  方法执行 SQL 查询 
sql='SELECT * FROM ssdq'
try:
    #执行SQL语句
    cursor.execute(sql)
    #获取所有记录列表
    results = cursor.fetchall()
    for row in results:
            if row[0]=='R':
                rmc.append(row[1])
            elif row[0]=='SR':
                srmc.append(row[1])
            elif row[0]=='SSR':
                ssrmc.append(row[1])
                if row[2]=='有':
                    specialSkinmc.append(row[3])
                    flagspecialSkin.append(True)
                else:
                    specialSkinmc.append(row[3])
                    flagspecialSkin.append(False)
            elif row[0]=='SP':
                spmc.append(row[1])
    specialSkinmc.append('玉藻前·真红')
    flagspecialSkin.append(True)
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
#endregion
#自定义函数
#region
#endregion
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'),404
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
@app.route('/', methods=['GET'])
def index():
    id = request.cookies.get('account')
    yzm = request.cookies.get('weiyiyzm')
    db=pymysql.connect(host='localhost',user='',password='',database='')
    cursor=db.cursor()
    query_sql="SELECT * FROM account"
    try:
        cursor.execute(query_sql)
        #获取所有数据
        results = cursor.fetchall()
        for row in results:
            if row[0]==id and row[7]==yzm:
                return render_template('index.html',dl='欢迎您，'+id,lj='/account',specialname=specialname,activityname=activityname)
        return render_template('index.html',dl='登陆',lj='/login',specialname=specialname,activityname=activityname)
    except:
        return render_template('index.html',dl='登陆',lj='/login',specialname=specialname,activityname=activityname)
@app.route('/chouka',methods=['GET'])
def DrawCardData():#抽卡数据获取
    flagupssr=False
    flagupsp=False
    flagupspecial=False
    flagpiece=False
    for name in specialname:
        if name=='神劵':
            flagupspecial=True
        elif re.search('印花', name)!=None:
            flagpiece=True
        else:
            for name1 in ssrmc:
                if name1==name:
                    flagupssr=True
                else:
                    flagupsp=True
    if flagupssr==True or flagpiece==True or flagupspecial==True:
        flagupsp=False
    data={
    'flagpiece':flagpiece,
    'flagwsl':flagwsl,
    'flagupspecial':flagupspecial,
    'flagupsp':flagupsp,
    'flagupssr':flagupssr,
    'rmc':rmc,
    'srmc':srmc,
    'ssrmc':ssrmc,
    'spmc':spmc,
    'specialSkinmc':specialSkinmc,
    'flagspecialSkin':flagspecialSkin
    }
    return jsonify(data)
@app.route('/accountinfo',methods=['POST'])
def accountinfoget():
    accountname=request.cookies.get('account')
    paths=os.path.join(os.path.abspath('.'),'static','account',accountname,'AccountInfo.json')
    with open(paths, 'r' , errors='ignore') as f:
        data=f.read()
    return jsonify(data)
@app.route('/register',methods=['GET'])
def registerPage():#获取注册页面
    return render_template('registerPage.html')
@app.route('/register',methods=['POST'])
@app.route('/register',methods=['POST'])
def register():#注册信息处理
    zcjg=''
    hqyzm=request.form.get('flagyzm')
    id=request.form.get('id')
    password1=request.form.get('pass')
    # 收信方邮箱
    to_addr = request.form.get('email')
    db=pymysql.connect(host='localhost',user='',password='',database='')
    cursor=db.cursor()
    if hqyzm=='True':
        verify=''
        query_sql="SELECT * FROM account"
        try:
            cursor.execute(query_sql)
            #获取所有数据
            results = cursor.fetchall()
            for row in results:
                if row[0]==id:
                    results={
                        'success':500,
                        'zcjg':'该用户名已被占用！'
                    }
                    return jsonify(results)
                elif row[2]==to_addr:
                    results={
                        'success':500,
                        'zcjg':'该邮箱已被占用！'
                    }
                    return jsonify(results)
        except:
            zcjg="获取数据失败"
            results={
                        'success':500,
                        'zcjg':zcjg
                    }
            return jsonify(results)
        for i in range(1,9): #八位验证码
            randomstr = random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
            verify += randomstr
        # 用于构建邮件头
        # 发信方的信息：发信邮箱，腾讯免费企业邮授权码
        from_addr = ''
        password = ''
        # 发信服务器
        smtp_server = 'smtp.exmail.qq.com'
        """标题"""
        head="邮箱验证码"
        """正文"""
        text=f'【梦雨的后花园】您正在注册梦雨的后花园账号，验证码是：{verify}，该验证码5分钟内有效，请勿泄漏于他人！若该邮件并非由您本人请求，请忽略！'
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
        millis = int(round(time.time()))
        #mysql数据存入
        try:
            sql = "INSERT INTO account(id, \
            touxiang, email, yzm, time ,password,cs) \
            VALUES ('%s', '%s',  '%s',  '%s',  '%s', '%s', '%s')" % \
            (id, '/static/account/moren.jpg', to_addr, verify, millis , password1, 3)
            cursor.execute(sql)
            db.commit()
            db.close
            try:
                # 发送邮件
                server.sendmail(from_addr, to_addr, msg.as_string())
                yzmjg='邮件发送成功！'
            except Exception as ex :
                yzmjg="Error: 无法发送邮件",ex
            # 关闭服务器
            server.quit()
            results={
                'success':200,
                'yzmjg':yzmjg,
            }
            return jsonify(results)
        except:
            zcjg="账户新建失败"
            db.rollback()
            db.close
            results={
                'success':500,
                'zcjg':zcjg,
            }
            return jsonify(results)
    else:
        flagcz=False
        query_sql="SELECT * FROM account"
        try:
            cursor.execute(query_sql)
            #获取所有数据
            results = cursor.fetchall()
            for row in results:
                if row[0]==id:
                    flagcz=True
                    verify=row[3]
                    millis=row[4]
                    sycs=row[6]
                    break
        except:
            zcjg="获取数据失败"
            results={
                    'success':500,
                    'zcjg':zcjg,
                }
            return jsonify(results)
        if flagcz==False:
            zcjg='请先获取验证码！'
            results={
                        'success':500,
                        'zcjg':zcjg
                    }
            return jsonify(results)
        if int(round(time.time()))-int(millis)<=300 and sycs!=0:
            yzmsr=request.form.get('yzm')
            if len(yzmsr)!=8:
                zcjg="验证码位数不正确！"
                results={
                    'success':500,
                    'zcjg':zcjg,
                }
                return jsonify(results)
            elif yzmsr==verify:
                zcjg='验证成功！'
                results={
                    'success':200,
                    'zcjg':zcjg,
                }
                try:
                    paths=os.path.join(os.path.abspath('.'),'static','account',id)
                    os.mkdir(paths)
                    files = os.path.join(paths,"AccountInfo.json")
                    f=open(files,'w')
                    f.close()
                except:
                    zcjg+="新建文件出错"
                    results={
                        'success':200,
                        'zcjg':zcjg
                    }
                    return jsonify(results)
            else:
                if int(round(time.time()))-int(millis)>300:
                    zcjg='该验证码已经失效，请尝试重新注册！'
                    results={
                        'success':200,
                        'zcjg':zcjg
                    }
                    return jsonify(results)
                else:
                    sycs=sycs-1
                    zcjg='验证失败！请重试！剩余次数：'+str(sycs)+"次"
                    update_sql = "UPDATE account SET cs="+str(sycs)+" WHERE id='"+id+"'"
                    try:
                        #执行SQL语句
                        cursor.execute(update_sql)
                        #提交到数据库执行
                        db.commit()#数据的改变需要执行这个命令
                    except:
                        zcjg=+"更新失败！"
                        #发生错误时回滚
                        db.rollback()
                results={
                    'success':500,
                    'zcjg':zcjg,
                }
            return jsonify(results)
        if sycs==0:
            delete_sql = "DELETE FROM account WHERE id='"+id+"'"
            try:
                cursor.execute(delete_sql)
                db.commit()#提交数据库执行删除
                db.close
            except:
                zcjg+="删除数据失败！"
                db.rollback()#有错误时进行回滚
                db.close
                results={
                    'success':500,
                    'zcjg':zcjg,
                }
                return jsonify(results)
            zcjg="剩余次数耗尽！请尝试重新注册！"
            results={
                'success':500,
                'zcjg':zcjg,
            }
            return jsonify(results)
@app.route('/login',methods=['GET'])
def loginPage():#获取登陆页面
    return render_template('loginPage.html')
@app.route('/login',methods=['POST'])
def login():#登陆信息处理
    id=request.form.get('zh')
    password=request.form.get('pass')
    outdate=datetime.datetime.today() + datetime.timedelta(days=30) 
    flagdl=False
    db=pymysql.connect(host='localhost',user='',password='',database='')
    cursor=db.cursor()
    query_sql="SELECT * FROM account"
    cursor.execute(query_sql)
    #获取所有数据
    results = cursor.fetchall()
    for row in results:
        if row[0]==id or row[3]==id:
            flagdl=True
            if password==row[5]:
                temp=int(round(time.time()))
                weiyiyzm=''
                for i in range(1,4): #随机取四位唯一验证码
                    randomstr = random.choice(str(temp))
                    weiyiyzm+=randomstr
                for i in range(1,8): #八位附加验证码
                    randomstr = random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
                    weiyiyzm+=randomstr
                update_sql = "UPDATE account SET weiyiyzm='"+weiyiyzm+"' WHERE id='"+id+"'"
                try:
                    #执行SQL语句
                    cursor.execute(update_sql)
                    #提交到数据库执行
                    db.commit()#数据的改变需要执行这个命令
                    results={
                        'success':200,
                        'account':id,
                        'weiyiyzm':weiyiyzm,
                        'time':outdate,
                    }
                    return jsonify(results)
                except:
                    #发生错误时回滚
                    db.rollback()
                    results={
                        'success':406,
                        'dljg':'登陆失败！cookies设置失败，请重试或联系网站管理员！'
                    }
                    return jsonify(results)
            else:
                results={
                    'success':500,
                    'dljg':'登陆失败！密码错误！'
                }
                return jsonify(results)
    if flagdl==False:
        results={
                    'success':404,
                    'dljg':'该账户不存在，前往注册？'
                }
        return jsonify(results)
@app.route('/findpassword', methods=['GET'])
def findPassWordBackPage():#获取找回密码页面
    return render_template('findPassWordBackPage.html')
@app.route('/findpassword', methods=['POST'])
def findPassWordBack():#找回密码信息处理
    hqyzm=request.form.get('flagyzm')
    id=request.form.get('id')
    passWord=request.form.get('pass')
    # 收信方邮箱
    to_addr = request.form.get('email')
    db=pymysql.connect(host='localhost',user='',password='',database='')
    cursor=db.cursor()
    if hqyzm=='True':
        zcjg=''
        flag=False
        verify=''
        query_sql="SELECT * FROM account"
        try:
            cursor.execute(query_sql)
            #获取所有数据
            results = cursor.fetchall()
            for row in results:
                if row[3]==to_addr:
                    flag=True
        except:
            zcjg="获取数据失败"
        if flag==False:
            if zcjg=='':
                zcjg='账户不存在，请确认是否有输入错误或前往注册'
            results={
                'success':500,
                'zcjg':zcjg,
            }
            return jsonify(results)
        for i in range(1,9): #八位验证码
            randomstr = random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
            verify += randomstr
        # 用于构建邮件头
        # 发信方的信息：发信邮箱
        from_addr = ''
        password = ''
        # 发信服务器
        smtp_server = ''
        """标题"""
        head="邮箱验证码"
        """正文"""
        text=f'【梦雨的后花园】您正在您正在找回登录密码，验证码是：{verify}，该验证码5分钟内有效，请勿泄漏于他人！ 若该邮件并非由您本人请求，请忽略！'
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
        millis = int(round(time.time()))
        #mysql数据存入
        try:
            update_sql = "UPDATE account SET yzm=\""+str(verify)+"\",cs=3,time="+str(millis)+" WHERE id='"+id+"'"
            #执行SQL语句
            cursor.execute(update_sql)
            #提交到数据库执行
            db.commit()#数据的改变需要执行这个命令
            try:
                # 发送邮件
                server.sendmail(from_addr, to_addr, msg.as_string())
                yzmjg='邮件发送成功！'
            except Exception as ex :
                yzmjg="Error: 无法发送邮件",ex
            # 关闭服务器
            server.quit()
            results={
                'success':200,
                'yzmjg':yzmjg,
            }
            return jsonify(results)
        except:
            zcjg="邮件验证码更新失败"
            db.rollback()
            db.close
            results={
                'success':500,
                'zcjg':zcjg,
            }
            return jsonify(results)
    else:
        query_sql="SELECT * FROM account"
        try:
            flagcz=False
            cursor.execute(query_sql)
            #获取所有数据
            results = cursor.fetchall()
            for row in results:
                if row[0]==id:
                    flagcz=True
                    verify=row[3]
                    millis=row[4]
                    sycs=row[6]
                    break
        except:
            zcjg="获取数据失败"
            results={
                    'success':500,
                    'zcjg':zcjg,
                }
            return jsonify(results)
        if flagcz==False:
            results={
                'success':404,
                'zcjg':'该账户不存在，前往注册？',
            }
            return jsonify(results)
        if int(round(time.time()))-int(millis)<=300 and sycs!=0:
            yzmsr=request.form.get('yzm')
            if len(yzmsr)!=8:
                zcjg="验证码位数不正确！"
                results={
                    'success':500,
                    'zcjg':zcjg,
                }
                return jsonify(results)
            elif yzmsr==verify:
                zcjg='验证成功！'
                try:
                    update_sql = "UPDATE account SET password="+passWord+" WHERE id='"+id+"'"
                    #执行SQL语句
                    cursor.execute(update_sql)
                    #提交到数据库执行
                    db.commit()#数据的改变需要执行这个命令
                    results={
                        'success':200,
                        'zcjg':zcjg,
                    }
                    return jsonify(results)
                except:
                    zcjg="数据库密码更新失败！"
                    db.rollback()
                    db.close
                    results={
                        'success':500,
                        'zcjg':zcjg,
                    }
                    return jsonify(results)
            else:
                if int(round(time.time()))-int(millis)>300:
                    zcjg='该验证码已经失效，请尝试重新获取！'
                else:
                    sycs=sycs-1
                    zcjg='验证失败！请重试！剩余次数：'+str(sycs)+"次"
                    update_sql = "UPDATE account SET cs="+str(sycs)+" WHERE id='"+id+"'"
                    try:
                        #执行SQL语句
                        cursor.execute(update_sql)
                        #提交到数据库执行
                        db.commit()#数据的改变需要执行这个命令
                    except:
                        zcjg=+"更新失败！"
                        #发生错误时回滚
                        db.rollback()
                results={
                    'success':500,
                    'zcjg':zcjg,
                }
            return jsonify(results)
        if sycs==0:
            zcjg="剩余次数耗尽！请尝试重新获取验证码！"
            results={
                'success':500,
                'zcjg':zcjg,
            }
            return jsonify(results)
@app.route('/account', methods=['GET'])
def accountPageGET():
    id = request.cookies.get('account')
    yzm = request.cookies.get('weiyiyzm')
    db=pymysql.connect(host='localhost',user='',password='',database='')
    cursor=db.cursor()
    query_sql="SELECT * FROM account"
    flag=False
    try:
        cursor.execute(query_sql)
        #获取所有数据
        results = cursor.fetchall()
        for row in results:
            if row[0]==id and row[7]==yzm:
                name=id
                touxiang=row[1]
                flag=True
    except:
        return render_template('index.html',dl='登陆',lj='/login')
    if flag==False:
        return render_template('index.html',dl='登陆',lj='/login')
    else:
        ssmc={
            'rmc':rmc,
            'srmc':srmc,
            'ssrmc':ssrmc,
            'spmc':spmc,
        }
        return render_template('account.html',name=name,touxiang=touxiang,**ssmc)
@app.route('/account', methods=['POST'])
def accountPagePOST():
    id=request.cookies.get('account')
    passWord=request.form.get('pass')
    flagChangePassWord=request.form.get('flag')
    db=pymysql.connect(host='localhost',user='',password='',database='')
    cursor=db.cursor()
    changeResult="密码修改成功！"
    if flagChangePassWord=='True':
        try:
            update_sql = "UPDATE account SET password="+passWord+" WHERE id='"+id+"'"
            #执行SQL语句
            cursor.execute(update_sql)
            #提交到数据库执行
            db.commit()#数据的改变需要执行这个命令
            results={
                'success':200,
                'changeResult':changeResult,
            }
            return jsonify(results)
        except:
            changeResult="数据库密码更新失败！"
            db.rollback()
            db.close
            results={
                'success':500,
                'changeResult':changeResult,
            }
            return jsonify(results)
    else:
        rinfo=request.form.getlist('rinfo[]')
        srinfo=request.form.getlist('srinfo[]')
        ssrinfo=request.form.getlist('ssrinfo[]')
        spinfo=request.form.getlist('spinfo[]')
        accountname=request.cookies.get('account')
        info={
            'r':rinfo,
            'sr':srinfo,
            'ssr':ssrinfo,
            'sp':spinfo
        }
        paths=os.path.join(os.path.abspath('.'),'static','account',accountname,'AccountInfo.json')
        with open(paths, 'w' , errors='ignore') as f:
            json.dump(info,f)
            changeResult="载入文件完成..."
            print(info)
            results={
                'success':200,
                'changeResult':changeResult,
            }
        return jsonify(results)
@app.route('/setu', methods=['GET'])
def setu():
    return render_template('setu.html')
@app.route('/admin',methods=['GET'])
def adminget():
    return render_template('admin.html')
@app.route('/admin',methods=['POST'])
@app.route('/admin',methods=['POST'])
def adminpost():
    global specialname
    global flagwsl
    global activityname
    changeResult=''
    pj=request.form.get('pj')
    mc=request.form.get('mc')
    spflag=request.form.get('spflag')
    spmc1=request.form.get('spmc1')
    spmc2=request.form.get('spmc2')
    activityname=request.form.get('activityname')
    glupss=request.form.get('glupss')
    wslflag=request.form.get('wslflag')
    if wslflag=="无":
        flagwsl=False
    elif wslflag=="有":
        flagwsl=True
    data={
        'pj':pj,
        'mc':mc,
        'spflag':spflag,
        'spmc1':spmc1,
        'spmc2':spmc2,
        'activityname':activityname,
        'glupss':glupss,
        'wslflag':wslflag
    }
    print(data)#测试用,可以删
    a = glupss.split(",")
    print(a)
    specialname.clear()
    specialname=a
    db=pymysql.connect(host='localhost',user='',password='',database='ssdq')
    cursor = db.cursor()
    try:
        sql = "INSERT INTO ssdq(品阶, 式神名称, 有无SP皮肤, SP皮肤名称, SP皮肤名称2) \
        VALUES ('%s', '%s',  '%s',  '%s',  '%s')" % \
        (pj,mc,spflag,spmc1,spmc2)
        cursor.execute(sql)
        db.commit()
        db.close
    except:
        changeResult="数据新建失败"
        db.rollback()
        db.close
        results={
            'success':500,
            'changeResult':changeResult,
        }
        return jsonify(results)
    results={
        'success':200
    }
    return jsonify(results)
@app.route('/yaohao',methods=['GET'])
if __name__ == '__main__':
    app.run(debug=True)
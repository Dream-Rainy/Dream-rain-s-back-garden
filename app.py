#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#模块导入
#region
import re
import random
import pymysql
from flask import Flask,request,render_template,jsonify,send_from_directory
#endregion
#变量设定
#region
rmc=[]
srmc=[]
ssrmc=[]
spmc=[]
specialname=['无']
specialSkinmc=[]
flagspecialSkin=[]
flagwsl=False
activityname='迦楼罗'
app = Flask(__name__, static_folder='static') 
#endregion
#外部数据读入(MySQL)
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
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'),404
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
@app.route('/', methods=['GET'])
def index():
def index():
    ssmc={
        'ssrmc':ssrmc,
        'spmc':spmc,
    }
    return render_template('index.html',specialname=specialname,activityname=activityname,**ssmc)
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
    if flagupssr==True:
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
@app.route('/admin',methods=['GET'])
def adminget():
    return render_template('admin.html')
@app.route('/admin',methods=['POST'])
@app.route('/admin',methods=['POST'])
def adminpost():
    global specialname
    global flagwsl
    global activityname
    activitynametemp=activityname
    changeResult=''
    pj=request.form.get('pj')
    mc=request.form.get('mc')
    spflag=request.form.get('spflag')
    spmc1=request.form.get('spmc1')
    spmc2=request.form.get('spmc2')
    activityname=request.form.get('activityname')
    glupss=request.form.get('glupss')
    wslflag=request.form.get('wslflag')
    if wslflag=="无" or wslflag=="":
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
    print(data)
    a = glupss.split(",")
    print(a)
    specialname.clear()
    specialname=a
    if activityname=="":
        activityname=activitynametemp
    if pj!="":
        db=pymysql.connect(host='',user='',password='',database='')
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
        #使用 execute()  方法执行 SQL 查询 
        rmc.clear()
        srmc.clear()
        ssrmc.clear()
        spmc.clear()
        specialSkinmc.clear()
        flagspecialSkin.clear()
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
            db.close
            changeResult="Error: unable to fetch data"
            results={
                'success':500,
                'changeResult':changeResult,
            }
            return jsonify(results)
        # 关闭数据库连接
        db.close()
    results={
        'success':200
    }
    return jsonify(results)
@app.route('/yaohao',methods=['GET'])
if __name__ == '__main__':
    app.run(debug=True)
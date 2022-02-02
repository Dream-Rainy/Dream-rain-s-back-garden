import re
Email='jcottonq@163.com'
Emails=[]
Emails.append(Email)
EmailRegular=re.compile(r"[^@]+@[^@]+\.[^@]+")
for each in Emails:
    if not EmailRegular.match(each):
        print(False)
    else:
        print(True)
#式神基础信息，前台输入，以后更新，现在手动输入
import random
n=input("输入模拟次数")#获取模拟次数
RedFormula=[]#以下数据暂时内嵌代码
BlueFormula=[]
#式神血量存储
RedBlood=[]
BlueBlood=[]
#式神攻击
RedAttack=[]
BlueAttack=[]
#式神防御
RedDefence=[]
BlueDefence=[]
#式神速度
RedSpeed=[]
BlueSpeed=[]
#式神暴击
RedCrit=[]
BlueCrit=[]
#式神爆伤
RedCritDamage=[]
BlueCritDamage=[]
#式神命中
RedHit=[]
BlueHit=[]
#式神抵抗
RedResistance=[]
BlueResistance=[]
#buff存储
RedActiveBuff=[]
BlueActiveBuff=[]
RedDeBuff=[]
BlueDeBuff=[]
#自动从shisheng.json文件获取式神信息
#没写好，手动输入，以后更新
RedSkill=[[[2,0.65,0,0],[],[],[]],]
BlueSkill=[]
#信息获取完成
#是否暴击判断
def Crit(Team,Location):#需要传入队伍和位置
    if Team=="Red":
        if random.random>=RedCrit[Location]:return(RedCritDamage[Location])
    else:
        if random.random>=BlueCrit[Location]:return(BlueCritDamage[Location])
    return(1)
#攻击过程
def Attack(Skill,Team,Location):#需要传入式神的位置和队伍以及是什么技能(Skill变量请传入Number)
    if Skill==1:#普通攻击
        if Team=="Red":#读取倍率
            affect=RedSkill[Skill]
        else:
            affect=BlueSkill[Skill]
        Target=random.randint(1,5)#选取对象
        if Team=="Red":#进行攻击
            while BlueBlood[Target]==0:Target=random.randint(1,5)
            BlueBlood[Target]=BlueBlood[Target]-RedAttack*Crit(Team,Location)*affect*(random.uniform(-0.15,0.15)+1)#攻击*爆伤*倍率*波动（如果遇到小小黑手动添加条件）
        else:
            while RedBlood[Target]==0:Target=random.randint(1,5)
            RedBlood[Target]=RedBlood[Target]-RedAttack*Crit(Team,Location)*affect*(random.uniform(-0.15,0.15)+1)#攻击*爆伤*倍率*波动（如果遇到小小黑手动添加条件）
#进入战斗模拟
for i in range(n):
    while sum(RedBlood)==0 or sum(BlueBlood)==0:
        pass
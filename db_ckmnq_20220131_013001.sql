-- MySQL dump 10.13  Distrib 5.5.62, for Linux (x86_64)
--
-- Host: localhost    Database: ckmnq
-- ------------------------------------------------------
-- Server version	5.5.62-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ssdq`
--

DROP TABLE IF EXISTS `ssdq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ssdq` (
  `品阶` varchar(45) NOT NULL,
  `式神名称` varchar(45) NOT NULL,
  `有无SP皮肤` varchar(45) NOT NULL,
  `SP皮肤名称` varchar(45) NOT NULL,
  `SP皮肤名称2` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ssdq`
--

LOCK TABLES `ssdq` WRITE;
/*!40000 ALTER TABLE `ssdq` DISABLE KEYS */;
INSERT INTO `ssdq` VALUES ('R','三尾狐','无','无','无'),('R','座敷童子','无','无','无'),('R','鲤鱼精','无','无','无'),('R','九命猫','无','无','无'),('R','狸猫','无','无','无'),('R','河童','无','无','无'),('R','童男','无','无','无'),('R','童女','无','无','无'),('R','饿鬼','无','无','无'),('R','巫蛊师','无','无','无'),('R','鸦天狗','无','无','无'),('R','食发鬼','无','无','无'),('R','武士之灵','无','无','无'),('R','雨女','无','无','无'),('R','跳跳弟弟','无','无','无'),('R','跳跳妹妹','无','无','无'),('R','兵俑','无','无','无'),('R','丑时之女','无','无','无'),('R','独眼小僧','无','无','无'),('R','铁鼠','无','无','无'),('R','椒图','无','无','无'),('R','管狐','无','无','无'),('R','山兔','无','无','无'),('R','莹草','无','无','无'),('R','蝴蝶精','无','无','无'),('R','山童','无','无','无'),('R','首无','无','无','无'),('R','觉','无','无','无'),('R','青蛙瓷器','无','无','无'),('R','古笼火','无','无','无'),('R','虫师','无','无','无'),('SR','桃花妖','无','无','无'),('SR','雪女','无','无','无'),('SR','鬼使白','无','无','无'),('SR','鬼使黑','无','无','无'),('SR','孟婆','无','无','无'),('SR','犬神','无','无','无'),('SR','骨女','无','无','无'),('SR','鬼女红叶','无','无','无'),('SR','跳跳哥哥','无','无','无'),('SR','傀儡师','无','无','无'),('SR','海坊主','无','无','无'),('SR','判官','无','无','无'),('SR','凤凰火','无','无','无'),('SR','吸血姬','无','无','无'),('SR','妖狐','无','无','无'),('SR','妖琴师','无','无','无'),('SR','食梦貘','无','无','无'),('SR','清姬','无','无','无'),('SR','镰鼬','无','无','无'),('SR','姑获鸟','无','无','无'),('SR','二口女','无','无','无'),('SR','白狼','无','无','无'),('SR','樱花妖','无','无','无'),('SR','惠比寿','无','无','无'),('SR','络新妇','无','无','无'),('SR','般若','无','无','无'),('SR','青坊主','无','无','无'),('SR','夜叉','无','无','无'),('SR','黑童子','无','无','无'),('SR','白童子','无','无','无'),('SR','烟烟罗','无','无','无'),('SR','金鱼姬','无','无','无'),('SR','鸩','无','无','无'),('SR','以津真天','无','无','无'),('SR','匣中少女','无','无','无'),('SR','书翁','无','无','无'),('SR','百目鬼','无','无','无'),('SR','追月神','无','无','无'),('SR','熏','无','无','无'),('SR','弈','无','无','无'),('SR','猫掌柜','无','无','无'),('SR','於菊虫','无','无','无'),('SR','一反木绵','无','无','无'),('SR','入殓师','无','无','无'),('SR','化鲸','无','无','无'),('SR','久次良','无','无','无'),('SR','蟹姬','无','无','无'),('SR','纸舞','无','无','无'),('SR','星熊童子','无','无','无'),('SR','风狸','无','无','无'),('SR','蝎女','无','无','无'),('SSR','大天狗','有','大天狗·青竹','无'),('SSR','酒吞童子','有','酒吞童子·山吹','无'),('SSR','荒川之主','有','荒川之主·薄香','无'),('SSR','阎魔','有','阎魔·京紫','无'),('SSR','小鹿男','有','小鹿男·白堇','无'),('SSR','茨木童子','有','茨木童子·薄香','无'),('SSR','青行灯','有','青行灯·浅葱','无'),('SSR','妖刀姬','有','妖刀姬·真红','无'),('SSR','一目连','有','一目连·京紫','无'),('SSR','花鸟卷','有','花鸟卷·绀色','无'),('SSR','辉夜姬','有','辉夜姬·绀色','无'),('SSR','荒','有','荒·山吹','无'),('SSR','彼岸花','有','彼岸花·白堇','无'),('SSR','雪童子','有','雪童子·京紫','无'),('SSR','山风','有','山风·青竹','无'),('SSR','玉藻前','有','玉藻前·白堇','玉藻前·真红'),('SSR','御馔津','有','御馔津·青竹','无'),('SSR','面灵气','无','无','无'),('SSR','鬼切','有','无','无'),('SSR','白藏主','无','无','无'),('SSR','八岐大蛇','无','无','无'),('SSR','不知火','无','无','无'),('SSR','大岳丸','无','无','无'),('SSR','泷夜叉姬','无','无','无'),('SSR','云外镜','无','无','无'),('SSR','鬼童丸','无','无','无'),('SSR','缘结神','无','无','无'),('SSR','铃鹿御前','无','无','无'),('SSR','紧那罗','无','无','无'),('SSR','千姬','无','无','无'),('SSR','帝释天','无','无','无'),('SP','少羽大天狗','无','无','无'),('SP','炼狱茨木童子','无','无','无'),('SP','稻荷神御馔津','无','无','无'),('SP','苍风一目连','无','无','无'),('SP','骁浪荒川之主','无','无','无'),('SP','烬天玉藻前','无','无','无'),('SP','鬼王酒吞童子','无','无','无'),('SP','天剑韧心鬼切','无','无','无'),('SP','聆海金鱼姬','无','无','无'),('SP','浮世青行灯','无','无','无'),('SP','缚骨清姬','无','无','无'),('SP','待宵姑获鸟','无','无','无'),('SP','麓铭大岳丸','无','无','无'),('SP','初翎山风','无','无','无'),('SP','夜溟彼岸花','无','无','无'),('SP','蝉冰雪女','无','无','无'),('SSR','阿修罗','无','无','无'),('SP','空相面灵气','无','无','无'),('SP','绘世花鸟卷','无','无','无'),('SSR','饭笥','无','无','无'),('SSR','食灵','无','无','无'),('SR','饴细工','无','无','无'),('SR','川猿','无','无','无'),('SP','因幡辉夜姬','无','无','无');
/*!40000 ALTER TABLE `ssdq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ckmnq'
--

--
-- Dumping routines for database 'ckmnq'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-31  1:30:02

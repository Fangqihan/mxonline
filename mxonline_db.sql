-- MySQL dump 10.13  Distrib 5.7.21, for Win64 (x86_64)
--
-- Host: localhost    Database: mxonline_db
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `城市`
--

DROP TABLE IF EXISTS `城市`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `城市` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `城市`
--

LOCK TABLES `城市` WRITE;
/*!40000 ALTER TABLE `城市` DISABLE KEYS */;
INSERT INTO `城市` VALUES (1,'武汉','2018-06-27 16:27:00.000000'),(2,'广州','2018-06-27 16:27:00.000000'),(3,'北京','2018-06-27 16:27:00.000000'),(4,'上海','2018-06-27 16:28:00.000000'),(5,'成都','2018-06-27 16:28:00.000000'),(6,'江苏','2018-06-27 16:30:00.000000'),(7,'南京','2018-06-27 16:30:00.000000'),(8,'厦门','2018-06-27 16:32:00.000000');
/*!40000 ALTER TABLE `城市` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `教师`
--

DROP TABLE IF EXISTS `教师`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `教师` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `work_year` int(11) DEFAULT NULL,
  `work_position` varchar(20) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `introduction` varchar(100) NOT NULL,
  `click_num` int(11) NOT NULL,
  `favor_num` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `org_id` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `company` varchar(20) NOT NULL,
  `nick_name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `organization_teacher_org_id_cd000a1a_fk_organizat` (`org_id`),
  CONSTRAINT `organization_teacher_org_id_cd000a1a_fk_organizat` FOREIGN KEY (`org_id`) REFERENCES `课程机构` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `教师`
--

LOCK TABLES `教师` WRITE;
/*!40000 ALTER TABLE `教师` DISABLE KEYS */;
INSERT INTO `教师` VALUES (1,'乔峰','teacher/2018/06/4.png',22,'丐帮大学终身校长',46,'降龙十八掌独步武林',0,0,'2018-06-27 16:37:00.000000',1,'male','丐帮大学','乔帮主'),(2,'马云','teacher/2018/06/mayun.png',16,'阿里大学校长',33,'中国首富',22,18,'2018-06-27 16:42:00.000000',1,'male','阿里巴巴','JackMa');
/*!40000 ALTER TABLE `教师` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户信息`
--

DROP TABLE IF EXISTS `用户信息`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户信息` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nick_name` varchar(20) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(20) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户信息`
--

LOCK TABLES `用户信息` WRITE;
/*!40000 ALTER TABLE `用户信息` DISABLE KEYS */;
INSERT INTO `用户信息` VALUES (1,'pbkdf2_sha256$36000$0tyMNSAJa9Cg$q8SN0cdqwF28SxZTUS3ISEJCfagRSQ3Q73NK+S7U48E=','2018-06-27 16:01:34.645990',1,'admin','','','',1,1,'2018-06-27 16:00:55.939547','',NULL,'',NULL,NULL,'image/default.png'),(2,'pbkdf2_sha256$36000$T3qR7cNcZy3c$qFluuyuhWMHo8kKDFRD9Ek79q57Lp0pMNS49g3ypnWs=','2018-06-27 17:14:34.054136',0,'bob','','','',0,0,'2018-06-27 17:04:23.299678','神雕大侠','2018-06-05','male','终南山','100000000','image/2018/06/1.png'),(3,'pbkdf2_sha256$36000$UkUpOWeKlFUu$zYftwYw25ABA1Un2FYsYu+xOyZkUbRh1r+9xARw0J1w=','2018-06-27 19:18:20.921994',0,'alex','','','',0,0,'2018-06-27 17:05:39.459216','大理世子','2006-06-06','male','云南大理','10201020120','image/2018/06/default.png');
/*!40000 ALTER TABLE `用户信息` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户信息_groups`
--

DROP TABLE IF EXISTS `用户信息_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户信息_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `个人信息_groups_userprofile_id_group_id_68380ac0_uniq` (`userprofile_id`,`group_id`),
  KEY `个人信息_groups_group_id_1452d986_fk_auth_group_id` (`group_id`),
  CONSTRAINT `个人信息_groups_group_id_1452d986_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `个人信息_groups_userprofile_id_97873f42_fk_个人信息_id` FOREIGN KEY (`userprofile_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户信息_groups`
--

LOCK TABLES `用户信息_groups` WRITE;
/*!40000 ALTER TABLE `用户信息_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `用户信息_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户信息_user_permissions`
--

DROP TABLE IF EXISTS `用户信息_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户信息_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `个人信息_user_permissions_userprofile_id_permission_id_4068944d_uniq` (`userprofile_id`,`permission_id`),
  KEY `个人信息_user_permission_permission_id_08d79d29_fk_auth_perm` (`permission_id`),
  CONSTRAINT `个人信息_user_permission_permission_id_08d79d29_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `个人信息_user_permissions_userprofile_id_cd966fe0_fk_个人信息_id` FOREIGN KEY (`userprofile_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户信息_user_permissions`
--

LOCK TABLES `用户信息_user_permissions` WRITE;
/*!40000 ALTER TABLE `用户信息_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `用户信息_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户咨询`
--

DROP TABLE IF EXISTS `用户咨询`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户咨询` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `course` varchar(20) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户咨询`
--

LOCK TABLES `用户咨询` WRITE;
/*!40000 ALTER TABLE `用户咨询` DISABLE KEYS */;
/*!40000 ALTER TABLE `用户咨询` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户收藏`
--

DROP TABLE IF EXISTS `用户收藏`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户收藏` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `favor_type` int(11) NOT NULL,
  `favor_id` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_userfavorite_user_id_ad46a6af_fk_个人信息_id` (`user_id`),
  CONSTRAINT `operation_userfavorite_user_id_ad46a6af_fk_个人信息_id` FOREIGN KEY (`user_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户收藏`
--

LOCK TABLES `用户收藏` WRITE;
/*!40000 ALTER TABLE `用户收藏` DISABLE KEYS */;
INSERT INTO `用户收藏` VALUES (1,1,1,'2018-06-27 16:38:58.627834',1);
/*!40000 ALTER TABLE `用户收藏` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户消息`
--

DROP TABLE IF EXISTS `用户消息`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户消息` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `has_read` tinyint(1) NOT NULL,
  `message` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_usermessages_user_id_0f17785f_fk_个人信息_id` (`user_id`),
  CONSTRAINT `operation_usermessages_user_id_0f17785f_fk_个人信息_id` FOREIGN KEY (`user_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户消息`
--

LOCK TABLES `用户消息` WRITE;
/*!40000 ALTER TABLE `用户消息` DISABLE KEYS */;
/*!40000 ALTER TABLE `用户消息` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户课程`
--

DROP TABLE IF EXISTS `用户课程`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户课程` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_usercourses_course_id_0c440998_fk_课程_id` (`course_id`),
  KEY `operation_usercourses_user_id_5a0b8789_fk_个人信息_id` (`user_id`),
  CONSTRAINT `operation_usercourses_course_id_0c440998_fk_课程_id` FOREIGN KEY (`course_id`) REFERENCES `课程` (`id`),
  CONSTRAINT `operation_usercourses_user_id_5a0b8789_fk_个人信息_id` FOREIGN KEY (`user_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户课程`
--

LOCK TABLES `用户课程` WRITE;
/*!40000 ALTER TABLE `用户课程` DISABLE KEYS */;
INSERT INTO `用户课程` VALUES (1,'2018-06-27 16:39:11.252216',1,1),(2,'2018-06-27 19:10:03.123864',1,3);
/*!40000 ALTER TABLE `用户课程` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `用户课程评论`
--

DROP TABLE IF EXISTS `用户课程评论`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `用户课程评论` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(150) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_coursecomments_course_id_c88f1b6a_fk_课程_id` (`course_id`),
  KEY `operation_coursecomments_user_id_f5ff70b3_fk_个人信息_id` (`user_id`),
  CONSTRAINT `operation_coursecomments_course_id_c88f1b6a_fk_课程_id` FOREIGN KEY (`course_id`) REFERENCES `课程` (`id`),
  CONSTRAINT `operation_coursecomments_user_id_f5ff70b3_fk_个人信息_id` FOREIGN KEY (`user_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `用户课程评论`
--

LOCK TABLES `用户课程评论` WRITE;
/*!40000 ALTER TABLE `用户课程评论` DISABLE KEYS */;
/*!40000 ALTER TABLE `用户课程评论` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `章节`
--

DROP TABLE IF EXISTS `章节`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `章节` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_chapter_course_id_24d15099_fk_courses_course_id` (`course_id`),
  CONSTRAINT `courses_chapter_course_id_24d15099_fk_courses_course_id` FOREIGN KEY (`course_id`) REFERENCES `课程` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `章节`
--

LOCK TABLES `章节` WRITE;
/*!40000 ALTER TABLE `章节` DISABLE KEYS */;
INSERT INTO `章节` VALUES (1,'数据结构','2018-06-27 16:44:00.000000',1),(2,'计算机语言','2018-06-27 16:44:00.000000',1),(3,'python函数','2018-06-27 16:45:00.000000',1),(4,'流程控制','2018-06-27 16:45:00.000000',1),(5,'面向对象','2018-06-27 16:45:00.000000',2),(6,'网络编程','2018-06-27 16:45:00.000000',2),(7,'并发编程','2018-06-27 16:45:00.000000',2),(8,'协程','2018-06-27 16:45:00.000000',2);
/*!40000 ALTER TABLE `章节` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `视频`
--

DROP TABLE IF EXISTS `视频`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `视频` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `url` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `chapter_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `视频_chapter_id_66a71172_fk_章节_id` (`chapter_id`),
  CONSTRAINT `视频_chapter_id_66a71172_fk_章节_id` FOREIGN KEY (`chapter_id`) REFERENCES `章节` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `视频`
--

LOCK TABLES `视频` WRITE;
/*!40000 ALTER TABLE `视频` DISABLE KEYS */;
INSERT INTO `视频` VALUES (1,'dict','http://oyhijg3iv.bkt.clouddn.com/6-4%20%E9%85%8D%E7%BD%AE%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83.mp4','2018-06-27 16:46:00.000000',1),(2,'list','http://oyhijg3iv.bkt.clouddn.com/6-4%20%E9%85%8D%E7%BD%AE%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83.mp4','2018-06-27 16:53:00.000000',1),(3,'string','http://oyhijg3iv.bkt.clouddn.com/6-4%20%E9%85%8D%E7%BD%AE%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83.mp4','2018-06-27 16:59:00.000000',1);
/*!40000 ALTER TABLE `视频` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `课程`
--

DROP TABLE IF EXISTS `课程`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `课程` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `detail` longtext NOT NULL,
  `degree` varchar(10) NOT NULL,
  `learn_times` int(11) NOT NULL,
  `students_num` int(11) NOT NULL,
  `category` varchar(20) NOT NULL,
  `favor_num` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `click_num` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `org_id` int(11) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `recommend` tinyint(1) NOT NULL,
  `has_favor` tinyint(1) NOT NULL,
  `notice` varchar(200) NOT NULL,
  `is_banner` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_course_org_id_387fdc72_fk_organization_courseorg_id` (`org_id`),
  KEY `courses_course_teacher_id_846fa526_fk_organization_teacher_id` (`teacher_id`),
  CONSTRAINT `courses_course_org_id_387fdc72_fk_organization_courseorg_id` FOREIGN KEY (`org_id`) REFERENCES `课程机构` (`id`),
  CONSTRAINT `courses_course_teacher_id_846fa526_fk_organization_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `教师` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `课程`
--

LOCK TABLES `课程` WRITE;
/*!40000 ALTER TABLE `课程` DISABLE KEYS */;
INSERT INTO `课程` VALUES (1,'python入门','计算机语言基础、python数据结构等','计算机语言基础、python数据结构、函数、文件处理、流程控制','CJ',360,22,'后端开发',1,'course/2018/06/1.png',0,'2018-06-27 16:35:00.000000',1,1,0,0,'计算机基础',0),(2,'python进阶','socket网络编程、面向对象编程以及并发编程','socket网络编程、面向对象编程以及并发编程','ZJ',0,0,'后端开发',0,'course/2018/06/c6.jpg',0,'2018-06-27 16:39:00.000000',1,2,0,0,'python基础知识',0);
/*!40000 ALTER TABLE `课程` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `课程机构`
--

DROP TABLE IF EXISTS `课程机构`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `课程机构` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `category` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `click_num` int(11) NOT NULL,
  `favor_num` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  `students_num` int(11) NOT NULL,
  `courses_num` varchar(5) NOT NULL,
  `has_favor` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `organization_courseorg_city_id_4a842f85_fk_organization_city_id` (`city_id`),
  CONSTRAINT `organization_courseorg_city_id_4a842f85_fk_organization_city_id` FOREIGN KEY (`city_id`) REFERENCES `城市` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `课程机构`
--

LOCK TABLES `课程机构` WRITE;
/*!40000 ALTER TABLE `课程机构` DISABLE KEYS */;
INSERT INTO `课程机构` VALUES (1,'北京大学','school','org/2018/06/s1.jpg','北京市海淀区','北京大学（英文：Peking University），简称北大，诞生于1898年，初名京师大学堂，是中国近代第一所国立大学，也是最早以“大学”身份及名称而建立的学校，其成立标志着中国近代高等教育的开端。北大是中国近代以来唯一以国家最高学府身份创立的学校，最初也是国家最高教育行政机关，行使教育部职能，统管全国教育。','2018-06-27 16:28:00.000000',0,0,3,100,'0',0),(2,'南京大学','school','org/2018/06/s2.png','中国江苏南京','南京大学坐落于钟灵毓秀、虎踞龙蟠的金陵古都，是一所历史悠久、声誉卓著的百年名校。其前身是创建于1902年的三江师范学堂，此后历经两江师范学堂、南京高等师范学校、国立东南大学、第四中山大学、国立中央大学、国立南京大学等历史时期，于1950年更名为南京大学。\r\n\r\n1994年，南京大学被确定为国家“211工程”重点支持的大学；1999年，南京大学进入国家“985工程”首批重点建设的高水平大学行列；2016年，南京大学入选首批国家级双创示范基地；2017年，南京大学入选A类世界一流大学建设高校名单，15个学科入选世界一流学科建设名单。','2018-06-27 16:29:00.000000',0,0,7,0,'0',0),(3,'武汉大学','training_org','org/2018/06/s5_LanpuS7.png','湖北省武汉市武昌区珞珈山街16号','武汉大学（Wuhan University），简称“武大”，位于湖北武汉，是直属于中华人民共和国教育部的副部级全国重点大学，国家首批“985工程”、“211工程”、“2011计划”重点建设高校，同时是“111计划”、“珠峰计划”、“海外高层次人才引进计划”、“卓越工程师教育培养计划”、“卓越法律人才教育培养计划”和“卓越医生教育培养计划”等重点建设的综合研究型大学，是与法国高校联系最紧密、合作最广泛的中国高校之一，是世界权威期刊《Science》列出的“中国最杰出的大学”之一。 \r\n\r\n武汉大学办学源头可溯源于清朝末期1893年湖广总督张之洞奏请清政府创办的自强学堂；1913年改名国立武昌高等师范学校；1926年组建国立武昌中山大学；1928年定名国立武汉大学，是民国四大名校之一；1949年，更名为武汉大学。\r\n\r\n截至2018年5月，学校现有专任教师3700余人，其中正副教授2700余人，有11位中国科学院院士、7位中国工程院院士、3位欧亚科学院院士、10位人文社科资深教授、22人次“973项目”（含国家重大基础研究计划）首席科学家、6位“863项目”计划领域专家、7个国家创新研究群体、56位国家杰出青年科学基金获得者、15位国家级教学名师、23位国家新世纪“百千万人才工程”入选者、62位“长江学者奖励计划”特聘教授、24位“长江学者奖励计划”讲座教授人数、9个“长江学者和创新团队发展计划”创新团队。','2018-06-27 16:30:00.000000',0,0,1,0,'0',0),(4,'厦门大学','personal','org/2018/06/s7.png','厦门市思明南路422号','厦门大学（Xiamen University），简称厦大（XMU），是中华人民共和国教育部直属的全国重点大学，是国家“211工程”、“985工程”重点建设高校，是国家“2011计划”牵头高校。入选“111计划”、“珠峰计划”、“卓越工程师教育培养计划”、“卓越法律人才教育培养计划”、“卓越医生教育培养计划”、国家建设高水平大学公派研究生项目。学校由著名爱国华侨领袖陈嘉庚先生于1921年创办，是中国近代教育史上第一所华侨创办的大学，是国内最早招收研究生的大学之一，被誉为“南方之强” 。\r\n\r\n截至2018年3月，学校占地9000多亩，校舍建筑总面积210多万平方米；图书馆馆藏纸质图书490多万册，电子图书560多万册，固定资产总值91亿元，仪器设备总值25亿元；拥有8家附属医院；设有研究生院、6个学部以及28个学院（含76个系）和14个研究院；拥有31个博士后流动站，33个博士学位授权一级学科，1个博士专业学位学科授权，52个硕士学位授权一级学科，24个硕士专业学位学科授权；有专任教师2657人；有在校学生近40000人（含外国学历留学生1235人），其中本科生19843人、硕士研究生16172人、博士研究生3647人；12个学科进入ESI全球前1%。','2018-06-27 16:31:00.000000',0,0,8,0,'0',0),(5,'中山大学','personal','org/2018/06/s8.jpg','广东省广州市海珠区新港西路135号','中山大学（Sun Yat-sen University），简称中大，前身是孙中山先生创立于1924年的国立广东大学，有着一百多年办学传统，是学术与文化中国南方重镇和人才培养南方高地。\r\n\r\n中山大学是中华人民共和国教育部直属的综合性重点大学，国家“985工程”、“211工程”建设高校，同时是“珠峰计划”、“111计划”、“卓越法律人才教育培养计划”、“卓越医生教育培养计划”实施高校。中山大学已经成为一所国内一流、国际知名的现代综合性大学，正努力成为全球学术重镇。\r\n\r\n学校有18个学科领域进入ESI世界前1%，学科领域数量位居国内高校第2位，其中有11个学科领域进入前0.5%，2个学科领域进入前0.1%。在第三轮全国学科评估中，学校33个参评学科有16个学科进入水平排名前5，32个学科进入水平排名前10。\r\n\r\n学校现有院士20人，国家“千人计划”专家114人、享受政府特殊津贴专家138人、“长江学者”特聘教授46人、“长江学者”青年学者14人、国家杰出青年科学基金获得者78人，“百千万人才工程” 国家级人选28人，教育部新世纪优秀人才支持计划170人。\r\n\r\n学校拥有10个国家级人才培养基地，经济管理等多个本科专业通过了国内、国际认证。入选教育部的基础学科拔尖学生培养试验计划、卓越医生教育培养计划、卓越法律人才培养教育计划，与法国民用核能工程师教学联盟等国际一流大学开展的中外合作办学项目顺利通过相关国际认证。并拥有10家附属医院。','2018-06-27 16:32:00.000000',0,0,2,0,'0',0),(6,'慕课网','training_org','org/2018/06/s6.png','北京市海淀区西三环北路甲2号院中关村国防科技园2号楼','慕课网是国内规模最大 、互动性最高的IT技能学习平台，以培养企业实用型人才为己任，打造从人才培养到技术输出全产业链的跨终端IT学习应用平台，该平台几乎覆盖了前端/PHP/Android/iOS/Python/Java等主流技术方向。慕课网选取企业真实案例，还原开发真实场景，精心创作700余门免费课程及若干门实战课程（内容自制+PGC）；与BAT专业技术团队深度合作，与顶级互联网行业大会零距离接轨，以新潮学习体验颠覆传统教育模式，打造IT在线教育明星品牌。','2018-06-27 16:32:00.000000',0,0,3,0,'0',0),(7,'新东方','training_org','org/2018/06/s6_CfwKm1J.png','北京市海淀区海淀中街6号','新东方教育科技集团，由1993年11月16日成立的北京新东方学校发展壮大而来，目前集团以语言培训为核心，拥有短期培训系统、基础教育系统、文化传播系统、科技产业系统、咨询服务系统等多个发展平台，是一家集教育培训、教育产品研发、教育服务等于一体的大型综合性教育科技集团。新东方教育科技集团于2006年9月7日在美国纽约证券交易所成功上市，成为中国大陆首家海外上市的教育培训机构。','2018-06-27 16:33:00.000000',0,0,3,0,'0',0);
/*!40000 ALTER TABLE `课程机构` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `课程资源下载`
--

DROP TABLE IF EXISTS `课程资源下载`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `课程资源下载` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `download` varchar(100) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `courses_courseresource_course_id_5eba1332_fk_courses_course_id` (`course_id`),
  CONSTRAINT `courses_courseresource_course_id_5eba1332_fk_courses_course_id` FOREIGN KEY (`course_id`) REFERENCES `课程` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `课程资源下载`
--

LOCK TABLES `课程资源下载` WRITE;
/*!40000 ALTER TABLE `课程资源下载` DISABLE KEYS */;
/*!40000 ALTER TABLE `课程资源下载` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `轮播图`
--

DROP TABLE IF EXISTS `轮播图`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `轮播图` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  `index` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `轮播图`
--

LOCK TABLES `轮播图` WRITE;
/*!40000 ALTER TABLE `轮播图` DISABLE KEYS */;
INSERT INTO `轮播图` VALUES (5,'b1','banner/2018/06/b1_xAFtXPQ.jpeg','http://www.cnblogs.com/fqh202',100,'2018-06-27 16:26:00.000000'),(6,'b2','banner/2018/06/b2.jpg','http://www.cnblogs.com/fqh202',100,'2018-06-27 16:26:00.000000'),(7,'b3','banner/2018/06/b3.jpg','http://www.cnblogs.com/fqh202',100,'2018-06-27 16:26:00.000000'),(8,'b4','banner/2018/06/b4_HRtfl31.jpg','http://www.cnblogs.com/fqh202',100,'2018-06-27 16:26:00.000000'),(9,'b5','banner/2018/06/b6.jpg','http://www.cnblogs.com/fqh202',100,'2018-06-27 16:26:00.000000');
/*!40000 ALTER TABLE `轮播图` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `邮箱验证码`
--

DROP TABLE IF EXISTS `邮箱验证码`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `邮箱验证码` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_type` varchar(20) NOT NULL,
  `send_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `邮箱验证码`
--

LOCK TABLES `邮箱验证码` WRITE;
/*!40000 ALTER TABLE `邮箱验证码` DISABLE KEYS */;
/*!40000 ALTER TABLE `邮箱验证码` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 章节',6,'add_chapter'),(17,'Can change 章节',6,'change_chapter'),(18,'Can delete 章节',6,'delete_chapter'),(19,'Can add 课程',7,'add_course'),(20,'Can change 课程',7,'change_course'),(21,'Can delete 课程',7,'delete_course'),(22,'Can add 课程资源下载',8,'add_courseresource'),(23,'Can change 课程资源下载',8,'change_courseresource'),(24,'Can delete 课程资源下载',8,'delete_courseresource'),(25,'Can add 视频',9,'add_video'),(26,'Can change 视频',9,'change_video'),(27,'Can delete 视频',9,'delete_video'),(28,'Can add 用户课程评论',10,'add_coursecomments'),(29,'Can change 用户课程评论',10,'change_coursecomments'),(30,'Can delete 用户课程评论',10,'delete_coursecomments'),(31,'Can add 用户咨询',11,'add_userask'),(32,'Can change 用户咨询',11,'change_userask'),(33,'Can delete 用户咨询',11,'delete_userask'),(34,'Can add 用户学习课程',12,'add_usercourses'),(35,'Can change 用户学习课程',12,'change_usercourses'),(36,'Can delete 用户学习课程',12,'delete_usercourses'),(37,'Can add 用户收藏',13,'add_userfavorite'),(38,'Can change 用户收藏',13,'change_userfavorite'),(39,'Can delete 用户收藏',13,'delete_userfavorite'),(40,'Can add 用户消息',14,'add_usermessages'),(41,'Can change 用户消息',14,'change_usermessages'),(42,'Can delete 用户消息',14,'delete_usermessages'),(43,'Can add 城市',15,'add_city'),(44,'Can change 城市',15,'change_city'),(45,'Can delete 城市',15,'delete_city'),(46,'Can add 课程机构',16,'add_courseorg'),(47,'Can change 课程机构',16,'change_courseorg'),(48,'Can delete 课程机构',16,'delete_courseorg'),(49,'Can add 讲师',17,'add_teacher'),(50,'Can change 讲师',17,'change_teacher'),(51,'Can delete 讲师',17,'delete_teacher'),(52,'Can add 用户信息',18,'add_userprofile'),(53,'Can change 用户信息',18,'change_userprofile'),(54,'Can delete 用户信息',18,'delete_userprofile'),(55,'Can add 轮播图',19,'add_banner'),(56,'Can change 轮播图',19,'change_banner'),(57,'Can delete 轮播图',19,'delete_banner'),(58,'Can add 邮箱验证码',20,'add_emailverifyrecord'),(59,'Can change 邮箱验证码',20,'change_emailverifyrecord'),(60,'Can delete 邮箱验证码',20,'delete_emailverifyrecord'),(61,'Can add captcha store',21,'add_captchastore'),(62,'Can change captcha store',21,'change_captchastore'),(63,'Can delete captcha store',21,'delete_captchastore');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (29,'TNNT','tnnt','25b4e5b0ee54ba22e57aefd0632f8d0592e0fc37','2018-06-27 19:22:37.699788');
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_个人信息_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_个人信息_id` FOREIGN KEY (`user_id`) REFERENCES `用户信息` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-06-27 16:04:04.958703','1','b1',1,'[{\"added\": {}}]',19,1),(2,'2018-06-27 16:04:15.534724','2','b2',1,'[{\"added\": {}}]',19,1),(3,'2018-06-27 16:04:24.952976','3','b3',1,'[{\"added\": {}}]',19,1),(4,'2018-06-27 16:04:38.054675','4','b4',1,'[{\"added\": {}}]',19,1),(5,'2018-06-27 16:25:46.393327','4','b1',2,'[{\"changed\": {\"fields\": [\"title\", \"image\"]}}]',19,1),(6,'2018-06-27 16:25:59.192826','4','b1',3,'',19,1),(7,'2018-06-27 16:25:59.199829','3','b3',3,'',19,1),(8,'2018-06-27 16:25:59.206834','2','b2',3,'',19,1),(9,'2018-06-27 16:25:59.210836','1','b1',3,'',19,1),(10,'2018-06-27 16:26:20.146739','5','b1',1,'[{\"added\": {}}]',19,1),(11,'2018-06-27 16:26:28.863524','6','b2',1,'[{\"added\": {}}]',19,1),(12,'2018-06-27 16:26:39.304456','7','b3',1,'[{\"added\": {}}]',19,1),(13,'2018-06-27 16:26:47.943191','8','b4',1,'[{\"added\": {}}]',19,1),(14,'2018-06-27 16:27:04.207989','9','b5',1,'[{\"added\": {}}]',19,1),(15,'2018-06-27 16:27:55.269894','1','武汉',1,'[{\"added\": {}}]',15,1),(16,'2018-06-27 16:27:58.943328','2','广州',1,'[{\"added\": {}}]',15,1),(17,'2018-06-27 16:28:02.270537','3','北京',1,'[{\"added\": {}}]',15,1),(18,'2018-06-27 16:28:05.117428','4','上海',1,'[{\"added\": {}}]',15,1),(19,'2018-06-27 16:28:11.622751','5','成都',1,'[{\"added\": {}}]',15,1),(20,'2018-06-27 16:29:28.355503','1','北京大学',1,'[{\"added\": {}}]',16,1),(21,'2018-06-27 16:30:22.137094','6','江苏',1,'[{\"added\": {}}]',15,1),(22,'2018-06-27 16:30:35.203769','7','南京',1,'[{\"added\": {}}]',15,1),(23,'2018-06-27 16:30:36.194427','2','南京大学',1,'[{\"added\": {}}]',16,1),(24,'2018-06-27 16:31:27.065201','3','武汉大学',1,'[{\"added\": {}}]',16,1),(25,'2018-06-27 16:32:05.201339','8','厦门',1,'[{\"added\": {}}]',15,1),(26,'2018-06-27 16:32:06.695332','4','厦门大学',1,'[{\"added\": {}}]',16,1),(27,'2018-06-27 16:32:39.796327','5','中山大学',1,'[{\"added\": {}}]',16,1),(28,'2018-06-27 16:33:55.615664','6','慕课网',1,'[{\"added\": {}}]',16,1),(29,'2018-06-27 16:35:00.343637','7','新东方',1,'[{\"added\": {}}]',16,1),(30,'2018-06-27 16:38:36.809349','1','乔峰',1,'[{\"added\": {}}]',17,1),(31,'2018-06-27 16:38:43.984115','1','python入门',1,'[{\"added\": {}}]',7,1),(32,'2018-06-27 16:43:37.224797','2','马云',1,'[{\"added\": {}}]',17,1),(33,'2018-06-27 16:43:46.439916','2','python进阶',1,'[{\"added\": {}}]',7,1),(34,'2018-06-27 16:44:36.652252','1','python入门',2,'[{\"changed\": {\"fields\": [\"description\", \"detail\"]}}]',7,1),(35,'2018-06-27 16:44:51.841337','1','数据结构',1,'[{\"added\": {}}]',6,1),(36,'2018-06-27 16:45:03.879327','2','计算机语言',1,'[{\"added\": {}}]',6,1),(37,'2018-06-27 16:45:11.383310','3','python函数',1,'[{\"added\": {}}]',6,1),(38,'2018-06-27 16:45:19.474681','4','流程控制',1,'[{\"added\": {}}]',6,1),(39,'2018-06-27 16:45:27.637100','5','面向对象',1,'[{\"added\": {}}]',6,1),(40,'2018-06-27 16:45:36.886243','6','网络编程',1,'[{\"added\": {}}]',6,1),(41,'2018-06-27 16:45:49.151383','7','并发编程',1,'[{\"added\": {}}]',6,1),(42,'2018-06-27 16:45:59.333146','8','协程',1,'[{\"added\": {}}]',6,1),(43,'2018-06-27 16:53:15.287617','1','数据机构',1,'[{\"added\": {}}]',9,1),(44,'2018-06-27 16:53:28.565672','2','计算机语言',1,'[{\"added\": {}}]',9,1),(45,'2018-06-27 16:58:03.426479','2','v1',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(46,'2018-06-27 16:58:10.049881','1','v2',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(47,'2018-06-27 16:59:16.817203','2','list',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(48,'2018-06-27 16:59:24.193101','1','dict',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(49,'2018-06-27 16:59:35.065320','3','string',1,'[{\"added\": {}}]',9,1),(50,'2018-06-27 16:59:55.087610','2','list',2,'[{\"changed\": {\"fields\": [\"chapter\"]}}]',9,1),(51,'2018-06-27 17:01:32.638377','6','慕课网',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',16,1),(52,'2018-06-27 17:01:51.517909','6','慕课网',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',16,1),(53,'2018-06-27 17:02:12.164618','6','慕课网',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',16,1),(54,'2018-06-27 17:02:29.722273','6','慕课网',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',16,1),(55,'2018-06-27 17:02:48.116488','7','新东方',2,'[{\"changed\": {\"fields\": [\"image\"]}}]',16,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(21,'captcha','captchastore'),(4,'contenttypes','contenttype'),(6,'courses','chapter'),(7,'courses','course'),(8,'courses','courseresource'),(9,'courses','video'),(10,'operation','coursecomments'),(11,'operation','userask'),(12,'operation','usercourses'),(13,'operation','userfavorite'),(14,'operation','usermessages'),(15,'organization','city'),(16,'organization','courseorg'),(17,'organization','teacher'),(5,'sessions','session'),(19,'users','banner'),(20,'users','emailverifyrecord'),(18,'users','userprofile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-06-27 14:56:38.685838'),(2,'contenttypes','0002_remove_content_type_name','2018-06-27 14:56:38.824930'),(3,'auth','0001_initial','2018-06-27 14:56:39.242207'),(4,'auth','0002_alter_permission_name_max_length','2018-06-27 14:56:39.328263'),(5,'auth','0003_alter_user_email_max_length','2018-06-27 14:56:39.339270'),(6,'auth','0004_alter_user_username_opts','2018-06-27 14:56:39.352281'),(7,'auth','0005_alter_user_last_login_null','2018-06-27 14:56:39.364289'),(8,'auth','0006_require_contenttypes_0002','2018-06-27 14:56:39.369291'),(9,'auth','0007_alter_validators_add_error_messages','2018-06-27 14:56:39.380298'),(10,'auth','0008_alter_user_username_max_length','2018-06-27 14:56:39.394307'),(11,'users','0001_initial','2018-06-27 14:56:39.977694'),(12,'admin','0001_initial','2018-06-27 14:56:40.187835'),(13,'admin','0002_logentry_remove_auto_add','2018-06-27 14:56:40.211850'),(14,'captcha','0001_initial','2018-06-27 14:56:40.257882'),(15,'organization','0001_initial','2018-06-27 14:56:40.547073'),(16,'organization','0002_auto_20171112_1554','2018-06-27 14:56:40.572089'),(17,'organization','0003_auto_20171112_1555','2018-06-27 14:56:40.659146'),(18,'organization','0004_auto_20171115_2225','2018-06-27 14:56:40.670154'),(19,'courses','0001_initial','2018-06-27 14:56:41.450672'),(20,'courses','0002_auto_20171115_2225','2018-06-27 14:56:41.466683'),(21,'courses','0003_course_teacher','2018-06-27 14:56:41.624788'),(22,'courses','0004_course_recommend','2018-06-27 14:56:41.718851'),(23,'courses','0005_course_has_favor','2018-06-27 14:56:41.805909'),(24,'courses','0006_auto_20171119_0952','2018-06-27 14:56:41.917983'),(25,'courses','0007_auto_20171119_1015','2018-06-27 14:56:42.113112'),(26,'courses','0008_auto_20171120_2048','2018-06-27 14:56:42.238196'),(27,'courses','0009_auto_20171120_2050','2018-06-27 14:56:42.370285'),(28,'courses','0010_auto_20171120_2120','2018-06-27 14:56:42.496367'),(29,'courses','0011_auto_20171120_2121','2018-06-27 14:56:42.629456'),(30,'courses','0012_auto_20171120_2122','2018-06-27 14:56:42.736527'),(31,'courses','0013_auto_20171120_2123','2018-06-27 14:56:42.845599'),(32,'courses','0014_auto_20171120_2125','2018-06-27 14:56:42.952671'),(33,'courses','0015_auto_20171120_2126','2018-06-27 14:56:43.056739'),(34,'courses','0016_auto_20171120_2130','2018-06-27 14:56:43.159807'),(35,'courses','0017_auto_20171120_2144','2018-06-27 14:56:43.266879'),(36,'courses','0018_auto_20171120_2145','2018-06-27 14:56:43.374950'),(37,'courses','0019_auto_20171120_2151','2018-06-27 14:56:43.490026'),(38,'courses','0020_auto_20171120_2156','2018-06-27 14:56:43.610106'),(39,'courses','0021_auto_20171120_2159','2018-06-27 14:56:43.718177'),(40,'courses','0022_auto_20171120_2201','2018-06-27 14:56:43.822247'),(41,'courses','0023_auto_20171120_2201','2018-06-27 14:56:43.932321'),(42,'courses','0024_auto_20171120_2203','2018-06-27 14:56:44.033388'),(43,'courses','0025_auto_20171120_2203','2018-06-27 14:56:44.140459'),(44,'courses','0026_auto_20171120_2205','2018-06-27 14:56:44.252533'),(45,'courses','0027_auto_20171120_2209','2018-06-27 14:56:44.386622'),(46,'courses','0028_auto_20171120_2210','2018-06-27 14:56:44.514707'),(47,'courses','0029_auto_20171120_2213','2018-06-27 14:56:44.632786'),(48,'courses','0030_auto_20171120_2230','2018-06-27 14:56:44.750864'),(49,'courses','0031_auto_20171120_2231','2018-06-27 14:56:44.857935'),(50,'courses','0032_auto_20171122_1302','2018-06-27 14:56:45.048061'),(51,'courses','0033_auto_20180601_1341','2018-06-27 14:56:45.278213'),(52,'courses','0034_auto_20180604_2227','2018-06-27 14:56:45.393290'),(53,'courses','0035_auto_20180627_1456','2018-06-27 14:56:45.508366'),(54,'operation','0001_initial','2018-06-27 14:56:45.691488'),(55,'operation','0002_auto_20171111_1544','2018-06-27 14:56:46.442987'),(56,'operation','0003_usercourses_user','2018-06-27 14:56:46.614100'),(57,'operation','0004_auto_20171118_2021','2018-06-27 14:56:46.747189'),(58,'operation','0005_auto_20180601_1341','2018-06-27 14:56:46.962332'),(59,'organization','0005_courseorg_students_num','2018-06-27 14:56:47.046387'),(60,'organization','0006_teacher_gender','2018-06-27 14:56:47.130445'),(61,'organization','0007_teacher_company','2018-06-27 14:56:47.221503'),(62,'organization','0008_courseorg_courses_num','2018-06-27 14:56:47.310563'),(63,'organization','0009_teacher_nick_name','2018-06-27 14:56:47.389615'),(64,'organization','0010_courseorg_has_favor','2018-06-27 14:56:47.477674'),(65,'organization','0011_teacher_has_favor','2018-06-27 14:56:47.559728'),(66,'organization','0012_teacher_favor_id','2018-06-27 14:56:47.643784'),(67,'organization','0013_auto_20171120_2213','2018-06-27 14:56:47.672803'),(68,'organization','0014_remove_teacher_favor_user_id','2018-06-27 14:56:47.749855'),(69,'organization','0015_remove_teacher_has_favor','2018-06-27 14:56:47.826906'),(70,'organization','0016_auto_20180601_1341','2018-06-27 14:56:47.899953'),(71,'sessions','0001_initial','2018-06-27 14:56:47.965999'),(72,'users','0002_auto_20171111_1552','2018-06-27 14:56:48.072069'),(73,'users','0003_auto_20171112_0700','2018-06-27 14:56:48.157126'),(74,'users','0004_auto_20171115_2013','2018-06-27 14:56:48.315231'),(75,'users','0005_auto_20180601_1341','2018-06-27 14:56:48.431307');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('o909jntn3v24jtl2nqe2jybf9rzfxnvu','MDFjZWQ4ZjM3YWZlOTQ1NzIzMDlhNGU3ZmMzOWE4NWJhZmM4NTg0NDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuTXlCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNmU3MjYzNzRhZmIwNGViNzdjYzg2YjIwNWU3ZGJjYWE3YjQ2NmIyNSJ9','2018-07-11 19:18:20.933003');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-27 20:12:55

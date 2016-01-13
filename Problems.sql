-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: gbatchsec
-- ------------------------------------------------------
-- Server version	5.5.38-0ubuntu0.14.04.1

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add site',5,'add_site'),(14,'Can change site',5,'change_site'),(15,'Can delete site',5,'delete_site'),(16,'Can add content type',6,'add_contenttype'),(17,'Can change content type',6,'change_contenttype'),(18,'Can delete content type',6,'delete_contenttype'),(19,'Can add session',7,'add_session'),(20,'Can change session',7,'change_session'),(21,'Can delete session',7,'delete_session'),(22,'Can add user',8,'add_ojuser'),(23,'Can change user',8,'change_ojuser'),(24,'Can delete user',8,'delete_ojuser'),(25,'Can add detail',9,'add_detail'),(26,'Can change detail',9,'change_detail'),(27,'Can delete detail',9,'delete_detail'),(28,'Can add problem',10,'add_problem'),(29,'Can change problem',10,'change_problem'),(30,'Can delete problem',10,'delete_problem'),(31,'Can add submission',11,'add_submission'),(32,'Can change submission',11,'change_submission'),(33,'Can delete submission',11,'delete_submission');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$OG7aRs06rfmo$/HqvaWyBNjB5w7L8jvfFGjJt/xMmH1HY8fpxrVgEmkc=','2014-12-30 08:35:43',1,'admin','','','admin@admin.com',1,1,'2014-12-30 07:59:05');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-12-30 08:05:40','1','POSNEG',1,'',9,1),(2,'2014-12-30 08:06:16','POSNEG','POSNEG',1,'',10,1),(3,'2014-12-30 08:09:39','2','NAMENUM',1,'',9,1),(4,'2014-12-30 08:09:48','NAMENUM','NAMENUM',1,'',10,1),(5,'2014-12-30 08:10:38','NAMENUM','NAMENUM',2,'No fields changed.',10,1),(6,'2014-12-30 08:13:52','3','MINNMAX',1,'',9,1),(7,'2014-12-30 08:14:03','MINNMAX','MINNMAX',1,'',10,1),(8,'2014-12-30 08:16:44','4','AVERAGE',1,'',9,1),(9,'2014-12-30 08:39:19','5','AVERAGE',1,'',9,1),(10,'2014-12-30 08:39:26','AVERAGE','AVERAGE',1,'',10,1),(11,'2014-12-30 08:40:41','AVERAGE','AVERAGE',2,'Changed sample_input, sample_output and explanation.',10,1),(12,'2014-12-30 08:42:31','6','DIGSUM',1,'',9,1),(13,'2014-12-30 08:42:39','DIGSUM','DIGSUM',1,'',10,1);
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
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'site','sites','site'),(6,'content type','contenttypes','contenttype'),(7,'session','sessions','session'),(8,'user','users','ojuser'),(9,'detail','problems','detail'),(10,'problem','problems','problem'),(11,'submission','problems','submission');
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
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2014-12-30 07:58:36'),(2,'auth','0001_initial','2014-12-30 07:58:40'),(3,'admin','0001_initial','2014-12-30 07:58:41'),(4,'users','0001_initial','2014-12-30 07:58:41'),(5,'problems','0001_initial','2014-12-30 07:58:43'),(6,'sessions','0001_initial','2014-12-30 07:58:43'),(7,'sites','0001_initial','2014-12-30 07:58:43');
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
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('814bk62prueth5hfvhgl9wd90wig3fiv','YTUyNjIwYzJjMjU3N2FmYzMwOGI0YjMzNTFkZGE5YjAwZWM0ZmY4YTqAAn1xAShVD19hdXRoX3VzZXJfaGFzaHECVShjMTdmNmE4ZTcxYzNjYmMxNTRlMThmZGM3ZjY4MWNjMzRjNDk1Yjk2VRJfYXV0aF91c2VyX2JhY2tlbmRxA1UpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBFUNX2F1dGhfdXNlcl9pZHEFigEBdS4=','2015-01-13 08:35:43'),('zaxrv59yvg9dwh024quq4ul5rlmdzyos','YTUyNjIwYzJjMjU3N2FmYzMwOGI0YjMzNTFkZGE5YjAwZWM0ZmY4YTqAAn1xAShVD19hdXRoX3VzZXJfaGFzaHECVShjMTdmNmE4ZTcxYzNjYmMxNTRlMThmZGM3ZjY4MWNjMzRjNDk1Yjk2VRJfYXV0aF91c2VyX2JhY2tlbmRxA1UpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBFUNX2F1dGhfdXNlcl9pZHEFigEBdS4=','2015-01-13 08:02:18');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problems_detail`
--

DROP TABLE IF EXISTS `problems_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problems_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` varchar(10) NOT NULL,
  `total` int(11) NOT NULL,
  `tle` int(11) NOT NULL,
  `acc` int(11) NOT NULL,
  `wa` int(11) NOT NULL,
  `ce` int(11) NOT NULL,
  `rte` int(11) NOT NULL,
  `accuracy` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problems_detail`
--

LOCK TABLES `problems_detail` WRITE;
/*!40000 ALTER TABLE `problems_detail` DISABLE KEYS */;
INSERT INTO `problems_detail` VALUES (1,'POSNEG',0,0,0,0,0,0,0),(2,'NAMENUM',0,0,0,0,0,0,0),(3,'MINNMAX',0,0,0,0,0,0,0),(4,'AVERAGE',0,0,0,0,0,0,0),(5,'AVERAGE',0,0,0,0,0,0,0),(6,'DIGSUM',0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `problems_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problems_problem`
--

DROP TABLE IF EXISTS `problems_problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problems_problem` (
  `pid` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `sample_input` longtext NOT NULL,
  `sample_output` longtext NOT NULL,
  `explanation` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `testfiles` int(11) NOT NULL,
  `time_limit` double NOT NULL,
  `details_id` int(11) NOT NULL,
  PRIMARY KEY (`pid`),
  KEY `problems_problem_4fa90093` (`details_id`),
  CONSTRAINT `problems_probl_details_id_636e528b26c3c19d_fk_problems_detail_id` FOREIGN KEY (`details_id`) REFERENCES `problems_detail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problems_problem`
--

LOCK TABLES `problems_problem` WRITE;
/*!40000 ALTER TABLE `problems_problem` DISABLE KEYS */;
INSERT INTO `problems_problem` VALUES ('AVERAGE','Average of Numbers','Given n numbers, find the average of them.\r\n\r\n\r\nInput consists of two lines. First line contains an integer n, the number of elements in the array.\r\n\r\nThe next line contains n integers, the numbers in the array.\r\n\r\n1 <= n <= 20\r\n\r\n1 <= elements <= 100\r\n\r\n\r\nOutput the average of the numbers.\r\n','5\r\n4 5 6 7 8','6','Find the average of the given numbers and print the integer value of the average',0,1,1,5),('DIGSUM','Sum of digits','Find the sum of digits of the given number.\r\n\r\nFirst line of the input contains an integer n.\r\n\r\n1 <= n <= 10000\r\n\r\nOutput a single integer, the sum of digits of n.','123','6','1 + 2 + 3 = 6',0,1,1,6),('MINNMAX','Minimum and Maximum','You are given an array of numbers and asked to find the minimum and maximum amongst them\r\n\r\nFirst line contains a number t, denoting the number of test cases. \r\n\r\nEach of the testcases contain 2 lines:\r\n\r\n1st line contains an integer n, denoting the number of elements in the array.\r\n\r\n2nd line contains n numbers, the numbers in the array.\r\n\r\n1<=t<=5\r\n\r\n1<=n<=100\r\n\r\n1<= Each element in the array <=100\r\n\r\nFor each testcase, output 2 integers in the same line, the minimum and the maximum in the array. If they are the same, it is enough to print it only once.','3\r\n2\r\n1 1\r\n5 \r\n1 4 5 0 3\r\n8\r\n5 23 64 19 324 34 12 78','1\r\n0 5\r\n5 324 ','If minimum and maximum are the same, print them only once. Print output of each test case in a single line',0,1,1,3),('NAMENUM','Welcome to Programming','Since this is your frst step into programming, lets make it simple. Given a name and a phone number, get the values and print them back.\r\n\r\nInput consists of two lines, a name and a phone number, each in a single line.\r\n\r\nOutput the name and the number in the same order, each in a single line.','John\r\n987654321','John\r\n987654321','Print both the name and the phone number each in a single line',0,2,1,2),('POSNEG','Positive or Negative','Given a number, tell me if it is a positive or a negative number.\r\n\r\nYou will be given a number. Print \"positive\" if the number is positive. \"negative\" if the number is negative and \"zero\" if the number is 0.\r\n\r\nInput contains a single integer n.\r\n\r\n-500 <= n <= 500\r\n\r\nOutput a single line as shown above','4','positive','4 is positive :D',0,3,1,1);
/*!40000 ALTER TABLE `problems_problem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problems_submission`
--

DROP TABLE IF EXISTS `problems_submission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problems_submission` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(100) DEFAULT NULL,
  `language` varchar(10) NOT NULL,
  `subtime` datetime NOT NULL,
  `status` varchar(20) NOT NULL,
  `extime` double NOT NULL,
  `errorcode` longtext NOT NULL,
  `prob_id` varchar(10) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`sid`),
  KEY `problems_submission_96025dbd` (`prob_id`),
  KEY `problems_submission_e8701ad4` (`user_id`),
  CONSTRAINT `problems_su_user_id_5b53a4b5d7dd8453_fk_users_ojuser_user_ptr_id` FOREIGN KEY (`user_id`) REFERENCES `users_ojuser` (`user_ptr_id`),
  CONSTRAINT `problems_submis_prob_id_7d5c3e03abe75b25_fk_problems_problem_pid` FOREIGN KEY (`prob_id`) REFERENCES `problems_problem` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problems_submission`
--

LOCK TABLES `problems_submission` WRITE;
/*!40000 ALTER TABLE `problems_submission` DISABLE KEYS */;
/*!40000 ALTER TABLE `problems_submission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_ojuser`
--

DROP TABLE IF EXISTS `users_ojuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_ojuser` (
  `user_ptr_id` int(11) NOT NULL,
  `gender` varchar(3) DEFAULT NULL,
  `reg_no` varchar(23) DEFAULT NULL,
  `tot_sub` int(11) NOT NULL,
  `succ_sub` int(11) NOT NULL,
  `points` double NOT NULL,
  `rank` int(11) NOT NULL,
  `is_loggedin` tinyint(1) NOT NULL,
  `ex_time` double NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  CONSTRAINT `users_ojuser_user_ptr_id_6fd37eb6bd8cdcd3_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_ojuser`
--

LOCK TABLES `users_ojuser` WRITE;
/*!40000 ALTER TABLE `users_ojuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_ojuser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-30 14:13:36

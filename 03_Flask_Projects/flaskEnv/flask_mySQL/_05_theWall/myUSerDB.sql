CREATE DATABASE  IF NOT EXISTS `myuserdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `myuserdb`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: myuserdb
-- ------------------------------------------------------
-- Server version	5.6.34-log

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (2,'ONE MORE AGAIN!','2017-05-18 15:45:49','2017-05-18 15:45:49',3,3,1),(3,'trying another one','2017-05-18 16:29:24','2017-05-18 16:29:24',4,3,1),(4,'OLDEST ONE','2017-05-18 16:29:50','2017-05-18 16:29:50',1,3,1),(5,'newest post','2017-05-18 16:29:59','2017-05-18 16:29:59',6,3,1),(6,'comment on oldest one','2017-05-18 16:38:49','2017-05-18 16:38:49',1,3,1),(7,'another comment on oldest one','2017-05-18 16:39:43','2017-05-18 16:39:43',1,3,1),(8,'Commenting on newest post for test as MAT','2017-05-18 16:40:50','2017-05-18 16:40:50',6,1,1),(9,'No you aren\'t.','2017-05-18 16:41:19','2017-05-18 16:41:19',5,1,1),(10,'I comment on all of my own posts!!!','2017-05-18 19:07:43','2017-05-18 19:07:43',11,1,NULL),(11,'Blair in da house!','2017-05-18 19:07:56','2017-05-18 19:07:56',11,1,NULL),(12,'Yeah, she says that a lot.','2017-05-18 20:26:06','2017-05-18 20:26:06',12,1,NULL);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'asdasd','2017-05-18 13:58:06','2017-05-18 13:58:06',2,1),(2,'sadsadsad','2017-05-18 13:59:26','2017-05-18 13:59:26',2,1),(3,'sadsadsad','2017-05-18 13:59:26','2017-05-18 13:59:26',2,1),(4,'My firends are teh best!','2017-05-18 14:35:58','2017-05-18 14:35:58',1,0),(5,'I\'m an interesting dude.','2017-05-18 14:36:28','2017-05-18 14:36:28',3,1),(6,'Time test','2017-05-18 15:22:25','2017-05-18 15:22:25',3,1),(7,'WE DID IT, Y\'ALL!','2017-05-18 16:48:44','2017-05-18 16:48:44',1,1),(8,'This should get deleted!!!','2017-05-18 18:25:52','2017-05-18 18:25:52',6,0),(9,'Delete this one too!','2017-05-18 18:28:45','2017-05-18 18:28:45',6,0),(10,'Test for delete\r\n','2017-05-18 18:48:52','2017-05-18 18:48:52',6,1),(11,'Delete this!','2017-05-18 19:07:24','2017-05-18 19:07:24',1,0),(12,'I AM GROOT!','2017-05-18 20:25:41','2017-05-18 20:25:41',7,0),(13,'Another new post','2017-05-18 20:33:06','2017-05-18 20:33:06',7,0),(14,'I AM GROOT!!','2017-05-18 20:33:19','2017-05-18 20:33:19',7,0);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Mat','Cohen','mat@mat.com','070be8457979b8c0c715da9bbfd5d820','2c93eb5b5635bda3bec7c75986ad4b','2017-05-18 11:27:20','2017-05-18 11:27:20'),(2,'Jerry','Racecardriver','j.driver@racecar.com','a2c6b3c52311301081f7bb74db5f3510','328596f2e18803d5ac4680fbd496bc','2017-05-18 12:23:47','2017-05-18 12:23:47'),(3,'James','Franco','j.franco@actors.com','833f2920d6bebd7047fcacf5a873ef66','550ec6452cd27edf351eec487f9e75','2017-05-18 12:31:34','2017-05-18 12:31:34'),(4,'Jessica','Molenaar','j.mo@dopest.com','48b3754768ae2777b9d235e49a6a643e','d56b94e6bf0fac48f620cc0080a4f9','2017-05-18 16:50:52','2017-05-18 16:50:52'),(5,'Brad','Sherman','b.rad@dopeshow.org','d1ae6768e9f053644c10932d890c0266','f762c55c26990dabb045e4be16b963','2017-05-18 16:51:44','2017-05-18 16:51:44'),(6,'Graham','Layman','golden@grahams.com','780c04c4eeca312309aaaadee6bd5747','bb8d36c9cecc021f81f37e5344cf48','2017-05-18 16:52:24','2017-05-18 16:52:24'),(7,'Megan','Blanchard','me@gan.com','e86110212862e79f50e2aa26195edd4c','3a385418bb37336dc9bf584ce2ac5e','2017-05-18 20:25:08','2017-05-18 20:25:08');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-19  6:55:39

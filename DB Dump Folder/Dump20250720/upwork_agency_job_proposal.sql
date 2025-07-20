-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: upwork_agency
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `job_proposal`
--

DROP TABLE IF EXISTS `job_proposal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_proposal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_description` varchar(255) DEFAULT NULL,
  `job_client_name` varchar(50) DEFAULT NULL,
  `proposal` varchar(255) DEFAULT NULL,
  `feasibility` int DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `approval` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_proposal`
--

LOCK TABLES `job_proposal` WRITE;
/*!40000 ALTER TABLE `job_proposal` DISABLE KEYS */;
INSERT INTO `job_proposal` VALUES (1,'Build a scalable e-commerce platform for electronics.','James Parker','We will use Django and React with Stripe integration.',85,'inactive','E-commerce Website Development','approved'),(2,'Create an AI tool to extract structured data from resumes.','Sophia Watson','We propose a Python NLP pipeline using spaCy and ML models.',78,'inactive','AI Resume Parser','rejected'),(3,'Develop a web-based inventory management system for retail stores.','Michael Jordan','Flask backend with MySQL and Vue.js frontend will be used.',67,'inactive','Inventory Management System','approved'),(4,'Design a cross-platform app for doctor appointment bookings.','Dr. Amanda Li','Flutter app with Firebase integration.',74,'inactive','Healthcare Appointment App','approved'),(5,'Online marketplace for rental and sales properties.','Rachel Green','Modern UI using Next.js and MongoDB.',82,'inactive','Real Estate Listing Platform','rejected'),(6,'A customer relationship management system tailored for freelancers.','Kevin Nguyen','Modular Laravel CRM with reporting and integrations.',90,'inactive','Custom CRM for Agency','approved'),(7,'A tool to optimize delivery routes using maps and real-time traffic.','Ayesha Siddiqui','Google Maps API with machine learning route predictions.',69,'inactive','Logistics Route Optimizer','approved'),(8,'Track applied jobs, proposals sent, and follow-ups.','Haroon Malik','Single-page Vue app with Flask and PostgreSQL backend.',73,'inactive','Job Tracker for Freelancers','approved'),(9,'Secure online portal for fee payments and records.','Sana Tariq','Node.js backend with Razorpay and dashboard analytics.',58,'inactive','School Fee Collection Portal','rejected'),(10,'Digitize menu and accept online food orders.','Kunal Mehra','Responsive menu with order system and real-time updates.',77,'inactive','Restaurant Online Menu & Ordering','approved'),(11,'Build a scalable e-commerce platform for electronics.','James Parker','We will use Django and React with Stripe integration.',85,'inactive','E-commerce Website Development','rejected'),(12,'Create an AI tool to extract structured data from resumes.','Sophia Watson','We propose a Python NLP pipeline using spaCy and ML models.',78,'inactive','AI Resume Parser','rejected'),(13,'Develop a web-based inventory management system for retail stores.','Michael Jordan','Flask backend with MySQL and Vue.js frontend will be used.',67,'inactive','Inventory Management System','rejected'),(14,'Design a cross-platform app for doctor appointment bookings.','Dr. Amanda Li','Flutter app with Firebase integration.',74,'inactive','Healthcare Appointment App','rejected'),(15,'Online marketplace for rental and sales properties.','Rachel Green','Modern UI using Next.js and MongoDB.',82,'inactive','Real Estate Listing Platform','rejected'),(16,'A customer relationship management system tailored for freelancers.','Kevin Nguyen','Modular Laravel CRM with reporting and integrations.',90,'inactive','Custom CRM for Agency','approved'),(17,'A tool to optimize delivery routes using maps and real-time traffic.','Ayesha Siddiqui','Google Maps API with machine learning route predictions.',69,'inactive','Logistics Route Optimizer','rejected'),(18,'Track applied jobs, proposals sent, and follow-ups.','Haroon Malik','Single-page Vue app with Flask and PostgreSQL backend.',73,'inactive','Job Tracker for Freelancers','rejected'),(19,'Secure online portal for fee payments and records.','Sana Tariq','Node.js backend with Razorpay and dashboard analytics.',58,'inactive','School Fee Collection Portal','rejected'),(20,'Digitize menu and accept online food orders.','Kunal Mehra','Responsive menu with order system and real-time updates.',77,'inactive','Restaurant Online Menu & Ordering','approved'),(21,'Build a scalable e-commerce platform for electronics.','James Parker','We will use Django and React with Stripe integration.',85,'inactive','E-commerce Website Development','approved'),(22,'Create an AI tool to extract structured data from resumes.','Sophia Watson','We propose a Python NLP pipeline using spaCy and ML models.',78,'inactive','AI Resume Parser','approved'),(23,'Develop a web-based inventory management system for retail stores.','Michael Jordan','Flask backend with MySQL and Vue.js frontend will be used.',67,'inactive','Inventory Management System','rejected'),(24,'Design a cross-platform app for doctor appointment bookings.','Dr. Amanda Li','Flutter app with Firebase integration.',74,'inactive','Healthcare Appointment App','approved'),(25,'Online marketplace for rental and sales properties.','Rachel Green','Modern UI using Next.js and MongoDB.',82,'inactive','Real Estate Listing Platform','approved'),(26,'A customer relationship management system tailored for freelancers.','Kevin Nguyen','Modular Laravel CRM with reporting and integrations.',90,'inactive','Custom CRM for Agency','approved'),(27,'A tool to optimize delivery routes using maps and real-time traffic.','Ayesha Siddiqui','Google Maps API with machine learning route predictions.',69,'inactive','Logistics Route Optimizer','approved'),(28,'Track applied jobs, proposals sent, and follow-ups.','Haroon Malik','Single-page Vue app with Flask and PostgreSQL backend.',73,'inactive','Job Tracker for Freelancers','rejected'),(29,'Secure online portal for fee payments and records.','Sana Tariq','Node.js backend with Razorpay and dashboard analytics.',58,'active','School Fee Collection Portal',NULL),(30,'Digitize menu and accept online food orders.','Kunal Mehra','Responsive menu with order system and real-time updates.',77,'active','Restaurant Online Menu & Ordering',NULL);
/*!40000 ALTER TABLE `job_proposal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-20 16:05:12

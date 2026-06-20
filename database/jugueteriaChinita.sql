-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: jugueteriapython
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `juguetes`
--

DROP TABLE IF EXISTS `juguetes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `juguetes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha_registro` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juguetes`
--

LOCK TABLES `juguetes` WRITE;
/*!40000 ALTER TABLE `juguetes` DISABLE KEYS */;
INSERT INTO `juguetes` VALUES (1,'Buzz Lightyear',900.00,52,'2025-05-27 18:41:26'),(2,'Terrenator',600.00,4,'2025-05-27 18:41:26'),(3,'Conejo',80.00,10,'2025-05-27 18:41:26'),(4,'Oso de peluche',60.00,7,'2025-05-27 18:41:26'),(5,'Canicas',20.00,52,'2025-05-27 18:41:26'),(7,'Woody',700.00,1,'2025-05-27 18:41:26'),(9,'Rayo McQueen',500.00,23,'2025-09-30 07:29:20'),(15,'Dinosaurio',120.00,22,'2026-05-09 20:20:29'),(16,'Lego Batimovil',1200.00,3,'2026-05-09 20:21:46'),(17,'Supermercado',800.00,5,'2026-05-09 20:22:05'),(18,'Pochita',650.00,10,'2026-05-09 20:23:46'),(19,'Slinky',200.00,15,'2026-05-09 20:24:23'),(20,'Zorg',750.00,14,'2026-05-09 20:24:38'),(21,'Barbie',900.00,22,'2026-05-09 20:24:52'),(23,'prueba',500.00,50,'2026-05-12 12:39:29');
/*!40000 ALTER TABLE `juguetes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `pin` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'ADMIN','1234ADMIN'),(2,'EMPLEADO','5678EMP'),(3,'CLIENTE','');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `fecha_registro` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `rol_id` (`rol_id`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'AndrePok','Andre','Siqueiros','hola123',3,'2025-05-27 18:46:32'),(2,'gol','Gael','Nevarez','hola123',1,'2025-05-27 18:46:32'),(3,'costaelpro18','Luis','Morales','hola123',2,'2025-05-27 18:46:32'),(4,'kacto','Luis','Eagler','hola122',2,'2025-09-11 08:26:05'),(9,'arsenal','Eduardo','Arce','hola123',3,'2025-09-11 08:58:48'),(10,'Torvics','Victor','Osornio','taiwan123',2,'2025-09-12 19:08:58'),(11,'SeaBassy','Sebastian','Pearson','hola123',1,'2025-09-12 19:10:27'),(12,'RomanDays','Jose','Romandia','holapapu890',3,'2025-09-12 19:11:07'),(13,'diosaOrtega','Jenna','Ortega','miamor',1,'2025-09-29 15:52:08');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-20 12:31:48

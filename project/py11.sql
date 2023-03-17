-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Mar 17, 2023 at 08:50 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py11`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
CREATE TABLE IF NOT EXISTS `bill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customername` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `billdate` date NOT NULL,
  `amount` int(11) NOT NULL,
  `iscash` int(1) NOT NULL DEFAULT '1',
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`id`, `customername`, `billdate`, `amount`, `iscash`, `email`) VALUES
(1, 'ankit', '2022-10-09', 100, 1, 'ankit@gmail.com'),
(2, 'harsh bhattt', '2022-10-09', 55100, 2, 'harsh@mail.com'),
(3, 'ram', '2022-10-09', 62600, 1, 'ram@gmail.com'),
(4, 'tarun', '2022-10-09', 57600, 1, 'tarun@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `bill_product`
--

DROP TABLE IF EXISTS `bill_product`;
CREATE TABLE IF NOT EXISTS `bill_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `billid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `bill_product`
--

INSERT INTO `bill_product` (`id`, `productid`, `quantity`, `price`, `billid`) VALUES
(5, 1, 1, 55000, 2),
(6, 8, 2, 50, 2),
(4, 1, 1, 100, 1),
(7, 1, 1, 55000, 3),
(8, 8, 2, 50, 3),
(9, 7, 3, 2500, 3),
(10, 1, 1, 55000, 4),
(11, 8, 2, 50, 4),
(12, 7, 1, 2500, 4);

-- --------------------------------------------------------

--
-- Table structure for table `mytransaction`
--

DROP TABLE IF EXISTS `mytransaction`;
CREATE TABLE IF NOT EXISTS `mytransaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tourid` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `flag` int(1) NOT NULL,
  `description` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `challanno` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `trandate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `mytransaction`
--

INSERT INTO `mytransaction` (`id`, `tourid`, `amount`, `flag`, `description`, `challanno`, `trandate`) VALUES
(1, 1, 55000, 1, 'ticket collection ', '1', '2022-05-05'),
(2, 1, 550, 2, 'mandir ticket', '1000', '2022-05-06'),
(3, 1, 1000, 2, 'tea', '2000', '2022-05-06'),
(4, 1, 5500, 2, '1st day lunch', '0', '2022-05-06'),
(5, 1, 1000, 1, 'last ticket ', '0', '2022-05-04');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `detail` varchar(128) NOT NULL,
  `price` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `isdeleted` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `detail`, `price`, `stock`, `isdeleted`) VALUES
(1, 'laptop', 'core i3 16gb ram 512GB ssd 3.1 GHZ processor', 55000, 6, 0),
(2, 'usb mouse', 'acer mouse', 500, 1000, 1),
(3, 'wireless keyboard', 'usb keyboard', 2500, 10, 1),
(5, 'Printer', 'HP lasterjet printer', 25000, 10, 1),
(6, 'web camera', 'web camera for shop', 2000, 10, 1),
(7, 'scanner', 'scanner for office use', 2500, 1, 0),
(8, 'mouse pad', 'mouse pad for mouse', 50, 98, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tour`
--

DROP TABLE IF EXISTS `tour`;
CREATE TABLE IF NOT EXISTS `tour` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `detail` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `start_date` date NOT NULL,
  `days` int(2) NOT NULL,
  `isdeleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tour`
--

INSERT INTO `tour` (`id`, `title`, `detail`, `start_date`, `days`, `isdeleted`) VALUES
(1, 'somanath visit', 'somnath dwarka visit', '2022-11-03', 5, 0),
(2, 'amabaji tour', 'abu ambaji tour', '2022-11-05', 3, 0),
(3, 'diu tour with tarun', 'tarun and prakash', '2022-12-01', 3, 1),
(4, 'pavagadh tour', 'jai mahakali', '2022-01-01', 2, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

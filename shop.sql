-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2020 at 11:34 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop`
--
CREATE DATABASE IF NOT EXISTS `shop` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `shop`;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--
-- Creation: Oct 28, 2020 at 04:54 AM
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `CID` int(11) NOT NULL,
  `CNAME` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `category`:
--

--
-- Dumping data for table `category`
--

INSERT DELAYED IGNORE INTO `category` (`CID`, `CNAME`) VALUES
(1, 'electronics'),
(2, 'shoes'),
(3, 'grocery'),
(4, 'toys'),
(5, 'stationery'),
(6, 'dress'),
(7, 'snacks');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--
-- Creation: Oct 28, 2020 at 04:54 AM
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `CUID` int(11) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `ADD1` varchar(50) DEFAULT NULL,
  `ADD2` varchar(50) DEFAULT NULL,
  `CITY` varchar(50) DEFAULT NULL,
  `PINCODE` varchar(50) DEFAULT NULL,
  `MOBILE` varchar(50) DEFAULT NULL,
  `GST` varchar(50) DEFAULT NULL,
  `EMAIL` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `customers`:
--

--
-- Dumping data for table `customers`
--

INSERT DELAYED IGNORE INTO `customers` (`CUID`, `NAME`, `ADD1`, `ADD2`, `CITY`, `PINCODE`, `MOBILE`, `GST`, `EMAIL`) VALUES
(1, 'KUMAR', '729-3758 Montes, Road', '375-725 Pharetra Av.', 'Herselt', '873431', '8', '9', 'dui.lectus@nunc.edu'),
(2, 'Harding', 'Ap #497-8353 Nam Rd.', '6765 Orci Avenue', 'Exeter', '5368', '6', '10', 'ut.pharetra.sed@Suspendissealiquet.edu'),
(3, 'Jolie', 'Ap #857-1437 Quis Street', '351-7347 Eu Av.', 'Abbateggio', '966127', '1', '3', 'pede@Mauris.org'),
(4, 'Tatum', 'P.O. Box 969, 6489 Nec Street', 'P.O. Box 298, 6329 Nulla Road', 'Couthuin', '425589', '2', '2', 'malesuada.fringilla.est@lacus.com'),
(5, 'Xyla', '4397 Dictum Av.', '473-1215 Vivamus Road', 'Tulita', '339762', '1', '6', 'velit@libero.edu'),
(6, 'Selma', '158-2516 Ridiculus Rd.', 'Ap #356-8059 Integer Rd.', 'Floridablanca', '97679', '3', '4', 'nec.urna@interdumfeugiatSed.co.uk'),
(7, 'Sloane', '3243 Blandit Rd.', '6000 Risus. Avenue', 'Drancy', '72679', '5', '6', 'nec@neque.ca'),
(8, 'Ivor', 'P.O. Box 436, 6790 Dictum. Ave', '5109 Nulla St.', 'Kitchener', '1410', '3', '8', 'Nullam@felisullamcorperviverra.edu'),
(9, 'Imani', '312-6882 Purus, St.', '5500 Tellus. St.', 'Velletri', '461738', '4', '5', 'dolor.dapibus@Nunc.com'),
(10, 'Mallory', '684-2242 Pharetra. Avenue', '6786 Molestie Street', 'Torella del Sannio', '5568', '7', '1', 'dolor.vitae@vestibulumneceuismod.co.uk'),
(11, 'geetha', 'sdf', 'sdfg343', 'salem', '636007', '99999', '45', 'geetha@gmail.com'),
(12, 'sd', 'sdf', 'sdf', 'sdf', 'sdf', 'sf', 'dsf', 'ds'),
(13, 'dsf', 'sdf', 'sdf', 'sdf', '3445', '4545', '5', 'dsfdf'),
(14, 'aaaa', 'aaaaa', 'aaaa', 'aaaa', '354354', '4543456', '6546', 'dgfg@fh'),
(15, 'cccc', 'cccc', 'cccc', 'cccc', '435', '46456', '2', 'ccc@fg');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--
-- Creation: Oct 28, 2020 at 05:44 AM
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `PID` int(11) NOT NULL,
  `PNAME` varchar(50) DEFAULT NULL,
  `DES` varchar(50) DEFAULT NULL,
  `CID` int(11) DEFAULT NULL,
  `PRICE` varchar(45) NOT NULL DEFAULT '',
  `SGST` varchar(45) NOT NULL DEFAULT '',
  `CGST` varchar(45) NOT NULL DEFAULT '',
  `IGST` varchar(45) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `product`:
--

--
-- Dumping data for table `product`
--

INSERT DELAYED IGNORE INTO `product` (`PID`, `PNAME`, `DES`, `CID`, `PRICE`, `SGST`, `CGST`, `IGST`) VALUES
(1, 'pc', 'pc flat', 7, '60000', '2', '2', '2'),
(2, 'MOTO', 'Moto G3', 1, '10000', '2', '2', '2'),
(3, 'NIKE', '8inch Black', 2, '5000', '2', '2', '2'),
(4, 'BOOK', 'C programming', 5, '500', '2', '2', '2'),
(5, 'PENCIL', 'HP Pencil', 5, '5', '2', '2', '2'),
(6, 'ERASER', 'HP Eraser', 5, '2', '2', '2', '2'),
(7, 'SCALE', '555 D Scale', 5, '5', '2', '2', '2'),
(9, 'dhal', 'dhal', 3, '50', '1', '1', '1'),
(10, 'rubic cube', 'rubic cube', 4, '100', '1', '1', '1'),
(12, 'barbie', 'barbie', 4, '200', '2', '2', '2');

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--
-- Creation: Oct 28, 2020 at 05:28 AM
--

DROP TABLE IF EXISTS `purchase`;
CREATE TABLE `purchase` (
  `PUID` int(11) NOT NULL,
  `VID` int(11) DEFAULT NULL,
  `PDATE` date DEFAULT NULL,
  `PID` int(11) DEFAULT NULL,
  `PRICE` varchar(50) DEFAULT NULL,
  `QTY` int(11) NOT NULL DEFAULT 0,
  `SGST` varchar(50) DEFAULT NULL,
  `CGST` varchar(50) DEFAULT NULL,
  `IGST` varchar(50) DEFAULT NULL,
  `TOTAL` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `purchase`:
--

--
-- Dumping data for table `purchase`
--

INSERT DELAYED IGNORE INTO `purchase` (`PUID`, `VID`, `PDATE`, `PID`, `PRICE`, `QTY`, `SGST`, `CGST`, `IGST`, `TOTAL`) VALUES
(1, 1, '2020-10-20', 1, '15000', 10, '2', '2', '2', '150000'),
(2, 1, '2020-10-20', 2, '20', 5, '2', '2', '2', '100'),
(3, 2, '2020-10-21', 1, '15000', 5, '2', '2', '2', '75000'),
(6, 2, '2020-10-31', 2, '2', 2, '2', '2', '2', '10'),
(7, 3, '2020-11-02', 10, '50', 20, '1', '1', '1', '1003'),
(8, 4, '2020-11-02', 10, '50', 20, '1', '1', '1', '1003'),
(9, 1, '2020-11-02', 6, '1500', 10, '2', '2', '2', '15006');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--
-- Creation: Oct 28, 2020 at 05:28 AM
--

DROP TABLE IF EXISTS `sales`;
CREATE TABLE `sales` (
  `SAID` int(11) NOT NULL,
  `CUID` int(11) DEFAULT NULL,
  `BILL` varchar(50) DEFAULT NULL,
  `PDATE` date DEFAULT NULL,
  `PID` int(11) DEFAULT NULL,
  `PRICE` varchar(50) DEFAULT NULL,
  `QTY` int(11) DEFAULT NULL,
  `SGST` varchar(50) DEFAULT NULL,
  `CGST` varchar(50) DEFAULT NULL,
  `IGST` varchar(50) DEFAULT NULL,
  `TOTAL` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `sales`:
--

--
-- Dumping data for table `sales`
--

INSERT DELAYED IGNORE INTO `sales` (`SAID`, `CUID`, `BILL`, `PDATE`, `PID`, `PRICE`, `QTY`, `SGST`, `CGST`, `IGST`, `TOTAL`) VALUES
(1, 1, '2000', '2020-10-29', 1, '75000', 5, '1500.0', '1500.0', '1500.0', '79500.0'),
(2, 1, '2000', '2020-10-29', 2, '30000', 3, '600.0', '600.0', '600.0', '31800.0'),
(3, 1, '2000', '2020-10-29', 3, '30000', 6, '600.0', '600.0', '600.0', '31800.0'),
(4, 1, '2001', '2020-10-30', 4, '2000', 4, '40.0', '40.0', '40.0', '2120.0'),
(5, 1, '2001', '2020-10-30', 5, '25', 5, '0.5', '0.5', '0.5', '26.5'),
(6, 1, '2002', '2020-10-29', 2, '10000', 1, '200.0', '200.0', '200.0', '10600.0'),
(7, 1, '2002', '2020-10-29', 3, '25000', 5, '500.0', '500.0', '500.0', '26500.0'),
(8, 1, '2002', '2020-10-29', 4, '2000', 4, '40.0', '40.0', '40.0', '2120.0'),
(9, 1, '2003', '2020-10-29', 3, '5000', 1, '100.0', '100.0', '100.0', '5300.0'),
(10, 2, '2004', '2020-11-02', 9, '200', 4, '2.0', '2.0', '2.0', '206.0'),
(11, 2, '2004', '2020-11-02', 10, '3000', 30, '30.0', '30.0', '30.0', '3090.0'),
(12, 4, '2005', '2020-11-02', 6, '20', 10, '0.4', '0.4', '0.4', '21.199999999999996'),
(13, 4, '2005', '2020-11-02', 7, '25', 5, '0.5', '0.5', '0.5', '26.5');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--
-- Creation: Oct 28, 2020 at 05:28 AM
--

DROP TABLE IF EXISTS `stock`;
CREATE TABLE `stock` (
  `SID` int(11) NOT NULL,
  `PID` int(11) DEFAULT NULL,
  `QTY` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `stock`:
--

--
-- Dumping data for table `stock`
--

INSERT DELAYED IGNORE INTO `stock` (`SID`, `PID`, `QTY`) VALUES
(1, 1, 0),
(2, 2, 2),
(3, 3, 0),
(4, 4, 0),
(5, 5, 0),
(6, 6, 10),
(7, 7, 5),
(8, 8, 10),
(9, 10, 10),
(10, 12, 50),
(11, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--
-- Creation: Oct 28, 2020 at 04:54 AM
--

DROP TABLE IF EXISTS `user_login`;
CREATE TABLE `user_login` (
  `ID` int(11) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `UNAME` varchar(50) DEFAULT NULL,
  `PASS` varchar(50) DEFAULT NULL,
  `ROLE` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `user_login`:
--

--
-- Dumping data for table `user_login`
--

INSERT DELAYED IGNORE INTO `user_login` (`ID`, `NAME`, `UNAME`, `PASS`, `ROLE`) VALUES
(1, 'admin', 'admin', 'admin', 'admin'),
(2, 'stock', 'stock', 'stock', 'stock'),
(3, 'sales', 'sales', 'sales', 'sales'),
(5, 'harini', 'harini', '1234', 'sales'),
(6, 'kumar', 'kumar', '1234', 'stock'),
(7, 'prasanna', 'prasanna', 'prasanna', 'sales'),
(8, 'ram', 'ram', 'ram', 'sales');

-- --------------------------------------------------------

--
-- Table structure for table `vendor`
--
-- Creation: Oct 28, 2020 at 04:54 AM
--

DROP TABLE IF EXISTS `vendor`;
CREATE TABLE `vendor` (
  `VID` int(11) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL,
  `ADD1` varchar(50) DEFAULT NULL,
  `ADD2` varchar(50) DEFAULT NULL,
  `CITY` varchar(50) DEFAULT NULL,
  `PINCODE` varchar(50) DEFAULT NULL,
  `MOBILE` varchar(50) DEFAULT NULL,
  `GST` varchar(50) DEFAULT NULL,
  `EMAIL` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- RELATIONSHIPS FOR TABLE `vendor`:
--

--
-- Dumping data for table `vendor`
--

INSERT DELAYED IGNORE INTO `vendor` (`VID`, `NAME`, `ADD1`, `ADD2`, `CITY`, `PINCODE`, `MOBILE`, `GST`, `EMAIL`) VALUES
(1, 'Harini', '3781 Mus. Road', 'Ap #599-799 Urna. Ave', 'Padre Hurtado', '76-293', '6', '5', 'pede.ultrices.a@tempus.org'),
(2, 'Bell', 'Ap #295-9841 Proin Rd.', '5440 Dis Street', 'Develi', '24030', '1', '1', 'neque@leoVivamusnibh.net'),
(3, 'Louis', '519-9001 Donec Av.', 'Ap #743-9388 Facilisis, Rd.', 'Bangalore', '8625', '5', '7', 'faucibus.lectus@necmauris.co.uk'),
(4, 'Fallon', '6892 In Avenue', '759-7698 Dolor. Rd.', 'Farciennes', 'VN1 8IW', '9', '7', 'nisl.Nulla.eu@mienimcondimentum.org'),
(5, 'Ishmael', 'Ap #781-3076 Velit. Street', '8645 Nonummy Av.', 'Sant\'Eusanio Forconese', '75501', '4', '5', 'urna.convallis.erat@metusIn.org'),
(6, 'Brennan', '858-5960 Tempor Road', 'P.O. Box 687, 8558 Interdum. Av.', 'Belcarra', '74346', '4', '6', 'vel.turpis.Aliquam@Nulla.org'),
(7, 'Anastasia', '7429 Ullamcorper Rd.', 'Ap #751-8477 Quis Avenue', 'Höchst', '27778', '4', '6', 'at@Pellentesque.com'),
(8, 'Nerea', 'P.O. Box 947, 5871 Ut, St.', 'Ap #188-3069 Lacus. Ave', 'Orange', '5943', '8', '9', 'ornare.egestas.ligula@bibendumullamcorper.ca'),
(9, 'Austin', '748-2731 Primis Rd.', 'P.O. Box 601, 1489 Nam Av.', 'Saint-Pierre', '58411-325', '8', '6', 'sagittis.lobortis.mauris@Morbinequetellus.edu'),
(10, 'Kieran', 'Ap #936-7573 Vivamus Avenue', '5577 Sociis St.', 'Çarşamba', '766746', '8', '5', 'urna.suscipit@fermentumrisusat.co.uk'),
(11, 'Elmo', 'Ap #635-3982 Sed, St.', 'Ap #325-2901 Mauris Ave', 'Amqui', '70674', '6', '5', 'leo@Aliquam.co.uk'),
(12, 'Kermit', 'P.O. Box 385, 4841 Semper, Avenue', '489-5177 Sed Street', 'Nankana Sahib', '217820', '6', '6', 'dictum.eu@euodioPhasellus.co.uk'),
(13, 'Forrest', 'Ap #776-1990 Integer Road', 'P.O. Box 256, 6004 Egestas Street', 'Belvedere Ostrense', '56-942', '3', '7', 'vitae.erat@vitaeposuereat.co.uk'),
(14, 'Bernard', 'P.O. Box 337, 171 Ipsum Street', 'Ap #781-2805 Ut Rd.', 'Workum', '995908', '6', '6', 'felis@consectetuer.edu'),
(15, 'Ferris', 'Ap #128-6102 Dapibus Rd.', '2291 Erat Ave', 'Gullegem', '08980', '2', '9', 'tempus.mauris.erat@nisisemsemper.org'),
(16, 'Moana', '559-3393 Ut Street', 'P.O. Box 716, 4008 Ligula Ave', 'Multan', '17360', '6', '10', 'Donec.elementum@eu.net'),
(17, 'Berk', '235-2661 Donec St.', 'P.O. Box 999, 3983 Et Street', 'Nil-Saint-Vincent-Saint-Martin', '52646', '2', '7', 'pharetra.Quisque@quislectusNullam.co.uk'),
(18, 'Vera', '269-4482 Arcu St.', '4803 Est, Ave', 'Campomorone', '472193', '1', '4', 'a.scelerisque.sed@lacinia.org'),
(19, 'Wilma', 'P.O. Box 523, 7714 Massa. St.', '310-8057 Est. Rd.', 'Guadalupe', '1136', '9', '4', 'Donec@eu.ca'),
(20, 'Amber', 'Ap #887-9134 Nibh. Rd.', '887-3636 Scelerisque Avenue', 'Te Awamutu', '242970', '10', '6', 'urna.Nunc@turpisIn.net'),
(21, 'sara', 'nagar', 'kumaran', 'salem', '12345', '2', '2', 'sarakumar@gmail.com'),
(22, 'ddddd', 'ddd', 'd', 'dd', '5465', '4564768', '3', 'dfd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CUID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`PID`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`PUID`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`SAID`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`SID`);

--
-- Indexes for table `user_login`
--
ALTER TABLE `user_login`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `vendor`
--
ALTER TABLE `vendor`
  ADD PRIMARY KEY (`VID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `CID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `CUID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `purchase`
--
ALTER TABLE `purchase`
  MODIFY `PUID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `SAID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `SID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `user_login`
--
ALTER TABLE `user_login`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `vendor`
--
ALTER TABLE `vendor`
  MODIFY `VID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

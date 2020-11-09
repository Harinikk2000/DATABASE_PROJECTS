-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2020 at 01:56 PM
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
-- Database: `movie`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `BID` int(11) NOT NULL,
  `CID` int(11) NOT NULL,
  `MID` int(11) NOT NULL,
  `SEAT` text NOT NULL,
  `TOTAL` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`BID`, `CID`, `MID`, `SEAT`, `TOTAL`) VALUES
(1, 1, 3, '10', '1500'),
(2, 1, 2, '40', '6000'),
(3, 3, 1, '30', '6000'),
(4, 1, 1, '2', '400'),
(5, 4, 4, '2', '600');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `CID` int(11) NOT NULL,
  `CNAME` varchar(20) NOT NULL,
  `PHNO` varchar(10) NOT NULL,
  `ADDR` varchar(20) NOT NULL,
  `EMAIL` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`CID`, `CNAME`, `PHNO`, `ADDR`, `EMAIL`) VALUES
(1, 'harini', '9047688507', 'shankar nagar', 'harini@gmail.com'),
(2, 'kumar', '123456789', 'asfasdfsfdsf', 'ssdfffdsf'),
(3, 'geetha', '789456123', 'dsferet', 'wercxv'),
(4, 'ram', '9994748507', 'kumaran nagar', 'ram@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `MID` int(11) NOT NULL,
  `NAME` varchar(25) NOT NULL,
  `FORMAT` varchar(5) NOT NULL,
  `SHOWDATE` date NOT NULL,
  `SHOWTIME` time NOT NULL,
  `PRICE` varchar(10) NOT NULL,
  `SEAT` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`MID`, `NAME`, `FORMAT`, `SHOWDATE`, `SHOWTIME`, `PRICE`, `SEAT`) VALUES
(1, 'Titanic', '3D', '2020-11-10', '04:20:00', '200', '8'),
(2, 'Titanic', '2D', '2020-11-11', '04:20:00', '150', '0'),
(3, 'The detail', '2D', '2020-11-12', '06:30:00', '150', '0'),
(4, 'penguin', '3D', '2020-11-21', '12:00:00', '300', '48'),
(5, 'penguin', '3D', '2020-11-21', '00:00:00', '300', '50');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UID` int(11) NOT NULL,
  `UNAME` varchar(15) NOT NULL,
  `UPASS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UID`, `UNAME`, `UPASS`) VALUES
(1, 'admin', 123);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`BID`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`MID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `BID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `CID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `MID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

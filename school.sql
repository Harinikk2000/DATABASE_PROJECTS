-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2020 at 11:40 AM
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
-- Database: `school`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_class`
--

CREATE TABLE `add_class` (
  `CID` int(10) UNSIGNED NOT NULL,
  `STD` varchar(45) NOT NULL DEFAULT '',
  `SEC` varchar(45) NOT NULL DEFAULT '',
  `TID` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `TPASS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `add_class`
--

INSERT INTO `add_class` (`CID`, `STD`, `SEC`, `TID`, `TPASS`) VALUES
(1, '1', 'a', 1002, 1302),
(2, '1', 'b', 1003, 1303),
(3, '2', 'a', 1002, 1302),
(4, '2', 'b', 1003, 1303),
(5, '1', 'c', 1002, 1302);

-- --------------------------------------------------------

--
-- Table structure for table `add_staff`
--

CREATE TABLE `add_staff` (
  `TID` int(10) UNSIGNED NOT NULL,
  `TNAME` varchar(45) NOT NULL DEFAULT '',
  `TCODE` int(45) UNSIGNED NOT NULL,
  `TPASS` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `TLOGS` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `add_staff`
--

INSERT INTO `add_staff` (`TID`, `TNAME`, `TCODE`, `TPASS`, `TLOGS`) VALUES
(1, 'Harini', 1002, 1302, '2020-07-24 07:33:31'),
(2, 'Geetha', 1003, 1303, '2020-07-24 07:33:51');

-- --------------------------------------------------------

--
-- Table structure for table `add_student`
--

CREATE TABLE `add_student` (
  `SID` int(11) NOT NULL,
  `SNAME` varchar(50) NOT NULL,
  `ROLL` int(11) NOT NULL,
  `DOB2` varchar(50) NOT NULL,
  `STDD` int(11) NOT NULL,
  `SEC` varchar(5) NOT NULL,
  `FNAME` varchar(50) NOT NULL,
  `ADDRESS` varchar(255) NOT NULL,
  `PHONE` int(11) NOT NULL,
  `TC` varchar(5) NOT NULL,
  `added_date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `add_student`
--

INSERT INTO `add_student` (`SID`, `SNAME`, `ROLL`, `DOB2`, `STDD`, `SEC`, `FNAME`, `ADDRESS`, `PHONE`, `TC`, `added_date`) VALUES
(1, 'Aarthi', 100, '14-10-2000', 1, 'a', 'aaa', 'aaa111', 123, 'y', '2020-07-24 07:37:13'),
(2, 'Aashika', 101, '11-01-2000', 1, 'a', 'bbb', 'bbb222', 234, 'y', '2020-07-24 07:38:29'),
(3, 'Banu', 103, '02-02-2000', 1, 'b', 'ccc', 'ccc111', 456, 'y', '2020-07-24 07:39:04'),
(4, 'Babu', 104, '03-05-2000', 2, 'a', 'ddd', 'ddd111', 5678, 'y', '2020-07-24 07:39:41'),
(5, 'Chatty', 105, '01-01-2000', 1, 'b', 'eee', 'eee444', 678, 'y', '2020-07-24 07:53:52'),
(6, 'DivyaVM', 106, '07-05-2000', 1, 'b', 'nnn', 'nnn777', 890, 'y', '2020-07-24 07:54:57'),
(7, 'Deepika', 107, '17-11-2000', 2, 'a', 'mmm', 'mmm222', 164, 'y', '2020-07-24 07:55:40'),
(8, 'HariniKK', 108, '19-10-2000', 2, 'a', 'zzz', 'zzz333', 187, 'y', '2020-07-24 07:56:14'),
(9, 'HariniS', 109, '14-12-2000', 2, 'a', 'rrr', 'rrr333', 140, 'y', '2020-07-24 07:56:48'),
(10, 'JaisreeV', 110, '01-03-2000', 1, 'b', 'fff', 'fff777', 374, 'y', '2020-07-24 07:57:22');

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE `exam` (
  `EID` int(11) NOT NULL,
  `ENAME` varchar(255) NOT NULL,
  `logss` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `exam`
--

INSERT INTO `exam` (`EID`, `ENAME`, `logss`) VALUES
(1, 'unit1', '2020-08-29 20:34:54'),
(2, 'unit2', '2020-08-29 20:35:01');

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `EID1` int(11) NOT NULL,
  `EXID1` int(11) NOT NULL,
  `ROLL1` int(11) NOT NULL,
  `ENG` int(11) NOT NULL,
  `MATH` int(11) NOT NULL,
  `SCI` int(11) NOT NULL,
  `TOTAL` int(11) DEFAULT NULL,
  `AVG` float DEFAULT NULL,
  `RESULT1` varchar(5) DEFAULT 'PASS',
  `GRADE` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`EID1`, `EXID1`, `ROLL1`, `ENG`, `MATH`, `SCI`, `TOTAL`, `AVG`, `RESULT1`, `GRADE`) VALUES
(1, 1, 100, 10, 10, 10, 30, 10, 'FAIL', 'F'),
(2, 1, 101, 60, 60, 60, 180, 60, 'PASS', 'C'),
(3, 1, 102, 70, 70, 70, 210, 70, 'PASS', 'B'),
(4, 1, 103, 80, 80, 80, 240, 80, 'PASS', 'A'),
(5, 1, 104, 90, 90, 90, 270, 90, 'PASS', 'O'),
(6, 1, 105, 95, 95, 95, 285, 95, 'PASS', 'O'),
(7, 1, 106, 84, 51, 74, 209, 70, 'PASS', 'B'),
(8, 1, 107, 55, 77, 99, 231, 77, 'PASS', 'B'),
(9, 1, 110, 100, 100, 100, 300, 100, 'PASS', 'O'),
(10, 2, 100, 90, 90, 90, 270, 90, 'PASS', 'O');

-- --------------------------------------------------------

--
-- Table structure for table `pay_fee`
--

CREATE TABLE `pay_fee` (
  `PID` int(11) NOT NULL,
  `ROLL2` int(11) NOT NULL DEFAULT 0,
  `SNAME2` varchar(50) NOT NULL,
  `CLASS2` int(11) NOT NULL DEFAULT 0,
  `SEC2` varchar(5) NOT NULL,
  `FEES2` int(11) NOT NULL,
  `PAID2` int(11) NOT NULL DEFAULT 0,
  `BAL2` int(11) NOT NULL,
  `LOGS2` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pay_fee`
--

INSERT INTO `pay_fee` (`PID`, `ROLL2`, `SNAME2`, `CLASS2`, `SEC2`, `FEES2`, `PAID2`, `BAL2`, `LOGS2`) VALUES
(1, 100, 'Aarthi', 1, 'a', 5000, 200, 4400, '2020-07-24 07:37:13'),
(2, 101, 'Aashika', 1, 'a', 5000, 0, 5000, '2020-07-24 07:38:29'),
(3, 103, 'Banu', 1, 'b', 5000, 0, 5000, '2020-07-24 07:39:04'),
(4, 104, 'Babu', 2, 'a', 5500, 0, 5500, '2020-07-24 07:39:41'),
(5, 105, 'Chatty', 1, 'b', 5000, 0, 5000, '2020-07-24 07:53:52'),
(6, 106, 'DivyaVM', 1, 'b', 5000, 0, 5000, '2020-07-24 07:54:57'),
(7, 107, 'Deepika', 2, 'a', 5500, 0, 5500, '2020-07-24 07:55:40'),
(8, 108, 'HariniKK', 2, 'a', 5500, 0, 5500, '2020-07-24 07:56:14'),
(9, 109, 'HariniS', 2, 'a', 5500, 0, 5500, '2020-07-24 07:56:48'),
(10, 110, 'JaisreeV', 1, 'b', 5000, 0, 5000, '2020-07-24 07:57:22');

-- --------------------------------------------------------

--
-- Table structure for table `staff_att`
--

CREATE TABLE `staff_att` (
  `stid` int(11) NOT NULL,
  `stcode` int(11) NOT NULL,
  `ID1` int(11) NOT NULL,
  `atend` varchar(5) NOT NULL DEFAULT 'P',
  `atdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff_att`
--

INSERT INTO `staff_att` (`stid`, `stcode`, `ID1`, `atend`, `atdate`) VALUES
(1, 1002, 1, 'P', '2020-07-28'),
(2, 1003, 2, 'P', '2020-07-28'),
(3, 1002, 1, 'A', '2020-07-29'),
(4, 1003, 2, 'A', '2020-07-29');

-- --------------------------------------------------------

--
-- Table structure for table `std1`
--

CREATE TABLE `std1` (
  `CLASSID1` int(11) NOT NULL,
  `STD1` int(11) DEFAULT NULL,
  `SECTION` varchar(5) DEFAULT NULL,
  `SID1` int(11) DEFAULT NULL,
  `ROLLNO` int(11) DEFAULT NULL,
  `DOB1` varchar(50) DEFAULT NULL,
  `SNAME1` varchar(255) DEFAULT NULL,
  `ATDATE1` datetime DEFAULT NULL,
  `ATD1` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `std1`
--

INSERT INTO `std1` (`CLASSID1`, `STD1`, `SECTION`, `SID1`, `ROLLNO`, `DOB1`, `SNAME1`, `ATDATE1`, `ATD1`) VALUES
(1, 1, 'a', 1, 100, '14-10-2000', 'Aarthi', '2020-07-24 07:37:13', 'P'),
(2, 1, 'a', 2, 101, '11-01-2000', 'Aashika', '2020-07-24 07:38:29', 'P'),
(3, 1, 'b', 3, 103, '02-02-2000', 'Banu', '2020-07-24 07:39:04', 'P'),
(4, 2, 'a', 4, 104, '03-05-2000', 'Babu', '2020-07-24 07:39:41', 'P'),
(5, 1, 'b', 5, 105, '01-01-2000', 'Chatty', '2020-07-24 07:53:52', 'P'),
(6, 1, 'b', 6, 106, '07-05-2000', 'DivyaVM', '2020-07-24 07:54:57', 'P'),
(7, 2, 'a', 7, 107, '17-11-2000', 'Deepika', '2020-07-24 07:55:40', 'P'),
(8, 2, 'a', 8, 108, '19-10-2000', 'HariniKK', '2020-07-24 07:56:14', 'P'),
(9, 2, 'a', 9, 109, '14-12-2000', 'HariniS', '2020-07-24 07:56:48', 'P'),
(10, 1, 'b', 10, 110, '01-03-2000', 'JaisreeV', '2020-07-24 07:57:22', 'P'),
(11, 1, 'a', 1, NULL, NULL, NULL, '2020-07-26 20:14:50', 'A'),
(12, 1, 'a', 2, NULL, NULL, NULL, '2020-07-26 20:14:50', 'P'),
(13, 1, 'a', 1, NULL, NULL, NULL, '2020-07-26 22:34:43', 'P'),
(14, 1, 'a', 2, NULL, NULL, NULL, '2020-07-26 22:34:43', 'A'),
(15, 1, 'b', 1, NULL, NULL, NULL, '2020-07-26 22:34:55', 'A'),
(16, 1, 'b', 2, NULL, NULL, NULL, '2020-07-26 22:34:55', 'A'),
(17, 1, 'b', 3, NULL, NULL, NULL, '2020-07-26 22:34:55', 'P'),
(18, 1, 'b', 5, NULL, NULL, NULL, '2020-07-26 22:34:55', 'P'),
(19, 1, 'b', 6, NULL, NULL, NULL, '2020-07-26 22:34:55', 'P'),
(20, 1, 'b', 10, NULL, NULL, NULL, '2020-07-26 22:34:55', 'P');

-- --------------------------------------------------------

--
-- Table structure for table `stud_att`
--

CREATE TABLE `stud_att` (
  `CLASSID1` int(11) NOT NULL,
  `STD1` int(11) NOT NULL,
  `SECTION` varchar(5) NOT NULL,
  `SID1` int(11) NOT NULL,
  `ROLLNO` int(11) NOT NULL,
  `ATDATE1` date NOT NULL,
  `ATD1` varchar(5) NOT NULL DEFAULT 'P'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stud_att`
--

INSERT INTO `stud_att` (`CLASSID1`, `STD1`, `SECTION`, `SID1`, `ROLLNO`, `ATDATE1`, `ATD1`) VALUES
(1, 1, 'a', 1, 100, '2020-07-27', 'P'),
(2, 1, 'a', 2, 101, '2020-07-27', 'A'),
(3, 1, 'b', 3, 103, '2020-07-27', 'P'),
(4, 1, 'b', 5, 105, '2020-07-27', 'P'),
(5, 1, 'b', 6, 106, '2020-07-27', 'P'),
(6, 1, 'b', 10, 110, '2020-07-27', 'A'),
(7, 2, 'a', 4, 104, '2020-07-27', 'P'),
(8, 2, 'a', 7, 107, '2020-07-27', 'P'),
(9, 2, 'a', 8, 108, '2020-07-27', 'P'),
(10, 2, 'a', 9, 109, '2020-07-27', 'A'),
(11, 1, 'a', 1, 100, '2020-08-29', 'A'),
(12, 1, 'a', 2, 101, '2020-08-29', 'P');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UID` int(11) NOT NULL,
  `UNAME` varchar(50) NOT NULL DEFAULT '',
  `UCODE` int(11) NOT NULL,
  `UPASS` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `UROLE` varchar(50) NOT NULL DEFAULT 'Staff'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UID`, `UNAME`, `UCODE`, `UPASS`, `UROLE`) VALUES
(1, 'admin', 1000, 1300, 'admin'),
(2, 'office', 1001, 1301, 'office'),
(3, 'Harini', 1002, 1302, 'Staff'),
(4, 'Geetha', 1003, 1303, 'Staff');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_class`
--
ALTER TABLE `add_class`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `add_staff`
--
ALTER TABLE `add_staff`
  ADD PRIMARY KEY (`TID`);

--
-- Indexes for table `add_student`
--
ALTER TABLE `add_student`
  ADD PRIMARY KEY (`SID`);

--
-- Indexes for table `exam`
--
ALTER TABLE `exam`
  ADD PRIMARY KEY (`EID`);

--
-- Indexes for table `marks`
--
ALTER TABLE `marks`
  ADD PRIMARY KEY (`EID1`);

--
-- Indexes for table `pay_fee`
--
ALTER TABLE `pay_fee`
  ADD PRIMARY KEY (`PID`);

--
-- Indexes for table `staff_att`
--
ALTER TABLE `staff_att`
  ADD PRIMARY KEY (`stid`);

--
-- Indexes for table `std1`
--
ALTER TABLE `std1`
  ADD PRIMARY KEY (`CLASSID1`);

--
-- Indexes for table `stud_att`
--
ALTER TABLE `stud_att`
  ADD PRIMARY KEY (`CLASSID1`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_class`
--
ALTER TABLE `add_class`
  MODIFY `CID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `add_staff`
--
ALTER TABLE `add_staff`
  MODIFY `TID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `add_student`
--
ALTER TABLE `add_student`
  MODIFY `SID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `exam`
--
ALTER TABLE `exam`
  MODIFY `EID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `marks`
--
ALTER TABLE `marks`
  MODIFY `EID1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `pay_fee`
--
ALTER TABLE `pay_fee`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `staff_att`
--
ALTER TABLE `staff_att`
  MODIFY `stid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `std1`
--
ALTER TABLE `std1`
  MODIFY `CLASSID1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `stud_att`
--
ALTER TABLE `stud_att`
  MODIFY `CLASSID1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `UID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

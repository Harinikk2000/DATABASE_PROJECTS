-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2020 at 11:41 AM
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
-- Database: `lib`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `BID` int(10) UNSIGNED NOT NULL,
  `BNAME` varchar(150) NOT NULL,
  `ISBN` varchar(45) NOT NULL DEFAULT '',
  `AUTHOR` text NOT NULL DEFAULT '',
  `STOCK` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`BID`, `BNAME`, `ISBN`, `AUTHOR`, `STOCK`) VALUES
(1, 'Web technology', '89880', 'Bharat Lohiya', 5),
(2, 'Grow with GK 7', '89010', 'Nisha Rajesh', 7),
(3, 'Computer Graphics Hand Book (MCQs with Answers)', '90240', 'Ms. M. Rajathi and Dr. R. Arumugam', 5),
(4, 'INDIAN CONSTITUTIONAL LAW', '90210', 'D.S. CHOPRA', 10),
(5, 'Abhirup Shishyvarti Margdarshika Std 3. 2', '94650', 'Rupesh Jadhav', 2),
(6, 'A Handbook to Learn Tulu', '94630', 'Mr. Pradyoth Hegde', 7),
(7, 'COMPUTER ARCHITECTURE Multiple Choice and Two Mark question and Answer', '90240', 'Ms. C. RAJANANDHINI and Mr. M. CHANDRAKUMAR PETER', 2),
(8, 'Abhirup Shishyvarti Margdarshika Std. 2', '94650', 'Rupesh Jadhav', 7),
(9, 'Learning with Fun', '89960', 'Mrs. Khushboo Agrawal', 4),
(10, 'Experimental Physics for Engineering Students', '54070', 'Mrs.A.JAYANTHI , Dr.K.SURESH KUMAR, Mr.N.SIDDHARDHAN', 9),
(11, 'Abhirup Shishyvarti Margdarshika Std. 1', '94650', 'Rupesh Jadhav', 7),
(12, 'A Fountain Pen Story', '90150', 'Bibek Debroy', 9),
(13, 'BYGL-001 YOGA Practical', '89960', 'IGNOU', 7),
(14, 'Emerging Trends in Software Design and Architecture', '90250', 'YV Subrahmanyam, Editor', 9),
(15, 'HASYARNAVA PRAHASANAM', '94150', 'M. Kesava Pateri', 7),
(16, 'VARIYAMKUNNATHU KUNJAHAMMAD HAJI : malabar kalapathile kalapakarikal', '53900', 'M Gangadaran', 2),
(17, 'Emerging Trends in E-Business', '90250', 'Vaibhav Mishra, Editor', 6),
(18, 'METAMORPHOSIS', '87260', 'FRANZ KAFKA', 6),
(19, 'Emerging Trends in Business Intelligence', '90250', 'Sashikala P, Editor', 9),
(20, 'SMACS Applications in Business', '90250', 'Bijeta Shaw, Editor', 7),
(21, 'Gurbani de Sankalpan di Vigianak Viakhia', '90060', 'Gurmit Singh Tiwana', 7),
(22, 'Elements of Big Data and Business Analytics', '90250', 'Sashikala P, Editor', 3),
(23, 'Mobile Technologies for Business - An Introduction', '90250', 'Bijeta Shaw, Editor', 9),
(24, 'Pikoos Friend', '94650', 'Avijit Roy', 1),
(25, 'BLUEBELLS WITH MALAYALAM ELEGANT UKG PART I1I', '89820', 'NEW JYOTHI PUBLICATIONS', 9),
(26, 'BLUEBELLS WITH MALAYALAM ELEGANT UKG PART I1', '89820', 'NEW JYOTHI PUBLICATIONS', 8),
(27, 'BLUEBELLS WITH MALAYALAM ELEGANT UKG PART 1', '89820', 'NEW JYOTHI PUBLICATIONS', 8),
(28, 'BLUEBELLS WITH MALAYALAM ELEGANT LKG PART III', '89820', 'NEW JYOTHI PUBLICATIONS', 2),
(29, 'Bharti Itihaas, Mithihaas', '89990', 'Manmohan Singh Bawa', 4),
(30, 'BLUEBELLS WITH MALAYALAM ELEGANT LKG PART II', '89820', 'NEW JYOTHI PUBLICATIONS', 9),
(31, 'BLUEBELLS WITH MALAYALAM ELEGANT LKG PART 1', '89820', 'NEW JYOTHI PUBLICATIONS', 7),
(32, 'Paranjothimunivar aruliya Thiruvilaiyaadal Puranam-Volume-I- Maduraik Kaandam', '54070', 'Dr.R. Vasantha Kumar, Dr.P.Thamilarasi & Dr.R.Madhan Kumar', 8),
(33, 'Practical Physics for Class 12', '89290', 'Binay P. Akhouri', 7),
(34, 'adhyapikiye jeevan ka gudanphal', '89190', 'shyam narayan mishra', 5),
(35, 'Gacchit Rekhechi Icchamrityu', '94510', 'Pallab Tewari', 10),
(36, 'KRUTIBHAV', '94650', 'DR BHARAT SOLANKI', 1),
(37, 'Wild Lentils: Treasure of Novel Diversity', '93710', 'Mohar Singh, Ashutosh Sarker, Sandeep Kumar, Ashok Kumar, Shiv Kumar and Kuldeep Singh', 2),
(38, 'Bharatya Sangeet Kosh', '87600', 'Bimalakanta Roychowdhury', 5),
(39, 'Sanjwel', '94650', 'Babalu karale', 10),
(40, 'Prasanga: Ramkinkar Beji', '87600', 'Shibaprasad Beij', 8),
(41, 'Lockdown and Severity of Migration', '93980', 'Prem P. Verma', 9),
(42, 'Prachin Bharater Dandoniti', '87600', 'Sri Jogendranath Tarko-Sankho-Vedantatirtho', 2),
(43, 'Journey from beginner to elite', '90190', 'Dr. Vishwas Kalyanrao Kadam & Dr. Ravi Bhushan', 6),
(44, 'Dak-Tikit-a Bangla O Bangalee', '87600', 'Amarendranath Bag', 4),
(45, 'MY THIRY ONE SHORT STORIES', '94650', 'DR DHANESH DWIVEDI', 6),
(46, 'Aviral', '88750', 'Ajoy Mallick', 8),
(47, 'Numerical Techniques', '89940', 'Dr. Kalyanrao Takale, Dr. Shrikisan Gaikwad, Dr. Mrs. Nivedita Mahajan, Dr. Amjad Shaikh, Mrs. Shamal Deshmukh, Dr. Veena Kshirsagar, S.R. Patil', 10),
(48, 'Air Power In Joint Operations: A Game Changer In A Limited Conflict With China', '90150', 'Arjun Subramaniam', 6),
(49, 'Graph Theory', '89940', 'Dr. Shrikisan Gaikwad, Dr. Kalyanrao Takale, Dr Pravin Jadhav, Dr. Amjad Shaikh, Dr Vikas Jadhav, Dr Veena Kshirsagar, S.R. Patil', 3),
(50, 'VIMARSH KE VIVIDH AAYAM', '94650', 'SUDHAKAR BABU PATHAK', 4);

-- --------------------------------------------------------

--
-- Table structure for table `persons`
--

CREATE TABLE `persons` (
  `UID` int(11) NOT NULL,
  `UNAME` varchar(255) NOT NULL,
  `UPASS` varchar(255) DEFAULT NULL,
  `ROLE` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `ID` int(10) UNSIGNED NOT NULL,
  `NAME` varchar(45) NOT NULL,
  `ROLL` varchar(45) NOT NULL,
  `STATUS` varchar(45) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`ID`, `NAME`, `ROLL`, `STATUS`) VALUES
(1, 'harini', 'AE101', 'yes'),
(2, 'geetha', 'AE102', 'yes'),
(3, 'kumar', 'AE103', 'no');

-- --------------------------------------------------------

--
-- Table structure for table `trans`
--

CREATE TABLE `trans` (
  `TID` int(10) UNSIGNED NOT NULL,
  `ID` int(11) DEFAULT NULL,
  `BID` int(11) DEFAULT NULL,
  `REMARKS` varchar(45) NOT NULL DEFAULT 'issued',
  `LOGS` datetime NOT NULL DEFAULT current_timestamp(),
  `STATUS` varchar(45) NOT NULL DEFAULT 'yes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trans`
--

INSERT INTO `trans` (`TID`, `ID`, `BID`, `REMARKS`, `LOGS`, `STATUS`) VALUES
(22, 1, 2, 'issued', '2020-06-30 20:10:32', 'yes'),
(23, 1, 2, 'received', '2020-06-30 20:10:32', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UID` int(11) NOT NULL,
  `UNAME` varchar(100) DEFAULT NULL,
  `UPASS` varchar(100) DEFAULT NULL,
  `ROLE` varchar(100) DEFAULT NULL,
  `dob` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UID`, `UNAME`, `UPASS`, `ROLE`, `dob`) VALUES
(1, 'Ram', '1234', 'Admin', '0000-00-00'),
(2, 'Sam', '1234', 'Student', '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`BID`);

--
-- Indexes for table `persons`
--
ALTER TABLE `persons`
  ADD PRIMARY KEY (`UID`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `trans`
--
ALTER TABLE `trans`
  ADD PRIMARY KEY (`TID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `BID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `persons`
--
ALTER TABLE `persons`
  MODIFY `UID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `trans`
--
ALTER TABLE `trans`
  MODIFY `TID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `UID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

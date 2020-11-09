-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2020 at 01:55 PM
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
-- Database: `dictionary`
--

-- --------------------------------------------------------

--
-- Table structure for table `english`
--

CREATE TABLE `english` (
  `sno` int(11) NOT NULL,
  `word` varchar(25) NOT NULL,
  `pronunciation` varchar(20) NOT NULL DEFAULT '',
  `definition` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `english`
--

INSERT INTO `english` (`sno`, `word`, `pronunciation`, `definition`) VALUES
(1, 'Abaciscus', 'ab.uh.sis.ahy', 'One of the tiles or squares of a tessellated pavement;\n   an abaculus.'),
(2, 'Abacist', 'abacus.ista.ist', 'One who uses an abacus in casting accounts; a calculator.'),
(3, 'Aback', 'uh.bak', 'An abacus.'),
(4, 'Abactinal', 'ab.actinal', 'Pertaining to the surface or end opposite to the mouth\n   in a radiate animal; -- opposed to actinal.'),
(5, 'Abaction', 'uh.bat.tion', 'Stealing cattle on a large scale.'),
(6, 'Abactor', 'uh.ba.ur', 'One who steals and drives away cattle or beasts by herds\n   or droves.'),
(7, 'Abaculi', 'a\'baek.ku.li', 'of Abaculus'),
(8, 'Cold', 'kowld', 'The sensation produced by the escape of heat; chilliness'),
(9, 'Collapse', 'kuh.laps', 'Extreme depression or sudden failing of all the vital'),
(10, 'Collision', 'kuh.li.zhn', 'The act of striking together'),
(11, 'Colon', 'ku.lon', 'A point or character, used to separate'),
(12, 'Column', 'kaw.luhm', 'A number of ships so arranged as to follow one another in'),
(13, 'Comb', 'kowm', 'A toothed instrument used for separating and cleansing wool,\n   flax, hair, etc.'),
(15, 'apple', 'a.ple', 'a fruit'),
(16, 'board', 'po.rd', 'It is a black coated sheat to write something.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `english`
--
ALTER TABLE `english`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `english`
--
ALTER TABLE `english`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

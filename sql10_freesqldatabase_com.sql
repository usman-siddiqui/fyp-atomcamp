-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql10.freesqldatabase.com
-- Generation Time: Aug 12, 2024 at 05:18 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql10725426`
--
CREATE DATABASE IF NOT EXISTS `sql10725426` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sql10725426`;

-- --------------------------------------------------------

--
-- Table structure for table `maintain_history`
--

CREATE TABLE `maintain_history` (
  `id` int(11) NOT NULL,
  `question` varchar(255) DEFAULT NULL,
  `answer` varchar(255) DEFAULT NULL,
  `session_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `maintain_history`
--

INSERT INTO `maintain_history` (`id`, `question`, `answer`, `session_id`) VALUES
(68, 'is chicken karahi available?', 'Apologies, the information does not specify if Chicken Karahi is available.', NULL),
(70, 'Is chicken wings available', 'Yes, Chicken Wings are available.', NULL),
(72, 'what is its price?', 'The price of Chicken Wings is 780.', NULL),
(74, 'Can you share its average ratings?', 'The average rating for Chicken Wings is 4.4.', NULL),
(76, 'what about mutton karahi?', 'Mutton Karahi is a spicy mutton curry cooked in a karahi. The price is 2480, and it has an average rating of 4.7.', NULL),
(78, 'but my son likes french fries', 'French Fries are available. They are crispy and golden, priced at 290, and have an average rating of 4.2.', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `maintain_history`
--
ALTER TABLE `maintain_history`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `maintain_history`
--
ALTER TABLE `maintain_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 21, 2023 at 01:52 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diabetes_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `detection_records`
--

CREATE TABLE `detection_records` (
  `id` int(11) NOT NULL,
  `pregnancies` varchar(20) NOT NULL,
  `glucose` varchar(20) NOT NULL,
  `blood_pressure` varchar(20) NOT NULL,
  `skin_thickness` varchar(20) NOT NULL,
  `insulin` varchar(20) NOT NULL,
  `bmi` varchar(20) NOT NULL,
  `dpf` varchar(20) NOT NULL,
  `age` varchar(20) NOT NULL,
  `outcome` int(1) NOT NULL,
  `detected_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detection_records`
--

INSERT INTO `detection_records` (`id`, `pregnancies`, `glucose`, `blood_pressure`, `skin_thickness`, `insulin`, `bmi`, `dpf`, `age`, `outcome`, `detected_at`) VALUES
(2, '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', 0, '2023-01-17 20:42:09'),
(4, '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', 1, '2023-01-17 21:21:20'),
(5, '2.0', '2.0', '2.0', '2.0', '2.0', '2.0', '2.0', '2.0', 1, '2023-01-17 21:35:07'),
(6, '1.0', '3.0', '2.0', '1.0', '1.0', '1.0', '1.0', '1.0', 1, '2023-01-21 12:29:46'),
(7, '1.0', '1.0', '1.0', '1.0', '1.0', '1.0', '11.0', '1.0', 1, '2023-01-21 12:32:10'),
(8, '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 0, '2023-01-21 12:32:27');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `phone`, `password`) VALUES
(3, 'James Daniel', 'james@example.com', '09000000000', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detection_records`
--
ALTER TABLE `detection_records`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detection_records`
--
ALTER TABLE `detection_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

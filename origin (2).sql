-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Machine: 127.0.0.1
-- Gegenereerd op: 21 mrt 2015 om 21:25
-- Serverversie: 5.6.21
-- PHP-versie: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Databank: `4sreviews`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `origin`
--

CREATE TABLE IF NOT EXISTS `origin` (
  `user_id` int(11) DEFAULT NULL,
  `North America` int(11) DEFAULT '0',
  `Mexico` int(11) DEFAULT '0',
  `South America` int(11) DEFAULT '0',
  `North Africa` int(11) DEFAULT '0',
  `South Africa` int(11) DEFAULT '0',
  `North Europe` int(200) NOT NULL DEFAULT '0',
  `South Europe` int(200) NOT NULL DEFAULT '0',
  `East Europe` int(200) NOT NULL DEFAULT '0',
  `England` int(200) NOT NULL DEFAULT '0',
  `Indonesia` int(200) NOT NULL DEFAULT '0',
  `Australia + New Zealand` int(200) NOT NULL DEFAULT '0',
  `West Asia` int(200) NOT NULL DEFAULT '0',
  `Middle East` int(200) NOT NULL DEFAULT '0',
  `India/Pakistan` int(200) NOT NULL DEFAULT '0',
  `Southeast Asia` int(200) NOT NULL DEFAULT '0',
  `China` int(200) NOT NULL DEFAULT '0',
  `Japan` int(200) NOT NULL DEFAULT '0',
  `No Idea!` int(200) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `origin`
--
ALTER TABLE `origin`
 ADD UNIQUE KEY `user_id` (`user_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

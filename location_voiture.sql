-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 21 fév. 2026 à 22:00
-- Version du serveur : 9.1.0
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `location_voiture`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add reservation', 7, 'add_reservation'),
(26, 'Can change reservation', 7, 'change_reservation'),
(27, 'Can delete reservation', 7, 'delete_reservation'),
(28, 'Can view reservation', 7, 'view_reservation'),
(29, 'Can add utilisateur', 8, 'add_utilisateur'),
(30, 'Can change utilisateur', 8, 'change_utilisateur'),
(31, 'Can delete utilisateur', 8, 'delete_utilisateur'),
(32, 'Can view utilisateur', 8, 'view_utilisateur'),
(33, 'Can add paiement', 9, 'add_paiement'),
(34, 'Can change paiement', 9, 'change_paiement'),
(35, 'Can delete paiement', 9, 'delete_paiement'),
(36, 'Can view paiement', 9, 'view_paiement'),
(37, 'Can add voiture', 10, 'add_voiture'),
(38, 'Can change voiture', 10, 'change_voiture'),
(39, 'Can delete voiture', 10, 'delete_voiture'),
(40, 'Can view voiture', 10, 'view_voiture'),
(41, 'Can add avis', 11, 'add_avis'),
(42, 'Can change avis', 11, 'change_avis'),
(43, 'Can delete avis', 11, 'delete_avis'),
(44, 'Can view avis', 11, 'view_avis');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'voiture', 'reservation'),
(8, 'voiture', 'utilisateur'),
(9, 'voiture', 'paiement'),
(10, 'voiture', 'voiture'),
(11, 'voiture', 'avis');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-09-26 15:36:51.338105'),
(2, 'auth', '0001_initial', '2025-09-26 15:36:52.069196'),
(3, 'admin', '0001_initial', '2025-09-26 15:36:52.350646'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-09-26 15:36:52.363064'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-09-26 15:36:52.373873'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-09-26 15:36:52.480884'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-09-26 15:36:52.539416'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-09-26 15:36:52.592339'),
(9, 'auth', '0004_alter_user_username_opts', '2025-09-26 15:36:52.601373'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-09-26 15:36:52.643058'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-09-26 15:36:52.644632'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-09-26 15:36:52.654692'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-09-26 15:36:52.693286'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-09-26 15:36:52.731560'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-09-26 15:36:52.773029'),
(16, 'auth', '0011_update_proxy_permissions', '2025-09-26 15:36:52.782238'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-09-26 15:36:52.820799'),
(18, 'sessions', '0001_initial', '2025-09-26 15:36:52.863224'),
(19, 'voiture', '0001_initial', '2025-09-26 15:36:53.347961'),
(20, 'voiture', '0002_alter_reservation_options_reservation_date_creation', '2025-09-29 16:05:16.541405'),
(21, 'voiture', '0003_alter_utilisateur_date_creation', '2025-09-30 12:41:33.174923'),
(22, 'voiture', '0004_utilisateur_is_2fa_enabled_utilisateur_otp_code_and_more', '2025-10-01 00:25:14.309235'),
(23, 'voiture', '0005_rename_is_2fa_enabled_utilisateur_email_verified', '2025-10-01 14:57:14.504816'),
(24, 'voiture', '0006_alter_reservation_statutr', '2025-10-03 20:46:02.974660');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('sg9uprm2fcu8j9j1tij3ypkniqb8lv19', '.eJyrViotyczJLE4sSS0tis9MUbIy1EERysvPVbJSKs5MyVRClSgoSoXIVSUWJaLJpeYmZuZApRzSQRy9ZKBaVEVF-TmpQDVlqZVA_bUAkJkyJw:1v8LZT:SxVYE-PJS0jBzLpgndIyPb2hUFhU6vSAiWhje6omceY', '2025-10-27 16:38:51.145958'),
('otpprcq965i3db63jnym8n9fsm8xwtwq', '.eJyrViotyczJLE4sSS0tis9MUbIyNNZBEcvLz1WyUnKszC9NSlRClSooSoXK5pfmJJbkl6LJp-YmZuYApRPB0gZmDukgAb1koB5UhUX5OalAdck5mal5JUq1APEhNkQ:1vIAW2:op5N0ycYYNF_x6zXDBjo71ZeZBK8aSi0q-JNgGEV7U0', '2025-11-23 18:51:54.426962'),
('2ibalf2kykqpt488df6gep4o3ytmiz6n', '.eJyrViotyczJLE4sSS0tis9MUbIy1EERysvPVbJSKs5MyVRClSgoSoXIVSUWJaLJpeYmZuZApRzSQRy9ZKBaVEVF-TmpQDVlqZVA_bUAkJkyJw:1vPLOo:2N0QoJ62bsVgMJ8creL9D2v9mdtalnTZXPUa_l9y204', '2025-12-13 13:54:06.583268'),
('t0xh4pcnfgqqqnkp5m2siost57nzyhxz', '.eJyrViotyczJLE4sSS0tis9MUbIy1EERysvPVbJSKs5MyVRClSgoSoXIVSUWJaLJpeYmZuZApRzSQRy9ZKBaVEVF-TmpQDVlqZVA_bUAkJkyJw:1vPsdK:kjgHWF3KlmzgyHrhmp_CfdG7n8QxMyEM6RygWJTbZ9w', '2025-12-15 01:23:18.031446'),
('quxgegsf4d8468wiq1mwhs18f6u3qd4b', '.eJyrViotyczJLE4sSS0tis9MUbIy1EERysvPVbJSKs5MyVRClSgoSoXIVSUWJaLJpeYmZuZApRzSQRy9ZKBaVEVF-TmpQDVlqZVA_bUAkJkyJw:1vT68t:zikqoA6INhHyXWHcndSNqJGoW8HfAxqfzNHKSS4fjQM', '2025-12-23 22:25:11.971472'),
('95ji5kyrhe8ngl5bg5t78vd3gdymzom5', '.eJyrViotyczJLE4sSS0tis9MUbIy1EERysvPVbJSKs5MyVRClSgoSoXIVSUWJaLJpeYmZuZApRzSQRy9ZKBaVEVF-TmpQDVlqZVA_bUAkJkyJw:1vmBnk:EEMKneHjAACdjTynX7SRnJs6p2s9Znn6sFWaXiEFs3s', '2026-02-14 14:18:16.282794');

-- --------------------------------------------------------

--
-- Structure de la table `voiture_avis`
--

DROP TABLE IF EXISTS `voiture_avis`;
CREATE TABLE IF NOT EXISTS `voiture_avis` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `note` smallint UNSIGNED NOT NULL,
  `commentaire` longtext,
  `dateAvis` datetime(6) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `voiture_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voiture_avis_utilisateur_id_7c1003a1` (`utilisateur_id`),
  KEY `voiture_avis_voiture_id_b8c139b0` (`voiture_id`)
) ;

--
-- Déchargement des données de la table `voiture_avis`
--

INSERT INTO `voiture_avis` (`id`, `note`, `commentaire`, `dateAvis`, `utilisateur_id`, `voiture_id`) VALUES
(1, 5, 'Excellent état', '2025-09-26 21:59:34.000000', 1, 1),
(13, 4, 'Satisfaisant', '2025-10-04 14:48:31.741561', 15, 3),
(3, 3, 'Correct', '2025-09-26 21:59:34.000000', 5, 3),
(4, 4, 'Bon rapport qualité/prix', '2025-09-26 21:59:34.000000', 7, 4),
(11, 4, 'tres bon', '2025-10-04 09:49:54.189843', 4, 2),
(8, 5, 'Superbe', '2025-09-26 21:59:34.000000', 5, 8),
(9, 4, 'Satisfaisant', '2025-09-26 21:59:34.000000', 7, 9),
(12, 4, 'Tres bon', '2025-10-04 09:50:54.611484', 13, 11);

-- --------------------------------------------------------

--
-- Structure de la table `voiture_paiement`
--

DROP TABLE IF EXISTS `voiture_paiement`;
CREATE TABLE IF NOT EXISTS `voiture_paiement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `montant` decimal(10,2) NOT NULL,
  `datePaiement` datetime(6) NOT NULL,
  `moyenPaiement` varchar(20) NOT NULL,
  `statutP` varchar(20) NOT NULL,
  `reservation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservation_id` (`reservation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `voiture_paiement`
--

INSERT INTO `voiture_paiement` (`id`, `montant`, `datePaiement`, `moyenPaiement`, `statutP`, `reservation_id`) VALUES
(4, 24000.00, '2025-09-26 21:57:38.000000', 'Carte', 'rembourse', 10),
(6, 16000.00, '2025-09-26 21:57:38.000000', 'Carte', 'effectue', 4),
(9, 20000.00, '2025-09-26 21:57:38.000000', 'PayPal', 'rembourse', 8),
(10, 15000.00, '2025-09-26 21:57:38.000000', 'MobileMoney', 'effectue', 9);

-- --------------------------------------------------------

--
-- Structure de la table `voiture_reservation`
--

DROP TABLE IF EXISTS `voiture_reservation`;
CREATE TABLE IF NOT EXISTS `voiture_reservation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dateDebut` date NOT NULL,
  `dateFin` date NOT NULL,
  `statutR` varchar(20) NOT NULL,
  `montant` decimal(10,2) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `voiture_id` bigint NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero` (`numero`),
  KEY `voiture_reservation_utilisateur_id_f37ee03b` (`utilisateur_id`),
  KEY `voiture_reservation_voiture_id_21eeae3e` (`voiture_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `voiture_reservation`
--

INSERT INTO `voiture_reservation` (`id`, `dateDebut`, `dateFin`, `statutR`, `montant`, `numero`, `utilisateur_id`, `voiture_id`, `date_creation`) VALUES
(14, '2025-11-09', '2025-11-12', 'EN_ATTENTE', 300000.00, 'Z8977', 1, 2, '2025-11-09 18:48:18.032300'),
(13, '2025-10-05', '2025-10-10', 'confirmee', 510000.00, 'L2534', 15, 3, '2025-10-04 14:39:23.792572'),
(4, '2025-10-02', '2025-10-06', 'en_attente', 16000.00, 'R1004', 7, 4, '2025-09-29 16:05:16.404154'),
(8, '2025-10-08', '2025-10-12', 'annulee', 20000.00, 'R1008', 5, 8, '2025-09-29 16:05:16.404154'),
(9, '2025-10-02', '2025-10-05', 'en_attente', 15000.00, 'R1009', 7, 9, '2025-09-29 16:05:16.404154'),
(10, '2025-10-07', '2025-10-11', 'confirmmee', 24000.00, 'R1010', 9, 10, '2025-09-29 16:05:16.404154'),
(12, '2025-10-04', '2025-10-07', 'en_cours', 320000.00, 'X5002', 13, 11, '2025-10-04 09:48:30.333242');

-- --------------------------------------------------------

--
-- Structure de la table `voiture_utilisateur`
--

DROP TABLE IF EXISTS `voiture_utilisateur`;
CREATE TABLE IF NOT EXISTS `voiture_utilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `adresse` longtext NOT NULL,
  `role` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `email_verified` tinyint(1) NOT NULL,
  `otp_code` varchar(6) DEFAULT NULL,
  `otp_created_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `voiture_utilisateur`
--

INSERT INTO `voiture_utilisateur` (`id`, `nom`, `prenom`, `email`, `telephone`, `adresse`, `role`, `password`, `date_creation`, `is_active`, `email_verified`, `otp_code`, `otp_created_at`) VALUES
(1, 'sidi', 'zara', 'zara@gmail.com', '20554154', '                        Niamey-Niger\r\n                    ', 'veyra', 'pbkdf2_sha256$1000000$2Xpv37DKOgIJugrJgLRw5p$l/hva/1OKVEaazmBNMaThedlvess93r6nWbEvsPNzGw=', '2025-09-26 15:40:51.287899', 1, 1, NULL, NULL),
(2, 'Diallo', 'Aoulat', 'aoulat1@example.com', '+22790000001', '                                                Niamey, Niger\r\n                    \r\n                    ', 'proprietaire', '123456', '2025-09-26 21:48:12.000000', 1, 0, '087776', '2025-10-04 14:08:47.405033'),
(4, 'Hassan', 'Ali', 'hassan3@example.com', '+22790000003', 'Niamey, Niger', 'client', 'password3', '2025-09-24 21:48:12.000000', 1, 0, NULL, NULL),
(5, 'Fatou', 'Issa', 'fatou4@example.com', '+22790000004', 'Niamey, Niger\r\n ', 'proprietaire', 'pbkdf2_sha256$1000000$MTBd1akOTlowGDCjfnc7ME$KeKASKbqnomQpOpXw3N7tdWARCNs+hr4VTJL9iu3jnw=', '2025-09-22 21:48:12.000000', 1, 0, '160116', '2025-10-04 11:22:41.526774'),
(6, 'Mariama', 'Salif', 'mariama5@example.com', '+22790000005', '                        Niamey, Niger\r\n                    ', 'client', 'pbkdf2_sha256$1000000$qROsw2peNTZpVB6v6XcKAY$AYfUjEW/aqMpPptbQAqSIT7r5jjqaDQkDZ7bHQlPCDI=', '2025-09-30 13:44:44.000000', 1, 0, NULL, NULL),
(7, 'Abdou', 'Kader', 'abdou6@example.com', '+22790000006', 'Niamey, Niger', 'proprietaire', 'password6', '0000-00-00 00:00:00.000000', 1, 0, NULL, NULL),
(8, 'Aissatou', 'Adam', 'aissatou7@example.com', '+22790000007', 'Niamey, Niger', 'client', 'password7', '2025-09-25 21:50:26.000000', 1, 0, NULL, NULL),
(9, 'Souleymane', 'Yacouba', 'souleymane8@example.com', '+22790000008', 'Niamey, Niger', 'veyra', 'password8', '2025-09-25 21:50:26.000000', 1, 0, NULL, NULL),
(10, 'Ramatou', 'Oumarou', 'ramatou9@example.com', '+22790000009', 'Niamey, Niger', 'client', 'password9', '0000-00-00 00:00:00.000000', 1, 0, NULL, NULL),
(11, 'Salif', 'Harouna', 'salif10@example.com', '+22790000010', 'Niamey, Niger', 'proprietaire', 'password10', '0000-00-00 00:00:00.000000', 1, 0, NULL, NULL),
(13, 'Ayouba', 'Aoulatou', 'aoulat06@gmail.com', '92628815', '                        niamey-niger\r\n                    ', 'client', 'pbkdf2_sha256$1000000$e4NU08Rf8V4BTQVtUIf7HY$4ivbFOpRFJLoE7wu38kk4SWemnxO6G1a8oxJryORf10=', '2025-10-01 14:58:48.291967', 1, 1, NULL, NULL),
(14, 'Ayouba Abdoulaye', 'Aoulat', 'aoulatouayoubaabdoulaye26@gmail.com', '88347667', '                        Plateau-Niamey\r\n                    ', 'proprietaire', 'pbkdf2_sha256$1000000$kxoFeuqegUhlDb1tXkdpbw$NMUyxxQNkLFxTUbFuLtJddZb40jrhtmyqu9Tliud11Y=', '2025-10-02 17:49:02.646609', 1, 1, NULL, NULL),
(15, 'Seyni', 'Ibrahim', 'ibseyha@gmail.com', '88777372', 'niamey-niger', 'CLIENT', 'pbkdf2_sha256$1000000$9nQt95rcoVMc8Btw8pnf1l$VQGvwNAHsT7BunB/OxSKPvpuYCbfiCAq6V/fMpgIBfE=', '2025-10-04 14:36:10.761901', 1, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `voiture_voiture`
--

DROP TABLE IF EXISTS `voiture_voiture`;
CREATE TABLE IF NOT EXISTS `voiture_voiture` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `marque` varchar(100) NOT NULL,
  `modele` varchar(100) NOT NULL,
  `annee` int UNSIGNED NOT NULL,
  `couleur` varchar(30) NOT NULL,
  `immatriculation` varchar(50) NOT NULL,
  `transmission` varchar(20) NOT NULL,
  `nb_places` int NOT NULL,
  `prix_jour` decimal(10,2) NOT NULL,
  `disponibilite` tinyint(1) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `description` longtext,
  `proprietaire_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `immatriculation` (`immatriculation`),
  KEY `voiture_voiture_proprietaire_id_f9e30882` (`proprietaire_id`)
) ;

--
-- Déchargement des données de la table `voiture_voiture`
--

INSERT INTO `voiture_voiture` (`id`, `marque`, `modele`, `annee`, `couleur`, `immatriculation`, `transmission`, `nb_places`, `prix_jour`, `disponibilite`, `photo`, `description`, `proprietaire_id`) VALUES
(1, 'Mercedes', 'Classe C', 2022, 'Noir', 'ABC123', 'automatique', 5, 15000.00, 0, 'voitures/2022_20.avif', '                                                                                                Véhicule de luxe pour vos occasions spéciales. La Mercedes Classe C offre un raffinement incomparable avec des finitions premium et des technologies de pointe pour une expérience de conduite d\'exception.\r\n                    \r\n                    \r\n                    \r\n                    ', 7),
(2, 'BMW', 'Série 5', 2021, 'Blanc', 'DEF456', 'automatique', 5, 75000.00, 1, 'voitures/2.jpg', '                                                Véhicule élégant et performant, idéal pour les trajets confortables et les déplacements professionnels. La BMW Série 5 allie style et technologie.\r\n                    \r\n                    ', 11),
(3, 'Audi', 'A6', 2022, 'Gris ', 'GHI789', 'automatique', 5, 85000.00, 0, 'voitures/3.jpeg', '                                                                                                Véhicule raffiné pour vos voyages. L\'Audi A6 offre un confort optimal avec des équipements modernes et une conduite agréable.\r\n                    \r\n                    \r\n                    \r\n                    ', 11),
(4, 'Tesla', 'Model 3', 2023, 'Rouge', 'JKL012', 'automatique', 5, 95000.00, 0, 'voitures/4.jpeg', '                                                                        Voiture électrique haut de gamme. La Tesla Model 3 combine performance, autonomie et technologies avancées pour une conduite innovante.\r\n                    \r\n                    \r\n                    ', 5),
(7, 'Peugeot', '508', 2022, 'Blanc', 'STU901', 'automatique', 5, 50000.00, 1, 'voitures/7.jpg', '                                                                                                Voiture moderne et stylée pour les trajets quotidiens et professionnels. La Peugeot 508 allie confort et design.\r\n                    \r\n                    \r\n                    \r\n                    ', 7),
(8, 'Honda', 'Civic', 2021, 'Gris', 'VWX234', 'manuelle', 5, 85000.00, 1, 'voitures/8.png', '                                                Voiture compacte et sportive, parfaite pour la ville et les longs trajets. La Honda Civic est fiable et économique.\r\n                    \r\n                    ', 2),
(9, 'Toyota', 'Corolla', 2022, 'Bleu', 'YZA567', 'automatique', 5, 95000.00, 1, 'voitures/9.jpg', '                        Voiture sûre et pratique pour tous les jours. La Toyota Corolla offre confort et fiabilité.\r\n                    ', 5),
(10, 'Ford', 'Mustang', 2023, 'Rouge', 'BCD890', 'automatique', 4, 110000.00, 1, 'voitures/10.jpg', '                                                Voiture sportive emblématique. La Ford Mustang offre puissance, style et sensations de conduite uniques.\r\n                    \r\n                    ', 2),
(11, 'Volkswagen', 'Passat', 2020, 'Bleu', 'MNO345', 'manuelle', 5, 80000.00, 1, 'voitures/5_Z6vs8qU.jpg', 'Voiture confortable et fiable pour tous les trajets. La Volkswagen Passat est idéale pour la famille et les déplacements quotidiens.', 2),
(12, 'Renault', 'Megane', 2021, 'Noir', 'PQR678', 'manuelle', 5, 65000.00, 0, 'voitures/6.jpg', 'ne offre confort et économie de carburant', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

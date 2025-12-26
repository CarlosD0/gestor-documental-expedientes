-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.4.3 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para db_biblioteca
CREATE DATABASE IF NOT EXISTS `db_biblioteca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_biblioteca`;

-- Volcando estructura para tabla db_biblioteca.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.auth_group: ~0 rows (aproximadamente)
DELETE FROM `auth_group`;

-- Volcando estructura para tabla db_biblioteca.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.auth_group_permissions: ~0 rows (aproximadamente)
DELETE FROM `auth_group_permissions`;

-- Volcando estructura para tabla db_biblioteca.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.auth_permission: ~40 rows (aproximadamente)
DELETE FROM `auth_permission`;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 3, 'add_permission'),
	(6, 'Can change permission', 3, 'change_permission'),
	(7, 'Can delete permission', 3, 'delete_permission'),
	(8, 'Can view permission', 3, 'view_permission'),
	(9, 'Can add group', 2, 'add_group'),
	(10, 'Can change group', 2, 'change_group'),
	(11, 'Can delete group', 2, 'delete_group'),
	(12, 'Can view group', 2, 'view_group'),
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
	(25, 'Can add autor', 7, 'add_autor'),
	(26, 'Can change autor', 7, 'change_autor'),
	(27, 'Can delete autor', 7, 'delete_autor'),
	(28, 'Can view autor', 7, 'view_autor'),
	(29, 'Can add libro', 8, 'add_libro'),
	(30, 'Can change libro', 8, 'change_libro'),
	(31, 'Can delete libro', 8, 'delete_libro'),
	(32, 'Can view libro', 8, 'view_libro'),
	(33, 'Can add categoria', 9, 'add_categoria'),
	(34, 'Can change categoria', 9, 'change_categoria'),
	(35, 'Can delete categoria', 9, 'delete_categoria'),
	(36, 'Can view categoria', 9, 'view_categoria'),
	(37, 'Can add prestamo', 10, 'add_prestamo'),
	(38, 'Can change prestamo', 10, 'change_prestamo'),
	(39, 'Can delete prestamo', 10, 'delete_prestamo'),
	(40, 'Can view prestamo', 10, 'view_prestamo'),
	(41, 'Can add reserva', 11, 'add_reserva'),
	(42, 'Can change reserva', 11, 'change_reserva'),
	(43, 'Can delete reserva', 11, 'delete_reserva'),
	(44, 'Can view reserva', 11, 'view_reserva'),
	(45, 'Can add configuracion', 12, 'add_configuracion'),
	(46, 'Can change configuracion', 12, 'change_configuracion'),
	(47, 'Can delete configuracion', 12, 'delete_configuracion'),
	(48, 'Can view configuracion', 12, 'view_configuracion');

-- Volcando estructura para tabla db_biblioteca.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.auth_user: ~1 rows (aproximadamente)
DELETE FROM `auth_user`;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$1200000$RWjCHke96LOcAIq9EjtZLn$lKUEntTGVA1OBnt/q7U4+QY4zJvLXkS+P73j3uEQsig=', '2025-12-26 02:22:54.662228', 1, 'admin', 'Administrador', '', 'admin@biblioteca.com', 1, 1, '2025-12-25 23:49:59.991036'),
	(2, 'pbkdf2_sha256$1200000$M5OjysuEoYUSl3xEzV4dZm$LLsslobp+P55kebxMv2jC7Ef5hiEFtkLHo9I8TlcDc0=', '2025-12-26 02:01:35.049008', 0, '12345678', 'Juan', '', '', 0, 1, '2025-12-26 01:06:10.749092'),
	(3, 'pbkdf2_sha256$1200000$hOXrrLfeIqlvhDBxwrb9yE$6T0KjOq8CXNcpUAM7LGhBhrAlwqufOpm7kgBFPplhHg=', NULL, 0, '10101010', 'Mario', 'Lopez', 'mario@biblioteca.com', 0, 1, '2025-12-26 05:42:41.510731');

-- Volcando estructura para tabla db_biblioteca.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.auth_user_groups: ~0 rows (aproximadamente)
DELETE FROM `auth_user_groups`;

-- Volcando estructura para tabla db_biblioteca.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.auth_user_user_permissions: ~0 rows (aproximadamente)
DELETE FROM `auth_user_user_permissions`;

-- Volcando estructura para tabla db_biblioteca.biblioteca_autor
CREATE TABLE IF NOT EXISTS `biblioteca_autor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nacionalidad` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.biblioteca_autor: ~1 rows (aproximadamente)
DELETE FROM `biblioteca_autor`;
INSERT INTO `biblioteca_autor` (`id`, `nombre`, `nacionalidad`) VALUES
	(1, 'Gabriel García Márquez', 'Española'),
	(2, 'Antoine de Saint', 'Desconocida'),
	(3, 'Cervantes', 'Desconocida');

-- Volcando estructura para tabla db_biblioteca.biblioteca_categoria
CREATE TABLE IF NOT EXISTS `biblioteca_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.biblioteca_categoria: ~1 rows (aproximadamente)
DELETE FROM `biblioteca_categoria`;
INSERT INTO `biblioteca_categoria` (`id`, `nombre`, `descripcion`) VALUES
	(1, 'Novela', ''),
	(2, 'Fábula', 'Importada');

-- Volcando estructura para tabla db_biblioteca.biblioteca_libro
CREATE TABLE IF NOT EXISTS `biblioteca_libro` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isbn` varchar(13) COLLATE utf8mb4_unicode_ci NOT NULL,
  `stock` int unsigned NOT NULL,
  `autor_id` bigint NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  `disponible` tinyint(1) NOT NULL,
  `categoria_id` bigint DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  `portada` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `biblioteca_libro_autor_id_c1df5079_fk_biblioteca_autor_id` (`autor_id`),
  KEY `biblioteca_libro_categoria_id_a729cd97_fk_bibliotec` (`categoria_id`),
  CONSTRAINT `biblioteca_libro_autor_id_c1df5079_fk_biblioteca_autor_id` FOREIGN KEY (`autor_id`) REFERENCES `biblioteca_autor` (`id`),
  CONSTRAINT `biblioteca_libro_categoria_id_a729cd97_fk_bibliotec` FOREIGN KEY (`categoria_id`) REFERENCES `biblioteca_categoria` (`id`),
  CONSTRAINT `biblioteca_libro_stock_818d6bc9_check` CHECK ((`stock` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.biblioteca_libro: ~0 rows (aproximadamente)
DELETE FROM `biblioteca_libro`;
INSERT INTO `biblioteca_libro` (`id`, `titulo`, `isbn`, `stock`, `autor_id`, `descripcion`, `disponible`, `categoria_id`, `activo`, `portada`) VALUES
	(1, 'LIBRO 1', '1212121211', 0, 1, '', 0, 1, 0, 'portadas/2025-12-25_20h22_02.png'),
	(2, 'LIBRO 2', '444444444', 1, 1, '', 1, 1, 1, 'portadas/2025-12-25_20h22_48.png'),
	(3, 'LIBRO 3', '555555555', 1, 1, '', 1, 1, 1, 'portadas/2025-12-25_20h23_46.png'),
	(4, 'LIBRO 4', '6666666', 0, 1, '', 0, 1, 1, 'portadas/2025-12-25_20h29_37.png'),
	(5, 'LIBRO 5', '77777777', 1, 1, '', 1, 1, 1, 'portadas/2025-12-25_20h34_33.png'),
	(6, 'LIBRO 6', '9999999', 1, 1, '', 1, 1, 1, 'portadas/2025-12-25_20h35_13.png'),
	(7, 'El Principito', '999888777', 9, 2, 'Un clásico.', 1, 2, 1, ''),
	(8, 'Don Quijote', '111222333', 5, 3, 'Obra maestra.', 1, 1, 1, ''),
	(9, 'Libro Coquito', '65656565', 4, 2, '', 1, 2, 1, 'portadas/2025-12-26_00h40_42.png');

-- Volcando estructura para tabla db_biblioteca.biblioteca_prestamo
CREATE TABLE IF NOT EXISTS `biblioteca_prestamo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_prestamo` date NOT NULL,
  `fecha_devolucion_estimada` date NOT NULL,
  `fecha_devolucion_real` date DEFAULT NULL,
  `estado` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `libro_id` bigint NOT NULL,
  `usuario_id` int NOT NULL,
  `renovaciones` int unsigned NOT NULL,
  `multa` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `biblioteca_prestamo_libro_id_c71c231b_fk_biblioteca_libro_id` (`libro_id`),
  KEY `biblioteca_prestamo_usuario_id_4b00abe5_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `biblioteca_prestamo_libro_id_c71c231b_fk_biblioteca_libro_id` FOREIGN KEY (`libro_id`) REFERENCES `biblioteca_libro` (`id`),
  CONSTRAINT `biblioteca_prestamo_usuario_id_4b00abe5_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `biblioteca_prestamo_chk_1` CHECK ((`renovaciones` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.biblioteca_prestamo: ~0 rows (aproximadamente)
DELETE FROM `biblioteca_prestamo`;
INSERT INTO `biblioteca_prestamo` (`id`, `fecha_prestamo`, `fecha_devolucion_estimada`, `fecha_devolucion_real`, `estado`, `libro_id`, `usuario_id`, `renovaciones`, `multa`) VALUES
	(1, '2025-12-25', '2025-12-25', '2025-12-26', 'D', 1, 1, 0, 0.00),
	(2, '2025-12-25', '2026-01-09', NULL, 'P', 1, 2, 2, 0.00),
	(3, '2025-12-25', '2025-12-31', NULL, 'P', 4, 1, 0, 0.00),
	(4, '2025-12-25', '2025-12-31', NULL, 'P', 7, 2, 0, 0.00),
	(5, '2025-12-26', '2025-12-27', NULL, 'P', 9, 3, 0, 0.00);

-- Volcando estructura para tabla db_biblioteca.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.django_admin_log: ~2 rows (aproximadamente)
DELETE FROM `django_admin_log`;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2025-12-26 00:27:57.119564', '1', 'Gabriel García Márquez', 1, '[{"added": {}}]', 7, 1),
	(2, '2025-12-26 00:28:07.954268', '1', 'Novela', 1, '[{"added": {}}]', 9, 1);

-- Volcando estructura para tabla db_biblioteca.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.django_content_type: ~10 rows (aproximadamente)
DELETE FROM `django_content_type`;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(2, 'auth', 'group'),
	(3, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(7, 'biblioteca', 'autor'),
	(9, 'biblioteca', 'categoria'),
	(12, 'biblioteca', 'configuracion'),
	(8, 'biblioteca', 'libro'),
	(10, 'biblioteca', 'prestamo'),
	(11, 'biblioteca', 'reserva'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session');

-- Volcando estructura para tabla db_biblioteca.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.django_migrations: ~20 rows (aproximadamente)
DELETE FROM `django_migrations`;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2025-12-25 23:42:44.574400'),
	(2, 'auth', '0001_initial', '2025-12-25 23:42:45.320235'),
	(3, 'admin', '0001_initial', '2025-12-25 23:42:45.511130'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2025-12-25 23:42:45.520489'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-12-25 23:42:45.531705'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2025-12-25 23:42:45.659896'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2025-12-25 23:42:45.735433'),
	(8, 'auth', '0003_alter_user_email_max_length', '2025-12-25 23:42:45.774233'),
	(9, 'auth', '0004_alter_user_username_opts', '2025-12-25 23:42:45.783193'),
	(10, 'auth', '0005_alter_user_last_login_null', '2025-12-25 23:42:45.890671'),
	(11, 'auth', '0006_require_contenttypes_0002', '2025-12-25 23:42:45.893624'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2025-12-25 23:42:45.901814'),
	(13, 'auth', '0008_alter_user_username_max_length', '2025-12-25 23:42:46.015017'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2025-12-25 23:42:46.120734'),
	(15, 'auth', '0010_alter_group_name_max_length', '2025-12-25 23:42:46.163976'),
	(16, 'auth', '0011_update_proxy_permissions', '2025-12-25 23:42:46.176537'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2025-12-25 23:42:46.268907'),
	(18, 'biblioteca', '0001_initial', '2025-12-25 23:42:46.431623'),
	(19, 'sessions', '0001_initial', '2025-12-25 23:42:46.492959'),
	(20, 'biblioteca', '0002_categoria_autor_nacionalidad_libro_descripcion_and_more', '2025-12-25 23:48:37.923658'),
	(21, 'biblioteca', '0003_libro_activo', '2025-12-26 00:39:28.555091'),
	(22, 'biblioteca', '0004_libro_portada', '2025-12-26 01:19:23.077474'),
	(23, 'biblioteca', '0005_prestamo_renovaciones', '2025-12-26 03:28:57.756790'),
	(24, 'biblioteca', '0006_prestamo_multa', '2025-12-26 03:48:07.170177'),
	(25, 'biblioteca', '0007_reserva', '2025-12-26 05:06:46.212062'),
	(26, 'biblioteca', '0008_configuracion_alter_reserva_estado', '2025-12-26 05:26:53.584108');

-- Volcando estructura para tabla db_biblioteca.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Volcando datos para la tabla db_biblioteca.django_session: ~1 rows (aproximadamente)
DELETE FROM `django_session`;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('15l3cweo8vbo3vakmk6i5zl5fi77i991', '.eJxVjDsOwjAQRO_iGln-Y1PScwZrvfbiALKlOKkQdyeRUkAzxbw382YR1qXGdZQ5TpldmGSn3y4BPkvbQX5Au3eOvS3zlPiu8IMOfuu5vK6H-3dQYdRtbUAWJCSjsxJeURFJkpf2rFxGdBi2AOvQkhM6gU1BEXrSxhsVyEj2-QIEDThi:1vYxTi:ChgUokuCCwXfXUoLvovj3hIfSWyjdNMpKdl_LT5EC-Y', '2026-01-09 02:22:54.668016');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

drop database if exists `amazonPriceTracker`;
create database amazonPriceTracker;
USE `amazonPriceTracker`;

SET NAMES utf8 ;
SET character_set_client = utf8 ;

create table userDetails(
`user_id` tinyint(4) NOT NULL AUTO_INCREMENT primary key,
`name` varchar(20) not null,
`eMail` varchar(50) not null);

create table products(
`product_id` tinyint(4) NOT NULL AUTO_INCREMENT primary key,
`productName` varchar(30) not null,
`price` int(5) not null);

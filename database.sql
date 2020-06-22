drop database if exists `amazonPriceTracker`;
create database amazonPriceTracker;
USE `amazonPriceTracker`;

SET NAMES utf8 ;
SET character_set_client = utf8 ;

create table userDetails(
`user_id` tinyint(4) NOT NULL  primary key,
`name` varchar(20) not null,
`eMail` varchar(50) not null
);


CREATE TABLE products (
	user_id tinyint(4) not null,
    product_id int NOT NULL,
    productName VARCHAR(50) not null,
    productLink VARCHAR(50) NOT NULL,
    price INT(5) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES userDetails(user_id)
);


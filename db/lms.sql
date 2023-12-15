create database if not exists lms;
use `lms`

create table `admim` (
    `admin_id` int(11) NOT NULL AUTO_INCREMENT primary key,
    `email` varchar(255) NOT NULL,
    `password` varchar(1000)
);

create table `books` (
    `book_id` int(11) NOT NULL AUTO_INCREMENT primary key,
    `name` varchar(255) NOT NULL,
    `description` longtext NOT NULL,
    `author` varchar(255),
    `availability` tinyint(1) NOT NULL DEFAULT '1',
    `edition` varchar(255) NOT NULL,
    `count` int(11) NOT NULL
);

create table `reserved` (
    `reserve_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` int(11) NOT NULL,
    `book_id` int(11) NOT NULL
);
use lms;
create table `users` (
    `user_id` int(11) NOT NULL AUTO_INCREMENT primary key,
    `name` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL,
    `password` varchar(1000) NOT NULL,
    `bio` longtext not null,
    `mob` varchar(255) NOT NULL,
    `lock` tinyint(1) not NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);
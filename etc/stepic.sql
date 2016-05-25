create database if not exists ask charset = 'utf-8';
create user if not exists 'stepic'@'localhost' identified by 'stepic';
grant all privileges on ask.* to 'stepic'@'localhost';
flush privileges;

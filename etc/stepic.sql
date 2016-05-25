create database if not exists ask;
create user 'stepic'@'localhost' identified by 'stepic';
grant all privileges on ask.* to 'stepic'@'localhost';
flush privileges;

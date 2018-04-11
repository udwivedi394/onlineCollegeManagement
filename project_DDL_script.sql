--Drop Table
DROP TABLE `user_validation`;


--Create Table
CREATE TABLE `user_validation` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `user_id` varchar(255) default NULL,
  `password` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

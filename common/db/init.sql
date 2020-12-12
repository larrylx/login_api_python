CREATE TABLE `user_basic` (
  `user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'User ID',
  `email` varchar(320) NOT NULL COMMENT 'User Email',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'User Status, 0-Disable，1-Normal',
  `password` BINARY(60) NOT NULL COMMENT 'Password',
  `user_name` varchar(32) NOT NULL COMMENT 'User Name',
  `profile_photo` varchar(128) NULL COMMENT 'Profile Picture',
  `last_login` datetime NULL COMMENT 'User Last Log in Time',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User Table';
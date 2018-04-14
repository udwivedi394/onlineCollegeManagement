/*Drop Table*/
DROP TABLE IF EXISTS user_details;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS `user_validation`;
DROP TABLE IF EXISTS branch_subjects;
DROP TABLE IF EXISTS branch;
DROP TABLE IF EXISTS subjects;


/*Create Table*/
CREATE TABLE `user_validation` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `user_id` varchar(255) default NULL,
  `password` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

create table user_details (
    id INT,
    parent_user_id mediumint(8) unsigned,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    gender VARCHAR(50),
    PRIMARY KEY (id),
    FOREIGN KEY (parent_user_id) REFERENCES user_validation(id)
);

CREATE TABLE branch(
   branch_code VARCHAR(3) NOT NULL,
   branch_name VARCHAR(45) NOT NULL,
   open_year INTEGER  NOT NULL,
   max_strength INTEGER NOT NULL,
   PRIMARY KEY (branch_code)
);

create table students(
    id INT,
    parent_user_id mediumint(8) unsigned,
    std_roll_no INT,
    std_admission_year INT,
    std_semester INT,
    std_branch VARCHAR(3),
    PRIMARY KEY (id),
    FOREIGN KEY (parent_user_id) REFERENCES user_validation(id),
    FOREIGN KEY (std_branch) REFERENCES branch(branch_code)
);

CREATE TABLE subjects(
   Subject_Code VARCHAR(6) NOT NULL PRIMARY KEY,
   Subject      VARCHAR(76),
   Credits      NUMERIC(5,2)
);

CREATE TABLE branch_subjects(
   id MEDIUMINT NOT NULL AUTO_INCREMENT,
   branch_code VARCHAR(3) NOT NULL,
   subject_code VARCHAR(6) NOT NULL,
   semester INTEGER  NOT NULL,
   PRIMARY KEY (id),
   FOREIGN KEY (branch_code) REFERENCES branch(branch_code),
   FOREIGN KEY (subject_code) REFERENCES subjects(subject_code)
);

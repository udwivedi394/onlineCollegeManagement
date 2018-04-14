/*Drop Table*/
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS user_details;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS `user_validation`;
DROP TABLE IF EXISTS branch_subjects;
DROP TABLE IF EXISTS branch;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS class_attendance_details;
DROP TABLE IF EXISTS class_attendance_header;
DROP TABLE IF EXISTS faculty_subjects;
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS employee;
SET FOREIGN_KEY_CHECKS = 1;


/*Create Table*/
CREATE TABLE `user_validation` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `user_id` varchar(255) default NULL,
  `password` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

create table user_details (
    id INT,
    parent_user_id mediumint(8) unsigned UNIQUE,
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
    parent_user_id mediumint(8) unsigned UNIQUE,
    std_roll_no INT UNIQUE,
    std_admission_year INT,
    std_semester INT,
    std_branch VARCHAR(3),
    PRIMARY KEY (id),
    INDEX(std_roll_no),
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
   UNIQUE(branch_code, subject_code),
   FOREIGN KEY (branch_code) REFERENCES branch(branch_code),
   FOREIGN KEY (subject_code) REFERENCES subjects(Subject_code)
);

CREATE TABLE employee(
    employee_id INTEGER NOT NULL AUTO_INCREMENT,
    parent_user_id mediumint(8) unsigned UNIQUE,
    emp_category VARCHAR(15) NOT NULL CHECK (emp_category IN ('Faculty', 'Security', 'Other Staff')),
    PRIMARY KEY(employee_id),
    FOREIGN KEY (parent_user_id) REFERENCES user_validation(id)
)AUTO_INCREMENT=74000;


CREATE TABLE faculty(
    faculty_id VARCHAR(6),
    employee_id INTEGER NOT NULL UNIQUE,
    designation VARCHAR(20) NOT NULL CHECK (designation IN ('Assistant Professor', 'Professor', 'Lab Assistant', 'HOD')),
    salary INTEGER NOT NULL,
    PRIMARY KEY(faculty_id),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

CREATE TABLE faculty_subjects(
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    taught_by_faculty_id VARCHAR(6),
    subject_code VARCHAR(6),
    branch_subject_id MEDIUMINT NOT NULL,
    total_classes INTEGER DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE(taught_by_faculty_id, branch_subject_id),
    FOREIGN KEY (taught_by_faculty_id) REFERENCES faculty(faculty_id),
    FOREIGN KEY (subject_code) REFERENCES subjects(Subject_code),
    FOREIGN KEY (branch_subject_id) REFERENCES branch_subjects(id)
);

CREATE TABLE class_attendance_header(
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    faculty_subject_id MEDIUMINT NOT NULL,
    class_id MEDIUMINT NOT NULL,
    class_startdatetime DATETIME NOT NULL,
    class_duration_minutes INTEGER DEFAULT 45,
    class_total_strength INTEGER NOT NULL,
    class_present INTEGER,
    PRIMARY KEY (id),
    UNIQUE(faculty_subject_id,class_id,class_startdatetime),
    FOREIGN KEY (faculty_subject_id) REFERENCES faculty_subjects(id),
    FOREIGN KEY (class_id) REFERENCES branch_subjects(id)
);

CREATE TABLE class_attendance_details(
    class_id MEDIUMINT NOT NULL,
    student_roll_no INT NOT NULL,
    PRIMARY KEY(class_id, student_roll_no),
    FOREIGN KEY (class_id) REFERENCES class_attendance_header(id),
    FOREIGN KEY (student_roll_no) REFERENCES students(std_roll_no) 
);

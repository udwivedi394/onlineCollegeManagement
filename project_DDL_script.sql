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
DROP TABLE IF EXISTS stu_semwise_status;
DROP TABLE IF EXISTS stu_subject_marks;
SET FOREIGN_KEY_CHECKS = 1;
DROP TRIGGER IF EXISTS student_enrollment;


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
    id INT auto_increment,
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
    internal_marks INT,
    external_marks INT,
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

CREATE TABLE stu_semwise_status(
    std_roll_no INT NOT NULL,
    sem_1_max_marks INT NOT NULL,
    sem_1_marks INT NULL,
    sem_1_status VARCHAR(8) NULL CHECK (sem_1_status IN ('PASS','FAIL')),
    sem_2_max_marks INT NOT NULL,
    sem_2_marks INT NULL,
    sem_2_status VARCHAR(8) NULL CHECK (sem_2_status IN ('PASS','FAIL')),
    sem_3_max_marks INT NOT NULL,
    sem_3_marks INT NULL,
    sem_3_status VARCHAR(8) NULL CHECK (sem_3_status IN ('PASS','FAIL')),
    sem_4_max_marks INT NOT NULL,
    sem_4_marks INT NULL,
    sem_4_status VARCHAR(8) NULL CHECK (sem_4_status IN ('PASS','FAIL')),
    sem_5_max_marks INT NOT NULL,
    sem_5_marks INT NULL,
    sem_5_status VARCHAR(8) NULL CHECK (sem_5_status IN ('PASS','FAIL')),
    sem_6_max_marks INT NOT NULL,
    sem_6_marks INT NULL,
    sem_6_status VARCHAR(8) NULL CHECK (sem_6_status IN ('PASS','FAIL')),
    sem_7_max_marks INT NOT NULL,
    sem_7_marks INT NULL,
    sem_7_status VARCHAR(8) NULL CHECK (sem_7_status IN ('PASS','FAIL')),
    sem_8_max_marks INT NOT NULL,
    sem_8_marks INT NULL,
    sem_8_status VARCHAR(11) NULL CHECK (sem_8_status IN ('PASS','FAIL','IN PROGRESS')),
    PRIMARY KEY(std_roll_no),
    FOREIGN KEY (std_roll_no) REFERENCES students(std_roll_no)
);

CREATE TABLE stu_subject_marks(
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    subject_code VARCHAR(6),
    semester INT NOT NULL,
    year INTEGER  NOT NULL,
    student_roll_no INT NOT NULL,
    max_internal_marks INT NOT NULL,
    internal_marks INT NOT NULL,
    max_external_marks INT NOT NULL,
    external_marks INT NOT NULL,
    max_credits NUMERIC(5,2) NOT NULL,
    credits NUMERIC(5,2) NOT NULL,
    UNIQUE(subject_code,semester,year,student_roll_no),
    PRIMARY KEY (id),
    FOREIGN KEY (subject_code) REFERENCES subjects(Subject_code),
    FOREIGN KEY (student_roll_no) REFERENCES students(std_roll_no)
);



/*Triggers*/
delimiter |
CREATE TRIGGER student_enrollment AFTER INSERT
ON students
FOR EACH ROW
BEGIN
    INSERT INTO stu_semwise_status SET std_roll_no = NEW.std_roll_no;
END;
|

delimiter ;

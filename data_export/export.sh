rm *.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
branch;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > branch.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
branch_subjects;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > branch_subjects.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
class_attendance_details;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > class_attendance_details.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
class_attendance_header;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > class_attendance_header.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
faculty;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > faculty.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
faculty_subjects;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > faculty_subjects.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select parent_user_id, std_roll_no, 
std_admission_year, std_semester, std_branch from
students;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > students.csv      

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
subjects;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > subjects.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
user_details;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > user_details.csv

mysql --defaults-extra-file=config.cfg collegeDB -B -e "select * from
user_validation;" | sed 's/\t/","/g;s/^/"/;s/$/"/;s/\n//g' > user_validation.csv

# to solve an error using data import wizard
select @@global.sql_mode;
set @@global.sql_mode = 'NO_ENGINE_SUBSTITUTION';

# use data import wizard and truncate data
use project;
truncate setting;
rename table setting to original_shop_seoul;

# import data from a file after cleaning sepearators (deleted unwanted commas)
LOAD DATA LOCAL INFILE "C:/Users/kb464/OneDrive - g.skku.edu/2022/2022-2_rdbms/original_shop_seoul.csv"
INTO TABLE original_shop_seoul
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 
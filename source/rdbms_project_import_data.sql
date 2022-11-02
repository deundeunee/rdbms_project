# to solve an error using data import wizard
select @@global.sql_mode;
set @@global.sql_mode = 'NO_ENGINE_SUBSTITUTION';

# create schema for a project
create schema project;
use project;
# Use 'table data import wizard' with setting.csv and truncate data
# Leaves an empty table with column names
truncate setting;
# Rename the table
rename table setting to original_shop_seoul;
# Import original data from a file, which is cleaned by deleting unwanted commas
LOAD DATA LOCAL INFILE "C:/Users/kb464/OneDrive - g.skku.edu/2022/2022-2_rdbms/original_shop_seoul.csv"
INTO TABLE original_shop_seoul
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 
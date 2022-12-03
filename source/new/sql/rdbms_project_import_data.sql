# To solve an error using data import wizard
select @@global.sql_mode;
set @@global.sql_mode = 'NO_ENGINE_SUBSTITUTION';
# Enable loading local data
SET GLOBAL local_infile=1;

# Create schema for a project
create schema project;
use project;
# Use 'table data import wizard' with setting.csv and truncate data
# Leaves an empty table with column names
truncate setting;
# Rename the table
rename table setting to original_shop_seoul;
# Import original data from a file, which is cleaned by deleting unwanted commas
LOAD DATA LOCAL INFILE "C:/Users/kb464/OneDrive - g.skku.edu/2022/2022-2_rdbms/rdbms_project/original_shop_seoul.csv"
INTO TABLE original_shop_seoul
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

set sql_safe_updates=0;
DELETE FROM project.original_shop_seoul where 상호명 like "%파리바%";
INSERT INTO original_shop_seoul (상호명, 시군구명, 법정동명, 도로명주소)
SELECT store_title, gu, dong, store_addr
FROM parisbaguette_gu_dong;
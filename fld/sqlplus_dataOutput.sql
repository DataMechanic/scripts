
--use sqlplus to write sql output to a file:
--cmd
--sqlplus <user_name>/<password>@<hostname>:<port>/<database>
set linesize 1000 --max line width
set pagesize 1000 --numbers of lines to output for each repetition of the header
spool d:\scripts\output_file.txt
--select statement
select * from hr.employees;
--or run script from file
@d:\scripts\orcl_table_select.sql
spool off
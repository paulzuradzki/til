# Problem

* I want to update a table using an inner join to another reference table so I can update to values from that reference table or limit the values to update based on the reference table.
* This also avoids the need from constructing separate UPDATE statements

# Solution
* Different SQL dialects seem to have varying support for update joins
* In PostgreSQL, you need to carefully restrict your data using WHERE criteria, the table specified in the UPDATE line, and the FROM table
  * additional tables can be joined in the FROM clause

```sql
/*

UPDATE JOIN - DEMO (for postgreSQL)


DO NOT DO THIS:
    * this will update all values in data_all to 'foo'
    * rather than filtering to only values that are in the 'id_filter' table

    update data_all
    set status = 'foo'
    from data_all t1, id_filter t2
    where t1.id = t2.id;

*/


/* setup */
-- table that we will update
drop table if exists data_all;
create table data_all (id int, status text);
insert into data_all values 
(1, ''), 
(2, ''),
(3, ''),
(4, ''),
(5, '')
;


-- inner join table on which keys will be used to filter 'data_all'
drop table if exists id_filter;
create temp table id_filter (id int);
insert into id_filter values 
(2),
(3)
;


/*
 select * from data_all; 
 
    |   id | status   |
    |-----:|:---------|
    |    1 |          |
    |    2 |          |
    |    3 |          |
    |    4 |          |
    |    5 |          |
    
select * from id_filter; 

    |   id |
    |-----:|
    |    2 |
    |    3 |
    
*/


/* OPTION A */
update data_all t1
set status = 'foo'
from id_filter t2
where t1.id = t2.id;

/* OPTION B 
 * define filter values in CTE
     * 'tmp_table' is the name of the table
     * 'id' is the name of the column
     * tmp_table is a 2 row x 1 column table (like id_filter above)
*/
with filter_ids as (
    select * 
    from (values (2), (3)) tmp_table(id)
)
update data_all t1
set status = 'foo'
from filter_ids t2
where t1.id = t2.id;


/*
RESULTS
* resulting table after update-join

  select * from data_all order by id; 
  
    |   id | status   |
    |-----:|:---------|
    |    1 |          |
    |    2 | foo      |
    |    3 | foo      |
    |    4 |          |
    |    5 |          |

*/
```

## SQL Database
>The content in this section is adapted from  
[Dr. Thyago Mota's](https://github.com/thyagomota) course  
**CS 3810: Principles of Database Systems**  
Spring 2021 - MSU Denver  
 
---

### Flowers Database
The goal of this project was to use SQL to create a small database with three tables, populate them with data, and query the database.


### Files
`create_tables.sql` creates and populates the tables.  
`queries.pdf` contains a list of queries and the expected output of each.  
`queries.sql` contains the statements to execute the queries listed in the pdf file.

### Queries

The queries require techniques which include:
- Aliases
- Conditional Filtering
- Grouping
- Joining multiple tables
- Ordering
- Text pattern matching
- Variables



<!-- <details><summary>Tables and Data</summary> -->

### Tables and Data


```
Zones
+----+-----------+------------+    +------------+------+------+-----+---------+-------+
| id | lowerTemp | higherTemp |    | Field      | Type | Null | Key | Default | Extra |
+----+-----------+------------+    +------------+------+------+-----+---------+-------+
|  2 |       -50 |        -40 |    | id         | int  | NO   | PRI | NULL    |       |
|  3 |       -40 |        -30 |    | lowerTemp  | int  | NO   |     | NULL    |       |
|  4 |       -30 |        -20 |    | higherTemp | int  | NO   |     | NULL    |       |
|  5 |       -20 |        -10 |    +------------+------+------+-----+---------+-------+
|  6 |       -10 |          0 |    
|  7 |         0 |         10 |    
|  8 |        10 |         20 |    
|  9 |        20 |         30 |    
| 10 |        30 |         40 |    
+----+-----------+------------+    
```
```
Deliveries
+----+-------+---------+    +---------+--------------+------+-----+---------+----------------+
| id | categ | delSize |    | Field   | Type         | Null | Key | Default | Extra          |
+----+-------+---------+    +---------+--------------+------+-----+---------+----------------+
|  1 | pot   |   1.500 |    | id      | int          | NO   | PRI | NULL    | auto_increment |
|  2 | pot   |   2.250 |    | categ   | varchar(5)   | NO   |     | NULL    |                |
|  3 | pot   |   2.625 |    | delSize | decimal(5,3) | YES  |     | NULL    |                |
|  4 | pot   |   4.250 |    +---------+--------------+------+-----+---------+----------------+
|  5 | plant |    NULL |    
|  6 | bulb  |    NULL |    
|  7 | hedge |  18.000 |    
|  8 | shrub |  24.000 |    
|  9 | tree  |  36.000 |    
+----+-------+---------+     
```

```
FlowersInfo
+-----+-------------------------+---------------------------------+-------+-------+---------+----------+    +----------+--------------+------+-----+---------+-------+
| id  | comName                 | latName                         | cZone | hZone | deliver | sunNeeds |    | Field    | Type         | Null | Key | Default | Extra |
+-----+-------------------------+---------------------------------+-------+-------+---------+----------+    +----------+--------------+------+-----+---------+-------+
| 101 |  Lady Fern              |  Atbyrium filix-femina          |     2 |     9 |       5 |  SH      |    | id       | int          | NO   | PRI | NULL    |       |
| 102 |  Pink Caladiums         |  C.x bortulanum                 |    10 |    10 |       6 |  PtoSH   |    | comName  | varchar(30)  | NO   |     | NULL    |       |
| 103 |  Lily-of-the-Valley     |  Convallaria majalis            |     2 |     8 |       5 |  PtoSH   |    | latName  | varchar(35)  | NO   |     | NULL    |       |
| 105 |  Purple Liatris         |  Liatris spicata                |     3 |     9 |       6 |  StoP    |    | cZone    | int          | NO   | MUL | NULL    |       |
| 106 |  Black Eyed Susan       |  Rudbeckia fulgida var. specios |     4 |    10 |       2 |  StoP    |    | hZone    | int          | NO   | MUL | NULL    |       |
| 107 |  Nikko Blue Hydrangea   |  Hydrangea macrophylla          |     5 |     9 |       4 |  StoSH   |    | deliver  | int          | YES  | MUL | NULL    |       |
| 108 |  Variegated Weigela     |  W. florida Variegata           |     4 |     9 |       8 |  StoP    |    | sunNeeds | varchar(255) | NO   |     | NULL    |       |
| 110 |  Lombardy Poplar        |  Populus nigra Italica          |     3 |     9 |       9 |  S       |    +----------+--------------+------+-----+---------+-------+
| 111 |  Purple Leaf Plum Hedge |  Prunus x cistena               |     2 |     8 |       7 |  S       |    
| 114 |  Thorndale Ivy          |  Hedera belix Thorndale         |     3 |     9 |       1 |  StoSH   |    
+-----+-------------------------+---------------------------------+-------+-------+---------+----------+       
```
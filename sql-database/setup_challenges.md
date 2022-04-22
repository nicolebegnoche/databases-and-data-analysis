Setup Challenges

I wrote this code using:
>Ubuntu 20.04.4 LTS (focal) through  
Windows Subsystem for Linux v2  
MySQL 8.0.28-0ubuntu0.20.04.3  

Install command: `$ sudo apt-get install mysql-server`

---

### Pain points during setup:

<details>
  <summary>Access denied for user 'root'@'localhost'</summary>
  
`Problem: No password is set for root.`

```
$ mysql -u root -p
Enter password: 
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
```
  <details>
    <summary>
    Solution 1:  Add your username with all privileges
    </summary>

    sudo mysql -u root
    mysql> USE mysql;
    mysql> CREATE USER 'USERNAME'@'localhost' IDENTIFIED BY 'YOUR_PASSWORD';
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'localhost';
    mysql> UPDATE user SET plugin='auth_socket' WHERE User='USERNAME';
    mysql> FLUSH PRIVILEGES;
    mysql> exit;
    sudo service mysql restart

  </details>

  <details>
    <summary>
    Solution 2:  Change the password for root
    </summary>

    $ sudo mysql -u root
    mysql> USE mysql;
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'NEW_PASSWORD';
    mysql> UPDATE user SET plugin='auth_socket' WHERE User='USERNAME';
    mysql> FLUSH PRIVILEGES;
    mysql> exit;
    $ sudo service mysql restart

  </details>

--- 

</details>


<details>
  <summary>
  The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
  </summary>
  
`Problem: Server won't access local files.`

  <details>
    <summary>
    Solution 1:  Restart server with local files allowed *and* use the LOCAL keyword in the sql statement.
    </summary>

    $ sudo service mysql restart
    $ mysql --local-infile=1 -u root -p
    mysql> set global local_infile=true;

in file:  LOAD DATA LOCAL INFILE 'flowers.csv'

  </details>

  <details>
    <summary>
    Solution 2:  Hypothetically, but good luck
    </summary>
  </details>

---

</details>


<details>
  <summary>ERROR 2 (HY000): File 'flowers.csv' not found (OS errno 2 - No such file or directory)</summary>

  <details>
    <summary>Possible Solution: Check the relative path</summary>
Be sure that the relative filepath is accurate - the origin is the folder which was **active in linux upon login**.  

In other words, `~/github/$ mysql` requires different relative paths than `~/github/databases-and-data-analysis/sql-database/`
  </details>

</details>

<!-- 
ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides

RESOLVED BY:
service mysql restart
mysql --local-infile=1 -u root -p
mysql> set global local_infile=true;


-->
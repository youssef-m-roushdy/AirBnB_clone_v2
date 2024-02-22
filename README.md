# Background Context
Environment variables will be your best friend for this project!

* HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
* `HBNB_MYSQL_USER`: the username of your MySQL
* `HBNB_MYSQL_PWD`: the password of your MySQL
* `HBNB_MYSQL_HOST`: the hostname of your MySQL
* `HBNB_MYSQL_DB`: the database name of your MySQL
* `HBNB_TYPE_STORAGE`: the type of storage used. It can be “file” (using `FileStorage`) or `db` (using `DBStorage`)

# Resources
<b>Read or watch:</b>

* [cmd module](https://docs.python.org/3/library/cmd.html)
* <b>packages</b> concept page
* [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [Python3 and environment variables](https://docs.python.org/3/library/os.html#os.getenv)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

<img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png" alt="hbnb_step2.png">

# 0. Fork me if you can!

For this project you will fork this [codebase](https://github.com/justinmajetich/AirBnB_clone)

# 2. Console improvements

Update the def `do_create(self, arg)`: function of your command interpreter (`console.py`) to allow for object creation with given parameters:

* Command syntax: create `<Class name> <param 1> <param 2> <param 3>...`
* Param syntax: `<key name>=<value>`
* Value syntax:
  * String: `"<value>"` => starts with a double quote
    * any double quote inside the value must be escaped with a backslash `\`
    * all underscores _ must be replace by spaces . Example: You want to set the string `My little house` to the attribute `name`, your command line must be `name="My_little_house"`
  * Float: `<unit>.<decimal>` => contains a dot .
  * Integer: `<number>` => default case
* If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped

<b>Don’t forget to add tests for this new feature!</b>

Also, this new feature will be tested here only with `FileStorage` engine.

```
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create | ./console.py 
(hbnb) d80e0344-63eb-434a-b1e0-07783522124e
(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7
(hbnb) [[State] (d80e0344-63eb-434a-b1e0-07783522124e) {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name': 'California'}, [State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) {'id': '092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), 'name': 'Arizona'}]
(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) [[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) {'number_bathrooms': 2, 'longitude': -122.431297, 'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 'My little house', 'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, 'number_rooms': 4, 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843747)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$
```

# 3. MySQL setup development

Write a script that prepares a MySQL server for the project:

* A database `hbnb_dev_db`
* A new user `hbnb_dev` (in `localhost`)
* The password of `hbnb_dev` should be set to hbnb_dev_pwd
* `hbnb_dev` should have all privileges on the database `hbnb_dev_db` (and only this database)
* `hbnb_dev` should have `SELECT` privilege on the database `performance_schema` (and only this database)
* If the database `hbnb_dev_db` or the user `hbnb_dev` already exists, your script should not fail

```
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
Enter password: 
hbnb_dev_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_dev@localhost
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 
```

# 4. MySQL setup test

Write a script that prepares a MySQL server for the project:

* A database `hbnb_test_db`
* A new user `hbnb_test` (in `localhost`)
* The password of `hbnb_test` should be set to `hbnb_test_pwd`
* `hbnb_test` should have all privileges on the database `hbnb_test_db` (and only this database)
* `hbnb_test` should have `SELECT` privilege on the database `performance_schema` (and only this database)
* If the database `hbnb_test_db` or the user `hbnb_test` already exists, your script should not fail

```
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
Enter password: 
hbnb_test_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_test@localhost
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 
```
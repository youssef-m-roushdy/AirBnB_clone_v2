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

# 5. Delete object

Update `FileStorage`: (`models/engine/file_storage.py`)

* Add a new public instance method: `def delete(self, obj=None):` to delete `obj` from `__objects` if it’s inside - if `obj` is equal to `None`, the method should not do anything
* Update the prototype of `def all(self)` to `def all(self, cls=None)` - that returns the list of objects of one type of class. Example below with `State` - it’s an optional filtering

```
guillaume@ubuntu:~/AirBnB_v2$ cat main_delete.py
#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

guillaume@ubuntu:~/AirBnB_v2$ ./main_delete.py
All States: 0
New State: [State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 1
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
Another State: [State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 2
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 1
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
guillaume@ubuntu:~/AirBnB_v2$ 
```

# 6. DBStorage - States and Cities

SQLAlchemy will be your best friend!

It’s time to change your storage engine and use `SQLAlchemy`

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/daaef631636b40e0a279a8f240703e065f9d3481.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240222T120225Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0133592fb1629b8f43fb9fb60d42e695068cfb881c99ab96beb32f1ecbc842ae" alt="">

In the following steps, you will make multiple changes:

* the biggest one is the transition between `FileStorage` and `DBStorage`: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the <b>abstraction</b>: Make your code running without knowing how it’s stored.
* add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)

Please follow all these steps:

* Update `BaseModel`: (`models/base_model.py`)

Create `Base = declarative_base()` before the class definition of `BaseModel`
* <b>Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, `created_at`, `updated_at`), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.</b>
* Add or replace in the class `BaseModel`:
  * class attribute `id`
    * represents a column containing a unique string (60 characters)
    * can’t be null
    * primary key
  * class attribute `created_at`
    * represents a column containing a datetime
    * can’t be null
    * default value is the current datetime (use `datetime.utcnow()`)
  * class attribute `updated_at`
    * represents a column containing a datetime
    * can’t be null
    * default value is the current datetime (use `datetime.utcnow()`)
* Move the `models.storage.new(self)` from `def __init__(self, *args, **kwargs):` to `def save(self):` and call it just before `models.storage.save()`
In `def __init__(self, *args, **kwargs):`, manage `kwargs` to create instance attribute from this dictionary. Ex: `kwargs={ 'name': "California" }` => `self.name = "California"` if it’s not already the case
* Update the `to_dict()` method of the class `BaseModel`:
remove the key `_sa_instance_state` from the dictionary returned by this method <b>only if this key exists</b>
* Add a new public instance method: `def delete(self):` to delete the current instance from the storage (`models.storage`) by calling the method `delete`

Update `City`: (`models/city.py`)

* `City` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `City`:
  * class attribute `__tablename__` -
    * represents the table name, `cities`
  * class attribute `name`
    * represents a column containing a string (128 characters)
    * can’t be null
  * class attribute `state_id`
    * represents a column containing a string (60 characters)
    * can’t be null
    * is a foreign key to `states.id`

Update `State`: (`models/state.py`)

* `State` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class State:
  * class attribute `__tablename__`
    * represents the table name, `states`
  * class attribute `name`
    * represents a column containing a string (128 characters)
    * can’t be null
  * for `DBStorage`: class attribute `cities` must represent a relationship with the class `City`. If the `State` object is deleted, all linked `City` objects must be automatically deleted. Also, the reference from a `City` object to his `State` should be named `state`
  * for `FileStorage`: getter attribute `cities` that returns the list of `City` instances with `state_id` equals to the current `State.id` => It will be the `FileStorage` relationship between `State` and `City`

New engine `DBStorage`: (`models/engine/db_storage.py`)

* Private class attributes:
  * `__engine`: set to `None`
  * `__session`: set to `None`
* Public instance methods:
  * `__init__(self):`
    * create the engine (`self.__engine`)
    * the engine must be linked to the MySQL database and user created before (`hbnb_dev` and `hbnb_dev_db`):
      * dialect: `mysql`
      * driver: `mysqldb`
    * all of the following values must be retrieved via environment variables:
      * MySQL user: `HBNB_MYSQL_USER`
      * MySQL password: `HBNB_MYSQL_PWD`
      * MySQL host: `HBNB_MYSQL_HOST` (here = `localhost`)
      * MySQL database: `HBNB_MYSQL_DB`
    * don’t forget the option `pool_pre_ping=True` when you call `create_engine`
    * drop all tables if the environment variable `HBNB_ENV` is equal to `test`
  * `all(self, cls=None):`
    * query on the current database session (`self.__session`) all objects depending of the class name (argument `cls`)
    * if `cls=None`, query all types of objects (`User`, `State`, `City`, `Amenity`, `Place` and `Review`)
    * this method must return a dictionary: (like `FileStorage`)
      * key = `<class-name>.<object-id>`
      * value = object
  * `new(self, obj):` add the object to the current database session (`self.__session`)
  * `save(self):` commit all changes of the current database session (`self.__session`)
  * `delete(self, obj=None):` delete from the current database session `obj` if not `None`
  * `reload(self):`
    * create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`)
    * create the current database session (`self.__session`) from the engine (`self.__engine`) by using a [sessionmaker](https://docs.sqlalchemy.org/en/13/orm/session_api.html) - the option `expire_on_commit` must be set to `False` ; and [scoped_session](https://docs.sqlalchemy.org/en/13/orm/contextual.html) - to make sure your Session is thread-safe

Update `__init__.py`: (`models/__init__.py`)

* Add a conditional depending of the value of the environment variable `HBNB_TYPE_STORAGE`:
  * If equal to `db`:
    * Import `DBStorage` class in this file
    * Create an instance of `DBStorage` and store it in the variable `storage` (the line `storage.reload()` should be executed after this instantiation)
  * Else:
    * Import `FileStorage` class in this file
    * Create an instance of `FileStorage` and store it in the variable `storage` (the line `storage.reload()` should be executed after this instantiation)
* This “switch” will allow you to change storage type directly by using an environment variable (example below)

State creation:
```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
guillaume@ubuntu:~/AirBnB_v2$ 
```

City creation:
```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$
```
```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
guillaume@ubuntu:~/AirBnB_v2$ 
```
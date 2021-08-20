# SQL-Insert-Generator
This is a simple Python script that I wrote for creating large SQL inserts of junk data for database testing. Just open the python file in your REPL, or import and run in your own application.

On calling `write_seed_file()`, a .SQL file will be written in the same directory as the script.

`write_seed_file()` has the following params:

- **b** = `string` the name of the database the SQL script should connect to
- **table** = `string` the name of the table the SQL script will INSERT INTO

- **columns** = `list` of tuples, each tuple should follow this format: (**col_name**, **col_type**, **max**)
  - Where **col_name** is the name of the column, as a string.
  - **col_type** is the data type of that column, as a Python type class (Supported: `str`, `int`, `bool`, `float`)
  - **max** is the maximum number of characters, or max value for a number. This should be an integer, but can be left blank (the Index Error will be catched)

- **file_name** = `string`, the name of the output SQL script file, note that the .sql extension is added automatically. (DEFAULT: gen_seed)

- **entries** = Int, the number of entries to insert into the table (DEFAULT: 100)

## Example:
``` Python
write_seed_file(db = "testing_db", table = "my_kittens", columns = [("name", str), ("age", int, 20), ("female", bool)], file_name = "seed_kittens", entries=20000)
```
The above function call will create `seed_kittens.sql`, which has the following contents:
``` SQL
\c testing_db;
INSERT INTO my_kittens (name, age, female) VALUES 
('ucxfpjvhmwmhcxialqjzzmmbbgjwzmejxhxkjlq', 9, false),
('lrpssjgwqmzwg', 14, true),
('baiiqmbmengng', 5, false),
('tdrsjtjbgjnevmpqhitkkgbbgckmilzoqawpqaocgbeh', 3, true),
('cqwlnbylpdjfbitrgumfahwfjhmtnav', 5, false),
-- 19,995 other entries...
```

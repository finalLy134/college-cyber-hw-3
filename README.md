# Cyber Security Homework No. 3
This is a repository for Cyber Security Course homework number 3.

## Explanation on the files
- `exercise.ipynb`: The main exercise code Jupyter Python Notebook, open it in your favorite code editor.
- `exercise.db`: A lightweight SQLite database for the exercise.
- `_wParent.py`: The "parent" worm script for question number 4 in the homework document.
- `docs/doc.pdf`: The homework document.

## How can you run the project?
1. Clone the repository or download the source code
2. Navigate to the project folder and open it in VSCode (Recommended)
3. If you want to run the code and see the Python Notebook open `exercise.ipynb`, choose a Python kernel and press **Run All**
4. If you want to run `_wParent.py` simply run `python _wParent.py` in the project folder


## The Python Notebook
Disclaimer: The code shown in this Python Notebook was fully written by me, Amitai Dvora. I used AI as a tool, not a crutch.


```batch
%pip install -r requirements.txt
```

#### 0. Initializing database
Here we create an example database to test our SQL injections.


```python
import sqlite3

# Creation of a lightweight local db using SQLite
with sqlite3.connect("exercise.db") as conn:
    cursor = conn.cursor()
    
    # Creation of tables and setting the name field as unique to prevent users duplicates later
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT UNIQUE, password TEXT)")
    
    # Inserting the users while preventing duplicates with INSERT OR IGNORE
    cursor.execute("INSERT OR IGNORE INTO users (name, password) VALUES (?, ?)", ("Bob", "Bb1234"))
    cursor.execute("INSERT OR IGNORE INTO users (name, password) VALUES (?, ?)", ("Alice", "Ac6543"))
    
    # Printing to see if everything worked
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
```

    (1, 'Bob', 'Bb1234')
    (2, 'Alice', 'Ac6543')
    

#### 1. SQL Injection-Vulnerable code


```python
def get_user(id: str):
    sql = f"SELECT * FROM users WHERE id={id}" # Using regular sql query
    cursor.execute(sql)
    return cursor.fetchall()

print(f"Valid Usage Output: {get_user('1')}")
print(f"SQL Injection Output: {get_user('0 OR 1=1;--')}")
```

    Valid Usage Output: [(1, 'Bob', 'Bb1234')]
    SQL Injection Output: [(1, 'Bob', 'Bb1234'), (2, 'Alice', 'Ac6543')]
    

#### 2. The above function but invulnerable to SQL Injection


```python
def get_user(id: str):
    sql = f"SELECT * FROM users WHERE id=?" # Using prepared statement
    cursor.execute(sql, (id,))
    return cursor.fetchall()

print(f"Valid Usage Output: {get_user('1')}")
print(f"SQL Injection Output: {get_user('0 OR 1=1;--')}")
```

    Valid Usage Output: [(1, 'Bob', 'Bb1234')]
    SQL Injection Output: []
    

#### 3. Trojan Horse function code


```python
# Intentionally overriding the regular Python's sum() to emphasize we're making a "Trojan Horse"
def sum(a, b):
    if a + b < 10:
        return a + b
    return 10

# Test runs
print(sum(1, 3))  # 4
print(sum(9, 3))  # 10
print(sum(10, 1)) # 10
```

    4
    10
    10
    

#### 4. Worm files
In order to run the worm script you need to run it specifically from the _wParent.py in the project folder.

#### 5. Hashing Algorithm


```python
def hash(string: str):
    return 'A' + string

str1 = "B"
str2 = "AB"

hash1 = hash(str1)
hash2 = hash(str2)

print(f"str1: {str1}, hash: {hash1}")
print(f"str2: {str2}, hash: {hash2}")

print(f"Is same hash?: {hash1 == hash2}")
```

    str1: B, hash: AB
    str2: AB, hash: AAB
    Is same hash?: False
    

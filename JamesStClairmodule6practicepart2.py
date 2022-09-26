sqlite work/practice

In [1]: import sqlite3

In [2]: connection = sqlite3.connect('books.db')

In [3]: JamesStClair = 'Working on module 6'

In [4]: import pandas as pd

In [5]: pd.options.display.max_columns = 10

In [6]: pd.read_sql('SELECT * FROM authors', connection, index_col=['id']) (accidentally did indec_col)

pd.read_sql('SELECT * FROM titles', connection) (ran it with index_col=['id'] the first time)

pd.read_sql('SELECT * FROM author_ISBN', connection)

using the where clause: 

pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)

pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])

using the ORDER BY clause

pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection) (accidentally did 'ORDER BY titles' the first time)

pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""", connection, index_col=['id'])

pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id'])

pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection)



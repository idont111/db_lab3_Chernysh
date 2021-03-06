import csv
import psycopg2

username = 'Chernysh_Alina'
password = '111'
database = 'Chernysh_Alina_DB'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'kaggle_import_book.csv'

query_0 = '''

CREATE TABLE book_new(
    book_id char(10) NOT NULL,
    book_Name VARCHAR(255) NOT NULL,
    Author_name VARCHAR(255) NOT NULL,
    CONSTRAINT pk_products_new PRIMARY KEY (book_id)
    );
'''

query_1 = '''
DELETE FROM book_new
'''

query_2 = '''
INSERT INTO book_new (book_id, book_Name, Author_name) VALUES (%s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS book_new')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            values = (idx, row['book_Name'], row['Author_name'])
            cur.execute(query_2, values)

    conn.commit()

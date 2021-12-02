import psycopg2
import matplotlib.pyplot as plt

username = 'Chernysh_Alina'
password = '111'
database = 'Chernysh_Alina_DB'
host = 'localhost'
port = '5432'


query_1 = '''
CREATE VIEW AuthorCountBooks AS
SELECT TRIM(CONCAT(first_name, ' ', last_name)) as "author_name", COUNT(title) as "count books"
FROM book
INNER JOIN author ON book.author_id = author.author_id
GROUP BY author_name;
'''

query_2 = '''
CREATE VIEW QuantityGenreBook AS
SELECT TRIM(genre_name), COUNT(title)
FROM book
JOIN genre ON book.genre_id = genre.genre_id
GROUP BY genre_name
ORDER BY genre_name
'''

query_3 = '''
CREATE VIEW BookPeriod AS
SELECT rank_period_name, COUNT(title)
FROM book
INNER JOIN rank_period ON book.period_id = rank_period.period_id
JOIN genre ON book.genre_id = genre.genre_id
where genre_name in ('Diary fiction', 'Science fiction')
GROUP BY rank_period_name
ORDER BY COUNT(title) desc
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:
    cur = conn.cursor()

    cur.execute('drop view if exists AuthorCountBooks')

    cur.execute(query_1)
    cur.execute('select * from AuthorCountBooks')
    book = []
    quantity = []

    print("Query 1")
    for row in cur:
        print(row)
        book.append(row[0])
        quantity.append(row[1])

    x_range = range(len(book))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    plt.subplots_adjust(wspace=0.5)
    bar = bar_ax.bar(x_range, quantity)
    bar_ax.set_title('Кількість книжок написаних кожним автором')
    bar_ax.set_xlabel('Автори')
    bar_ax.set_ylabel('Кількість книжок')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(book, fontsize=7)
    for label in bar_ax.get_xticklabels():
        label.set_rotation(30)
        label.set_ha('right')

    cur.execute('drop view if exists QuantityGenreBook')

    cur.execute(query_2)
    cur.execute('select * from QuantityGenreBook')
    author = []
    songs = []

    print("Query 2")
    for row in cur:
        print(row)
        author.append(row[0])
        songs.append(row[1])

    pie_ax.pie(songs, labels = author, autopct='%1.1f%%')
    pie_ax.set_title('Частка жанрів написаних кожним автором')

    cur.execute('drop view if exists BookPeriod')

    cur.execute(query_3)
    cur.execute('select * from BookPeriod')
    rank_period = []
    quantity_book = []

    print("Query 3")
    for row in cur:
        print(row)
        rank_period.append(row[0])
        quantity_book.append(row[1])

    graph_ax.plot(rank_period, quantity_book, marker='o')

    graph_ax.set_xlabel('Жанри')
    graph_ax.set_ylabel('Кількість книжок')
    graph_ax.set_title('Графік залежності кількості книжок у віповідних період, \n причому жанром є фантастика')
    for label in graph_ax.get_xticklabels():
        label.set_rotation(30)
        label.set_ha('right')

    for pl, sng in zip(rank_period, quantity_book):
        graph_ax.annotate(sng, xy=(pl, sng), xytext=(7, 2), textcoords='offset points')

mng = plt.get_current_fig_manager()
mng.resize(1450, 700)

plt.show()

import sqlite3

# Connects to the database, executes the SQL query to fetch 'Dexter' genres, and prints the results.
connection = sqlite3.connect('tv_shows.db')
cursor = connection.cursor()

query = """
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
"""

cursor.execute(query)
genres = cursor.fetchall()

for row in genres:
    print(row[0])

connection.close()
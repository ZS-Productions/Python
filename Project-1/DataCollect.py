import sqlite3

con = sqlite3.connect("data.db")

cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")
#cur.execute("""
#    INSERT INTO movie VALUES
#        ('Monty Python and the Holy Grail', 1975, 8.2),
#        ('And Now for Something Completely Different', 1971, 7.5)
#""")
#cur.execute("""DELETE FROM movie WHERE (year=1982 OR year=1983 OR year=1979)""")

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0)
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()
print("Hello World")

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())
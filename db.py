import sqlite3

con = sqlite3.connect("todolist.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS task(description)")
# cur.execute("""
#     INSERT INTO task('description') VALUES
#         ('Devoir de francais'),
#         ('Rapport de math'),
#         ('TOEIC a 15h')
# """)
# con.commit()
res = cur.execute("SELECT description FROM task")
print(res.fetchall())
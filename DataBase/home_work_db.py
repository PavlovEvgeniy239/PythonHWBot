import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('home_work.db')
    cur = base.cursor()
    if base:
        print('Data Base connected')
    base.execute("""CREATE TABLE IF NOT EXISTS Home_work(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sub TEXT, 
    day TEXT, 
    HW TEXT
    )""")
    base.commit()


async def sql_add_row(data):
    cur.execute('INSERT INTO Home_work(sub, day, HW) VALUES(?, ?, ?)', tuple(data.values()))
    base.commit()


async def sql_show_all_table():
    r = cur.execute('SELECT * FROM Home_work').fetchall()
    return r


async def delete_from_table(id):
    cur.execute('DELETE FROM Home_work WHERE id = ?', tuple(id))
    base.commit()
    r = cur.execute('SELECT sub, day, HW FROM Home_work').fetchall()
    cur.execute('DROP TABLE IF EXISTS Home_work')
    base.commit()
    base.execute("""CREATE TABLE IF NOT EXISTS Home_work(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sub TEXT, 
        day TEXT, 
        HW TEXT
        )""")
    base.commit()
    for hv in r:
        cur.execute('INSERT INTO Home_work(sub, day, HW) VALUES(?, ?, ?)', hv)
        base.commit()


async def take_id_from_table():
    r = cur.execute('SELECT id FROM Home_work').fetchall()
    return r
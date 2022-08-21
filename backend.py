import sqlite3


def connect():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS InStock(id INTEGER PRIMARY KEY, item TEXT, price FLOAT, quantity INTEGER)")
    conn.commit()
    conn.close()

def insert(item, price, quantity):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO InStock VALUES(NULL, ?, ?,?)", (item, price, quantity))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM InStock")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(item):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM InStock WHERE item=?", (item,))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM InStock WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, item, price, quantity):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("UPDATE InStock SET item=?, price=?, quantity=? WHERE id=?", (item, price, quantity,id,))
    conn.commit()
    conn.close()
    

connect()
#insert("Polish", 5.00, 50)
#print(view())
#update(3,"Tilapia", 20.00, 5)
#delete(2)
#print(search(item="Polish"))
#print(view())

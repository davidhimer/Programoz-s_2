import sqlite3

"""
Ebben a functionban hozódik létre az adatbázis amiben a bolt termékai vannak
"""

def connect():
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, nev text, ar real) ")
    conn.commit()
    conn.close()

def insert(nev, ar):
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO products VALUES(NULL,?,?)",(nev, ar))
    conn.commit()
    conn.close()

def torles(id):
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()

def all_products():
    conn = sqlite3.connect("products.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products ORDER BY nev")
    rows=cur.fetchall()
    conn.close()
    return rows

"""
Ebben a functionban hozódik létre az adatbázis a bevásárlókosárról
"""

def connect_sl():
    conn = sqlite3.connect("shoppinglist.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS shoppinglist (id INTEGER PRIMARY KEY, nev text, ar real, darad integer, ar_netto real, ar_brutto real) ")
    conn.commit()
    conn.execute("DELETE FROM shoppinglist")
    conn.close()

def insert_sl(nev, ar, darab,):
    ar_netto = float(ar) * int(darab)
    ar_brutto = ar_netto * 1.27
    conn = sqlite3.connect("shoppinglist.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO shoppinglist VALUES(NULL,?,?,?,?,?)",(nev, ar, darab, ar_netto, ar_brutto))
    conn.commit()
    conn.close()

def torles_sl(id):
    conn = sqlite3.connect("shoppinglist.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM shoppinglist WHERE id=?", (id,))
    conn.commit()
    conn.close()

def all_shoppinglist():
    conn = sqlite3.connect("shoppinglist.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM shoppinglist")
    rows=cur.fetchall()
    conn.close()
    return rows

"""
Ebben a functionban készül el a számla
"""

def bill():
    conn = sqlite3.connect("shoppinglist.db")
    cur = conn.cursor()
    cur.execute("SELECT ROUND(SUM(ar_brutto)) From shoppinglist")
    rows=cur.fetchall()
    conn.close()
    return rows

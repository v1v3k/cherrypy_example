__author__ = 'george'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

uId = 1
uPrice = 62300

con = lite.connect('test.db')

with con:

    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
    con.commit()

    print "Number of rows updated: %d" % cur.rowcount




uId = 4

con = lite.connect('test.db')

with con:

    cur = con.cursor()

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id",
        {"Id": uId})
    con.commit()

    row = cur.fetchone()
    print row[0], row[1]
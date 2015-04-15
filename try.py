#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('proteindata.sqlite')
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars WHERE Id=3")

    rows = cur.fetchall()
    
    for row in rows:
        print row

# Real stuff
con = lite.connect('proteindata.sqlite')
with con:
    
    cur = con.cursor()    
    
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("SELECT * FROM protein")
    
    rows = cur.fetchall()

    
    print "Database has " + str(len(rows)) + " rows"
    
    cur.execute("SELECT * FROM protein WHERE ID=4")
    names = cur.fetchone()

    
    for x in names:
        print x
        print
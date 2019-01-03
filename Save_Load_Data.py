import pygame
import sqlite3

class Save():
    def __init__(self):
        try:
            self.conn = sqlite3.connect("Data/saved.db")
            print("SQLite3 version: " + sqlite3.version + ", minimum required is 2.3.0")
            self.c = self.conn.cursor()
        except:
            print("Database connection failed.")


    def createDataTable(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft})'.format(tn="t1", nf="col1", ft='INTEGER'))
            
        self.conn.commit()
        self.conn.close()

class Load():
    def __init__(self):
        pass
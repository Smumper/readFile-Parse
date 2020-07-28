import sqlite3
import os


class Database:
    def __init__(self, name):
        # Datenbank initialisieren
        try:
            os.makedirs("Projekte/")
            # Ordner muss immer Erstellt sein Ansonsten kommt eine fehler meldung
            self.connection = sqlite3.connect("Projekte/" + name + ".db")
            self.cur = self.connection.cursor()
        except FileExistsError:
            # Wenn Ordner bereits existiert wird diese nicht nochmals erstellt
            self.connection = sqlite3.connect("Projekte/" + name + ".db")
            self.cur = self.connection.cursor()

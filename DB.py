import mysql.connector

class Connessione:

    def conn(): 
        
        connessione = mysql.connector.connect(host = "localhost", user = "root", password = "DJm4tt0&", port = "3306", database = "sakila")

        return connessione
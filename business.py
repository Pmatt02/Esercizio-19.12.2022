import mysql.connector
import time

from DB import Connessione

connessione = None
connessione = Connessione.conn()

#Funzione Film

class Azioni:

    def Film():

        try:
            
            mycursor = connessione.cursor()
            mycursor.execute("SELECT title FROM film")
            result = mycursor.fetchall()

            for x in result:
                
                print(x)

        except mysql.connector.Error as errore:

            print("Errore:", errore)

        finally:

            if connessione is not None:

                connessione.close()
                print("Chiusura file in corso...")
                time.sleep(3)

    #Funzione attori

    def Attori():

        try:

            mycursor = connessione.cursor()
            mycursor.execute("SELECT first_name, last_name FROM actor")
            result2 = mycursor.fetchall()

            for x in result2:

                print(x)

        except mysql.connector.Error as errore:

            print("Errore:", errore)

        finally:

            if connessione is not None:

                print("Chiusura file in corso...")
                connessione.close()
                time.sleep(3)






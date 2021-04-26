###############   modulo de conexion a la base de datos   ###############
import mysql.connector

###############   conexin database   ###############
def conextar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python",
        port=3306
    )

    cursor = database.cursor(buffered=True)
    
    return [database, cursor]
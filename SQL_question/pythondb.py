import sqlite3
from sqlite3 import Error
import os

def sql_exercise(db_file):
    conn = None

    # You have been given the JSON output for time purposes
    mock_json  = {"Acme Corp.":2070,"Quik Mart":1620,"Luffy & Co.":1880,
                "Evermart":1510,"MgRonalds":1800,"Farmacy":820,"Baratier":920,
                "Eden Hall":2240,"Anteiku":1780}
    
    try:
        conn = sqlite3.connect(db_file)

        # Create the table by storing your SQL command within this variable
        # NAME IT total_inventories
        sql_create_table = """ """
        
        # Insert an entry into the databse by modifying this variable
        sql_insert = """ """

        # Get the row with the maximum total
        sql_max = """ """

        # Get the rows with the top 3 totals
        sql_top = """ """

        # Get the rows with totals between 1000 and 2000
        sql_range = """ """

        if conn is not None:
            cursor = conn.cursor()
            
            # cursor.execute(query) executes the query
            # print(cursor.fetchall()) prints out the result of your 
            # most recent query and can be used as you please.

            # Create the table
            cursor.execute(sql_create_table)

            # Insert an entry(s) into the database
            cursor.execute(sql_insert)

            # Save the insertion
            conn.commit()

            # Get the row with the maximum total
            cursor.execute(sql_max)

            # Get the rows with the top 3 totals
            cursor.execute(sql_top)

            # Get the rows with totals between 1000 and 2000
            cursor.execute(sql_range)

            # Feel free to print out the contents of your table by uncommenting this line
            # cursor.execute("SELECT * FROM total_inventories;")

        print(cursor.fetchall())
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    sql_exercise(r"total_inventories.db")
'''
This one is the main file of this utility and the code base starts from here.
'''

import sqlite3
import time
import os

def start_work():
    pass

if __name__ == "__main__":
    print("Starting the Monitoring Loading Prerequisite...")
    
    print("Creating the app_status.db...")
    try:
        app_status_file = "app_status.db"
        if os.path.isfile(app_status_file):
            os.remove(app_status_file)

        main_connection = sqlite3.connect("app_status.db")
        
        print("Creating the main_cursor...")
        main_cursor = main_connection.cursor()

        
        main_connection.execute(''' 
            CREATE TABLE app_status
            (APPSTATUS INT NOT NULL);
         ''')
    
        print("app_status.db created successfully...")
 
        print("Generating app status as 1[true]...")
        main_connection.execute(''' 
           INSERT INTO app_status VALUES(1);
         ''')
        
        print("Entering into the monitoring daemon...")
        inside_daemon = 0
        while 1:
            if not inside_daemon:
                print("Inside the monitoring daemon...")
                inside_daemon = 1
                
            start_work()
            
            # Check app status
            query = "SELECT * FROM app_status;"
            main_cursor.execute(query)
            output = main_cursor.fetchall()
                        
            for row in output:
                if row[0] == 0:
                    print("Stopping procedure initiated...")
                    
            # daemon monitoring timer
            time.sleep(1)
    
    finally:
        if main_connection:
            main_connection.close()
            print('Closing connection...')

            app_status_file = "app_status.db"
            if os.path.isfile(app_status_file):
                os.remove(app_status_file)
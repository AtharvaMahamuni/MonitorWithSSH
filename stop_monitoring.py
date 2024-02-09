import sqlite3


# dropping the idea as sqlite don't support the concurrent access to the user.
# for now assuming only one user will use it, and it is good idea to keep connection open all the time.
# In start_monitoring.py, instead of opening and closing it in each iteration.
if __name__ == "__main__":
    print("Stopping initiated for monitoring application...")
    
    try:
        # Establishing the connection
        main_connection = sqlite3.connect("app_status.db")
        
        print("Creating the main_cursor...")
        main_cursor = main_connection.cursor()
        
        print("Making app status 0[false]...")
        main_connection.execute(''' 
           UPDATE app_status SET appstatus=0;
        ''')
        print("Application status changed to 0[false]...")
        
    finally:
        if main_connection:
            main_connection.close()
            print('Closing main_connection...')
        

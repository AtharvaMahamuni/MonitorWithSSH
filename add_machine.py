#!/bin/python3

import sqlite3
import getpass

if __name__ == "__main__":
    print("*********************************************")
    print("Give the following details to add your machine:")
    ip_hostname = str(input("Machine IP/Host Name: "))
    ssh_port = int(input("Port to SSH: "))
    user_name = str(input("User name: "))
    user_pass = str(input("User Password: "))
    
    try:
        print("Making connection with the machine list...")
        machine_list_file_connection = sqlite3.connect("machine_list.db")
        
        print("Creating cursor to add the machine...")
        machine_list_cursor = machine_list_file_connection.cursor()
        
        print("Making machines table if not exists...")
        machine_list_file_connection.execute(''' 
            CREATE TABLE IF NOT EXISTS machine_list
            (machine_id INTEGER PRIMARY KEY,
            ip_hostname TEXT NOT NULL,
            ssh_port INT NOT NULL,
            user_name TEXT NOT NULL,
            user_pass TEXT NOT NULL);
         ''')

        query = '''INSERT INTO machine_list (ip_hostname, ssh_port, user_name, user_pass)
            VALUES ('{}', {}, '{}', '{}');'''.format(ip_hostname, ssh_port, user_name, user_pass)
        machine_list_cursor.execute(query)
    
    finally:
        if machine_list_file_connection:
            print("Committing changes to machine list...")
            machine_list_file_connection.commit()
            print('Closing connection with machine list...')
            machine_list_file_connection.close()
            print("Machine registered sucsessfully...")


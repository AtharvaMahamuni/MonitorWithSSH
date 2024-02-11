import os
import sqlite3

if __name__ == "__main__":
    print("*********************************************")
    
    machine_list_file = "machine_list.db"
    if os.path.isfile(machine_list_file):
        try:
            print("Making connection with the machine list...")
            machine_list_file_connection = sqlite3.connect("machine_list.db")
            
            print("Creating cursor to add the machine...")
            machine_list_cursor = machine_list_file_connection.cursor()
            
            # Check app status
            query = "SELECT * FROM machine_list;"
            machine_list_cursor.execute(query)
            print("Fetching the machine list...")
            machine_list = machine_list_cursor.fetchall()
            
            print("Machine list is as follows...")
            row = "|{name1:^20}|{name2:^20}|{name3:^20}|{name4:^20}|{name5:^20}|".format
            print(row(name1="machine_id", name2="host_name/ip", name3="ssh_port", name4="user_name", name5="user_pass"))
            for value in machine_list:
                print(row(name1=value[0], name2=value[1], name3=value[2], name4=value[3], name5=value[4]))
                        
        finally:
            if machine_list_file_connection:
                machine_list_file_connection.close()
                print('Closing connection with machine list...')
                
    else:
        print("You do not have any machine, or not maintaining any machine...")

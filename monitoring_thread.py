import paramiko
import sqlite3
import os
import time


def main(path):
    print("Hello, World!")
    print(path)
    
    try:
        os.makedirs(os.path.join(path, "results", "one_more", "another_one"))
    except FileExistsError:
        pass
        

if __name__ == "__main__": main()
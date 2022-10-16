from mysql.connector import connect, Error

class DatabaseM: 
    def __init__(self): 
        host='localhost'
        user='root'
        password='root'
        self.connection_general = connect(host=host, user=user, password=password)
        try: self.create_database() 
        except Exception as e: print(e) 
        self.connection = connect(host=host, user=user, password=password, database='datab1')
        try: self.create_table_1() 
        except Exception as e: print(e) 

    def show_all_db(self): 
        query = 'SHOW DATABASES' 
        dbs = self.execute_cursor(query)
        for db in dbs: print(db) 
        return dbs

    def execute_cursor(self, query, execm=None): 
        with self.connection.cursor(buffered=True) as cursor:
            cursor.executemany(query, execm) if execm != None else cursor.execute(query) 
            return cursor

    def create_database(self): 
        query = "CREATE DATABASE datab1"
        with self.connection_general.cursor(buffered=True) as cursor:
            cursor.execute(query)
            self.connection.commit()
    
    def create_table_1(self): 
        query = "CREATE TABLE table1 ( er_no TEXT, ntn TEXT, name TEXT, business_name TEXT)"
        self.execute_cursor(query) 

    def insert_data_into_table1(self, data): 
        query = f"INSERT INTO table1 (er_no, ntn, name, business_name) VALUES (%s, %s, %s, %s)"
        self.execute_cursor(query, execm=data) 
        self.connection.commit()

    def show_all_data(self): 
        query = "SELECT * FROM table1 LIMIT 200"
        crsr = self.execute_cursor(query)
        for row in crsr.fetchall(): print(row)
        
    def close_connection(self): 
        self.connection.close() 


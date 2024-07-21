import sqlite3
from pathlib import Path

class SqlManagement:

    def open_db(self):
        self.db_path = Path(__file__).parent / 'smart_family.db'
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def close_db(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, query, args=()):
        self.cursor.execute(query, args)
        self.commit()


    def is_table_exists(self, table_name: str) -> bool:
        sql.open_db()
        self.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name.lower(),))
        exists = self.cursor.fetchone() is not None
        self.close_db()
        return exists

    def add_table(self, table_name: str, *args: any) -> None:
        if self.is_table_exists(table_name):
            print(f'\n >> Table {table_name.upper()} already exists in the database')
        else:
            sql.open_db()
            Query = f'CREATE TABLE {table_name.lower()} (id INTEGER PRIMARY KEY AUTOINCREMENT,{",".join([str(arg) for arg in args])})'
            self.execute(Query)
            print(f'\n >> Table {table_name.upper()} added successfully to the database')
        self.close_db()
     

    def add_field(self, table_name: str, *args: any) -> None:
        self.open_db()
        cursor = self.connection.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall() if col[1].lower() != 'id']

        Query = f"INSERT INTO {table_name.lower()} ({','.join(columns)}) VALUES ({','.join(['?' for _ in args])})"
        self.execute(Query, args)
        print(f'\n >> Field added successfully to the table {table_name}')
        self.close_db()


    def delete_field(self, table_name: str, id_value: int) -> None:
        if self.fetch_by_id(table_name,id_value) is None:
            print(f'\n >> Field with id {id_value} don\'t exists in table {table_name}')
        else:
            self.open_db()
            self.execute(f"DELETE FROM {table_name} WHERE id = {id_value}")
            print(f'\n >> Field with id {id_value} deleted successfully from table {table_name}')
            self.close_db()

    def update_field(self, table_name: str, id_value: int, column_name: str, new_value: any) -> None:
        self.open_db()
        Query = f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?"
        self.execute(Query, (new_value, id_value))
        print(f'\n >> Field {column_name} of id {id_value} updated successfully in table {table_name}')
        self.close_db()


    def fetch_by_id(self, table_name: str, id: int) -> tuple:
        """be aware: >>> \if id don't exist the function return -> None type !"""
        self.open_db()
        try:
            self.execute(f'SELECT * FROM {table_name} WHERE id = {id}')
            last_one = self.cursor.fetchone()
            self.close_db()
            return last_one
        except sqlite3.Error:
            self.close_db()
            return None


    def fetch_last_one(self, table_name: str) -> tuple:
        self.open_db()
        self.execute(f'SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1')
        one_list = self.cursor.fetchone()
        self.close_db()
        return one_list
        

    def fetch_all_by_foreign_key(self, table_name: str, column_name: str, foreign_key: int) -> list[tuple]:
        self.open_db()
        self.execute(f'SELECT * FROM {table_name} WHERE {column_name} = {foreign_key}')
        list = self.cursor.fetchall()
        self.close_db()
        return list

    def fetch_all(self, table_name: str) -> list[tuple]:
        self.open_db()
        self.execute(f'SELECT * FROM {table_name}')
        list = self.cursor.fetchall()
        self.close_db()
        return list
    
sql = SqlManagement()
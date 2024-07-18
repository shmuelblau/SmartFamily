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
        self.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name={table_name.lower()}")
        exists = self.cursor.fetchone() is not None
        return exists


    def add_table(self, table_name: str, *args: any) -> None:
        if self.is_table_exists(table_name):
            print(f' >> Table {table_name.upper()} already exists in the database\n')
        else:
            Query = f'CREATE TABLE {table_name.lower()} (id INTEGER PRIMARY KEY AUTOINCREMENT,{",".join([str(arg) for arg in args])})'
            self.execute(Query)
            print(f' >> Table {table_name.upper()} added successfully to the database\n')
     

    def add_field(self, table_name: str, *args: any) -> None:
        cursor = self.connection.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall() if col[1].lower() != 'id']

        Query = f"INSERT INTO {table_name.lower()} ({','.join(columns)}) VALUES ({','.join(['?' for _ in args])})"
        self.execute(Query, args)
        print(f' >> Field added successfully to the table {table_name}')


    def delete_field(self, table_name: str, id_value: int) -> None:
        self.execute(f"DELETE FROM {table_name} WHERE id = {id_value}")
        print(f' >> Field with id {id_value} deleted successfully from table {table_name}')

    def update_field(self, table_name: str, id_value: int, column_name: str, new_value: any) -> None:
        Query = f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?"
        self.execute(Query, (new_value, id_value))
        print(f'Field {column_name} of id {id_value} updated successfully in table {table_name}')


    def fetch_by_id(self,table_name,id) -> tuple:
        self.execute(f'SELECT * FROM {table_name} WHERE id = {id}')
        return self.cursor.fetchone()

    def fetch_last_one(self,table_name) -> tuple:
        self.execute(f'SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1')
        return self.cursor.fetchone()

    def fetch_all_by_foreign_key(self,table_name,column_name,foreign_key) -> list[tuple]:
        self.execute(f'SELECT * FROM {table_name} WHERE {column_name} = {foreign_key}')
        return self.cursor.fetchall()

    def fetch_all(self,table_name,) -> list[tuple]:
        self.execute(f'SELECT * FROM {table_name}')
        return self.cursor.fetchall()
import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect("mydatabase.db")
    conn.close()


def create_table(conn, create_table_sql):
    """ create Tables for a SQLite database """
    c = conn.cursor()
    c.execute(create_table_sql)


def show_columns(conn,tableName):
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(tableName))
    col_name_list = [tuple[0] for tuple in c.description]
    return tuple(col_name_list)


def insert_data_into_table(conn, tableName, values):
    c = conn.cursor()
    columns = show_columns(conn,tableName)
    inset_query = ''' INSERT INTO {}{} VALUES {}'''.format(tableName,columns,values)
    print(inset_query)
    c.execute(inset_query)


def main():
    conn = sqlite3.connect('mydatabase.db')

    sql_create_projects_table = """{}""".format(input('create table :  '))

    if conn is not None:
        create_table(conn,sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")

    show_columns(conn,input('select table :  '))
    insert_data_into_table(conn,input('put table name :  '),tuple(input().split()))


if __name__ == '__main__':
    main()
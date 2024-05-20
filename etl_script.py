import mysql.connector

# Connect to MySQL production database
def connect_to_mysql_production():
    try:
        conn = mysql.connector.connect(
            host='mysql-production',
            user='root',
            password='your_production_password',
            database='your_production_database'
        )
        return conn
    except Exception as e:
        print("Error connecting to MySQL production database:", e)
        return None

# Connect to MySQL warehouse database
def connect_to_mysql_warehouse():
    try:
        conn = mysql.connector.connect(
            host='mysql-warehouse',
            user='root',
            password='your_warehouse_password',
            database='your_warehouse_database'
        )
        return conn
    except Exception as e:
        print("Error connecting to MySQL warehouse database:", e)
        return None

# Extract table names from MySQL production database
def get_table_names(cursor):
    cursor.execute("SHOW TABLES")
    return [table[0] for table in cursor.fetchall()]

# Extract data from a table in MySQL production database
def extract_table_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

# Load data into a table in MySQL warehouse database
def load_data_into_warehouse(cursor, table_name, data):
    placeholders = ', '.join(['%s'] * len(data[0]))
    columns = ', '.join(data[0].keys())
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.executemany(query, data)

def main():
    production_conn = connect_to_mysql_production()
    if not production_conn:
        return

    warehouse_conn = connect_to_mysql_warehouse()
    if not warehouse_conn:
        production_conn.close()
        return

    try:
        production_cursor = production_conn.cursor(dictionary=True)
        warehouse_cursor = warehouse_conn.cursor()

        table_names = get_table_names(production_cursor)
        for table_name in table_names:
            data = extract_table_data(production_cursor, table_name)
            load_data_into_warehouse(warehouse_cursor, table_name, data)

        warehouse_conn.commit()
        print("Data successfully loaded into MySQL warehouse database.")

    except Exception as e:
        print("Error:", e)

    finally:
        production_cursor.close()
        warehouse_cursor.close()
        production_conn.close()
        warehouse_conn.close()

if __name__ == "__main__":
    main()

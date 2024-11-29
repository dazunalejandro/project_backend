import mysql.connector

def get_db_connection(db_name=""):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Quantum27?",
        database=db_name
    )

def execute_sql_file(connection, file_path):
    """
    Executes the SQL statements in a given file.
    """
    try:
        with open(file_path, "r") as sql_file:
            sql_script = sql_file.read()
            cursor = connection.cursor()
            for statement in sql_script.split(";"):
                if statement.strip():  # Skip empty statements
                    cursor.execute(statement)
            connection.commit()
            print(f"Executed {file_path} successfully.")
    except Exception as e:
        print(f"Error executing {file_path}: {e}")
    finally:
        cursor.close()
    
def does_database_exist(connection, db_name):
    """
    Checks if a database with the given name exists.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT SCHEMA_NAME FROM information_schema.schemata WHERE SCHEMA_NAME = %s", (db_name,))
        return cursor.fetchone() is not None  # Returns True if the database exists
    except Exception as e:
        print(f"Error checking database existence: {e}")
        return False
    finally:
        cursor.close()

def execute_db_setup_files():
    db_name = "sports_calendar"
    try:
        # Create a connection to MySQL
        conn = get_db_connection()

        # Check if the database exists
        if does_database_exist(conn, db_name):
            print(f"Database '{db_name}' already exists. Skipping setup.")
        else:
            # Execute schema.sql
            execute_sql_file(conn, "database/schema.sql")
            
            # Execute seed.sql
            execute_sql_file(conn, "database/seed.sql")
            
            print("Schema and seed data executed successfully.")

    except Exception as e:
        print(f"Error executing SQL files: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    execute_db_setup_files()

from app.db import get_connection

def query(query_string):
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute(query_string)

        # Commit if it's an insert/update/delete
        if query_string.strip().lower().startswith(("insert", "update", "delete", "create", "drop", "alter")):
            connection.commit()

        # Fetch results if it's a SELECT
        if query_string.strip().lower().startswith("select"):
            results = cursor.fetchall()
            return results

    finally:
        cursor.close()
        connection.close()

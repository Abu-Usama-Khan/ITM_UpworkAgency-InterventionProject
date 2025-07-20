from app.db import get_connection

def query(query_string, params=None):
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        if params:
            cursor.execute(query_string, params)
        else:
            cursor.execute(query_string)

        if query_string.strip().lower().startswith(("insert", "update", "delete", "create", "drop", "alter")):
            connection.commit()

        if query_string.strip().lower().startswith("select"):
            results = cursor.fetchall()
            return results

    finally:
        cursor.close()
        connection.close()

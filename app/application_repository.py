from database import get_connection


def get_all_applications():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT
                    a.id,
                    s.hostname,
                    a.name,
                    a.version,
                    a.status
                FROM applications a
                INNER JOIN servers s
                    ON s.id = a.server_id
                ORDER BY a.id
            """)

            return cursor.fetchall()

    finally:
        conn.close()
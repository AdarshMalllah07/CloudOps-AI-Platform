from database import get_connection


def get_all_environments():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id,
                    name,
                    description,
                    created_at
                FROM environments
                ORDER BY id
            """)

            return cursor.fetchall()

    finally:
        conn.close()
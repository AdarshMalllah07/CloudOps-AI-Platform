from database import get_connection


def get_all_servers():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT
                    s.id,
                    e.name as environment_name,
                    s.hostname,
                    s.ip_address,
                    s.operating_system,
                    s.status
                FROM servers s
                INNER JOIN environments e
                    ON e.id = s.environment_id
                ORDER BY s.id
            """)

            return cursor.fetchall()

    finally:
        conn.close()
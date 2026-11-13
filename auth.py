from database import get_connection

def login_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM users
    WHERE username=%s
    AND password=%s
    """

    cursor.execute(
        query,
        (username,password)
    )

    user = cursor.fetchone()

    conn.close()

    return user
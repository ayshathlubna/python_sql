from database import get_connection

def add_customer(name,email,phone,city):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO customers
    (customer_name,email,phone,city)

    VALUES(%s,%s,%s,%s)
    """

    values = (name,email,phone,city)

    cursor.execute(query,values)

    conn.commit()

    print("Customer Added")

    conn.close()

def view_customers():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM customers
    """

    cursor.execute(query)

    data = cursor.fetchall()

    for row in data:
        print(row)

    conn.close()


def update_customer(customer_id,new_city):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE customers

    SET city=%s

    WHERE customer_id=%s
    """

    cursor.execute(
        query,
        (new_city,customer_id)
    )

    conn.commit()

    print("Updated Successfully")

    conn.close()       


def delete_customer(customer_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    DELETE FROM customers

    WHERE customer_id=%s
    """

    cursor.execute(query,(customer_id,))

    conn.commit()

    print("Customer Deleted")

    conn.close()

def get_all_customers():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM customers
    """

    cursor.execute(query)

    data = cursor.fetchall()

    conn.close()

    return data
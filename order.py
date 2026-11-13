from database import get_connection
from datetime import date

def create_order(customer_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO orders
    (
        customer_id,
        order_date
    )

    VALUES(%s,%s)
    """

    cursor.execute(
        query,
        (
            customer_id,
            date.today()
        )
    )

    conn.commit()

    order_id = cursor.lastrowid

    conn.close()

    return order_id

def add_order_item(
    order_id,
    product_id,
    quantity
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO order_details

    (
        order_id,
        product_id,
        quantity
    )

    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            order_id,
            product_id,
            quantity
        )
    )

    conn.commit()

    conn.close()

def reduce_stock(
    product_id,
    quantity
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE products

    SET stock = stock - %s

    WHERE product_id=%s
    """

    cursor.execute(
        query,
        (
            quantity,
            product_id
        )
    )

    conn.commit()

    conn.close()
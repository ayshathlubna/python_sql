from database import get_connection

def add_product(
    product_name,
    category,
    price,
    stock
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO products

    (product_name,
    category,
    price,
    stock)

    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            product_name,
            category,
            price,
            stock
        )
    )

    conn.commit()

    print("Product Added")

    conn.close()

def view_products():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM products
    """

    cursor.execute(query)

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

def update_stock(
    product_id,
    new_stock
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE products

    SET stock=%s

    WHERE product_id=%s
    """

    cursor.execute(
        query,
        (
            new_stock,
            product_id
        )
    )

    conn.commit()

    conn.close()

def delete_product(product_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    DELETE FROM products

    WHERE product_id=%s
    """

    cursor.execute(query,(product_id,))

    conn.commit()

    conn.close()


def get_all_products():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM products
    """

    cursor.execute(query)

    products = cursor.fetchall()

    conn.close()

    return products
from database import get_connection
import pandas as pd

def get_sales_report():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT

        o.order_id,

        c.customer_name,

        p.product_name,

        od.quantity,

        p.price,

        od.quantity * p.price AS total

    FROM orders o

    JOIN customers c
        ON o.customer_id =
           c.customer_id

    JOIN order_details od
        ON o.order_id =
           od.order_id

    JOIN products p
        ON od.product_id =
           p.product_id
    """

    cursor.execute(query)

    data = cursor.fetchall()

    conn.close()

    return data

def total_revenue():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT SUM(
        od.quantity * p.price
    )
    FROM order_details od
    JOIN products p
    ON od.product_id = p.product_id
    """

    cursor.execute(query)

    result = cursor.fetchone()

    revenue = 0 if result[0] is None else result[0]

    conn.close()

    return revenue

def total_orders():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM orders
    """

    cursor.execute(query)

    result = cursor.fetchone()[0]

    conn.close()

    return result

def total_customers():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM customers
    """

    cursor.execute(query)

    result = cursor.fetchone()[0]

    conn.close()

    return result

def total_products():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM products
    """

    cursor.execute(query)

    result = cursor.fetchone()[0]

    conn.close()

    return result

def top_products():

    conn = get_connection()

    query = """
    SELECT

        p.product_name,

        SUM(
            od.quantity
        ) AS total_sold

    FROM order_details od

    JOIN products p
    ON od.product_id =
       p.product_id

    GROUP BY
        p.product_name

    ORDER BY
        total_sold DESC
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df

def revenue_by_product():

    conn = get_connection()

    query = """
    SELECT

        p.product_name,

        SUM(
            od.quantity *
            p.price
        ) AS revenue

    FROM order_details od

    JOIN products p
    ON od.product_id =
       p.product_id

    GROUP BY
        p.product_name

    ORDER BY
        revenue DESC
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df

def customer_revenue():

    conn = get_connection()

    query = """
    SELECT

        c.customer_name,

        SUM(
            od.quantity *
            p.price
        ) AS revenue

    FROM customers c

    JOIN orders o
    ON c.customer_id =
       o.customer_id

    JOIN order_details od
    ON o.order_id =
       od.order_id

    JOIN products p
    ON od.product_id =
       p.product_id

    GROUP BY
        c.customer_name

    ORDER BY
        revenue DESC
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df

def low_stock_products():

    conn = get_connection()

    query = """
    SELECT *

    FROM products

    WHERE stock < 20
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df

def average_order_value():

    revenue = total_revenue()

    orders = total_orders()

    if orders == 0:
        return 0

    return revenue / orders

# Monthly Revenue Trend
def monthly_revenue():

    conn = get_connection()

    query = """
    SELECT

        YEAR(o.order_date) AS year,

        MONTH(o.order_date) AS month,

        SUM(
            od.quantity * p.price
        ) AS revenue

    FROM orders o

    JOIN order_details od
        ON o.order_id = od.order_id

    JOIN products p
        ON od.product_id = p.product_id

    GROUP BY

        YEAR(o.order_date),
        MONTH(o.order_date)

    ORDER BY

        YEAR(o.order_date),
        MONTH(o.order_date)
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

# Customer Ranking
def top_customers():

    conn = get_connection()

    query = """
    SELECT

        c.customer_id,

        c.customer_name,

        SUM(
            od.quantity * p.price
        ) AS revenue

    FROM customers c

    JOIN orders o
        ON c.customer_id =
           o.customer_id

    JOIN order_details od
        ON o.order_id =
           od.order_id

    JOIN products p
        ON od.product_id =
           p.product_id

    GROUP BY

        c.customer_id,
        c.customer_name

    ORDER BY revenue DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def product_performance():

    conn = get_connection()

    query = """
    SELECT

        p.product_name,

        COALESCE(
            SUM(od.quantity),
            0
        ) AS total_sold

    FROM products p

    LEFT JOIN order_details od

    ON p.product_id =
       od.product_id

    GROUP BY
        p.product_name

    ORDER BY
        total_sold ASC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def restock_report():

    conn = get_connection()

    query = """
    SELECT

        product_name,

        stock

    FROM products

    WHERE stock < 10
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def best_selling_product():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT

        p.product_name,

        SUM(
            od.quantity
        ) AS total_sold

    FROM products p

    JOIN order_details od

    ON p.product_id =
       od.product_id

    GROUP BY
        p.product_name

    ORDER BY
        total_sold DESC

    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    conn.close()

    return result

def revenue_between_dates(
    start_date,
    end_date
):

    conn = get_connection()

    query = """
    SELECT

        SUM(
            od.quantity *
            p.price
        ) AS revenue

    FROM orders o

    JOIN order_details od
    ON o.order_id =
       od.order_id

    JOIN products p
    ON od.product_id =
       p.product_id

    WHERE o.order_date
    BETWEEN %s AND %s
    """

    cursor = conn.cursor()

    cursor.execute(
        query,
        (
            start_date,
            end_date
        )
    )

    revenue = cursor.fetchone()[0]

    conn.close()

    return revenue

import pandas as pd

import pandas as pd

import pandas as pd

def export_sales_report():

    data = get_sales_report()

    df = pd.DataFrame(
        data,
        columns=[
            "Order ID",
            "Customer Name",
            "Product Name",
            "Quantity",
            "Price",
            "Total"
        ]
    )

    df.to_excel(
        "sales_report.xlsx",
        index=False
    )

    print("Report Exported")
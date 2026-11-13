import streamlit as st
from customer import *
from auth import login_user


st.set_page_config(
    page_title="Sales Management System",
    layout="wide"
)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    st.title("Sales Management System Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.success(
                "Login Successful"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )

    st.stop()

st.title("Sales Management System")


menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Customers",
        "Products",
        "Orders",
        "Reports"
    ]
)

if menu == "Customers":

    st.header("Customer Management")

    with st.form("customer_form"):

        name = st.text_input("Customer Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        city = st.text_input("City")

        submit = st.form_submit_button("Add Customer")

        if submit:

            add_customer(
                name,
                email,
                phone,
                city
            )

            st.success(
                "Customer Added Successfully"
            )

    customers = get_all_customers()

    st.dataframe(customers)

from product import *
if menu=="Products":
    st.header("Product Management")

    with st.form("product_form"):
        product_name = st.text_input(
            "Product Name"
        )

        category = st.text_input(
            "Category"
        )

        price = st.number_input(
            "Price"
        )

        stock = st.number_input(
            "Stock"
        )

        submit = st.form_submit_button(
            "Add Product"
        )

        if submit:

            add_product(
                product_name,
                category,
                price,
                stock
            )

            st.success(
                "Product Added"
            )

    products = get_all_products()
    st.dataframe(products)

from order import * 
if menu == "Orders":

    st.header("Create Order")

    # select customer
    customer_id = st.number_input(
    "Customer ID",
    min_value=1
    )

    #select product
    product_id = st.number_input(
    "Product ID",
    min_value=1
    )
    
    quantity = st.number_input(
    "Quantity",
    min_value=1
    )

    if st.button("Place Order"):

        order_id = create_order(
            customer_id
        )

        add_order_item(
            order_id,
            product_id,
            quantity
        )

        reduce_stock(
            product_id,
            quantity
        )

        st.success(
            f"Order Created: {order_id}"
        )

from report import * 
if menu == "Reports":

    st.header("Sales Report")
    sales = get_sales_report()
    st.dataframe(sales)   
    if st.button(
    "Export Excel"
    ):

        export_sales_report()

        st.success(
            "Excel File Generated"
        )

   



if menu == "Dashboard":

    st.header("Sales Dashboard")
    start_date = st.date_input(
    "Start Date"
    )

    end_date = st.date_input(
        "End Date"
    )
    customers = get_all_customers()

    products = get_all_products()

    revenue = total_revenue()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric(
            "Revenue",
            total_revenue()
        )

    with col2:
        st.metric(
            "Orders",
            total_orders()
        )

    with col3:
        st.metric(
            "Customers",
            total_customers()
        )

    with col4:
        st.metric(
            "Products",
            total_products()
        )

    st.metric(
    "Average Order Value",
    round(
        average_order_value(),
        2
    )
    )
    
    st.subheader(
    "Top Selling Products"
    )

    df = top_products()

    st.bar_chart(
        df.set_index(
            "product_name"
        )
    )

    st.subheader(
    "Revenue By Product"
    )

    df = revenue_by_product()

    st.bar_chart(
        df.set_index(
            "product_name"
        )
    )

    st.subheader(
    "Customer Revenue"
    )

    df = customer_revenue()

    st.dataframe(df)

    st.subheader(
    "Low Stock Alert"
    )

    low_stock = low_stock_products()

    st.dataframe(low_stock)

    st.subheader(
    "Top Customers"
    )

    st.dataframe(
        top_customers()
    )

    st.subheader(
    "Monthly Revenue Trend"
    )

    df = monthly_revenue()

    st.line_chart(
        df["revenue"]
    )

    st.subheader(
    "Product Performance"
    )

    st.dataframe(
        product_performance()
    )


    st.subheader(
    "Restock Needed"
    )

    st.dataframe(
        restock_report()
    )

    best = best_selling_product()

    st.metric(
        "Best Seller",
        best[0]
    )

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
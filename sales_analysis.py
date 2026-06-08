# import pandas as pd
# import mysql.connector
# import matplotlib.pyplot as plt






# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Patil",
#     database="sales_project"
# )



# query = "SELECT * FROM sales_data"

# df = pd.read_sql(query, conn)
# print(df.columns)

# print(df.head())


# count_query = "SELECT COUNT(*) FROM sales_data"
# df = pd.read_sql(count_query, conn)
# print(df.head())

# df.groupby('city')['sales'].sum().plot(kind='bar')
# plt.title("City Wise Sales")
# plt.ylabel("Sales")
# plt.show()





import pandas as pd
import mysql.connector
import streamlit as st

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Patil",
    database="sales_project"
)

df = pd.read_sql("SELECT * FROM sales_data", conn)

st.title("Sales Dashboard")

st.metric("Total Sales", df['sales'].sum())

st.subheader("City Wise Sales")
st.bar_chart(df.groupby('City')['sales'].sum())

st.subheader("Product Wise Sales")
st.bar_chart(df.groupby('Product')['sales'].sum())
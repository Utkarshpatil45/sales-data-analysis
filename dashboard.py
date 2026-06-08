import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="wide")

df = pd.read_csv("sales_data.csv")

st.title("📊 Sales Analytics Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{df['sales'].sum():,.0f}")
col2.metric("Total Orders", len(df))
col3.metric("Products", df['Product'].nunique())

st.subheader("City Wise Sales")
city_sales = df.groupby('City')['sales'].sum()
st.bar_chart(city_sales)

st.subheader("Product Wise Sales")
product_sales = df.groupby('Product')['sales'].sum()
st.bar_chart(product_sales)

st.subheader("Raw Data")
st.dataframe(df)
import streamlit as st
import pandas as pd

st.title("Data App Assignment")

st.write("### Input Data")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)


# Aggregating by time
# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)

st.write("## Additions")
st.write("### (1) Drop down for Category")
category = st.selectbox("Select Category", df['Category'].unique())

st.write("### (2) Multi-select for Sub_Category *in the selected Category*")
sub_categories = st.multiselect("Select Sub-Category", df[df['Category'] == category]['Sub_Category'].unique())

st.write("### (3) Line chart of sales for the selected items")
def filter_data(category, sub_categories):
    filtered_df = df[(df['Category'] == category) & (df['Sub_Category'].isin(sub_categories))]
    return filtered_df

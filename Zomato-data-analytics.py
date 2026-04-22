import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("🍽️ Zomato Data Analysis")

# Load data
df = pd.read_csv("zomato.csv")

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# -------------------------
# Popular Food Types
st.subheader("Popular Food Types")

fig1, ax1 = plt.subplots()
df['listed_in(type)'].value_counts().plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# -------------------------
# Online Order Analysis
st.subheader("Online Order Availability")

fig2, ax2 = plt.subplots()
df['online_order'].value_counts().plot(kind='bar', ax=ax2)
st.pyplot(fig2)

# -------------------------
# Cost Analysis
st.subheader("Cost Distribution")

df['approx_cost(for_two_people)'] = df['approx_cost(for_two_people)'].astype(str).str.replace(',', '')
df['approx_cost(for_two_people)'] = pd.to_numeric(df['approx_cost(for_two_people)'], errors='coerce')

fig3, ax3 = plt.subplots()
sns.histplot(df['approx_cost(for_two_people)'], ax=ax3)
st.pyplot(fig3)

# -------------------------
# Rating Analysis
st.subheader("Rating Distribution")

df['rate'] = df['rate'].replace('NEW', None)
df['rate'] = df['rate'].replace('-', None)
df['rate'] = df['rate'].astype(str).str.split('/').str[0]
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

fig4, ax4 = plt.subplots()
sns.histplot(df['rate'], ax=ax4)
st.pyplot(fig4)

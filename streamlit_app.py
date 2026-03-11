import streamlit as st
import pandas as pd

st.title("Talking Rabbitt – Conversational Data Explorer")

# Preloaded dataset (no CSV upload needed)
data = {
    "Region": ["North", "South", "East", "West", "Central"],
    "Revenue": [1000, 1500, 1200, 1800, 900]
}

df = pd.DataFrame(data)

st.subheader("Dataset Preview")
st.dataframe(df)

question = st.text_input("Ask a question about the data")

if question:
    q = question.lower()

    if "highest revenue" in q or "max revenue" in q:
        region = df.loc[df["Revenue"].idxmax(), "Region"]
        value = df["Revenue"].max()

        st.success(f"{region} has the highest revenue: {value}")

        result = df.groupby("Region")["Revenue"].sum()
        st.bar_chart(result)

    elif "average revenue" in q:
        avg = df["Revenue"].mean()
        st.success(f"Average revenue is {avg}")

    else:
        st.info("Try asking: 'highest revenue' or 'average revenue'")

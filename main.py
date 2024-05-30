import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Advanced Streamlit Example')

# Generate some data
data = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100),
    'C': np.random.randn(100)
})

price = pd.read_excel('2618_Price.xlsx', dtype={'close':float})


st.write("Eva Air Line Historical Price:")
st.write(price)

# Plot the data
st.write("Line Chart of Column A:")
st.line_chart(price['close'])

st.write("Histogram of Column B:")
fig, ax = plt.subplots()
ax.hist(price['close'], bins=20)
st.pyplot(fig)

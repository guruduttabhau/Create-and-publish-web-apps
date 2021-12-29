import streamlit as st
import pandas
data={

  'series_1':[1,3,4,5,7],
  'series2':[10,30,40,100,250]
}
df=pandas.DataFrame(data)
st.title("First app")
st.subheader("automation")
st.write('''This is our first app
''')
st.write(df)
st.line_chart(df)
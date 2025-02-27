import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Stramlit")

st.write("This is simple text")




df = pd.DataFrame(

    {
        'first_column': [1,2,3,4],
        'second column': [10,20,30,40]
    }
)


st.write("Here is a dataframe")
st.write(df)

chart_data=pd.DataFrame(

    np.random.randn(20,3), columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

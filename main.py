import streamlit as st
import pandas as pd
# st.title("Welcome to Bangalore.")
# st.header('Python based Webpage')
# st.markdown("I Love Bangalore")
# st.code("""for i in range(1,5,1):
#                 print("Hello")""")
# dataset=pd.read_csv('test.csv')
# st.dataframe(dataset)

name=st.text_input("Enter Your name:")
fname=st.text_input("Enter Your father name:")
adr=st.text_area("Enter your address:")
class_data=st.selectbox('Enter Your Class:',(1,2,3,4,5))

button=st.button("Done")

if button:
    st.markdown(f"""
    Name:{name}
    Father Name:{fname}
    address:{adr}
    class:{class_data}""")
    
import streamlit as st 
number1 = st.number_input('Enter first number: ') 
number2 = st.number_input('Enter second number: ') 
number3 = st.number_input('Enter third number: ') 
if (number1 >= number2) and (number1 >= number3):   
  st.write('The maximum number is ', number1) 
elif (number2 >= number1) and (number2 >= number3):   
  st.write('The maximum number is ', number2) 
else:   st.write('The maximum number is ', number3)

import streamlit as st
import math
st.title("Simple Calculator")
number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Factorial"])
result = None  
if st.button("Calculate"):
    if operation == "Addition":
        result = number1 + number2
    elif operation == "Subtraction":
        result = number1 - number2
    elif operation == "Multiplication":
        result = number1 * number2
    elif operation == "Factorial":
        if number1 >= 0 and number2 == 0:  
            result = math.factorial(int(number1))
        elif number2 >= 0 and number1 == 0:  
            result = math.factorial(int(number2))
        else:
            result = "Factorial only defined for one number at a time"
    st.write("Result:", result)
    
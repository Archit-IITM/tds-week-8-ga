import streamlit as st

def run():
    st.set_page_config(
        page_title="TDS Week-8 GA - 22f2000744"
    )

    st.write("# TDS Week-8 GA - 22f2000744")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find largest number of the 3"):
        result = max(num1, num2, num3)
        st.success(f'The largest number is {result}')


if __name__ == "__main__":
    run()

import streamlit as st

def main():
    st.title("My Streamlit App")

    st.write("Welcome to my first Streamlit app!")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello {name}!")

    number = st.slider("Select a number", 0, 100)
    st.write(f"You selected: {number}")

if __name__ == "__main__":
    main()

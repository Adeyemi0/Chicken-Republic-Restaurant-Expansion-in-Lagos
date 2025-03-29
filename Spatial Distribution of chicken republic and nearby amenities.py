import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Chicken Republic Map in Streamlit")

    # Read the HTML file
    with open("Spatial Distribution of Chicken Republic Branches and Nearby Amenities in Lagos.html", "r", encoding="utf-8") as f:
        html_string = f.read()

    # Embed the HTML in Streamlit
    components.html(html_string, width=800, height=600, scrolling=True) #adjust width and height as needed.

if __name__ == "__main__":
    main()

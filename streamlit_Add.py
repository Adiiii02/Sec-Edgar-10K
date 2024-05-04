import streamlit as st

def display_sentiment_columns(heading,positive_text, negative_text):
    # Define CSS styles for each sentiment column and heading 
    heading_style = "color: white; font-size: 24px; padding-bottom: 10px; border-bottom: 1px solid #ccc; margin-bottom: 20px; background-color: #333; text-align: center;"
    positive_style = "background-color: lightgreen; padding: 10px; border-radius: 5px; margin: 5px;"
    positive_style = "background-color: lightgreen; padding: 10px; border-radius: 5px; margin: 5px;"
    negative_style = "background-color: lightcoral; padding: 10px; border-radius: 5px; margin: 5px;"

    # Display heading
    st.markdown(f'<div style="{heading_style}">{heading}</div>', unsafe_allow_html=True)

    # Display each sentiment text in its own column with respective style
    st.subheader("Positive Sentiment")
    if positive_text:
        for text in positive_text:
            st.markdown(f'<div style="{positive_style}">{text}</div>', unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="{positive_style}"></div>', unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)

    st.subheader("Negative Sentiment")
    if negative_text:
        for text in negative_text:
            st.markdown(f'<div style="{negative_style}">{text}</div>', unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="{negative_style}"></div>', unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)



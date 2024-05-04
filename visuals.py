import streamlit as st
import matplotlib.pyplot as plt

def generate_pie_chart(positive_sentences, negative_sentences):
    # Count positive and negative sentences
    positive_count = len(positive_sentences)
    negative_count = len(negative_sentences)
    
    # Generate pie chart
    labels = ['Positive', 'Negative']
    sizes = [positive_count, negative_count]
    colors = ['#1f77b4', '#ff7f0e']  
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display pie chart
    st.write(fig1)
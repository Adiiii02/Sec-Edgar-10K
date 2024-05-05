import streamlit as st

from Get_URL.Company_Tickers import get_ticker,company_names 

from Get_URL.Get_Urls import get_url

from Extraction.sections import sections,get_section_number

from Extraction.Extract_User_Given import get_any

from Extraction.Extract_Info import whole_info

from LLM_CALL.Summarizer import summarize_sentences

from LLM_CALL.Classifier import find_emotional_sentences

from streamlit_Add import display_sentiment_columns

from visuals import generate_pie_chart

#Title for the Page
st.title("Sec Edgar 10K Fillings Analysis")

#Drop Down for the list of companies the user can choose
company = st.selectbox("Select Company",company_names)

#Get Ticker of the choosen company from our dictionary
ticker = get_ticker(company)

#Drop Down for the list of sections the user can choose 
section_name = st.selectbox("Select Section", sections)

#Get Section number of the choosen section from our dictionary
section_number = get_section_number(section_name)

#Get the year from the user
Year = st.number_input("Choose Year to Analyze",value=2023)

#List of emotions to be used in the analysis
classifier_sentiment = ['positive', 'neutral', 'negative']

if st.button("Get Section Text"):

    #get the url of the choosen year
        url=get_url(ticker,Year)

        #get the information/text of the choosen section
        Result=get_any(url[0],section_number)

        #Extract text from the list
        text=Result[0]

        st.write(text)

#If User Selects to give his own Section to perform Analysis
if st.button("Analyze"):

    with st.spinner('Please Wait for a Minute ..'):

        #get the url of the choosen year
        url=get_url(ticker,Year)

        #get the information/text of the choosen section
        Result=get_any(url[0],section_number)

        #Extract text from the list
        text=Result[0]

        #pass all this into the function to get the sentiment of the sentences
        sentences_by_sentiment = find_emotional_sentences(text, classifier_sentiment, 0.85)

        #pass all these sentences into a fuction which summarizes the sentences
        positive,negative = summarize_sentences(sentences_by_sentiment)

        #Display them to the user
        display_sentiment_columns(section_name,positive,negative)

        if (len(positive)!=0 or len(negative)!=0):
            #Generate a Pie Chart
            generate_pie_chart(positive,negative)
        

if st.button("Auto Analyze"):

    with st.spinner('Please Wait for a Minute ..'):
    
        #get the url of the choosen year
        url=get_url(ticker,Year)

        #get the information/text of the specified section
        risk_factors,legal_pro,management_discuss,financial_statements = whole_info(url[0])

        #Extract text from the list
        risk_text = risk_factors[0]
        legal_text = legal_pro[0]
        management_text = management_discuss[0]
        finan_text = financial_statements[0]

        #Display the Summarized Risk factor Analysis to the user
        risk_sentences_by_sentiment= find_emotional_sentences(risk_text, classifier_sentiment, 0.85)
        risk_positive,risk_negative = summarize_sentences(risk_sentences_by_sentiment)
        display_sentiment_columns("Risk Factors",risk_positive,risk_negative)

        if(len(risk_positive)!=0 or len(risk_negative)!=0):
            #Generate a Pie Chart
            generate_pie_chart(risk_positive,risk_negative)

        #Display the Summarized Legal Proceedings Analysis to the user
        legal_sentences_by_sentiment = find_emotional_sentences(legal_text, classifier_sentiment, 0.85)
        legal_positive,legal_negative = summarize_sentences(legal_sentences_by_sentiment)
        display_sentiment_columns("Legal Proceedings",legal_positive,legal_negative)

        if(len(legal_positive)!=0 or len(legal_negative)!=0):
            #Generate a Pie Chart
            generate_pie_chart(legal_positive,legal_negative)

        #Display the Summarized Managements Discussion Analysis to the user
        manag_sentences_by_sentiment = find_emotional_sentences(management_text, classifier_sentiment, 0.85)
        manag_positive,manag_negative = summarize_sentences(manag_sentences_by_sentiment)
        display_sentiment_columns("Managements Discussion and Analysis",manag_positive,manag_negative)

        if(len(manag_positive)!=0 or len(manag_negative)!=0):
            #Generate a Pie Chart
            generate_pie_chart(manag_positive,manag_negative)

        #Display the Summarized Financial Statements and Supplementary Data Analysis to the user
        finan_sentences_by_sentiment = find_emotional_sentences(finan_text, classifier_sentiment, 0.85)
        finan_positive,finan_negative = summarize_sentences(finan_sentences_by_sentiment)
        display_sentiment_columns("Financial Statements and Supplementary Data",finan_positive,finan_negative)

        if(len(finan_positive)!=0 or len(finan_negative)!=0):
            #Generate a Pie Chart
            generate_pie_chart(finan_positive,finan_negative)

    

    

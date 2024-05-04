# SEC 10-K Analysis Tool

This project provides a web-based tool for analyzing SEC EDGAR 10-K filings of different companies. It allows users to select a company, fetch the relevant 10-K filing from the SEC API, extract various sections of the filing , auto analyse, perform sentiment analysis using the FinBERT model by ProsusAI, and summarize the content using the BART-Large-CNN model by Facebook. Additionally, it visualizes the sentiment analysis results using a pie chart.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack used](#techstackused)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Introduction

Analyzing SEC 10-K filings is crucial for understanding a company's financial health, risks, and performance. This project aims to simplify the process by providing a user-friendly interface to access, analyze, and summarize these filings.

## Features

- **Company Selection**: Users can select a company from a list of available options.
- **SEC API Integration**: Queries the SEC API to fetch the relevant 10-K filings for the selected company.
- **Extractor API**: Utilizes the Extractor API to extract different sections of the 10-K filings, such as Management's Discussion and Analysis (MD&A), Financial Statements, and Risk Factors.
- **Sentiment Analysis**: Performs sentiment analysis on the extracted sections using the FinBERT model to determine the sentiment (positive or negative) of the content.
- **Summarization**: Summarizes the extracted sections using the BART-Large-CNN model to provide concise summaries of the content.
- **Visualization**: Visualizes the sentiment analysis results using a pie chart to show the composition of positive and negative sentiments.


## Tech Stack Used

| Technology/Tool  | Purpose                                                                                             | 
|------------------|-----------------------------------------------------------------------------------------------------|
| Streamlit        | Frontend web framework for building interactive web applications with Python.                       |
| SEC API          | Provides access to SEC EDGAR filings, allowing retrieval of 10-K filings for analysis.              |
| Extractor API    | Extracts specific sections from 10-K filings, facilitating the analysis process.                    |
| FinBERT          | Pre-trained language model specialized in financial sentiment analysis.                             |
| BART-Large-CNN   | Pre-trained language model used for text summarization tasks.                                       |
| Matplotlib       | Python plotting library used to create visualizations, such as the pie chart for sentiment analysis.|

---

You can integrate this table into your README file. Let me know if you need further assistance!

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Adiiii02/Sec-Edgar-10K.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

Add API KEYS from https://sec-api.io/ and https://huggingface.co/

1. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

2. Access the app in your web browser (by default, it will be available at `http://localhost:8501`).

3. Select a company from the dropdown menu.

4. Wait for the analysis to complete. The tool will fetch the 10-K filing, extract sections, perform sentiment analysis, summarize the content, and visualize the results.

5. Explore the sentiment analysis results and summaries provided.

## Credits

- [SEC API](https://sec-api.io/)
- [Extractor API](https://extractorapi.com/)
- [FinBERT by ProsusAI](https://huggingface.co/ProsusAI/finbert)
- [BART-Large-CNN by Facebook](https://huggingface.co/facebook/bart-large-cnn)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
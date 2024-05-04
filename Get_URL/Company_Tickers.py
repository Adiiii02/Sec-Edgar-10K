company_names = [
    "Apple Inc.",
    "Microsoft Corporation",
    "Amazon.com Inc.",
    "Alphabet Inc.",
    "Facebook, Inc.",
    "Tesla, Inc.",
    "Johnson & Johnson",
    "Berkshire Hathaway Inc. (Class A)",
    "Berkshire Hathaway Inc. (Class B)",
    "JPMorgan Chase & Co.",
    "Exxon Mobil Corporation",
    "Walmart Inc.",
    "Visa Inc.",
    "Procter & Gamble Company",
    "Bank of America Corporation",
    "NVIDIA Corporation",
    "The Coca-Cola Company",
    "Pfizer Inc.",
    "The Walt Disney Company",
    "Intel Corporation",
    "AT&T Inc."
]


company_tickers = {
    "Apple Inc.": "AAPL",
    "Microsoft Corporation": "MSFT",
    "Amazon.com Inc.": "AMZN",
    "Alphabet Inc.": "GOOGL",
    "Facebook, Inc.": "FB",
    "Tesla, Inc.": "TSLA",
    "Johnson & Johnson": "JNJ",
    "Berkshire Hathaway Inc. (Class A)": "BRK.A",
    "Berkshire Hathaway Inc. (Class B)": "BRK.B",
    "JPMorgan Chase & Co.": "JPM",
    "Exxon Mobil Corporation": "XOM",
    "Walmart Inc.": "WMT",
    "Visa Inc.": "V",
    "Procter & Gamble Company": "PG",
    "Bank of America Corporation": "BAC",
    "NVIDIA Corporation": "NVDA",
    "The Coca-Cola Company": "KO",
    "Pfizer Inc.": "PFE",
    "The Walt Disney Company": "DIS",
    "Intel Corporation": "INTC",
    "AT&T Inc.": "T"
}

# Function to get ticker for a given company name
def get_ticker(company_name):
    return company_tickers.get(company_name)

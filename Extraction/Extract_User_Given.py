from sec_api import ExtractorApi

extractorApi = ExtractorApi("Your API Key From https://sec-api.io/")

def get_any(url_lists,number):
    User_Given=[] 

    # URL of the 10-K filing
    filing_10_k_url = url_lists

    # extract text section "Item Selected" from 10-K
    text = extractorApi.get_section(filing_10_k_url, f'{number}', 'text')

    User_Given.append(text)

    return User_Given
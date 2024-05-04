from sec_api import ExtractorApi

extractorApi = ExtractorApi("Your API Key From https://sec-api.io/")

def whole_info(url_lists):

    risk_factors=[] #1A
    legal_pro=[]    #3
    management_discuss=[] #7
    financial_statements=[] #8


    # URL of the 10-K filing
    filing_10_k_url = url_lists

    # extract text section "Item 1A" from 10-K
    item_1_text = extractorApi.get_section(filing_10_k_url, '1A', 'text')
    risk_factors.append(item_1_text)

    # extract text section "Item 3" from 10-K
    item_3_text = extractorApi.get_section(filing_10_k_url, '3', 'text')
    legal_pro.append(item_3_text)

    # extract text section "Item 7" from 10-K
    item_7_text = extractorApi.get_section(filing_10_k_url, '7', 'text')
    management_discuss.append(item_7_text)

    # extract text section "Item 8" from 10-K
    item_8_text = extractorApi.get_section(filing_10_k_url, '8', 'text')
    financial_statements.append(item_8_text)


    return risk_factors,legal_pro,management_discuss,financial_statements
    


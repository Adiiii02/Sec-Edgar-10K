from sec_api import QueryApi

queryApi = QueryApi(api_key="Your API Key From https://sec-api.io/")


def get_url(user_input,year):
    i=0
    url_lists=[]
    p=2023-year
    query = {
            "query": { "query_string": {
                "query": f"formType:\"10-K\" AND ticker:{user_input}", # only 10-Ks
            }},
            "from": f"{p}", # start returning matches from position null, i.e. the first matching filing
            "size": "1"  # return just one filing
        }


    response = queryApi.get_filings(query)

    #if no 10k for that year
    if response['filings']==[]:
        return 0

    url_lists.append(response['filings'][0]["linkToFilingDetails"])
    
    return url_lists
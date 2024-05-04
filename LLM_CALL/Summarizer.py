import requests

API_URL2 = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers2 = {"Authorization": "Bearer Your Access Token From https://huggingface.co/"}

def summ(payload):
	response = requests.post(API_URL2, headers=headers2, json=payload)
	return response.json()

def summarize_sentences(sentences_by_sentiment):
    positives=[]
    negatives=[]
    for k in sentences_by_sentiment.keys():
        #Check for sentences 
        if (len(sentences_by_sentiment[k])!=0):
            text = sentences_by_sentiment[k]
            summary = summ({"inputs": text})

            #add summarized sentences to the list
            idx=0
            while idx<len(summary):
                if k=='positive':
                    # print(summary)
                    positives.append(summary[idx]['summary_text'])
                else:
                    # print(summary)
                    negatives.append(summary[idx]['summary_text'])
                idx+=1
           
    return positives,negatives
        
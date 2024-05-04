import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
import requests

API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer Your Access Token From https://huggingface.co/"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def find_emotional_sentences(text, sentiment, threshold):
    sentences_by_sentiment = {}
    for e in sentiment:
        sentences_by_sentiment[e]=[]

    #chunk_size based on the length of the text
    if(len(text))>90000:
        sentence_chunks = chunk_sentences(text,480)
    elif(len(text))>65000:
        sentence_chunks = chunk_sentences(text,380)
    elif(len(text))>30000:
        sentence_chunks = chunk_sentences(text,270)
    else:
        sentence_chunks = chunk_sentences(text)

    # print(f'Document has {len(text)} characters and {len(sentence_chunks)} sentences.')

    for s in sentence_chunks:
        s=s[:500]
        prediction = query({"inputs": s})

        #Check if the sentence is not neutral and above the threshold
        if (prediction[0][0]['label']!='neutral' and prediction[0][0]['score']>threshold):

            #check no more than 10 sentences should be added
            if(len(sentences_by_sentiment[prediction[0][0]['label']])<10):
                sentences_by_sentiment[prediction[0][0]['label']].append(s)

    # for e in sentiment:
    #     print(f'{e}: {len(sentences_by_sentiment[e])} sentences')

    return sentences_by_sentiment


def chunk_sentences(corpus, max_words=100):
    sentences = sent_tokenize(corpus)
    chunks = []
    current_chunk = []
    word_count = 0
    
    for sentence in sentences:
        # Tokenize sentence into words
        words = word_tokenize(sentence)
        # Check if adding this sentence will exceed the word limit
        for word in words:
            if word_count + 1 <= max_words:
                current_chunk.append(word)
                word_count += 1
            else:
                # If adding this word exceeds the limit, start a new chunk
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                word_count = 1  # Reset word count for the new chunk
    
    # Add the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

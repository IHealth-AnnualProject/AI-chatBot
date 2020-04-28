#import necessary libraries
import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only


#Reading in the corpus
with open('chatbot.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("bonjour", "salut", "yo", "ça fait quoi", "ça va",)
GREETING_RESPONSES = ["ça va", "écoute, ça va", "salut mec", "bonjour", "Je suis trop content ! Tu me parles à moi"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='french')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"Je suis désolé ! Je ne vous comprends pas"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

print("sent_tokens[:2] = " + ''.join(sent_tokens[:2]))
print("word_tokens[:2] = " + ''.join(word_tokens[:2]))
flag=True
print("ROBO: Je m'appelle Robot. Je vais répondre vos questions sur les Chatbots. Si vous voulez quitter le chat, cliquez Bye !")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='merci' or user_response=='je vous remercie' ):
            flag=False
            print("ROBO: Je vous en prie...")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: " + greeting(user_response))
            else:
                print("ROBO: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO: Au revoir ! Restez chez vous...")    
        
        


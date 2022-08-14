import streamlit as st
import requests
import json
import pandas as pd

st.info('API Documentation:  \n ' + \
        '/all: Returns a list of all labels from the API ML model')

type = st.selectbox('Type of API call', ('Detect Hate Speech', 'Detect Homophobia', 'Detect Swearing', 
                    'Determine Sentiment (Emotion)', 'Detect Intent', 'Detect Toxicity', 'Detect All'))
text = st.text_area('Enter your text here')

if not text == "":
    if type == 'Detect Hate Speech':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/ishate?text={text}').json()
        df_all = pd.DataFrame.from_dict(data, orient='index', columns=['Confidence'])
        st.write(df_all)
        if data['HATE'] > data['NON_HATE']:
            st.write('Hate speech!')
        else:
            st.write('Not hate speech!')
    elif type == 'Detect Homophobia':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/ishomophobia?text={text}').json()
        if data['ishomophobia'] == True:
            st.write('Homophobic speech!')
        else: 
            st.write('Not homophobic!')
    elif type == 'Detect Swearing':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/isswearing?text={text}').json()
        if data['isswearing'] == True:
            st.write('Contains curse words!')
            st.write(f'Censored text: " + \n + data["text"])
        else: 
            st.write('No curse words!!')
    elif type == 'Determine Sentiment (Emotion)':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/sentiment?text={text}').json()
        df_all = pd.DataFrame.from_dict(data, orient='index', columns=['Result'])
        st.write(df_all)
    elif type == 'Determine Sentiment (Emotion)':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/sentiment?text={text}').json()
        df_all = pd.DataFrame.from_dict(data, orient='index', columns=['Result'])
        st.write(df_all)
    elif type == 'Detect Intent':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/intent?text={text}').json()
        df_all = pd.DataFrame.from_dict(data, orient='index', columns=['Result'])
        st.write(df_all)
    elif type == 'Detect Toxicity':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/toxicity?text={text}').json()
        df_all = pd.DataFrame.from_dict(data, orient='index', columns=['Result'])
        st.write(df_all)
    elif type == 'Detect All':
        data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/returnlabels?text={text}').json()
        df_all = pd.DataFrame.from_dict(data, orient='index', columns=['Result'])
        st.write(df_all)

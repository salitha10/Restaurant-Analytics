# In[1]:


# Imports
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import streamlit as st
import os
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import re
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


nltk.download('stopwords')

#Initializing the instances
tokenizer = RegexpTokenizer(r'\w+')
stopWords = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def app():
    st.markdown("""# Sentimental Analysis """)
    st.subheader("Analyze positive and negative reviews")
    st.write("")
    st.markdown(""" * Upload a csv file containing ratings and reviews """)

    def save_uploadedfile(uploadedfile):
        with open(os.path.join(uploadedfile.name),"wb") as f:
            f.write(uploadedfile.getbuffer())
        #  return st.success("Saved File:{}".format(uploadedfile.name))


    #Cleaning the review 
    def clean_sent(text):
        text = text.lower()

        #tokenize
        tokens = tokenizer.tokenize(text)
        new_tokens = [token for token in tokens if token not in stopWords]

        #lemmatizing
        stemmed_tokens = [lemmatizer.lemmatize(tokens) for tokens in new_tokens]

        return " ".join(stemmed_tokens)


    datafile = st.file_uploader("Upload CSV",type=['csv'])
    if datafile is not None:
        file_details = {"FileName":datafile.name,"FileType":datafile.type}
        data  = pd.read_csv(datafile)

        #Validate file
        if(data.shape[1]>2):
            st.error("File should contain only two columns")
        elif(data.columns[0]!="rating"):
            st.error("First column should be rating")
        elif(data.columns[1]!="review"):
            st.error("Second column should be review")
        else:
            save_uploadedfile(datafile)

            #Train model
            rating_df = pd.read_csv("SentimentalAnalysisData2.csv")

            # random split train and test data
            index = rating_df.index
            rating_df['random_number'] = np.random.randn(len(index))

            train = rating_df[rating_df['random_number'] <= 0.8]
            test = rating_df[rating_df['random_number'] > 0.8]

            X_train = train["review"]
            X_test = test["review"]
            y_train = train['sentiment']
            y_test = test['sentiment']

            cv = CountVectorizer(ngram_range = (1,2))
            XCV_train = cv.fit_transform(X_train).toarray()
            XCV_test = cv.transform(X_test).toarray()

            lr = LogisticRegression()
            lr.fit(XCV_train,y_train)
            y_pred = lr.predict(XCV_test)

            #New data
            data.dropna(inplace=True)
            data["review"] = data["review"].apply(clean_sent)

            pred_data = cv.transform(data['review']).toarray()
            data['predicted'] = lr.predict(pred_data)
            # st.write(predicted)

        
            #Visualizing the ratings
            st.subheader("Visualization of ratings")
            st.markdown(""" * Number of ratings for each rating category """)
            fig = px.histogram(data, x="rating")
            fig.update_traces(marker_color="orange")
            fig.update_layout(bargap=0.2)
            # fig.update_layout(title_text='Ratings')
            st.plotly_chart(fig)

            #Positive data
            dfp = data[data['predicted']==1]
            
            #Negaive data
            dfn = data[data['predicted']==0]

            original_title = '<b> <p style="font-family:Georgia; text-decoration: underline; color:Green; font-size: 40px;">Positive reviews</p></b>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.subheader("All positive reviews")
            st.dataframe(dfp[['rating', 'review']])

            #Word cloud
            st.subheader("Word cloud of positive reviews")
            st.markdown(""" * Bigger words are more prominent in positive reviews. That means customers are satisfied with those services.""")

            stopwords = set(STOPWORDS)
            stopwords.update(["br", "href"])
            pos = " ".join(review for review in dfp.review)
            wordcloud1 = WordCloud(stopwords=stopwords).generate(pos)

            plt.imshow(wordcloud1, interpolation='bilinear')
            plt.axis("off")
            plt.savefig('positive.png')
            st.image('positive.png')

            original_title = '<b><p style="font-family:Georgia; text-decoration: underline; color:Red; font-size: 40px;">Negative reviews</p></b>'
            st.markdown(original_title, unsafe_allow_html=True)
            st.subheader("All negative reviews")
            st.dataframe(dfn[['rating', 'review']])

            st.subheader("Word cloud of negative reviews")
            st.markdown(""" * Bigger words are more prominent in negative reviews. Take neecessaery actions to improve those areas.""")
            neg = " ".join(review for review in dfn.review)
            plt.imshow(wordcloud1, interpolation='bilinear')
            plt.axis("off")
            plt.savefig('negative.png')
            st.image('negative.png')


import pandas as pd
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st


def calc_avgRating(df):
    types = df['rest_type'].unique()
    for x in types:
        dfx = df[df['rest_type'] == x]
        avg_rating = df['rate'].mean()
        dfx['avg_rating'] = avg_rating
    return dfx



def app():
    data = pd.read_csv("DashData.csv")
    # data = data[0:10]
    # sns.distplot(data['rate'], color = 'red')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # fig, ax = plt.subplots(figsize = (5,5))
    # fig = sns.distplot(data['rate'], color = 'red', figsize = (5,5))
    # st.pyplot(fig)

    st.markdown(""" # Analytics """)
    st.markdown(" * Select a location to see ratings by restaurant type")

    loc = st.selectbox("Select a location", data['location'].unique())

    df = data[data['location'] == loc]
    dfz = df.groupby(['rest_type'],  as_index=False).mean()
    dfz.drop("Unnamed: 0", axis=1, inplace=True)
    dfz = dfz[['rest_type', 'rate', 'cost_two']]
    dfz.rename(columns = {'rest_type':'resturant_type', 'rate':'avg_rating','cost_two':'avg_cost_for_two'}, inplace = True)
    st.dataframe(dfz)

    plt.figure(figsize=(15,8))
    ax = sns.barplot( x = 'resturant_type', y = 'avg_rating', data = dfz)
    st.pyplot()


    # df = data['rate']
    # st.bar_chart(df)

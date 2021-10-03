#!/usr/bin/env python


# Import libraries
import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
from st_material_table import st_material_table




def app():



    st.write("""# Market Basket Analysis""")

    # Side bar
    st.sidebar.markdown("""# Apriori Algorithm """)
    st.sidebar.write('Select Parameters')
    #Dataset from streamlit sidebar dropdown
    dataset = 'restaurant-2-orders.csv'
    #Confidence
    min_threshold_for_metric = st.sidebar.slider('Minimum Confidence', 0.01, 0.99, 0.2)

    # Minimum support
    min_support = st.sidebar.slider('Minimum Support', 0.01, 0.5, 0.05,)


    # importing the data set
    orders = pd.read_csv(dataset)

    metric = "confidence"  # confidence is used as metric

    # Transform the data

    basket = (
        # group data (item name should be grouped in order to unstack later)
        orders.groupby([
            'Order ID', 'Item Name'
        ])['Quantity'].sum()  # Agregate quantity data just to apply unstack, the value doesnt change
        .unstack().reset_index()  # Transform to 1 transaction per row
        .fillna(0)  # fill the products that its not in the order with 0
        .set_index('Order ID')  # set the order number as index
    )

    basket_boolean_set = basket.applymap(lambda quantity: 1 if int(quantity) >= 1 else 0)

    frequent_itemsets = apriori(basket_boolean_set, min_support=min_support, use_colnames=True)


    # Association rule
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold_for_metric)

    rules.drop(['antecedent support','consequent support'], axis=1)
    # rules

    # formatting the values to proper decimal value

    rules['antecedents'] = rules['antecedents'].apply(lambda frozen_set: str(list(frozen_set))) # makes antecedent unchangeable
    rules['consequents'] = rules['consequents'].apply(lambda frozen_set: str(list(frozen_set))) # makes consequents unchangeable
    rules['support'] = rules['support'].apply(lambda value: round(value, 2))
    rules['confidence'] = rules['confidence'].apply(lambda value: round(value, 2))
    rules['lift'] = rules['lift'].apply(lambda value: round(value, 2))
    rules['leverage'] = rules['leverage'].apply(lambda value: round(value, 2))
    rules['conviction'] = rules['conviction'].apply(lambda value: round(value, 2))

    # Display data

    st.write(f"Rules using the metric {metric} with a minimun threshold of {metric} equals to  {min_threshold_for_metric}")

    dfx = rules[['antecedents', 'consequents']]
    dfx.columns = ["Antecedents", "Consequents"]

    dfx['Antecedents'] = dfx['Antecedents'].str.strip('[]')
    dfx['Antecedents'] = dfx['Antecedents'].str.strip("''")
    dfx['Antecedents'] = dfx['Antecedents'].apply(lambda x: x.replace("', '", ", "))

    dfx['Consequents'] = dfx['Consequents'].str.strip('[]')
    dfx['Consequents'] = dfx['Consequents'].str.strip("''")
    dfx['Consequents'] = dfx['Consequents'].apply(lambda x: x.replace("', '", ", "))

    filters = st.multiselect("Filter ", dfx['Antecedents'])

    if filters:
        st_material_table(dfx.loc[(dfx['Antecedents'].isin(filters))])
    else:
        st_material_table(dfx)







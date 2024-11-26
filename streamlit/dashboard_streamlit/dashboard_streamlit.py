import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Manipulation de données et création de graphique")

datasets_names = sns.get_dataset_names()
datasets = {dataset : sns.load_dataset(dataset) for dataset in datasets_names}

selected_dataset = st.selectbox("Quel dataset veux-tu utiliser ?", datasets_names)


selected_df = datasets[selected_dataset]


st.dataframe(selected_df)


columns_list = selected_df.columns.to_list()


selected_x = st.selectbox("Choisissez la colonne X :", columns_list)

selected_y = st.selectbox("Choisissez la colonne Y :", columns_list)


chart_list = ['scatter_chart', 'bar_chart', 'line_chart']


selected_chart = st.selectbox("Quel graphique veux-tu utiliser ?", chart_list)

if selected_chart == 'scatter_chart':
    sns.scatterplot(selected_df, x=selected_x, y=selected_y)
    plt.xlabel(selected_x)
    plt.ylabel(selected_y)
    st.pyplot(plt.gcf())

elif selected_chart == 'bar_chart':
    sns.barplot(selected_df, x=selected_x, y=selected_y)
    plt.xlabel(selected_x)
    plt.ylabel(selected_y)
    st.pyplot(plt.gcf())

elif selected_chart == 'line_chart':
    sns.lineplot(selected_df, x=selected_x, y=selected_y)
    plt.xlabel(selected_x)
    plt.ylabel(selected_y)
    st.pyplot(plt.gcf())


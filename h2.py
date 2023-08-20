import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import scipy.stats as stats
def dplot():
    uploaded_file = st.file_uploader("Выберите csv файл для загрузки", type=['csv'])
    if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
        df=df.dropna(how="any")
        df=df.astype({"Year":"int"})
        df=df.astype({"Year":"object"})
        df=df.astype({"Platform":"object"})
        df = df.replace(['2600'],['Atari2600'])
        col1, col2, col3 = st.columns(3)
        with col1:
            sd=st.selectbox("Выберите переменную, данные по которой хотите просмотреть", ["Rank", "Name", "Platform", "Year", "Genre", "Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"], key=1)
            if sd is not None:
                df[sd]
                if sd=="Platform" or sd=="Year" or sd=="Genre" or sd=="Publisher" or sd=="NA_Sales" or sd=="EU_Sales" or sd=="JP_Sales" or sd=="Other_Sales" or sd=="Global_Sales":
                    if st.button('Построить график', key="a"):
                        if sd=="Platform" or sd=="Year" or sd=="Genre" or sd=="Publisher":
                            fig = px.histogram(df.sort_values(by=[sd]), x=sd, width=1000, height=600, color=sd)
                            fig.show()
                        elif sd=="NA_Sales" or sd=="EU_Sales" or sd=="JP_Sales" or sd=="Other_Sales" or sd=="Global_Sales":
                            fig = px.violin(df, y=sd, box=True, width=800, height=800, points='all')
                            fig.show()
                elif sd=="Rank" or sd=="Name":
                    st.write("По выбранным данным невозможно построить график и провести статистический тест")
        with col2:
            sd2 = st.selectbox("Выберите переменную, данные по которой хотите просмотреть", ["Rank", "Name", "Platform", "Year", "Genre", "Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"], key=2)
            if sd2 is not None:
                df[sd2]
                if sd2=="Platform" or sd2=="Year" or sd2=="Genre" or sd2=="Publisher" or sd2=="NA_Sales" or sd2=="EU_Sales" or sd2=="JP_Sales" or sd2=="Other_Sales" or sd2=="Global_Sales":
                    if st.button('Построить график', key="b"):
                        if sd2=="Platform" or sd2=="Year" or sd2=="Genre" or sd2=="Publisher":
                            fig2 = px.histogram(df.sort_values(by=[sd2]), x=sd2, width=1000, height=600, color=sd2)
                            fig2.show()
                        elif sd2=="NA_Sales" or sd2=="EU_Sales" or sd2=="JP_Sales" or sd2=="Other_Sales" or sd2=="Global_Sales":
                            fig2 = px.violin(df, y=sd2, box=True, width=800, height=800, points='all')
                            fig2.show()
                elif sd2=="Rank" or sd2=="Name":
                    st.write("По выбранным данным невозможно построить график и провести статистический тест")
        with col3:
            if (sd=="Platform" or sd=="Year" or sd=="Genre" or sd=="Publisher") and (sd2=="Platform" or sd2=="Year" or sd2=="Genre" or sd2=="Publisher"):
                sd3 = st.selectbox("Выберите тест, который вы хотите произвести для выбранных данных", ["Тест Хи-квадрат"], key=3)
                if sd3=="Тест Хи-квадрат":
                    observed=pd.crosstab(df[sd], df[sd2])
                    chi2, pv, freedom, expected = stats.chi2_contingency(observed) 
                    st.write("Хи квадрат:", chi2,"Число степеней свободы:", freedom, "p-value:", pv)
            elif (sd=="NA_Sales" or sd=="EU_Sales" or sd=="JP_Sales" or sd=="Other_Sales" or sd=="Global_Sales") and (sd2=="NA_Sales" or sd2=="EU_Sales" or sd2=="JP_Sales" or sd2=="Other_Sales" or sd2=="Global_Sales"):
                sd3 = st.selectbox("Выберите тест, который вы хотите произвести для выбранных данных", ["t-тест", "Тест Манна-Уитни", "ANOVA тест"], key=4)
                if sd3=="t-тест":
                    tt=stats.ttest_ind(df[sd], df[sd2], equal_var=False)
                    st.write(tt)
                elif sd3=="Тест Манна-Уитни":
                    mwh=stats.mannwhitneyu(df[sd], df[sd2])
                    st.write(mwh)
                elif sd3=="ANOVA тест":
                    anov=stats.f_oneway(df[sd], df[sd2])
                    st.write(anov)

st.title("Homework 2")
dplot()       
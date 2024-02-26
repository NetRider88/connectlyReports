import streamlit as st
import pandas as pd
import plotly_express as px 


st.set_page_config(page_title='Connectly reports')
st.title('Connectly Reports')
st.subheader('upload connectly report')
uploaded_file = st.file_uploader('choose the excel file', type='csv')
if uploaded_file:
    st.markdown('---')
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    groupby_column = st.selectbox(
        'Whats would you like to analyse?',
        (
            'campaign_name',
            'delivered',
            'read',
            'has_error'
        )
    )
    
    output_column = ['delivered', 'read', 'has_error']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_column].sum()

    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y=['delivered', 'read', 'has_error'],
        color_discrete_sequence=['yellow', 'green', 'red'],
        barmode='group',
        template='plotly_white',
        title=f'<b>Delivered vs Read by {groupby_column}</b>'
    )
    st.plotly_chart(fig)
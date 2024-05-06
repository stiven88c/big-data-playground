import streamlit as st
import pandas as pd

DATA_DIR = 'data/'
data = pd.read_csv(DATA_DIR + 'temp-uppsala.csv', sep=";", skiprows=10)

data['DatumTid'] = data['Datum'] + ' ' + data['Tid (UTC)']
data['DatumTid'] = pd.to_datetime(data['DatumTid'], format='%Y-%m-%d %H:%M:%S')

data = data[['DatumTid', 'Lufttemperatur']]

start_date = st.date_input('Select a start date')
end_date = st.date_input('Select an end date')

data_1993 = data[(data['DatumTid'] >= str(start_date)) & (data['DatumTid'] <= str(end_date))]

st.write(data_1993.head())

st.line_chart(data_1993.set_index('DatumTid'))
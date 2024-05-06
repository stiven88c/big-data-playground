import streamlit as st
import pandas as pd

DATA_DIR = 'data/'
data = pd.read_csv(DATA_DIR + 'temp-uppsala.csv', sep=";", skiprows=10)

data['DatumTid'] = data['Datum'] + ' ' + data['Tid (UTC)']
data['DatumTid'] = pd.to_datetime(data['DatumTid'], format='%Y-%m-%d %H:%M:%S')

data = data[['DatumTid', 'Lufttemperatur']]

start_date = st.date_input('Select a start date', pd.to_datetime('1993-01-01'))
end_date = st.date_input('Select an end date', pd.to_datetime('1993-12-31'))

data_1993 = data[(data['DatumTid'] >= str(start_date)) & (data['DatumTid'] <= str(end_date))]

st.write(data_1993.head())

st.line_chart(data_1993.set_index('DatumTid'))
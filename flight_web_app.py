import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple flight Prediction App
This app predicts the price of flight!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Airline = st.text_input("label goes here")
    Date_of_Journey = st.text_input("label goes here")
    Source =  st.text_input("label goes here")
    Destination =  st.text_input("label goes here")
    Dep_Time=st.text_input("label goes here")
    Arrival_Time=st.text_input("label goes here")
    Duration=st.text_input("label goes here")
    Total_Stops=st.number_input("number goes here")
    Additional_Info=st.text_input("label goes here")
    date = st.text_input("label goes here")
    

    data = {'Name of airline': Airline,
            'Journey Date': Date_of_Journey,
            'Source': Source,
            'Destination': Destination,
            "Departure Time":Dep_Time,
            'Arrival_Time':Arrival_Time,
            'Duration':Duration,
            'Total Stops of flight':Total_Stops,
            'Additional Information':Additional_Info,
            'Date':date}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

df["Duration"]=df['Duration'].str.replace("h", '*60').str.replace(' ','+').str.replace('m','*1').apply(eval)

df["Journey_day"] = df['Date_of_Journey'].str.split('/').str[0].astype(int)
df["Journey_month"] = df['Date_of_Journey'].str.split('/').str[1].astype(int)
df.drop(["Date_of_Journey"], axis = 1, inplace = True)

df["Dep_hour"] = pd.to_datetime(df["Dep_Time"]).dt.hour
df["Dep_min"] = pd.to_datetime(df["Dep_Time"]).dt.minute
df.drop(["Dep_Time"], axis = 1, inplace = True)

df["Arrival_hour"] = pd.to_datetime(df.Arrival_Time).dt.hour
df["Arrival_min"] = pd.to_datetime(df.Arrival_Time).dt.minute
df.drop(["Arrival_Time"], axis = 1, inplace = True)

df['Total_Stops'].replace(['1 stop', 'non-stop', '2 stops', '3 stops', '4 stops'], [1, 0, 2, 3, 4], inplace=True)

df["Additional_Info"].replace({"1 Short layover":"Other",
                                "Change_airports":"Other",
                                "Business class":"Other",
                                "Red-eye flight":"Other",
                                "2 Long layover":"Other"},inplace=True)
                                

df['Airline'].replace(['Jet Airways', 'Indigo', 'Air India', 'SpiceJet''Vistara','Air Asia','GoAir','Multiple carriers Premium economy','Jet Airways Business','Vistara Premium economy','Trujet'], [4,3,1,8,10,0,2,7,5,11,9], inplace=True)

df['Source'].replace(['Delhi', 'Kolkata', 'Banglore', 'Mumbai', 'Chennai'], [2, 3, 0, 4, 1], inplace=True)

df['Destination'].replace(['Cochin', 'Banglore', 'Delhi', 'New Delhi', 'Hyderabad','Kolkata'], [1, 0, 2, 5, 3,4], inplace=True)

df['Additional_Info'].replace(['No info', 'In-flight meal not included', 'No check-in baggage included', '1 Long layover', 'Other'], [4, 2, 3, 0, 1], inplace=True)


import pickle
loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
result = loaded_model.predict(df)

st.subheader('Price')
st.write(result)


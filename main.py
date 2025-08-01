import pandas as pd
from gtts import gTTS
import time
from playsound import playsound
from datetime import datetime
import math


airplane_df = pd.read_csv("Airplane Announcement - Sheet1.csv")


# Steps:
# 1 create a dataframe from csv
# 2 use a while loop that infinitely will check for boarding updates

def call_boarding(i):
   text = f"Boarding for {airplane_df['Airline Name'][i]} flight number {airplane_df['Flight number'][i]} from {airplane_df['Airport'][i]} to {airplane_df['Destination'][i]} will begin shortly."

   boarding_call = gTTS(text=text, lang='en', slow=True)
   output = f"{airplane_df['Airline Name'][i]}_boarding_call.mp3"
   boarding_call.save(output)
   playsound(output)


def arrival(i):
   arrival_time = (str(str(datetime.fromtimestamp((airplane_df['Arrival'][i]))).split(' ')[1]).split(':00')[0])
   text = f"{airplane_df['Airline Name'][i]} flight number {airplane_df['Flight number'][i]} from {airplane_df['Airport'][i]} to {airplane_df['Destination'][i]} has arrived at {arrival_time} on {airplane_df['Arrival Date'][i]}."

   boarding_call = gTTS(text=text, lang='en', slow=True)
   output = f"{airplane_df['Airline Name'][i]}_arrival.mp3"
   boarding_call.save(output)
   playsound(output)


def departure(i):
   departure_time =  (str(str(datetime.fromtimestamp((airplane_df['Departure'][i]))).split(' ')[1]).split(':00')[0])
   text = f"{airplane_df['Airline Name'][i]} flight number {airplane_df['Flight number'][i]} from {airplane_df['Airport'][i]} to {airplane_df['Destination'][i]} has departed at {departure_time} on {airplane_df['Departure Date'][i]}."

   boarding_call = gTTS(text=text, lang='en', slow=True)
   output = f"{airplane_df['Airline Name'][i]}_departure.mp3"
   boarding_call.save(output)
   playsound(output)


announced = {
    'boarding': [False] * len(airplane_df),
    'departure': [False] * len(airplane_df),
    'arrival': [False] * len(airplane_df)
}



while not all(announced['boarding']) or not all(announced['departure']) or not all(announced['arrival']):
   for i in range(len(airplane_df)):
      if not announced['boarding'][i] and abs(int(airplane_df['Boarding Time'][i])- int(time.time()))<=0:
         call_boarding(i)
         announced['boarding'][i] = True

      if not announced['departure'][i] and abs(int(airplane_df['Departure'][i]) - int(time.time()))<=0:
         departure(i)
         announced['departure'][i] = True
         
      if not announced['arrival'][i] and abs(int(airplane_df['Arrival'][i]) - int(time.time()))<=0:
         arrival(i)
         announced['arrival'][i] = True

   time.sleep(1)



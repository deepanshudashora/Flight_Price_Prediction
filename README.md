# Flight_Price_Prediction
-------> A web app using stream lit which can predict the price of your next flight

## There are file in the whole project:
--> Exploration of data and making plots
--> making model using dataset and saving it using pickle
--> making a web app using streamlit

## Exploration of data--------------->>>>>>>>>
1) Importing the dataframe
2) Exploring the diffrent asspects of dataset
3) Checking the missing values
4) Making the plots using seaborn and matplotlib
5) Understanding the diffrent variations of price with the airlines and departure times
6) Then checking wheather the arrival place and departure place matter in terms of price or not
7) In this exploration notebook I am using bar plot, heatmap, scatter plot, cat plot, box plot, violin plot and many more

## Maiking the model----------------->>>>>>>>>>>
1) Exploring the data
2) Understanding the data
3) Preprocessing the data applying the date time processing, changing the hours and minute to only minute, droping the routs and changing some additional information
4) Now comes the model part basically I am using GridSearchCV and appltying diffrent algorithms of regression and coming on the conclusion that random forest and xg bosst working best
5) saving the model using pickle and good to go for webapp

## Making web app-------------------->>>>>>>>>>>>>>>>
1) I am using streamlit for making the web app
2) It is way easier comaper with flask and django
3) All I did was made a function for user input converting into dataframe and applying same preprocressing which I applied in model
4) Predicting the new data's price with saved model

## The project is done and Thanks for reding and giving your time

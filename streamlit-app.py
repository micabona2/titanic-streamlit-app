###
# Code originally written by Harry Wang (https://github.com/harrywang/mini-ml/)
# It was modified for the purpose of teaching how to deploy a machine learning 
# model using Streamlit.
###

import streamlit as st
import pandas as pd
import joblib

# load your machine learning model
tree_clf = joblib.load('model_dt.pickle')

### Streamnlit app code starts here

st.title('Titanic Survival Prediction')
st.markdown('**Please provide passenger information**:')  # you can use markdown like this

# get inputs
sex = st.selectbox('Sex', ['female', 'male'])
age = int(st.number_input('Age:', min_value=0, max_value=100, value=20))
sib_sp = int(st.number_input('# of siblings / spouses aboard:', min_value=0, max_value=100, value=0))
pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
fare = int(st.number_input('# of parents / children aboard:', min_value=0, max_value=1000, value=0))

# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

### Now the inference part starts here

passenger = pd.DataFrame(
    {
        'Pclass': [pclass],
        'Sex': [sex], 
        'Age': [age],
        'SibSp': [sib_sp],
        'Fare': [fare]
    }
)

y_pred = tree_clf.predict(passenger)

# Preparing the message to be displayed based on the prediction
if y_pred[0] == 0:
    msg = 'This passenger is predicted to be: **died**'
else:
    msg = 'This passenger is predicted to be: **survived**'

### Now add the prediction result to the Streamlit app

prediction_state.markdown(msg)
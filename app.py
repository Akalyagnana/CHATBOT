import streamlit as st
import pandas as pd
import pickle as pk

model=pk.load(open('model.pkl','rb'))
scaler=pk.load(open('scaler.pkl','rb'))

st.header('Loan Prediction')

no_of_dept=st.slider('Choose no of dependencies ',0,5)

grad=st.selectbox('Choose Education ',['Graduated','Not Graduated'])

self_emp=st.selectbox('Self Employed',['Yes','No'])

annual_income=st.slider('Choose annual income',0,10000000)
loan_amt=st.slider('Choose Loan Amount',0,10000000)
loan_duration=st.slider('Choose Loan Duration',0,20)
cibil=st.slider('Choose cibil Score',0,1000)
assets=st.slider('Choose Assets',0,10000000)



if grad== 'Graduated':
    grad_s=0
else:
    grad_s=1

if self_emp== 'Yes':
    emp_s=0
else:
    emp_s=1


if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dept,grad_s,emp_s,annual_income,loan_amt,loan_duration,cibil,assets]],
                         columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan Is Approved')
    else:
        st.markdown('Loan Is Rejected')
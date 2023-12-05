import streamlit as st
import joblib 
import numpy as np
#from PIL import Image
import time




add_selectbox=st.sidebar.radio("Select an oprion",
                                   ("Home","Prediction",))
if add_selectbox=="Prediction":
    st.title("Fack currency prediction")
    st.image('https://www.shutterstock.com/image-vector/game-money-one-dollar-bill-260nw-44730493.jpg',width=400)
    st.subheader("Give your details:-")
    varience = st.slider(":blue[Pick variance of currency]:",-8.00,8.00)
    skewness =st.slider(":blue[Pick skewness of currency]",-14.00,14.00)
    curtosis =st.slider(":blue[Pick curtosis of currency]",-6.00,18.00)
    entropy =st.slider(":blue[Pick entropy of currency]",-9.00,3.00)

    l1=[varience,skewness,curtosis,entropy]


    if st.button('submit'):
        with st.spinner('Wait for it...'):
            time.sleep(3)
        loaded_model = joblib.load("randomforest_model")
        result = loaded_model.predict([l1])
        print(result)
        st.success("Done!")
        result=result.tolist()
        if result==[1]:
            st.write("Congradulation it's a original currency")
            st.snow()
        else:
            st.subheader(":red[check with this currency]",divider='rainbow')


    else:
        st.info("click on submit button to predict")
elif add_selectbox=="Home":
    st.header(':red["BE AWARE OF FRUAD"]')
    st.image("https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/08/31/Photos/Processed/rupee4-kLcH--621x414@LiveMint.jpg",width=400)
    st.write('''1. Fake currency, also known as counterfeit money, is a form of illegal currency reproduction.
2. Counterfeiters create fake bills and coins with the intent to deceive and defraud people.
3. Counterfeit currency can lead to significant economic losses for individuals, businesses, and governments.
4. To raise awareness, it's crucial to educate people about the security features of genuine currency.
5. Security features include watermarks, holograms, color-shifting ink, and microprinting, among others.
6. People should learn how to detect counterfeit money to protect themselves from financial losses.
7. Businesses, especially cash-handling ones, should invest in counterfeit detection technology.
8. Governments and law enforcement agencies play a vital role in combating counterfeiting.
9. Reporting counterfeit currency and suspicious activity is essential in the fight against fake money.
10. Public awareness and cooperation are key in reducing the circulation of counterfeit currency and maintaining trust in the financial system.''')

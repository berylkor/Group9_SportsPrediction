
import pickle
import streamlit as st

# Opens the deployed model
model = pickle.load(open('C:/Users/beryl/OneDrive/Desktop/Deployment/deployment_model.pkl', 'rb'))

with open('scalar_model.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

def predict():
    st.title('Sports Prediction')

    # Features
    cf = st.text_input('cf')
    gk = st.text_input('gk')
    lm = st.text_input('lm')
    lcb = st.text_input('lcb')
    rm = st.text_input('rm')
    potential = st.number_input('potential')
    value_eur = st.number_input('value_eur')
    wage_eur = st.number_input('wage_eur')
    release_clause_eur = st.number_input('release_clause_eur')
    movement_reactions = int(st.number_input('movement_reactions'))
    age = int(st.number_input('age'))

   
    if st.button('Predict', key='predict_button'):
        
        user_inputs = [gk, lcb, cf, lm, rm, potential, value_eur, wage_eur, release_clause_eur, movement_reactions, age]

        scaled_inputs = scaler.transform([user_inputs])

        makeprediction = model.predict(scaled_inputs)

        output = round(makeprediction[0], 2)
        st.success("The player's overall rating is {}".format(output))

if __name__ == '__main__':
    predict()


#go to terminal and type (streamlit run football_prediction.py)

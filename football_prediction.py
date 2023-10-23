
import pickle
import streamlit as st


# def main_data():
st.title('Sports Prediction')

model = pickle.load(open('C:/Users/beryl/OneDrive/Desktop/alternative/deployment_model.pkl','rb'))
#scalar = pickle.load(open('C:/Users/beryl/OneDrive/Desktop/alternative/scalar_model.pkl','rb'))

# features
cf = st.number_input('cf')
gk = st.number_input('gk')
lm = st.number_input('lm')
lcb = st.number_input('lcb')
rm = st.number_input('rm')
potential = st.number_input('potential')
value_eur = st.number_input('value_eur')
wage_eur = st.number_input('wage_eur')
release_clause_eur = st.number_input('release_clause_eur')
movement_reactions = int(st.number_input('movement_reactions'))
age =int(st.number_input('age'))

overall_prediction = model.predict([[cf,gk,lm,lcb,rm,potential,value_eur,wage_eur,release_clause_eur,movement_reactions,age]])

    #this is the  code that we will use for prediction
if st.button('Predict'):
     st.write('The player\'s overall performance is ', overall_prediction[0])
        # user_inputs = [
        #     gk, lcb, cf, lm, rm, potential, value_eur, wage_eur, release_clause_eur, movement_reactions, age
        # ]

        # # Scale the user inputs using the loaded scaler
        # scaled_inputs = scalar.transform([user_inputs])

        # # Make predictions using the model
        # makeprediction = model.predict(scaled_inputs)

        # output = round(makeprediction[0], 2)

# if __name__=='__main__':
    main_data()

#go to terminal and type (streamlit run football_prediction.py)
#key='predict_button'
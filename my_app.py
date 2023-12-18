import streamlit as st
import pickle
import pandas as pd

from git import Object
import base64


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('g2.png')


html_temp = """
<div style="background-color:#00ab67;padding:10px">
<h1 style="color:white;text-align:center;">SAUDI CAR PRICE PREDICTION</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
st.write('\n')





# images


st.text("    ")

#pickles
model = pickle.load(open("LG_model2.pkl","rb"))
#columns = pickle.load(open("columns.pkl", 'rb'))


st.header("*Enter the Features of Your Car*")

current_year = 2023


car_model_year = st.slider('Car Model Year', current_year - 30, current_year, current_year)

age = current_year - car_model_year






km = st.slider("What is the km of your car?",0,600000,step=500)
Mileage= km/1.609
Type = st.selectbox("Select the model of your car", ('Accent','Camry','Hilux','Sonata','Taurus','Elantra',
 'Tahoe','Yukon','Corolla','Land Cruiser','Expedition','Furniture','Sunny','Accord','Yaris','ES','Prado',
'Pajero','Sierra','Suburban','6','Caprice','Innova',
 'Charger','Patrol','Cerato','Impala','FJ','Senta fe',
 'Explorer','Datsun','S','Rio','Optima','C','Tucson',
 'Azera','Land Cruiser Pickup', 'CX9','H1','Avalon','Victoria','Marquis','E','Range Rover','The 7','LX'))





Options = st.selectbox("Please select the type of options for your car", ('Full', 'Standard', 'Semi Full'))


#data
my_dict = {
	"Type": Type,	
    "Options": Options,
    
    "Mileage": Mileage,
	"vehicle_age": age,
	
}



df = pd.DataFrame([my_dict])
#df = pd.get_dummies(df)
#df = df.reindex(columns=columns, fill_value=0)
#df = final_scale.transform(df)

#evaluation
if st.button("Predict", type="primary"):
    pred = model.predict(df)
    st.markdown("### Your car's estimated price is **{} SR**.".format(int(pred)))
    
    

    


    

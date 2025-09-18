import pandas as pd
import streamlit as st
import pickle
data=pickle.load(open(r"D:\practices\cars_Predictions.sav",'rb'))

st.title("Car Price Prediction")
st.sidebar.header('Feature Selecting')
st.sidebar.info('Application For Prediction Cars_Price')
st.image("https://images.pexels.com/photos/1545743/pexels-photo-1545743.jpeg")


m1=['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
       'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
       'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
       'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
       'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
       'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
       'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
       'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
       'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
       'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
       'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']
m2=[16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 23, 20,  0, 44, 19, 39,  7, 25,  4,
       33, 47, 15,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]
manu_maping=dict(zip(m1,m2))
manu1=st.selectbox("Manufacturer",m1)
manu2 = manu_maping[manu1]
mm1=['RX 450', 'Equinox', 'FIT', 'E 230 124', 'RX 450 F SPORT','Prius C aqua']
mm2=[890,477,485,470,833]
model_maping=dict(zip(mm1,mm2))
Model1=st.selectbox('Model',mm1)
Model=model_maping[Model1]
c1=['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine', 'Pickup']
c2=[4,3,9,2,10,7,0,1,6,8,5]
category_maping=dict(zip(c1,c2))
category1=st.selectbox("Category",c1)
category=category_maping[category1]
l1=['yes', 'no']
l2 = [1,2]
leather_mapping = dict(zip (l1, l2))
Leather1 = st.selectbox('Leather interior', l1)
Leather=leather_mapping [Leather1]
f1=['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG','Hydrogen']
f2=[2, 5, 1, 6, 4, 0, 3]
Fuel_Mapping=dict(zip(f1, f2))
Fuel1=st.selectbox("Fuel type", f1)
Fuel=Fuel_Mapping[Fuel1]
Engin=st.selectbox('Engine volume', [3.5, 3., 1.3, 2.5, 2., 1.8, 2.4, 1.6, 2.2, 1.5, 3.3, 1.4, 2.3, 3.2, 1.2, 1.7, 2.9, 1.9, 2.7, 2.8, 2.1, 1., 0.8, 3.4, 2.6, 1.1])

Airbags=st.selectbox('Airbags', [12, 8, 2, 0, 4, 6, 10, 3, 1, 16, 5, 7, 9, 11,14,15,13])
G1=['Automatic', 'Tiptronic', 'Variator', 'Manual']
G2=[3, 0, 2, 1]
Gear_mapping=dict(zip(G1,G2))
Gear1=st.selectbox("Gear",G1)
Gear=Gear_mapping[Gear1]
w1=['Left wheel', 'Right-hand drive']
w2=[1, 0]
wheels_mapping=dict(zip(w1,w2))
wheel1=st.selectbox("Drive Wheels",w1)
Wheel=wheels_mapping[wheel1]
cc1=['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
cc2=[ 1, 14, 12,  7,  2, 13, 11,  8,  6, 15,  3,  5,  0,  4, 10,  9]
color_mapping=dict(zip(cc1,cc2))
color1=st.selectbox("Color",cc1)
Color=color_mapping[color1]
D1=['4x4', 'Front', 'Rear']
D2=[1, 0, 2]
Drive_mapping=dict(zip(D1,D2))
Drive1=st.selectbox("Drive Wheel",D1)
Drive=Drive_mapping[Drive1]
Cylinders = st.number_input("Cylinders")
Age=st.number_input('Age')
mileage=st.number_input("Mileage")
Levy=st.number_input("Levy")
#----------------------------------------------------
df = pd.DataFrame({
    'Manufacturer': [manu2],
    'Model': [Model],
    'Category': [category],
    'Leather interior': [Leather],
    'Fuel type': [Fuel],
    'Mileage': [mileage],
    'Gear box type': [Gear],
    'Drive wheels': [Drive],
    'Wheel': [Wheel],
    'Color': [Color],
    'Levy': [Levy],
    'Engine volume': [Engin],
    'Cylinders': [Cylinders],
    'Airbags': [Airbags],
    'Age': [Age]
}, index=[0])

p=st.sidebar.button("Predict Price")

if p:
    pre=data.predict(df)
    st.sidebar.write("Price is :",pre)
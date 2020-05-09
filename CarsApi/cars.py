import pandas as pd

cars_df = pd.read_csv(r'./CarsApi/car_ad.csv', encoding='ISO-8859-1')
cars_df = cars_df[cars_df['price']>0]

a_list=list(range(86))
b_list=sorted(list(cars_df.car.unique()))
car_list = tuple(zip(a_list, b_list))

c_list= list(range(6))
d_list= sorted(list(cars_df.body.unique()))
body_list = tuple(zip(c_list, d_list))

e_list= list(range(4))
f_list= sorted(list(cars_df.engType.unique()))
eng_list = tuple(zip(e_list, f_list))

x_list= x_list= list(range(3))
y_list= sorted(['full', 'rear', 'front'])
drive_list = tuple(zip(x_list, y_list))

m_list= list(range(880))
n_list= sorted(list(cars_df.model.unique()))
model_list = tuple(zip(m_list, n_list))

u_list= list(range(2))
v_list= sorted(list(cars_df.registration.unique()))
reg_list = tuple(zip(u_list, v_list))
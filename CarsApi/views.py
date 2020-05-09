from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from sklearn.externals import joblib
from django.contrib import messages
import numpy as np
import pandas as pd
import xgboost as xgb
from .forms import priceForm
from .models import Price
from .serializer import priceSerializer
# Create your views here.

class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = priceSerializer

def price_reject(unit):
    try:
        cars_model = joblib.load(r'./CarsApi/cars_model.pkl')
        x_test = unit
        y_pred = cars_model.predict(x_test)
        amount = np.exp(y_pred)
        price = int(amount[0])
        return 'Your car is valued at ${}'.format(price)
    except ValueError as bad:
        return Response(bad.args[0], status.HTTP_400_BAD_REQUEST)

def price_contact(request):
    if request.method == 'POST':
        form = priceForm(request.POST)
        if form.is_valid():
            mydict = form.cleaned_data
            for key in mydict:
                mydict[key] = int(mydict[key])
            my_df = pd.DataFrame(mydict, index=[0])
            X = xgb.DMatrix(my_df)
            print(price_reject(X))
            #print(my_df)
            answer = price_reject(X)
            messages.success(request, answer)
    form = priceForm()

    return render(request, 'CarsApi/form.html', {'form':form})
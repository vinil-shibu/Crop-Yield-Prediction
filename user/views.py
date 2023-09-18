from .models import register,yield_data
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def home(request):
    if(request.method=='POST'):
        Crop=int(request.POST['crop'])
        Rain=int(request.POST['rain'])
        Pesticide=int(request.POST['pesticide'])
        Avg_temp=int(request.POST['avg_temp'])

        df = pd.read_csv(r"static/Datasets/yield.csv")
        # x=df.drop(["yield","Area","ID"],axis=1)
        # y=df["yield"]

        # e=LabelEncoder()
        # item=e.fit_transform(x['Item'])
        # x['Crop']=item
        # X=x.drop('Item',axis=1)

        # X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.34)
        # #X_train=X[['Year','avg_rainfall_','pest_ton','avg_temp','Crop']]
        # y_train=df['yield']
        # reg=LinearRegression()
        # reg.fit(X_train,y_train)
        x=df.drop(["yield","Area","ID"],axis=1)
        y=df["yield"]

        e=LabelEncoder()
        item=e.fit_transform(x['Item'])
        x['Crop']=item
        X=x.drop('Item',axis=1)

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.34,shuffle=True)
        reg=RandomForestRegressor()
        reg.fit(X_train,y_train)
        pred=reg.predict([[Year,Rain,Pesticide,Avg_temp,Crop]])
        yld=yield_data.objects.create(crop=Crop,rain=Rain,pesticide=Pesticide,year=Year,avg_temp=Avg_temp)
        yld.save()
        prey=int(pred)
        return render(request,'p_yield.html',{'predict':prey,'crop':Crop,'rain':Rain,'pesticide':Pesticide,'year':Year,'avg_temp':Avg_temp})
    else:
        messages.info(request,"Enter the Input Values")
        return render(request,'home.html')

def p_yield(request):
    return render(request,'p_yield.html')

def logout(request):
    return render(request,'index.html')

# '''
def login(request):
    if request.method=='POST':
        e_mail=request.POST['email']
        pas=request.POST['password']
        if register.objects.filter(mail=e_mail).exists():
            if register.objects.filter(pasd=pas).exists():
                return redirect('home')
            else:
                messages.info(request,"Wrong Password")
                return render(request,'login.html')
        else:
            messages.info(request,"Invalid Email-ID")
            return render(request,'login.html')
    else:
        return render(request,'login.html')
# '''

def reg(request):
    if request.method=='POST':
        first=request.POST['fname']
        last=request.POST['lname']
        email=request.POST['email']
        pwd=request.POST['password']
        pwd1=request.POST['password1']
        if(pwd == pwd1):
            if register.objects.filter(mail=email).exists():
                messages.info(request,"E-mail already Exists")
                return render(request,'reg.html')
            else:
                sup=register.objects.create(ft_name=first,lt_name=last,mail=email,pasd=pwd)
                sup.save()
                return render(request,'login.html')
        else:
            messages.info(request,"Password Doesn't Match")
            return render(request,'reg.html')
    else:
        return render(request,'reg.html')

'''

def login(request):
    if(request.method=='POST'):
        mail=request.POST['email']
        pwd=request.POST['password']

        user=auth.authenticate(email=mail,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

'''
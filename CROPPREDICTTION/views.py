from django.shortcuts import render
import joblib
def index(request):
   return render(request, 'index.html')


def home(request):
   return render(request, 'predict.html')


def result(request):
   if request.method=="POST":
      cls = joblib.load("finall.sav")
      lis = []
      lis.append(request.POST["N"])
      lis.append(request.POST["P"])
      lis.append(request.POST["K"])
      lis.append(request.POST["T"])
      lis.append(request.POST["NEM"])
      lis.append(request.POST["pH"])
      lis.append(request.POST["mm"])
      ans = cls.predict([lis])
      return render(request,'result.html',{"ans":ans[0].upper(),"lis":lis})
def model(request):
       return render(request, 'model.html')



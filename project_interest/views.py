from django.shortcuts import render
from app_interest.models import SimpleInterest

def home(request):
     result='Nono'
     total='Nono'

     data={}
    
     
     if request.POST:
          principal = request.POST.get('principal') or 0
          rate = request.POST.get('rate') or 0
          time = request.POST.get('time') or 0

          principal = int(principal)
          rate = float(rate)
          time = int(time)

          result = (principal * rate * time) / 100
          total = principal + result
          print(principal)


          data={
               'result':result,
               'total':total
          }
          print(principal)
          print(rate)
          print(time)
          print(total)
          obj = SimpleInterest(
            principal=principal,
            rate=rate,
            time=time
        )
          obj.save()
          

     return render(request,"home.html",data)

     
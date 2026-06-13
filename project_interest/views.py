from django.shortcuts import render
from app_interest.models import SimpleInterest

def home(request):
     result='Nono'
     total='Nono'

     data={}
    
     
     if request.POST:
          principal = int(request.POST.get('principal') )
          rate = float(request.POST.get('rate') )
          time = float(request.POST.get('time') )

          principal = int(principal)
          rate = float(rate)
          time = float(time)

          result = (principal * rate * time) / 100
          total = principal + result
          
          data={
               'result':result,
               'total':total
          }
        
          obj = SimpleInterest(
            principal=principal,
            rate=rate,
            time=time
        )
          obj.save()
          

     return render(request,"home.html",data)

     
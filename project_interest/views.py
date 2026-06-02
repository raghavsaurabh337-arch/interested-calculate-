from django.shortcuts import render

def home(request):
     result='Nono'
     total='Nono'

     data={}
    
     
     if request.POST:
          principal=int(request.POST.get('principal',0))
          rate=float(request.POST.get('rate',0))
          time=int(request.POST.get('time',0))

          result=(principal*rate*time)/100
          total=principal+result
          print(principal)


          data={
               'result':result,
               'total':total
          }
          print(principal)
          print(rate)
          print(time)
          print(total)
          

     return render(request,"home.html",data)

     
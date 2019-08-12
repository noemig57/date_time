from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now()
    print(datetime.now())
    currentYear = now.year
    
    context = {
        "time": now,
        "year" : currentYear
    

    }
    return render(request,'timedate/index.html', context)

    



from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.




def greet_user(request, name):
    # Define your GMT offset (e.g., GMT+2)
    gmt_offset = 2
    current_time = datetime.utcnow() + timedelta(hours=gmt_offset)
    return render(request, 'greet_user.html', {'name': name, 'current_time': current_time})
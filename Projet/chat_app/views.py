from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def app_index(request):
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

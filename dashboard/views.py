from django.shortcuts import render
from django.db import connection
from .models import Client


def home(request):
    return render(request, 'index.html')

def home(request):

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM clients")
        total_clients = cursor.fetchone()[0]

    return render(request, 'index.html', {
        'total_clients': total_clients
    })
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})
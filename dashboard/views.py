from django.shortcuts import render
from django.db.models import Count
import json

from .models import (
    Student,
    MasterTrainer,
    Client,
    Course,
    Room,
    Certificate,
    Notification,
    Program
)


def home(request):

    # ====================================
    # KPI CARDS
    # ====================================

    total_students = Student.objects.count()

    active_trainees = Student.objects.filter(
        status='active'
    ).count()

    total_master_trainers = MasterTrainer.objects.count()

    active_master_trainers = MasterTrainer.objects.filter(
        status='Active'
    ).count()

    total_clients = Client.objects.count()

    total_courses = Course.objects.count()

    occupied_rooms = Room.objects.filter(
        status='Occupied'
    ).count()

    total_certificates = Certificate.objects.count()

    total_notifications = Notification.objects.count()

    # ====================================
    # PROGRAMS PER CLIENT BAR CHART
    # ====================================

    program_data = (
        Program.objects
        .values('client__client_name')
        .annotate(total=Count('program_id'))
    )

    client_labels = [
        item['client__client_name']
        for item in program_data
    ]

    client_totals = [
        item['total']
        for item in program_data
    ]

    # ====================================
    # PROGRAM DURATION CHART
    # ====================================

    programs = Program.objects.all()

    training_labels = []
    training_duration = []

    for program in programs:
        training_labels.append(program.program_name)
        training_duration.append(program.duration_days)

    # ====================================
    # PROGRAM CATEGORY PIE CHART
    # ====================================

    category_data = (
        Program.objects
        .values('category')
        .annotate(total=Count('program_id'))
        .order_by('category')
    )

    category_labels = [
        item['category']
        for item in category_data
    ]

    category_totals = [
        item['total']
        for item in category_data
    ]

    # ====================================
    # PROGRAM DETAILS
    # ====================================

    program_details = Program.objects.all()

    # ====================================
    # CONTEXT
    # ====================================

    context = {

        # KPI Cards
        'total_students': total_students,
        'active_trainees': active_trainees,
        'total_master_trainers': total_master_trainers,
        'active_master_trainers': active_master_trainers,
        'total_clients': total_clients,
        'total_courses': total_courses,
        'occupied_rooms': occupied_rooms,
        'total_certificates': total_certificates,
        'total_notifications': total_notifications,

        # Programs Per Client Chart
        'client_labels': json.dumps(client_labels),
        'client_totals': json.dumps(client_totals),

        # Program Duration Chart
        'training_labels': json.dumps(training_labels),
        'training_duration': json.dumps(training_duration),

        # Programs By Category Pie Chart
        'category_labels': json.dumps(category_labels),
        'category_totals': json.dumps(category_totals),

        # Program Details
        'program_details': program_details,
    }

    return render(request, 'index.html', context)
def report(request):
     return render(request, 'report.html')
   
from django.urls import path
from .views import home, send_due_date_emails, example_view, borrowers_list  # Import your views

urlpatterns = [
    path('', home, name='home'),  # Map the root URL to the home view
    path('send-due-date-emails/', send_due_date_emails, name='send_due_date_emails'),  # URL for sending due date emails
    path('api/borrowers/', borrowers_list, name='borrowers'),  # Updated endpoint for borrowers list
    path('api/example/', example_view, name='example'),  # URL for the example view
]

from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import Member
from .utils import generate_email_content
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return HttpResponse("Welcome to the Django Backend")

def send_due_date_emails(request):
    if request.method == 'POST':
        current_time = now()
        due_members = Member.objects.filter(due_date__date=current_time.date())

        if not due_members.exists():
            return JsonResponse({"message": "No members with due dates today."}, status=200)

        for member in due_members:
            email_content = generate_email_content({
                'borrower_name': member.borrower_name,
                'outstanding_amount': member.outstanding_amount,
                'due_date': member.due_date.strftime('%d-%m-%Y')
            })
            try:
                send_mail(
                    'Your Upcoming Payment Due',
                    email_content,
                    'kunalanvade20@gmail.com',  # Replace with your actual email
                    [member.email],
                    fail_silently=False,
                )
                print(f"Email sent to {member.email} successfully.")
            except Exception as e:
                print(f"Failed to send email to {member.email}: {e}")

        return JsonResponse({"message": "Emails sent successfully"}, status=200)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

@api_view(['GET'])
def example_view(request):
    data = {"message": "Hello from Django"}
    return Response(data)

@api_view(['GET'])
def borrowers_list(request):
    # Example logic to fetch and return borrower data
    data = {
        'borrowers': [
            {'id': 1, 'name': 'John Doe'},
            {'id': 2, 'name': 'Jane Doe'},
        ]
    }
    return Response(data)

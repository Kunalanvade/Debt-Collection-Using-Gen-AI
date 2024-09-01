import cohere
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings
from email_sender.models import Member

def generate_email_content(context):
    cohere_api_key = settings.COHERE_API_KEY
    co = cohere.Client(cohere_api_key)
    
    try:
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=(
                f"Generate an email for {context['borrower_name']} with an outstanding amount of "
                f"{context['outstanding_amount']} due on {context['due_date'] } from Debt_Collection."
            ),
            max_tokens=200
        )
        
        if response.generations and response.generations[0].text.strip():
            return response.generations[0].text.strip()
        else:
            return "No content generated."
    
    except Exception as e:
        return "Failed to generate email content due to an internal error."

def send_due_date_emails_function():
    borrowers = Member.objects.all()
    df = pd.DataFrame(list(borrowers.values()))

    required_columns = ['due_date', 'email', 'borrower_name', 'outstanding_amount']
    df.columns = df.columns.str.strip().str.lower()

    # Ensure required columns are present
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"DataFrame missing required columns: {', '.join(missing_columns)}")
        return

    # Ensure 'due_date' is a datetime object and not in string format
    if not pd.api.types.is_datetime64_any_dtype(df['due_date']):
        df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')

    # Drop duplicates based on email to avoid sending multiple emails to the same address
    due_dates = df.drop_duplicates(subset='email')

    for index, row in due_dates.iterrows():
        recipient_email = row.get('email')
        recipient_name = row.get('borrower_name')
        
        if not recipient_email:
            print(f"Skipping row with missing email: {row}")
            continue
        
        try:
            # Convert 'due_date' to string in the desired format
            due_date_str = row['due_date'].strftime('%d-%m-%y')
        except Exception as e:
            print(f"Error formatting due date for row {row}: {e}")
            continue
        
        context = {
            'borrower_name': recipient_name,
            'outstanding_amount': row.get('outstanding_amount', 'N/A'),
            'due_date': due_date_str
        }
        
        email_content = generate_email_content(context)

        try:
            send_mail(
                f'Due Date Reminder for {recipient_name}',
                email_content,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            print(f"Email sent Successfully")
        except Exception as e:
            print(f"Failed to send email ")

from django.core.management.base import BaseCommand
from email_sender.utils import send_due_date_emails_function

class Command(BaseCommand):
    help = 'Send due date emails'

    def handle(self, *args, **kwargs):
        send_due_date_emails_function()
        self.stdout.write(self.style.SUCCESS('Successfully sent due date emails'))

import csv
from django.core.management.base import BaseCommand
from email_sender.models import Member
from datetime import datetime
from django.db.utils import IntegrityError
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load data from CSV into the Member model'

    def handle(self, *args, **kwargs):
        file_path = r'"C:\Users\Yamraaj\Desktop\csv\load_member_data.csv"'
        
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        # Adjust the format to match the date format in your CSV
                        due_date = datetime.strptime(row['Due_Date'], '%d-%m-%y')

                        # Convert numerical values to appropriate types
                        total_loan_amount = Decimal(row['Loan_Amount'].replace(',', ''))
                        outstanding_amount = Decimal(row['Outstanding_Balance'].replace(',', ''))

                        Member.objects.create(
                            borrower_id=row['Borrower_ID'],
                            borrower_name=row['Borrowers_Name'],
                            total_loan_amount=total_loan_amount,
                            outstanding_amount=outstanding_amount,
                            due_date=due_date,
                            email=row['Email']
                        )
                    except ValueError as e:
                        self.stdout.write(self.style.ERROR(f"Value error for row {row}: {e}"))
                    except IntegrityError as e:
                        self.stdout.write(self.style.ERROR(f"Integrity error for row {row}: {e}"))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))

            self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))

from django.db import models

class Member(models.Model):
    borrower_id = models.IntegerField()
    borrower_name = models.CharField(max_length=255)
    total_loan_amount = models.FloatField()
    outstanding_amount = models.FloatField()
    due_date = models.DateTimeField()
    email = models.EmailField()
    # Add other fields as necessary

    def __str__(self):
        return self.borrower_name

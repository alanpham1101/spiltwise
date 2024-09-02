from datetime import date

from django.db import models

from constants import (
    SplitMode,
    ExpenseStatus,
    ActivityType,
)


class TimestampModel(models.Model):
    cdate = models.DateTimeField(db_column="cdate", auto_now_add=True)
    udate = models.DateTimeField(db_column="udate", auto_now=True)

    class Meta:
        abstract = True


class User(TimestampModel):
    user_id = models.IntegerField(primary_key=True, auto_created=True, db_column="user_id")
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Group(TimestampModel):
    group_id = models.IntegerField(primary_key=True, auto_created=True, db_column="group_id")
    name = models.CharField(max_length=255)


class Expense(TimestampModel):
    expense_id = models.IntegerField(primary_key=True, auto_created=True, db_column="expense_id")
    expense_date = models.DateField(default=date.today)
    title = models.CharField(max_length=255, required=True)
    amount = models.IntegerField(required=True)
    payer = models.ForeignKey(to=User, on_delete=models.CASCADE, db_column="payer_id")
    payees = models.ManyToManyField(to=User)
    split_mode = models.CharField(choices=SplitMode.SPLIT_MODE_CHOICES)


class ExpenseLine(TimestampModel):
    expense_line_id = models.IntegerField(primary_key=True, auto_created=True, db_column="expense_line_id")
    expense = models.ForeignKey(to=Expense, on_delete=models.CASCADE, db_column="expense_id")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, db_column="user_id")
    status = models.CharField(choices=ExpenseStatus.EXPENSE_STATUS_CHOICE)


class Activity(TimestampModel):
    activity_id = models.IntegerField(primary_key=True, auto_created=True, db_column="activity_id")
    activity_type = models.CharField(choices=ActivityType.ACTIVITY_TYPE_CHOICE)

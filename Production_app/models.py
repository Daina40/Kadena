from django.db import models
from datetime import datetime, time


class ProductionModel(models.Model):
    FLOOR_CHOICES = (
        ("0", "*ALL"),
        ("1", "KSL-1"),
        ("2", "KSL-2"),
        ("3", "KSL-3"),
        ("4", "KSL-4"),
        ("5", "KSL-5"),
        ("6", "KSL-6"),
        ("7", "KSL-7"),
        ("8", "KSL-8"),
        ("9", "KSL-9"),
        ("10", "KSL-10"),
        ("11", "KSL-11"),
        ("12", "KSL-12"),
        ("13", "KSL-13"),
        ("14", "KSL-14"),
        ("15", "KSL-15"),
        ("16", "KSL-16"),
        ("17", "KSL-17"),
        ("18", "KSL-Sample"),
        ("19", "FSL-1"),
        ("20", "FSL-2"),
        ("21", "FSL-3"),
        ("22", "FSL-4"),
        ("23", "FSL-5"),
        ("24", "FSL-6"),
        ("25", "FSL-Sample"),
    )
    LINE_CHOICES = (
        ("0", "*ALL"),
        ("1", "A"),
        ("2", "A1"),
        ("3", "A2"),
        ("4", "B"),
        ("5", "B1"),
        ("6", "B2"),
        ("7", "C"),
        ("8", "C1"),
        ("9", "C2"),
        ("10", "D"),
        ("11", "D1"),
        ("12", "D2"),
        ("13", "E"),
        ("14", "E1"),
        ("16", "E2"),
        ("17", "F"),
        ("18", "F1"),
        ("19", "F2"),
        ("20", "G"),
        ("21", "H"),
    )
    date = models.DateField(default=datetime.now)
    floor = models.CharField(max_length=2, choices=FLOOR_CHOICES, default='')
    order_qty = models.IntegerField()
    daily_prod = models.IntegerField()
    total_prod = models.IntegerField()
    daily_insp = models.IntegerField()
    total_insp = models.IntegerField()
    daily_packpass = models.IntegerField()
    total_packpass = models.IntegerField()
    line_balance = models.IntegerField()
    insp_balance = models.IntegerField()
    total_balance = models.IntegerField(default=0)
    over_prod = models.IntegerField()
    over_pass = models.IntegerField()
    repair_balance = models.IntegerField()
    line = models.CharField(max_length=2, choices=LINE_CHOICES, default='')
    buyer = models.CharField(max_length=100)
    style = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    po_buy = models.CharField(max_length=50)
    remarks = models.TextField()
    

    def __str__(self):
        return self.floor

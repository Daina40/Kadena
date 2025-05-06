from django.db import models
from Production_app.models import ProductionModel

class DefectStatus(models.Model):
    month = models.CharField(max_length=20)
    date = models.DateField()
    
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
    floor = models.CharField(max_length=2, choices=FLOOR_CHOICES, default='')
    line = models.CharField(max_length=2, choices=LINE_CHOICES, default='')

    qc_name = models.CharField(max_length=50, null=True, blank=True)
    qc_id = models.CharField(max_length=50, null=True, blank=True)
    supervisor_name = models.CharField(max_length=50, null=True, blank=True)
    supervisor_id = models.CharField(max_length=50, null=True, blank=True)
    buyer = models.CharField(max_length=100)
    style = models.CharField(max_length=50)
    order_qty = models.IntegerField(null=True, blank=True)
    buy_po= models.CharField(max_length=50, null=True, blank=True)
    product_type = models.CharField(max_length=10, null=True, blank=True)
    total_inspect_quantity = models.IntegerField(null=True, blank=True)

    # Defect categories
    fabric_fault = models.IntegerField(null=True, blank=True, default=0)
    shading = models.IntegerField(null=True, blank=True, default=0)
    trims_missing = models.IntegerField(null=True, blank=True, default=0)
    bartack_missing = models.IntegerField(null=True, blank=True, default=0)
    label_stitch_wrong_panel = models.IntegerField(null=True, blank=True, default=0)
    others_1 = models.IntegerField(null=True, blank=True, default=0)
    others_2 = models.IntegerField(null=True, blank=True, default=0)
    broken = models.IntegerField(null=True, blank=True, default=0)
    pleat = models.IntegerField(null=True, blank=True, default=0)
    open_seam = models.IntegerField(null=True, blank=True, default=0)
    damage_1 = models.IntegerField(null=True, blank=True, default=0)
    damage_2 = models.IntegerField(null=True, blank=True, default=0)
    needle_mark = models.IntegerField(null=True, blank=True, default=0)
    run_off_stitch = models.IntegerField(null=True, blank=True, default=0)
    high_low = models.IntegerField(null=True, blank=True, default=0)
    bad_tension = models.IntegerField(null=True, blank=True, default=0)
    puckering = models.IntegerField(null=True, blank=True, default=0)
    uneven = models.IntegerField(null=True, blank=True, default=0)
    bias = models.IntegerField(null=True, blank=True, default=0)
    skip = models.IntegerField(null=True, blank=True, default=0)
    twisted = models.IntegerField(null=True, blank=True, default=0)
    fabric_loose = models.IntegerField(null=True, blank=True, default=0)
    fabric_catch = models.IntegerField(null=True, blank=True, default=0)
    zipper_wavy = models.IntegerField(null=True, blank=True, default=0)
    raw_edge = models.IntegerField(null=True, blank=True, default=0)
    out_of_tolerance = models.IntegerField(null=True, blank=True, default=0)
    oil = models.IntegerField(null=True, blank=True, default=0)
    soilage = models.IntegerField(null=True, blank=True, default=0)
    uncut_thread = models.IntegerField(null=True, blank=True, default=0)
    number_mark = models.IntegerField(null=True, blank=True, default=0)
    dirty_spot = models.IntegerField(null=True, blank=True, default=0)
    color_bleed = models.IntegerField(null=True, blank=True, default=0)
    others_defects = models.IntegerField(null=True, blank=True, default=0)

    total_defect_points = models.IntegerField(null=True, blank=True)
    dhu_shell_line = models.FloatField(null=True, blank=True)
    total_defect_pcs = models.IntegerField(null=True, blank=True)
    defective_shell = models.IntegerField(null=True, blank=True)

    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.month} - {self.date} - {self.buyer} - {self.style}"

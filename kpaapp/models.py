from django.db import models




class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=50, unique=True)
    submitted_by = models.CharField(max_length=50)
    submitted_date = models.DateField()

    tread_diameter_new = models.CharField(max_length=100)
    last_shop_issue_size = models.CharField(max_length=100)
    condemning_dia = models.CharField(max_length=100)
    wheel_gauge = models.CharField(max_length=100)
    variation_same_axle = models.CharField(max_length=50)
    variation_same_bogie = models.CharField(max_length=50)
    variation_same_coach = models.CharField(max_length=50)
    wheel_profile = models.CharField(max_length=100)
    intermediate_wwp = models.CharField(max_length=100)
    bearing_seat_diameter = models.CharField(max_length=100)
    roller_bearing_outer_dia = models.CharField(max_length=100)
    roller_bearing_bore_dia = models.CharField(max_length=100)
    roller_bearing_width = models.CharField(max_length=100)
    axle_box_housing_bore_dia = models.CharField(max_length=100)
    wheel_disc_width = models.CharField(max_length=100)

    def __str__(self):
        return self.form_number



class BogieChecksheet(models.Model):
    form_number = models.CharField(max_length=50, unique=True)
    inspection_by = models.CharField(max_length=50)
    inspection_date = models.DateField()
    bogie_no = models.CharField(max_length=50)
    maker_year_built = models.CharField(max_length=50)
    incoming_div_and_date = models.CharField(max_length=50)
    deficit_components = models.CharField(max_length=100)
    date_of_ioh = models.DateField()
    bogie_frame_condition = models.CharField(max_length=50)
    bolster = models.CharField(max_length=50)
    bolster_suspension_bracket = models.CharField(max_length=50)
    lower_spring_seat = models.CharField(max_length=50)
    axle_guide = models.CharField(max_length=50)
    cylinder_body = models.CharField(max_length=50)
    piston_trunnion = models.CharField(max_length=50)
    adjusting_tube = models.CharField(max_length=50)
    plunger_spring = models.CharField(max_length=50)

    def __str__(self):
        return self.form_number

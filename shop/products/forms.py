from django import forms


COLOR_CHOICES = (
    ("RED", "Red"),
    ("GREEN", "Green"),
    ("BLUE", "Blue"),
    ("WHITE", "White"),
)
class AddProduct(forms.Form):
    car_name = forms.CharField(max_length=255)
    model_name = forms.CharField(max_length=255)
    price_per_hour = forms.IntegerField(min_value=1, required=False)
    Description = forms.CharField(max_length=255)
    color = forms.ChoiceField(choices=COLOR_CHOICES)

from django import forms
from .models import User_detail, Pass_keyword

class UserdetailForm(forms.ModelForm):

    class Meta:
        model = User_detail
        fields = ['age','residence','gender','allergies']
    
class PasskeywordForm(forms.ModelForm):
    
    class Meta:
        model = Pass_keyword
        fields = ['pass_keyword']
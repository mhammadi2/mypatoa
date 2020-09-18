from django import  forms
from  .models import Claimset

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claimset
        fields = ['patno','pubno','add112','obj']
        labels = {'patno':'Application No.', 'pubno':'Publication No.', 'add112':'112para', 'obj':'Objection'}
        #initial_fields = ['patno', 'pubno', 'add112', 'obj']
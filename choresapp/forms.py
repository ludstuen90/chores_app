from django import forms
from models import Chore

class ChoresForm(forms.Form):

    chores_options = Chore.objects.values_list('id', 'chore_name')

    chores = forms.ChoiceField(label='Chore Completed', choices= chores_options, widget=forms.RadioSelect)
    print('Chore options are: ', chores)

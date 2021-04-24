import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class BorrowRequestForm(forms.Form):
    return_date = forms.DateField(
        help_text='Enter a date (yyyy-mm-dd) between today and 2 weeks (default = 1 week) ', 
        widget=forms.DateInput, 
        initial=datetime.date.today() + datetime.timedelta(weeks=1)
    )

    def clean_return_date(self):
        data = self.cleaned_data['return_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - return date before today\'s date'))

        if data > datetime.date.today() + datetime.timedelta(weeks=2):
            raise ValidationError(_('Invalid date - return date more than 2 weeks ahead of issue date'))

        return data
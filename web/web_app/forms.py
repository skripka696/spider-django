from django import forms
from web.settings import SPIDERS


class StartSpiderForm(forms.Form):
    SPIDER_CHOICES = SPIDERS
    spider = forms.ChoiceField(choices=SPIDERS)
    redis_key1 = forms.CharField(max_length=255, required=False)
    redis_key2 = forms.CharField(max_length=255, required=False)
    redis_key3 = forms.CharField(max_length=255, required=False)

    def __init__(self):
        super(StartSpiderForm, self).__init__()
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
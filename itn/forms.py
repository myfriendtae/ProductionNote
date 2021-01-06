from django import forms
from .models import DayEvent, NightEvent, UploadFile
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class DayForm(forms.ModelForm):
    day_content = forms.CharField(required=False, widget=CKEditorUploadingWidget())
    editor = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'editor'}))
    class Meta:
        model = DayEvent
        fields = ['day_content', 'editor']
        

class NightForm(forms.ModelForm):
    night_content = forms.CharField(required=False, widget=CKEditorUploadingWidget())
    editor = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'editor'}))
    class Meta:
        model = NightEvent
        fields = ['night_content', 'editor']

class UploadFileForm(forms.ModelForm):
    file = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'multiple': False}))
    class Meta:
        model = UploadFile
        fields = ['file']
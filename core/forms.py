from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class' : 'form-control input_search',
        "id" : "search",
        "placeholder" : "Поиск",
        "autocomplete" : "off"
    }))
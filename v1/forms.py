from django import forms


class ColabForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام', 'style': 'width: 300px; text-align : center;', 'class': 'form-control'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'شماره همراه', 'style': 'width: 300px; text-align : center;', 'class': 'form-control'}))
    code_melli = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'کد ملی', 'style': 'width: 300px; text-align : center;', 'class': 'form-control'}))



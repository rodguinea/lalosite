from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    affair = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=True)


class ProjectsInlineForm(forms.ModelForm):
    '''ElectroporationConditionsForm.  Used to size the text input boxes'''
    class Meta:
        widgets = {'language': forms.Select(), 'title': forms.TextInput(attrs={'class': 'input_sm'}), 'image': forms.ClearableFileInput(), 'video': forms.TextInput(attrs={'class': 'input_sm'}), 'description': forms.Textarea(attrs={'class': 'text_sm'}), 'is_principal': forms.CheckboxInput(), 'is_shown': forms.CheckboxInput(), 'order': forms.NumberInput(attrs={'class': 'input_number'})
                   }

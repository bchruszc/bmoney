from django import forms

class OFXForm(forms.Form):
    ofxfile = forms.FileField(
        label='Select a file'
    )
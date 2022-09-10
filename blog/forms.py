from django import forms
from .models import Post, TwitterProfile

class PostForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(atrrs={'class':'form-control', 'placeholder':'Enter your title'}))
    # content = forms.CharField(widget=forms.TextInput(atrrs={'class':'form-control', 'placeholder':'Enter your content', 'row':10}))

    # go to your html form and replace your input with {{form.title}}


    class Meta():
        model = Post
        fields = ('title','content')

class TwitterProfileForm(forms.ModelForm):

    class Meta():
        model = TwitterProfile
        fields = ('comment',)


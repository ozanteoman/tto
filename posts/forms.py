from django import forms
from .models import Posts,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields=['title','content','image']

    def __init__(self,*args,**kwargs):
        super(PostForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={"class":"form-control"}

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comments
        fields=['content']

from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=("author", "title", "text")

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
    # the css styling of class textinputclass will be applied only to the title
    # and the styling of classes editable medium-editor-textarea postcontent will bw applied to text widget
# attrs contain the css classes
class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=("author", "text")
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

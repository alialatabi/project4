from django import forms


class PostForm(forms.Form):
    New_Post = forms.Field(widget=forms.Textarea(
        {'rows': '4', 'maxlength': 255, 'class': 'form-control',
         'placeholder': "For The Love Of God Post Something 😪"}), label="New Post",
        required=True)

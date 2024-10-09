from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'text', 'rate']  # 必要なフィールドを指定
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトル'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'レビューを書く'}),
            'rate': forms.Select(attrs={'class': 'form-control'}),
        }
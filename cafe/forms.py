from django import forms
from .models import PreOrder, Review

class PreOrderForm(forms.ModelForm):
    class Meta:
        model = PreOrder
        fields = ['customer_name', 'phone', 'email', 'pickup_time']
        widgets = {
            'pickup_time': forms.Select(attrs={
                'class': 'glass-input',
                'style': 'background: rgba(255,255,255,0.1); border: 2px solid var(--neon-pink); color: white; padding: 15px; border-radius: 15px;'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'glass-input',
                'placeholder': 'Ваше имя',
                'style': 'background: rgba(255,255,255,0.1); border: 2px solid var(--neon-pink); color: white; padding: 15px; border-radius: 15px;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'glass-input', 
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'style': 'background: rgba(255,255,255,0.1); border: 2px solid var(--neon-blue); color: white; padding: 15px; border-radius: 15px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'glass-input',
                'placeholder': 'your@email.com',
                'style': 'background: rgba(255,255,255,0.1); border: 2px solid var(--neon-green); color: white; padding: 15px; border-radius: 15px;'
            }),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'text', 'rating', 'image']
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'glass-input',
                'placeholder': 'Ваше имя',
                'style': 'background: rgba(255,255,255,0.1); border: 2px solid var(--neon-pink); color: white; padding: 15px; border-radius: 15px;'
            }),
            'text': forms.Textarea(attrs={
                'class': 'glass-input',
                'placeholder': 'Ваш отзыв...', 
                'rows': 4,
                'style': 'background: rgba(255,255,255,0.1); border: 2px solid var(--neon-blue); color: white; padding: 15px; border-radius: 15px;'
            }),
            'rating': forms.RadioSelect(choices=[(i, '⭐' * i) for i in range(1, 6)]),
            'image': forms.FileInput(attrs={
                'class': 'glass-input-file',
                'style': 'background: rgba(255,255,255,0.1); border: 2px dashed var(--neon-green); color: white; padding: 15px; border-radius: 15px;'
            }),
        }
from django import forms
from django.core.validators import FileExtensionValidator
from django.forms import ClearableFileInput

from .models import Product
from .validators import validate_file_size


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']
        widgets = {
            'image': ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/jpeg,image/png',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].validators.append(
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        )
        self.fields['image'].validators.append(validate_file_size)

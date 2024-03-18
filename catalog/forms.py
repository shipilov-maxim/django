from django import forms
from catalog.models import Blog, Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('creator',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        wrong = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                 'бесплатно', 'обман', 'полиция', 'радар']
        for word in wrong:
            if word in cleaned_data:
                raise forms.ValidationError('Название содержит недопустимое слово')
        return cleaned_data

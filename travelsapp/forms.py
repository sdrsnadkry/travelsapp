from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from django import forms
from .models import Section, Category, Packages, Bookings, Blogs


class DateInput(forms.DateInput):
    input_type = 'date'


class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter Your Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter Your Password'
    }))


class ContactForm(forms.Form):
    email = forms.CharField()


class SectionAddForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"
        widgets = {
            'section_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Section Name Here...'
            }),
            'section_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Section Url Here'
            }),
            'section_desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Section Description Here'
            })

        }


class CategoryAddForm(forms.ModelForm):
    parent_category = forms.ModelChoiceField(required=False, widget=forms.Select(attrs={
        'class': 'form-control',
    }),
        queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'section': forms.Select(attrs={
                'class': 'form-control',
            }),
            'parent_category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'category_url': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'category_desc': SummernoteWidget(),
            'meta_tags': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }


class PackageAddForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),
        queryset=Category.objects.all())

    class Meta:
        model = Packages
        fields = "__all__"
        widgets = {
            'section': forms.Select(attrs={
                'class': 'form-control',
            }),
            'package_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'package_url': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'package_price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'package_discount': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'package_overview': SummernoteWidget(),
            'package_itinerary': SummernoteWidget(),
            'meta_tags': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }


class PackageBookForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['package_name', 'fullname', 'email', 'address',
                  'phone', 'count', 'date', 'pickup', 'message']
        widgets = {
            'package_name': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required ',
                'placeholder': 'Enter Your Name Here...',
                'type': 'hidden'

            }),
            'fullname': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required ',
                'placeholder': 'Enter Your Name Here...',

            }),
            'email': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email ',
                'placeholder': 'Enter Your Email Here...',

            }),
            'address': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required  ',
                'placeholder': 'Enter Your Address Here...',

            }),
            'phone': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required  ',
                'placeholder': 'Phone Number',

            }),
            'date': DateInput(),
            'count': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required  ',
                'placeholder': 'Number of Persom',

            }),
            'pickup': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required  ',
                'placeholder': 'Where Should We Pick You ?',

            }),
            'message': forms.TextInput(attrs={
                'class': ' wpcf7-form-control wpcf7-text  wpcf7-validates-as-required  ',
                'placeholder': 'Anything We can Help?',

            }),

        }


class BlogAddForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Date':  DateInput(),
            'content': SummernoteWidget(),

        }

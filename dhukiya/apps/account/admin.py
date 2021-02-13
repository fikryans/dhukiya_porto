from django.contrib import admin
from .models import Account, Divisi
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username','email','first_name','last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords didn't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = Account
        fields = ('username','email','first_name','last_name')

    def clean_password(self):
        return self.initial["password"]


class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('username','email','date_joined','last_login','is_admin','is_staff')
    list_filter = ('is_admin','is_staff',) 
    filter_horizontal = ()
    
    fieldsets = (None,{'fields': ('username','email','first_name','last_name','profile_pic','role','about_me','facebook','twitter','instagram','website','is_admin','is_staff','is_active','password',)}),
   

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','first_name','last_name','profile_pic','role','about_me','facebook','twitter','instagram','website', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','first_name')
    readonly_fields = ('date_joined','last_login')
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(Account, AccountAdmin)

class DivisiAdmin(admin.ModelAdmin):
    list_display = ('div_title','div_descriptions')

admin.site.register(Divisi, DivisiAdmin)

    

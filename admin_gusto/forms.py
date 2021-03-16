from django import forms
from main_gusto.models import Category, Dish


class FormMessage(forms.ModelForm):
    title = forms.CharField(max_length=50,
                                widget=forms.TextInput(
                                    attrs={"type": "text", "id": "name", "class": "form-control", "placeholder": "Имя",
                                           "required": "required"}))
    user_name = forms.CharField(max_length=20,
                                   widget=forms.Textarea(
                                       attrs={"name": "name", "id": "name", "class": "form-control", "rows": "1",
                                              "placeholder": "Имя", "required": " required"}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={"type": "email", "id": "email", "class": "form-control", "placeholder": "Email",
                                      "required": "required"}))
    user_message = forms.CharField(max_length=400,
                                   widget=forms.Textarea(
                                       attrs={"name": "message", "id": "message", "class": "form-control", "rows": "4",
                                              "placeholder": "Сообщение", "required": " required"}))

    class Meta:
        model = Category
        fields = ("title", "photo","category_order","is_visible")


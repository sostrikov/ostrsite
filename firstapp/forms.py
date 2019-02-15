from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Вася Пупкин")
    age = forms.IntegerField(label="Возраст", initial=18)
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea, initial="Вася Пупкин - народный герой")
    field_order = ["name", "age", "comment"]











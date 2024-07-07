from django import forms
from course_app.models import Course


class CourseForm(forms.ModelForm):
    name = forms.CharField(
        label='Название курса',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    description = forms.CharField(
        label='Описание курса',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    start_date = forms.DateField(
        label='Дата старта курса',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    end_date = forms.DateField(
        label='Дата окончания курса',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Course
        fields = '__all__'

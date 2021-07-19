    from django.forms import ModelForm
    from .models import Institution

    class InstitutionAddForm(ModelForm):
        class Meta:
            model = Institution
            exclude = ['representative']







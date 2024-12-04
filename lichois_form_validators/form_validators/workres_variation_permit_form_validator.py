from ..form_validator import FormValidator
from django.core.exceptions import ValidationError

class WorkResVariationPermitFormValidator(FormValidator):

    def clean(self):

        cleaned_data = self.cleaned_data

        new_company =cleaned_data.get('new_company_name')
        if (new_company and not cleaned_data.get('new_company_location')):

            msg = {'new_company_name':
                    'Company location must be provided for: '
                    f'{new_company}'}

            self._errors.update(msg)
            raise ValidationError(msg)

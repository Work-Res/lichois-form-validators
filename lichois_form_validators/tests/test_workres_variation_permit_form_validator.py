from ..form_validators import WorkResVariationPermitFormValidator
from .models import Permit,VariationPermit
from django.test import TestCase, tag
from django.core.exceptions import ValidationError

@tag('permit')
class TestWorkResVariationPermitForm(TestCase):

    def setUp(self):

        self.existing_permit = Permit.objects.create(
            permit_type='test',
            permit_no= '1234')

        self.variation_permit = VariationPermit.objects.create(
            existing_permit=self.existing_permit)

    @tag('variation')
    def test_valid_permit_form(self):
        cleaned_data = {
            'existing_permit': self.existing_permit,
            'new_company_name': 'Test',
            'new_company_location': 'Test Location',
        }
        form_validator = WorkResVariationPermitFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised for a valid form.Got{e}')

    @tag('variation_invalid')
    def test_invalid_permit_form(self):
        cleaned_data = {
            'existing_permit': self.existing_permit,
            'contact_type': 'phone_call',
            'new_company_name': 'Test',
            'new_company_location': '',

        }

        form_validator = WorkResVariationPermitFormValidator(
            cleaned_data=cleaned_data)

        with self.assertRaises(ValidationError) as ctx:
            form_validator.validate()

        self.assertIn('new_company_name', ctx.exception.message_dict)
        self.assertEqual(ctx.exception.message_dict['new_company_name'][0],
                         'Company location must be provided for: Test')

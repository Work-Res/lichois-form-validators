from django.forms import ValidationError
from lichois_constants.constants import OTHER

from .base_form_validator import BaseFormValidator, NOT_REQUIRED_ERROR, REQUIRED_ERROR


class OtherSpecifyFieldValidator(BaseFormValidator):
    """A modelform mixin that handles 'OTHER/Other specify'
    field pattern.
    """

    def validate_other_specify(self, field, other_specify_field=None,
                               required_msg=None, not_required_msg=None,
                               other_stored_value=None,
                               ref=None, **kwargs):
        """Returns False or raises a ValidationError.
        """
        cleaned_data = self.cleaned_data
        other = other_stored_value or OTHER

        # assume field naming convention
        if not other_specify_field:
            other_specify_field = f'{field}_other'

        if (cleaned_data.get(field)
                and cleaned_data.get(field) == other
                and not cleaned_data.get(other_specify_field)):
            ref = '' if not ref else f' ref: {ref}'
            message = {
                other_specify_field:
                required_msg or f'This field is required.{ref}'}
            self._errors.update(message)
            self._error_codes.append(REQUIRED_ERROR)
            raise ValidationError(message, code=REQUIRED_ERROR)
        elif (cleaned_data.get(field)
                and cleaned_data.get(field) != other
                and cleaned_data.get(other_specify_field)):
            ref = '' if not ref else f' ref: {ref}'
            message = {
                other_specify_field:
                not_required_msg or f'This field is not required.{ref}'}
            self._errors.update(message)
            self._error_codes.append(NOT_REQUIRED_ERROR)
            raise ValidationError(message, code=NOT_REQUIRED_ERROR)
        return False

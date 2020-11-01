from django.core.exceptions import ValidationError


def time_validator(value):
    if value <= 0:
        raise ValidationError('Time cannot be zero or negative')

from django.core.exceptions import ValidationError
import re

VALIDATE_CHARS_EXCEPTION_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."


def validate_username_chars(value):
    pattern = "^[A-Za-z0-9_-]*$"
    string = value
    state = bool(re.match(pattern, string))
    if not state:
        raise ValidationError(VALIDATE_CHARS_EXCEPTION_MESSAGE)


def validate_age(value):
    if value < 0:
        raise ValidationError


def validate_price(value):
    if value < 0.0:
        raise ValidationError

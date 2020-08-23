from wtforms.validators import ValidationError

from snakeeyes.blueprints.user.models import User


def ensure_identity_exists(form, field):
    """
    Ensure an indentity exists.

    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """
    user = User.find_by_identity(field.data)

    if not user:
        raise ValidationError('Unable to locate account')


def ensure_existing_password_matches(form, field):
    """
    Ensure that the current password matches their existing password.

    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """
    user = User.query.get(form._obj.id)

    if not user.authenticated(password=field.data):
        raise ValidationError('Does not match.')


def ensure_new_password_matches(form, field, original_field):
    """
    Ensures that the new password matches the confirmation to prevent
    the user from needing to submit a password reset if they entered
    the new password incorrectly.
    
    :param form: wtforms Instance
    :param field: Field being passed in
    :param original_field: Field to confirm
    :return: None
    """
    user = User.query.get(form._obj.id)
    
    if not field.data == '':
        if not field.data == original_field.data:
            raise ValidationError('New passwords do not match.')

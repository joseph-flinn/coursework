from lib.flask_mailplus import send_template_message
from snakeeyes.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_feedback_email(email, overall_experience,
                           playing_experience, account_experience,
                           concerns):
    """
    Send a feedback email.

    :param email: E-mail address of the vistior
    :type email: str
    :param overall_experience: Overall experience of the visitor
    :type overall_experience: str
    :param playing_experience: Playing experience of the visitor
    :type playing_experience: str
    :param account_experience: Account experience of the visitor
    :type account_experience: str
    :param concerns: Feedback concerns of the visitor
    :type concerns: str
    :return: None
    """
    ctx = {
        'email': email,
        'overall_experience': overall_experience,
        'playing_experience': playing_experience,
        'account_experience': account_experience,
        'concerns': concerns
    }

    send_template_message(subject='[Snake Eyes] Feedback',
                          sender=email,
                          recipients=[celery.conf.get('MAIL_USERNAME')],
                          reply_to=email,
                          template='feedback/mail/index', ctx=ctx)

    return None

import pytest

from snakeeyes.extensions import mail
from snakeeyes.blueprints.feedback.tasks import deliver_feedback_email


class TestFeedBackTasks:
    @pytest.mark.skip(reason='Two-Factor Auth on gmail account')
    def test_deliver_support_email(self):
        """ Deliver a feedback email. """
        form = {
            'email': 'foo@bar.com',
            'overall_experience': 'good',
            'playing_experience': 'good',
            'account_experience': 'good',
            'concerns': 'Test concerns'
        }

        with mail.record_messages() as outbox:
            deliver_feedback_email(
                form.get('email'),
                form.get('overall_experience'),
                form.get('playing_experience'),
                form.get('account_experience'),
                form.get('concerns')
            )

            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body

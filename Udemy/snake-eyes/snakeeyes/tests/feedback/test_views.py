import pytest
from flask import url_for

from lib.tests import assert_status_with_message


class TestFeedback:
    def test_feedback_page(self, client):
        """ Feedback page should respond with a success 200. """
        response = client.get(url_for('feedback.index'))
        assert response.status_code == 200

    @pytest.mark.skip(reason='Server name config messing this up since not localhost')
    def test_feedback_form(self, client):
        """ Feedback form should redirect with a message. """
        form = {
            'email': 'foo@bar.com',
            'overall_experience': 'good',
            'playing_experience': 'good',
            'account_experience': 'good',
            'concerns': 'Test concerns'
        }

        response = client.post(url_for('feedback.index'), data=form,
                               follow_redirect=True)
        assert_status_with_message(200, response, 'Thanks')

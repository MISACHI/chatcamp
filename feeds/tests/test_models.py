import pytest
from mixer.backend.django import mixer

from datetime import datetime
from uuid import UUID

pytestmark = pytest.mark.django_db


class TestFeed:
    @pytest.fixture
    def db_data(self):
        obj = mixer.blend('feeds.Feed')
        return obj

    def test_feed(self, db_data):
        feed_obj = db_data
        assert isinstance(feed_obj.feeds_id, UUID) == 1, 'Should check if database is in working as expected'
        assert type(feed_obj.time_updated) is datetime, 'Should verify datetime field'

    def test_user_feeds(self, db_data):
        feed_obj = db_data
        assert isinstance(feed_obj.get_user_feeds(datetime.today())[0].feeds_id, UUID) is True, \
            'Should check method return valid data if parameter is passed'
        assert feed_obj.get_user_feeds().exists() is False, \
            'Should check method returns valid data if parameter is not passed'

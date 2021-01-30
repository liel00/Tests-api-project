import datetime

import pytest

from pageObjects.userObjects import UserObjects


class TestDelete:
    @pytest.mark.delete
    def test_delety(self):
        "Deletes user number 1 and checks the status and response time"
        r = UserObjects()
        res = r.delete_user()
        assert res.status_code == 200
        t = res.elapsed
        assert t < datetime.timedelta(seconds=10)

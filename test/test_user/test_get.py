import datetime
import json

import pytest

from pageObjects.userObjects import UserObjects


class TestGet:
    @pytest.mark.get
    def test_get(self):
        "Retrieves user number 1 and checks the status and response time parameters"
        r = UserObjects()
        res = r.get_user()
        assert res.status_code == 200
        dic_response = json.loads(res.text)
        assert dic_response[0]['username'] == 'Bret'
        assert dic_response[0]['address']['city'] == 'Gwenborough'
        assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        t = res.elapsed
        assert t < datetime.timedelta(seconds=10)

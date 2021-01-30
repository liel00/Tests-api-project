import datetime
import json

import pytest

from pageObjects.userObjects import UserObjects
from utilites.jsonData.jsonDataUser import JsonData


class TestPost:
    @pytest.mark.post
    def test_post(self):
        "Submit a new user Check parameters and status time response headers"
        r = UserObjects()
        res = r.post_user()
        assert res.status_code == 201
        res_json = json.loads(res.text)
        assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert res.headers['Connection'] == 'keep-alive'
        assert res_json == JsonData.post_user_res
        print(res_json)
        t = res.elapsed
        assert t < datetime.timedelta(seconds=10)

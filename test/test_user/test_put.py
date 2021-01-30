import datetime
import json

import pytest

from pageObjects.userObjects import UserObjects
from utilites.jsonData.jsonDataUser import JsonData


class TestPut:
    @pytest.mark.put
    def test_put(self):
        "Change user status status and response time parameters"
        r = UserObjects()
        res = r.put_user()
        assert res.status_code == 200
        dic_response = json.loads(res.text)
        print(dic_response)
        assert JsonData.put_user_res == dic_response
        t = res.elapsed
        assert t < datetime.timedelta(seconds=10)

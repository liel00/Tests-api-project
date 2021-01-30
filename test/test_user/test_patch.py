import datetime
import json

import pytest

from pageObjects.userObjects import UserObjects


class Testpatch:
    @pytest.mark.patch
    def test_patch(self):
        "Checking the corrected username status and response time"
        r = UserObjects()
        res = r.patch_user()
        assert res.status_code == 200
        dic_response = json.loads(res.text)
        assert dic_response['name'] == 'Leanne Graham'
        assert dic_response['username'] == 'mamba'
        t = res.elapsed
        assert t < datetime.timedelta(seconds=10)

import json
import pytest
import re
from Utils.requests_util import RequestUtil
from Utils.yaml_util import YamlUtil


class Testsend:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('get_token.yml'))
    def test_start(self, caseinfo):
        print(caseinfo['name'])
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        req = RequestUtil().send_request(method=method, url=url, data=None)
        YamlUtil().set_state_yaml('login.yml', re.search('name="csrf_token" value="(.*?)"', req)[1])
        print(re.search('name="csrf_token" value="(.*?)"', req)[1])

    @pytest.mark.run(order=2)
    @ pytest.mark.parametrize('casecinfo', YamlUtil().read_testcase_yaml('loginresult.yml'))
    def test_login(self, casecinfo):
        print(casecinfo['request']['data']['csrf_token'])
        url = casecinfo['request']['url']
        method = casecinfo['request']['method']
        data = casecinfo['request']['data']
        headers = casecinfo['request']['headers']
        req = RequestUtil().send_request(method=method, url=url, data=data, headers=headers)
        result = json.loads(req)
        # print(result)



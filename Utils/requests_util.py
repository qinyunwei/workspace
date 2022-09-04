import json

import requests


class RequestUtil:

    # 类变量：通过类名访问
    session = requests.session()


    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        rep = None
        if method == 'get':
            rep = RequestUtil.session.request(method, url=url, params=data, **kwargs)

        elif method == 'post':
            data = json.dumps(data)
            rep = RequestUtil.session.request(method, url=url, data=data, **kwargs)

        elif method == 'put':
            pass

        else:
            data = json.dumps(data)
            rep = RequestUtil.session.request(method, url=url, data=data, **kwargs)

        return rep.text

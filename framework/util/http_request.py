# coding=utf-8
import os
import requests

from framework.util.log import Log


class HttpRequest:

    def __init__(self, host, port=-1, timeout=60, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}):
        self.host = host
        self.timeout = timeout
        self.headers = headers
        self.port = port;

        if port == -1:
            if host.startswith("https"):
                self.port = 443
            else:
                self.port = 80

    # defined http get method
    def get(self, api, params):
        url = "%s:%d/%s" % (self.host, self.port, api)
        try:
            resp = requests.get(url, headers=self.headers, params=params, timeout=float(self.timeout), verify=False)
            resp.raise_for_status()
            Log.i("response code: " + str(resp.status_code))
            return resp
        except TimeoutError:
            Log.e("Time out!")
            return None
        except requests.RequestException as e:
            Log.e("RequestException: " + str(e))
            return None

    # defined http post method
    def post(self, api, data):
        url = "%s:%d/%s" % (self.host, self.port, api)
        Log.i("request url: " + url)
        try:
            resp = requests.post(url, headers=self.headers, data=data,
                                 timeout=float(self.timeout), verify=False)
            resp.raise_for_status()
            Log.i("response code: " + str(resp.status_code))
            return resp
        except TimeoutError:
            Log.e("Time out!")
            return None
        except requests.RequestException as e:
            Log.e("RequestException: " + str(e))
            return None


if __name__ == "__main__":
    req = HttpRequest(host="https://cn.bing.com")
    resp = req.get("search", {"q": "python+requests"})
    fd = open(os.path.join(os.getcwd(), "bing.html"), "w");
    fd.write(str(resp.text))
    fd.close()

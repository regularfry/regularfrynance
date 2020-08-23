# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/regularfry/regularfrynance
#
# Copyright 2020 Alex Young
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests as _requests
from . import utils


class Remote:
    # Unlike elsewhere in the library, proxy must be a single str here, not
    # a dict, and it must be an HTTPS proxy.  This was being forced elsewhere
    # anyway, so I don't believe there's anything controversial here.
    def __init__(self, proxy=None):
        self._proxy = {"https": proxy}

    def get(self, url):
        return utils.get(url, proxy=self._proxy)

    def get_json_from_html(self, url):
        return utils.get_json(url, proxy=self._proxy)

    def request(self, **kwargs):
        return _requests.get(proxies=self._proxy, **kwargs)

    def is_available(self, url):
        response = _requests.head(url=url, proxies=self._proxy)
        return response.ok

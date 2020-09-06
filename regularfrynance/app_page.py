#!/usr/bin/env python
#
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

import re as _re

try:
    import ujson as _json
except ImportError:
    import json as _json

from .path_lens import path_lens


class AppPage:
    def __init__(self, html):
        self._html = html
        self._store_lens = path_lens('context.dispatcher.stores.QuoteSummaryStore')

    def json_str(self):
        return _re.search(r'root.App.main =(.*);', self._html)[1]

    def app_state(self):
        return _json.loads(self.json_str())

    def quote_summary_store(self):
        return self._store_lens.get()(self.app_state())

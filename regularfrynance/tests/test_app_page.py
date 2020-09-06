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

import json as _json

from regularfrynance.app_page import AppPage
from regularfrynance.path_lens import path_lens

class TestAppPage:
    def test_extract_app_state(self):
        html = """
        <html>
          <head>
            <title>noisenoisenoise</title>
            <script>
              nonsense();
            </script>
            <script>
              root.App.main = {"target":"find this please"};
            </script>
          </head>
        </html>
        """
        assert AppPage(html).app_state() == {"target":"find this please"};

    def test_extract_quote_summary_store(self):
        store = {"target": "find this please"}
        lens = path_lens("context.dispatcher.stores.QuoteSummaryStore")
        nested_obj = lens.set(store)({})
        html = f"""
          <script>
            root.App.main = {_json.dumps(nested_obj)};
          </script>
        """

        assert AppPage(html).quote_summary_store() == store

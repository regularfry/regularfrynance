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

from regularfrynance.ticker_urls import TickerUrls


class TestTickerUrls:
    def test_chart_url(self):
        urls = TickerUrls("0000")

        expected = "https://query1.finance.yahoo.com/v8/finance/chart/0000"
        assert urls.chart_json() == expected

    def test_options(self):
        urls = TickerUrls("0000")

        expected = "https://query1.finance.yahoo.com/v7/finance/options/0000"
        assert urls.options_json() == expected

    def test_options_with_date(self):
        urls = TickerUrls("0000")
        date = "mydate"

        expected = (
            "https://query1.finance.yahoo.com/v7/finance/options/0000?date=mydate"
        )
        assert urls.options_json(date=date) == expected

    def test_data(self):
        urls = TickerUrls("0000")

        expected = "https://finance.yahoo.com/quote/0000"
        assert urls.data_html() == expected

    def test_holders(self):
        urls = TickerUrls("0000")

        expected = "https://finance.yahoo.com/quote/0000/holders"
        assert urls.holders_html() == expected

    def test_financials(self):
        urls = TickerUrls("0000")

        expected = "https://finance.yahoo.com/quote/0000/financials"
        assert urls.financials_html() == expected

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

class TickerUrls:
    def __init__(self, sym):
        self.sym = sym

    def chart(self):
        return "https://query1.finance.yahoo.com/v8/finance/chart/" + self.sym

    def options(self, date=None):
        href = f"https://query1.finance.yahoo.com/v7/finance/options/{self.sym}"
        if date:
            href += "?date=" + date
        return href
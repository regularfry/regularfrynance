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

from functools import reduce

import lenses as _lenses


# This class fills what looks to me like a gap in the lenses library:
# the ability to look up the value of a key on get, and create it if
# it doesn't exist otherwise on set.  Itemlens almost does this, but
# it deals with tuples and I can't figure out what Lens I should be
# composing with it to make that not happen.
class DictKeyLens(_lenses.optics.base.Lens):
    def __init__(self, key):
        self._key = key

    def getter(self, state):
        if state:
            try:
                return state[self._key]
            except (KeyError, TypeError):
                return None

    def setter(self, state, value):
        if isinstance(state, dict):
            data = state.copy()
        else:
            data = {}

        data[self._key] = value
        return data

    def __repr__(self):
        return f"DictKeyLens({self._key})"

def dict_key(path):
    return _lenses.UnboundLens(DictKeyLens(path))

def path_lens(path):
    keys = path.split(".")
    lenses = [dict_key(k) for k in keys]
    result = reduce(lambda a,b: a & b, lenses)
    return result

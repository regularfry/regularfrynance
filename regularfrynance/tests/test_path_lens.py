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

from regularfrynance.path_lens import path_lens, dict_key

class TestDictKey:
    def test_get_value(self):
        lens = dict_key("foo")
        assert lens.get()({"foo": 42}) is 42

    def test_set_existing_key_value(self):
        lens = dict_key("foo")
        assert lens.set(23)({"foo": 42}) == {"foo": 23}

    def test_set_new_key_value(self):
        lens = dict_key("foo")
        assert lens.set(23)({}) == {"foo": 23}

    def test_set_new_key_preserves_other_values(self):
        lens = dict_key("foo")
        assert lens.set(23)({"bar": 1}) == {"foo": 23, "bar": 1}

class TestPathLens:
    def test_simple_key_access(self):
        lens = path_lens("foo")
        obj = {"foo": 42}
        assert lens.get()(obj) == 42
        assert lens.set(23)(obj) == {"foo": 23}
        assert lens.set(23)({}) == {"foo": 23}

    def test_nested_key_access(self):
        lens = path_lens("foo.bar")
        obj = {"foo": {"bar": 42}}
        assert lens.get()(obj) == 42
        assert lens.set(42)(obj) == {"foo": {"bar": 42}}
        assert lens.set(42)({}) == {"foo": {"bar": 42}}

    def test_insert_dict(self):
        lens = path_lens("foo.bar.qux")
        target = {"target": "find me please"}
        obj = {"foo": {"bar": {"qux": target}}}
        assert lens.get()(obj) == target
        replacement = {"target": "replacement"}
        replaced = lens.set(replacement)(obj)
        assert path_lens("foo.bar.qux.target").get()(replaced) == "replacement"

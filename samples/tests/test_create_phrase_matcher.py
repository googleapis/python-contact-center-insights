# -*- coding: utf-8 -*-
# Copyright 2021 Google LLC
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
import os

from samples import create_phrase_matcher
from samples import delete_phrase_matcher


def test_create_phrase_matcher_phone_or_cellphone(capsys):
    project_id = os.getenv('PROJECT_ID', '')
    assert project_id

    # Create a phrase matcher.
    phrase_matcher = create_phrase_matcher.create_phrase_matcher_phone_or_cellphone(project_id)
    phrase_matcher_name = phrase_matcher.name
    out, err = capsys.readouterr()
    assert "Created a phrase matcher named {}".format(phrase_matcher_name) in out

    # Delete the phrase matcher that we just created.
    delete_phrase_matcher.delete_phrase_matcher(phrase_matcher_name)
    out, err = capsys.readouterr()
    assert "Deleted a phrase matcher named {}".format(phrase_matcher_name) in out


def test_create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery(capsys):
    project_id = os.getenv('PROJECT_ID', '')
    assert project_id

    # Create a phrase matcher.
    phrase_matcher = create_phrase_matcher.create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery(project_id)
    phrase_matcher_name = phrase_matcher.name
    out, err = capsys.readouterr()
    assert "Created a phrase matcher named {}".format(phrase_matcher_name) in out

    # Delete the phrase matcher that we just created.
    delete_phrase_matcher.delete_phrase_matcher(phrase_matcher_name)
    out, err = capsys.readouterr()
    assert "Deleted a phrase matcher named {}".format(phrase_matcher_name) in out

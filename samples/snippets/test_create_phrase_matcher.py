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
import google.auth

from google.cloud import contact_center_insights_v1

import pytest

import create_phrase_matcher


@pytest.fixture
def project_id():
    _, project_id = google.auth.default()
    return project_id


@pytest.fixture
def insights_client():
    return contact_center_insights_v1.ContactCenterInsightsClient()


@pytest.fixture
def phrase_matcher_phone_or_cellphone(project_id, insights_client):
    # Create a phrase matcher.
    phrase_matcher = create_phrase_matcher.create_phrase_matcher_phone_or_cellphone(
        project_id
    )
    yield phrase_matcher

    # Delete the phrase matcher.
    insights_client.delete_phrase_matcher(name=phrase_matcher.name)


@pytest.fixture
def phrase_matcher_phone_or_cellphone_not_shipping_or_delivery(
    project_id, insights_client
):
    # Create a phrase matcher.
    phrase_matcher = create_phrase_matcher.create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery(
        project_id
    )
    yield phrase_matcher

    # Delete the phrase matcher.
    insights_client.delete_phrase_matcher(name=phrase_matcher.name)


def test_create_phrase_matcher_phone_or_cellphone(
    capsys, phrase_matcher_phone_or_cellphone
):
    phrase_matcher = phrase_matcher_phone_or_cellphone
    out, err = capsys.readouterr()
    assert f"Created a phrase matcher named {phrase_matcher.name}" in out


def test_create_phrase_matcher_phone_or_cellphone_not_shipping_or_delivery(
    capsys, phrase_matcher_phone_or_cellphone_not_shipping_or_delivery
):
    phrase_matcher = phrase_matcher_phone_or_cellphone_not_shipping_or_delivery
    out, err = capsys.readouterr()
    assert f"Created a phrase matcher named {phrase_matcher.name}" in out

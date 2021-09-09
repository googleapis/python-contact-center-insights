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

import create_issue_model


@pytest.fixture
def project_id():
    _, project_id = google.auth.default()
    return project_id


@pytest.fixture
def insights_client():
    return contact_center_insights_v1.ContactCenterInsightsClient()


@pytest.fixture
def project_has_enough_conversations(project_id, insights_client):
    # Check if the project has the minimum number of conversations required to create an issue model.
    # See https://cloud.google.com/contact-center/insights/docs/topic-model.
    list_request = contact_center_insights_v1.ListConversationsRequest()
    list_request.page_size = 1000
    list_request.parent = contact_center_insights_v1.ContactCenterInsightsClient.common_location_path(
        project_id, "us-central1"
    )

    min_conversation_count = 10000
    conversation_count = 0
    while conversation_count < min_conversation_count:
        list_response = insights_client.list_conversations(request=list_request)
        if len(list_response.conversations) == 0:
            break
        conversation_count += len(list_response.conversations)

        if not list_response.next_page_token:
            break
        list_request.page_token = list_response.next_page_token

    if conversation_count >= min_conversation_count:
        yield True
    yield False


@pytest.fixture
def issue_model_resource(project_id, insights_client, project_has_enough_conversations):
    if project_has_enough_conversations:
        # Create an issue model.
        issue_model = create_issue_model.create_issue_model(project_id)
        yield issue_model

        # Delete the issue model.
        insights_client.delete_issue_model(name=issue_model.name)
    else:
        yield None


def test_create_issue_model(capsys, issue_model_resource):
    issue_model = issue_model_resource
    if issue_model:
        out, err = capsys.readouterr()
        assert "Created {}".format(issue_model.name) in out

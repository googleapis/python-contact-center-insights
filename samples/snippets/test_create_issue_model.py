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

import create_issue_model


def test_create_issue_model(capsys):
    _, project_id = google.auth.default()

    # Check if the project has the minimum number of conversations required to create an issue model.
    # See https://cloud.google.com/contact-center/insights/docs/topic-model.
    has_minimum_conversation_count = False
    insights_client = contact_center_insights_v1.ContactCenterInsightsClient()
    list_request = contact_center_insights_v1.ListConversationsRequest()
    list_request.parent = contact_center_insights_v1.ContactCenterInsightsClient.common_location_path(project_id,
                                                                                                      "us-central1")
    list_request.page_size = 1000

    # List the first 9,000 conversations.
    next_page_token = ""
    conversation_count = 0
    for i in range(9):
        if next_page_token:
            list_request.page_token = next_page_token
        list_response = insights_client.list_conversations(request=list_request)

        # If there's a next page token, save it for the next run.
        if list_response.next_page_token:
            next_page_token = list_response.next_page_token
            conversation_count += 1000
        else:
            break

    # After 9,000 conversations, list the next 999 conversations if there's a next page token.
    if next_page_token and conversation_count == 9000:
        list_request.page_token = next_page_token
        list_request.page_size = 999
        list_response = insights_client.list_conversations(request=list_request)

        # If there's a next page token after 9,999 conversations, it means that the project has 9,999 conversations
        # and more, which meets the minimum number of conversations required to create an issue model.
        if list_response.next_page_token:
            has_minimum_conversation_count = True

    if has_minimum_conversation_count:
        # Create an issue model.
        issue_model = create_issue_model.create_issue_model(project_id)
        out, err = capsys.readouterr()
        assert "Created {}".format(issue_model.name) in out

        # Delete the issue model.
        insights_client.delete_issue_model(name=issue_model.name)

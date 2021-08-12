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
from google.cloud.contact_center_insights_v1.services.contact_center_insights import async_client
from google.cloud.contact_center_insights_v1.types import resources


# [START contactcenterinsights_create_issue_model]
def create_issue_model(project_id: str) -> resources.IssueModel:
    # Construct a parent resource.
    parent = "projects/{}/locations/us-central1".format(project_id)

    # Construct an issue model.
    issue_model = resources.IssueModel()
    issue_model.display_name = "my-model"

    input_data_config = resources.IssueModel.InputDataConfig()
    input_data_config.medium = resources.Conversation.Medium.CHAT
    issue_model.input_data_config = input_data_config

    # Call the Insights client to create an issue model.
    insights_client = async_client.ContactCenterInsightsClient()
    issue_model_operation = insights_client.create_issue_model(parent=parent, issue_model=issue_model)

    print("Waiting for the operation to complete...")
    issue_model = issue_model_operation.result(timeout=1200)
    print("Created an issue model named {}".format(issue_model.name))
    return issue_model

# [END contactcenterinsights_create_issue_model]

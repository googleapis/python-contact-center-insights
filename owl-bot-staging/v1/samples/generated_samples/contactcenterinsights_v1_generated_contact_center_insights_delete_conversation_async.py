# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteConversation
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-contact-center-insights


# [START contactcenterinsights_v1_generated_ContactCenterInsights_DeleteConversation_async]
from google.cloud import contact_center_insights_v1


async def sample_delete_conversation():
    # Create a client
    client = contact_center_insights_v1.ContactCenterInsightsAsyncClient()

    # Initialize request argument(s)
    request = contact_center_insights_v1.DeleteConversationRequest(
        name="name_value",
    )

    # Make the request
    await client.delete_conversation(request=request)


# [END contactcenterinsights_v1_generated_ContactCenterInsights_DeleteConversation_async]

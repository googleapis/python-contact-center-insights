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
# [START contactcenterinsights_create_conversation]
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client
from google.cloud.contact_center_insights_v1.types import resources


def create_conversation(parent: str, conversation: resources.Conversation) -> resources.Conversation:
    insights_client = client.ContactCenterInsightsClient()
    conversation = insights_client.create_conversation(parent=parent, conversation=conversation)

    print("Created a conversation named {}".format(conversation.name))
    return conversation


# [END contactcenterinsights_create_conversation]

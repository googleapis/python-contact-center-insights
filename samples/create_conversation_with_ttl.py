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
# [START contactcenterinsights_create_conversation_with_ttl]
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client
from google.cloud.contact_center_insights_v1.types import resources
from google.protobuf import duration_pb2


def create_conversation_with_ttl(project_id: str, transcript_uri: str, ttl_seconds: int) -> resources.Conversation:
    # Construct a parent resource.
    parent = client.ContactCenterInsightsClient.common_location_path(project_id, "us-central1")

    # Construct a TTL.
    ttl = duration_pb2.Duration()
    ttl.seconds = ttl_seconds

    # Construct a conversation.
    conversation = resources.Conversation()
    conversation.data_source.gcs_source.transcript_uri = transcript_uri
    conversation.medium = resources.Conversation.Medium.CHAT
    conversation.ttl = ttl

    # Call the Insights client to create a conversation.
    insights_client = client.ContactCenterInsightsClient()
    conversation = insights_client.create_conversation(parent=parent, conversation=conversation)

    print(f"Created a conversation named {conversation.name}")
    return conversation

# [END contactcenterinsights_create_conversation_with_ttl]

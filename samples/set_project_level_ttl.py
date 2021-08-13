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
# [START contactcenterinsights_set_project_level_ttl]
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client
from google.cloud.contact_center_insights_v1.types import resources
from google.protobuf import duration_pb2
from google.protobuf import field_mask_pb2


def set_project_level_ttl(project_id: str, ttl_seconds: int) -> None:
    # Construct a settings resource.
    settings = resources.Settings()
    settings.name = client.ContactCenterInsightsClient.settings_path(project_id, "us-central1")

    conversation_ttl = duration_pb2.Duration()
    conversation_ttl.seconds = ttl_seconds
    settings.conversation_ttl = conversation_ttl

    # Construct an update mask.
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("conversation_ttl")

    # Call the Insights client to set a project-level TTL.
    insights_client = client.ContactCenterInsightsClient()
    insights_client.update_settings(settings=settings, update_mask=update_mask)
    print(f"Set TTL for all incoming conversations to {ttl_seconds} seconds")

# [END contactcenterinsights_set_project_level_ttl]

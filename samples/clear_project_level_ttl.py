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
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client
from google.cloud.contact_center_insights_v1.types import resources
from google.protobuf import field_mask_pb2


def clear_project_level_ttl(project_id: str) -> None:
    # Construct a settings resource.
    settings = resources.Settings()
    settings.name = "projects/{}/locations/us-central1/settings".format(project_id)
    settings.conversation_ttl = None

    # Construct an update mask.
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("conversation_ttl")

    # Call the Insights client to clear the project-level TTL.
    insights_client = client.ContactCenterInsightsClient()
    insights_client.update_settings(settings=settings, update_mask=update_mask)
    print("Cleared TTL for all incoming conversations")

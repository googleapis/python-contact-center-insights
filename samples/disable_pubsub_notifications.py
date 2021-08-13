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


def disable_pubsub_notifications(project_id: str) -> None:
    # Construct a settings resource.
    settings = resources.Settings()
    settings.name = client.ContactCenterInsightsClient.settings_path(project_id, 'us-central1')
    settings.pubsub_notification_settings = {}

    # Construct an update mask.
    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("pubsub_notification_settings")

    # Call the Insights client to disable Pub/Sub notifications.
    insights_client = client.ContactCenterInsightsClient()
    insights_client.update_settings(settings=settings, update_mask=update_mask)
    print("Disabled Pub/Sub notifications")

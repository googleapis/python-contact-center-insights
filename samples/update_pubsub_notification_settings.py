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
# [START contactcenterinsights_update_pubsub_notification_settings]
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client
from google.cloud.contact_center_insights_v1.types import resources
from google.protobuf import field_mask_pb2
from typing import Dict


def update_pubsub_notification_settings(name: str, notification_settings: Dict[str, str]) -> resources.Settings:
    settings = resources.Settings()
    settings.name = name
    for key, value in notification_settings.items():
        settings.pubsub_notification_settings[key] = value

    update_mask = field_mask_pb2.FieldMask()
    update_mask.paths.append("pubsub_notification_settings")

    insights_client = client.ContactCenterInsightsClient()
    settings = insights_client.update_settings(settings=settings, update_mask=update_mask)

    print("Updated pubsub_notification_settings to {}".format(settings.pubsub_notification_settings))
    return settings

# [END contactcenterinsights_update_pubsub_notification_settings]

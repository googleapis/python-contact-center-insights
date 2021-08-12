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
# [START contactcenterinsights_get_operation]
from google.cloud.contact_center_insights_v1.services.contact_center_insights import client
from google.longrunning import operations_pb2


def get_operation(project_id: str, location_id: str, operation_id: str) -> operations_pb2.Operation:
    insights_client = client.ContactCenterInsightsClient()
    operation_name = "projects/{}/locations/{}/operations/{}".format(project_id, location_id, operation_id)
    return insights_client.transport.operations_client.get_operation(operation_name)

# [END contactcenterinsights_get_operation]

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


# [START contactcenterinsights_create_analysis]
def create_analysis(conversation_name: str) -> resources.Analysis:
    # Construct an analysis.
    analysis = resources.Analysis()

    # Call the Insights client to create an analysis.
    insights_client = async_client.ContactCenterInsightsClient()
    analysis_operation = insights_client.create_analysis(parent=conversation_name, analysis=analysis)

    print("Waiting for the operation to complete...")
    analysis = analysis_operation.result(timeout=1200)
    print("Created an analysis named {}".format(analysis.name))
    return analysis

# [END contactcenterinsights_create_analysis]

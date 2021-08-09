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
from google.cloud.contact_center_insights_v1.types import contact_center_insights


# [START contactcenterinsights_export_data_to_bigquery]
def export_data_to_bigquery(project_id: str, data_filter: str, kms_key: str,
                            bigquery_project_id: str, bigquery_dataset: str, bigquery_table: str) -> None:
    # Construct an export request.
    request = contact_center_insights.ExportInsightsDataRequest()
    request.parent = "projects/{}/locations/us-central1".format(project_id)
    request.filter = data_filter
    request.kms_key = kms_key

    destination = contact_center_insights.ExportInsightsDataRequest.BigQueryDestination()
    destination.project_id = bigquery_project_id
    destination.table = bigquery_table
    destination.dataset = bigquery_dataset
    request.big_query_destination = destination

    # Call the Insights client to export data to BigQuery.
    insights_client = async_client.ContactCenterInsightsClient()
    export_operation = insights_client.export_insights_data(request=request)

    print("Waiting for the operation to complete...")
    export_operation.result(timeout=7200)
    print("Exported data to the BigQuery named {}".format(bigquery_table))

# [END contactcenterinsights_export_data_to_bigquery]

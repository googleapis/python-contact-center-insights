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
import os

from samples import export_data_to_bigquery


def test_export_data_to_bigquery():
    project_id = os.getenv('PROJECT_ID', '')
    bigquery_project_id = os.getenv('BIGQUERY_PROJECT_ID', '')
    bigquery_dataset = os.getenv('BIGQUERY_DATASET', '')
    bigquery_table = os.getenv('BIGQUERY_TABLE', '')
    assert project_id
    assert bigquery_project_id
    assert bigquery_dataset
    assert bigquery_table

    export_data_to_bigquery.export_data_to_bigquery(project_id, bigquery_project_id, bigquery_dataset, bigquery_table)

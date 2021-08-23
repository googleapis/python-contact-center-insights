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
import google.auth

from google.cloud import contact_center_insights_v1

import create_issue_model


def test_create_issue_model(capsys):
    _, project_id = google.auth.default()

    # Create an issue model.
    issue_model = create_issue_model.create_issue_model(project_id)
    out, err = capsys.readouterr()
    assert "Created {}".format(issue_model.name) in out

    # Delete the issue model.
    insights_client = contact_center_insights_v1.ContactCenterInsightsClient()
    insights_client.delete_issue_model(name=issue_model.name)

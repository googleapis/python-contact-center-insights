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

from samples import create_issue_model
from samples import delete_issue_model


def test_create_issue_model():
    project_id = os.getenv('PROJECT_ID', '')
    assert project_id

    # Create an issue model then clean up by deleting it,
    issue_model = create_issue_model.create_issue_model(project_id)
    delete_issue_model.delete_issue_model(issue_model.name)

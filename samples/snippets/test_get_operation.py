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

import pytest

import get_operation


@pytest.fixture
def project_id():
    _, project_id = google.auth.default()
    return project_id


def test_get_operation(capsys, project_id):
    # TODO(developer): Replace this placeholder ID with your operation ID.
    operation_id = "12345"

    try:
        operation = get_operation.get_operation(project_id, operation_id)
        out, err = capsys.readouterr()
        if operation.done:
            assert "Operation is done" in out
        else:
            assert "Operation is in progress" in out
    except Exception as e:
        if "not found" in str(e):
            pass
        else:
            raise

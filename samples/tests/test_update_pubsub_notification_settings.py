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

from samples import update_pubsub_notification_settings


def test_update_pubsub_notification_settings(capsys):
    project_id = os.getenv('PROJECT_ID', '')
    assert project_id
    name = "projects/{}/locations/us-central1/settings".format(project_id)

    # Enable notifications for all events.
    notification_settings = {"all-triggers": "projects/my-project/topics/my-topic"}
    update_pubsub_notification_settings.update_pubsub_notification_settings(name, notification_settings)
    out, err = capsys.readouterr()
    assert "Updated pubsub_notification_settings to {}".format(notification_settings) in out

    # Enable notifications for specific events.
    notification_settings = {"create-conversation": "projects/my-project/topics/my-topic",
                             "create-analysis": "projects/my-project/topics/my-other-topic"}
    update_pubsub_notification_settings.update_pubsub_notification_settings(name, notification_settings)
    out, err = capsys.readouterr()
    assert "Updated pubsub_notification_settings to {}".format(notification_settings) in out

    # Clean up notification settings.
    update_pubsub_notification_settings.update_pubsub_notification_settings(name, {})
    out, err = capsys.readouterr()
    assert "Updated pubsub_notification_settings to {}" in out

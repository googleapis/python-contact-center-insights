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

from samples import enable_pubsub_notifications
from samples import disable_pubsub_notifications


def test_enable_pubsub_notifications():
    project_id = os.getenv('PROJECT_ID', '')
    topic_create_conversation = os.getenv('TOPIC_CREATE_CONVERSATION', '')
    topic_create_analysis = os.getenv('TOPIC_CREATE_ANALYSIS', '')
    assert project_id
    assert topic_create_conversation
    assert topic_create_analysis

    # Enable Pub/Sub notifications then clean up by disabling it.
    enable_pubsub_notifications.enable_pubsub_notifications(project_id, topic_create_conversation,
                                                            topic_create_analysis)
    disable_pubsub_notifications.disable_pubsub_notifications(project_id)

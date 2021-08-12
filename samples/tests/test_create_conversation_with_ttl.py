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

from samples import create_conversation_with_ttl
from samples import delete_conversation


def test_create_conversation_with_ttl():
    project_id = os.getenv('PROJECT_ID', '')
    transcript_uri = os.getenv('TRANSCRIPT_URI', 'gs://cloud-samples-data/ccai/chat_sample.json')
    assert project_id

    # Create a conversation then clean up by deleting it.
    conversation = create_conversation_with_ttl.create_conversation_with_ttl(project_id, transcript_uri, 600)
    delete_conversation.delete_conversation(conversation.name)

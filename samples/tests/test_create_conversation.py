# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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

from samples import create_conversation
from samples import delete_conversation
from google.cloud.contact_center_insights_v1.types import resources


def test_create_conversation(capsys):
    project_id = os.getenv('PROJECT_ID', '')
    transcript_uri = os.getenv('TRANSCRIPT_URI', 'gs://example-bucket/some-example.json')

    # Construct the parent resource.
    assert project_id
    parent = "projects/{}/locations/us-central1".format(project_id)

    # Provide a Cloud Storage URI that contains a conversation transcript.
    data_source = resources.ConversationDataSource()
    data_source.gcs_source.transcript_uri = transcript_uri

    # Construct a conversation object.
    conversation = resources.Conversation()
    conversation.medium = resources.Conversation.Medium.CHAT
    conversation.data_source = data_source

    # Create a conversation.
    conversation = create_conversation.create_conversation(parent, conversation)
    conversation_name = conversation.name

    out, err = capsys.readouterr()
    assert "Created a conversation named {}".format(conversation_name) in out

    # Clean up the conversation that we just created.
    delete_conversation.delete_conversation(conversation_name)

    out, err = capsys.readouterr()
    assert "Deleted a conversation named {}".format(conversation_name) in out

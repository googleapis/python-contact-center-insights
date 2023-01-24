# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.cloud.contact_center_insights_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.contact_center_insights import (
    ContactCenterInsightsAsyncClient,
    ContactCenterInsightsClient,
)
from .types.contact_center_insights import (
    BulkAnalyzeConversationsMetadata,
    BulkAnalyzeConversationsRequest,
    BulkAnalyzeConversationsResponse,
    CalculateIssueModelStatsRequest,
    CalculateIssueModelStatsResponse,
    CalculateStatsRequest,
    CalculateStatsResponse,
    ConversationView,
    CreateAnalysisOperationMetadata,
    CreateAnalysisRequest,
    CreateConversationRequest,
    CreateIssueModelMetadata,
    CreateIssueModelRequest,
    CreatePhraseMatcherRequest,
    CreateViewRequest,
    DeleteAnalysisRequest,
    DeleteConversationRequest,
    DeleteIssueModelMetadata,
    DeleteIssueModelRequest,
    DeleteIssueRequest,
    DeletePhraseMatcherRequest,
    DeleteViewRequest,
    DeployIssueModelMetadata,
    DeployIssueModelRequest,
    DeployIssueModelResponse,
    ExportInsightsDataMetadata,
    ExportInsightsDataRequest,
    ExportInsightsDataResponse,
    GetAnalysisRequest,
    GetConversationRequest,
    GetIssueModelRequest,
    GetIssueRequest,
    GetPhraseMatcherRequest,
    GetSettingsRequest,
    GetViewRequest,
    IngestConversationsMetadata,
    IngestConversationsRequest,
    IngestConversationsResponse,
    ListAnalysesRequest,
    ListAnalysesResponse,
    ListConversationsRequest,
    ListConversationsResponse,
    ListIssueModelsRequest,
    ListIssueModelsResponse,
    ListIssuesRequest,
    ListIssuesResponse,
    ListPhraseMatchersRequest,
    ListPhraseMatchersResponse,
    ListViewsRequest,
    ListViewsResponse,
    UndeployIssueModelMetadata,
    UndeployIssueModelRequest,
    UndeployIssueModelResponse,
    UpdateConversationRequest,
    UpdateIssueModelRequest,
    UpdateIssueRequest,
    UpdatePhraseMatcherRequest,
    UpdateSettingsRequest,
    UpdateViewRequest,
)
from .types.resources import (
    Analysis,
    AnalysisResult,
    AnnotationBoundary,
    AnnotatorSelector,
    AnswerFeedback,
    ArticleSuggestionData,
    CallAnnotation,
    Conversation,
    ConversationDataSource,
    ConversationLevelSentiment,
    ConversationParticipant,
    DialogflowIntent,
    DialogflowInteractionData,
    DialogflowSource,
    Entity,
    EntityMentionData,
    ExactMatchConfig,
    FaqAnswerData,
    GcsSource,
    HoldData,
    Intent,
    IntentMatchData,
    InterruptionData,
    Issue,
    IssueAssignment,
    IssueMatchData,
    IssueModel,
    IssueModelLabelStats,
    IssueModelResult,
    PhraseMatchData,
    PhraseMatcher,
    PhraseMatchRule,
    PhraseMatchRuleConfig,
    PhraseMatchRuleGroup,
    RuntimeAnnotation,
    SentimentData,
    Settings,
    SilenceData,
    SmartComposeSuggestionData,
    SmartReplyData,
    View,
)

__all__ = (
    "ContactCenterInsightsAsyncClient",
    "Analysis",
    "AnalysisResult",
    "AnnotationBoundary",
    "AnnotatorSelector",
    "AnswerFeedback",
    "ArticleSuggestionData",
    "BulkAnalyzeConversationsMetadata",
    "BulkAnalyzeConversationsRequest",
    "BulkAnalyzeConversationsResponse",
    "CalculateIssueModelStatsRequest",
    "CalculateIssueModelStatsResponse",
    "CalculateStatsRequest",
    "CalculateStatsResponse",
    "CallAnnotation",
    "ContactCenterInsightsClient",
    "Conversation",
    "ConversationDataSource",
    "ConversationLevelSentiment",
    "ConversationParticipant",
    "ConversationView",
    "CreateAnalysisOperationMetadata",
    "CreateAnalysisRequest",
    "CreateConversationRequest",
    "CreateIssueModelMetadata",
    "CreateIssueModelRequest",
    "CreatePhraseMatcherRequest",
    "CreateViewRequest",
    "DeleteAnalysisRequest",
    "DeleteConversationRequest",
    "DeleteIssueModelMetadata",
    "DeleteIssueModelRequest",
    "DeleteIssueRequest",
    "DeletePhraseMatcherRequest",
    "DeleteViewRequest",
    "DeployIssueModelMetadata",
    "DeployIssueModelRequest",
    "DeployIssueModelResponse",
    "DialogflowIntent",
    "DialogflowInteractionData",
    "DialogflowSource",
    "Entity",
    "EntityMentionData",
    "ExactMatchConfig",
    "ExportInsightsDataMetadata",
    "ExportInsightsDataRequest",
    "ExportInsightsDataResponse",
    "FaqAnswerData",
    "GcsSource",
    "GetAnalysisRequest",
    "GetConversationRequest",
    "GetIssueModelRequest",
    "GetIssueRequest",
    "GetPhraseMatcherRequest",
    "GetSettingsRequest",
    "GetViewRequest",
    "HoldData",
    "IngestConversationsMetadata",
    "IngestConversationsRequest",
    "IngestConversationsResponse",
    "Intent",
    "IntentMatchData",
    "InterruptionData",
    "Issue",
    "IssueAssignment",
    "IssueMatchData",
    "IssueModel",
    "IssueModelLabelStats",
    "IssueModelResult",
    "ListAnalysesRequest",
    "ListAnalysesResponse",
    "ListConversationsRequest",
    "ListConversationsResponse",
    "ListIssueModelsRequest",
    "ListIssueModelsResponse",
    "ListIssuesRequest",
    "ListIssuesResponse",
    "ListPhraseMatchersRequest",
    "ListPhraseMatchersResponse",
    "ListViewsRequest",
    "ListViewsResponse",
    "PhraseMatchData",
    "PhraseMatchRule",
    "PhraseMatchRuleConfig",
    "PhraseMatchRuleGroup",
    "PhraseMatcher",
    "RuntimeAnnotation",
    "SentimentData",
    "Settings",
    "SilenceData",
    "SmartComposeSuggestionData",
    "SmartReplyData",
    "UndeployIssueModelMetadata",
    "UndeployIssueModelRequest",
    "UndeployIssueModelResponse",
    "UpdateConversationRequest",
    "UpdateIssueModelRequest",
    "UpdateIssueRequest",
    "UpdatePhraseMatcherRequest",
    "UpdateSettingsRequest",
    "UpdateViewRequest",
    "View",
)

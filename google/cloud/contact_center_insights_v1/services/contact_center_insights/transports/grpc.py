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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.api_core import gapic_v1  # type: ignore
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.contact_center_insights_v1.types import contact_center_insights
from google.cloud.contact_center_insights_v1.types import resources
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from .base import ContactCenterInsightsTransport, DEFAULT_CLIENT_INFO


class ContactCenterInsightsGrpcTransport(ContactCenterInsightsTransport):
    """gRPC backend transport for ContactCenterInsights.

    An API that lets users analyze and explore their business
    conversation data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "contactcenterinsights.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "contactcenterinsights.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.CreateConversationRequest], resources.Conversation
    ]:
        r"""Return a callable for the create conversation method over gRPC.

        Creates a conversation.

        Returns:
            Callable[[~.CreateConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_conversation" not in self._stubs:
            self._stubs["create_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateConversation",
                request_serializer=contact_center_insights.CreateConversationRequest.serialize,
                response_deserializer=resources.Conversation.deserialize,
            )
        return self._stubs["create_conversation"]

    @property
    def update_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateConversationRequest], resources.Conversation
    ]:
        r"""Return a callable for the update conversation method over gRPC.

        Updates a conversation.

        Returns:
            Callable[[~.UpdateConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_conversation" not in self._stubs:
            self._stubs["update_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateConversation",
                request_serializer=contact_center_insights.UpdateConversationRequest.serialize,
                response_deserializer=resources.Conversation.deserialize,
            )
        return self._stubs["update_conversation"]

    @property
    def get_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.GetConversationRequest], resources.Conversation
    ]:
        r"""Return a callable for the get conversation method over gRPC.

        Gets a conversation.

        Returns:
            Callable[[~.GetConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_conversation" not in self._stubs:
            self._stubs["get_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetConversation",
                request_serializer=contact_center_insights.GetConversationRequest.serialize,
                response_deserializer=resources.Conversation.deserialize,
            )
        return self._stubs["get_conversation"]

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.ListConversationsRequest],
        contact_center_insights.ListConversationsResponse,
    ]:
        r"""Return a callable for the list conversations method over gRPC.

        Lists conversations.

        Returns:
            Callable[[~.ListConversationsRequest],
                    ~.ListConversationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_conversations" not in self._stubs:
            self._stubs["list_conversations"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListConversations",
                request_serializer=contact_center_insights.ListConversationsRequest.serialize,
                response_deserializer=contact_center_insights.ListConversationsResponse.deserialize,
            )
        return self._stubs["list_conversations"]

    @property
    def delete_conversation(
        self,
    ) -> Callable[[contact_center_insights.DeleteConversationRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete conversation method over gRPC.

        Deletes a conversation.

        Returns:
            Callable[[~.DeleteConversationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_conversation" not in self._stubs:
            self._stubs["delete_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteConversation",
                request_serializer=contact_center_insights.DeleteConversationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_conversation"]

    @property
    def create_analysis(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create analysis method over gRPC.

        Creates an analysis. The long running operation is
        done when the analysis has completed.

        Returns:
            Callable[[~.CreateAnalysisRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_analysis" not in self._stubs:
            self._stubs["create_analysis"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateAnalysis",
                request_serializer=contact_center_insights.CreateAnalysisRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_analysis"]

    @property
    def get_analysis(
        self,
    ) -> Callable[[contact_center_insights.GetAnalysisRequest], resources.Analysis]:
        r"""Return a callable for the get analysis method over gRPC.

        Gets an analysis.

        Returns:
            Callable[[~.GetAnalysisRequest],
                    ~.Analysis]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_analysis" not in self._stubs:
            self._stubs["get_analysis"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetAnalysis",
                request_serializer=contact_center_insights.GetAnalysisRequest.serialize,
                response_deserializer=resources.Analysis.deserialize,
            )
        return self._stubs["get_analysis"]

    @property
    def list_analyses(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysesRequest],
        contact_center_insights.ListAnalysesResponse,
    ]:
        r"""Return a callable for the list analyses method over gRPC.

        Lists analyses.

        Returns:
            Callable[[~.ListAnalysesRequest],
                    ~.ListAnalysesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_analyses" not in self._stubs:
            self._stubs["list_analyses"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListAnalyses",
                request_serializer=contact_center_insights.ListAnalysesRequest.serialize,
                response_deserializer=contact_center_insights.ListAnalysesResponse.deserialize,
            )
        return self._stubs["list_analyses"]

    @property
    def delete_analysis(
        self,
    ) -> Callable[[contact_center_insights.DeleteAnalysisRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete analysis method over gRPC.

        Deletes an analysis.

        Returns:
            Callable[[~.DeleteAnalysisRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_analysis" not in self._stubs:
            self._stubs["delete_analysis"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteAnalysis",
                request_serializer=contact_center_insights.DeleteAnalysisRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_analysis"]

    @property
    def export_insights_data(
        self,
    ) -> Callable[
        [contact_center_insights.ExportInsightsDataRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the export insights data method over gRPC.

        Export insights data to a destination defined in the
        request body.

        Returns:
            Callable[[~.ExportInsightsDataRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_insights_data" not in self._stubs:
            self._stubs["export_insights_data"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ExportInsightsData",
                request_serializer=contact_center_insights.ExportInsightsDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_insights_data"]

    @property
    def create_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.CreateIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create issue model method over gRPC.

        Creates an issue model.

        Returns:
            Callable[[~.CreateIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_issue_model" not in self._stubs:
            self._stubs["create_issue_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreateIssueModel",
                request_serializer=contact_center_insights.CreateIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_issue_model"]

    @property
    def update_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateIssueModelRequest], resources.IssueModel
    ]:
        r"""Return a callable for the update issue model method over gRPC.

        Updates an issue model.

        Returns:
            Callable[[~.UpdateIssueModelRequest],
                    ~.IssueModel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_issue_model" not in self._stubs:
            self._stubs["update_issue_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateIssueModel",
                request_serializer=contact_center_insights.UpdateIssueModelRequest.serialize,
                response_deserializer=resources.IssueModel.deserialize,
            )
        return self._stubs["update_issue_model"]

    @property
    def get_issue_model(
        self,
    ) -> Callable[[contact_center_insights.GetIssueModelRequest], resources.IssueModel]:
        r"""Return a callable for the get issue model method over gRPC.

        Gets an issue model.

        Returns:
            Callable[[~.GetIssueModelRequest],
                    ~.IssueModel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_issue_model" not in self._stubs:
            self._stubs["get_issue_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetIssueModel",
                request_serializer=contact_center_insights.GetIssueModelRequest.serialize,
                response_deserializer=resources.IssueModel.deserialize,
            )
        return self._stubs["get_issue_model"]

    @property
    def list_issue_models(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssueModelsRequest],
        contact_center_insights.ListIssueModelsResponse,
    ]:
        r"""Return a callable for the list issue models method over gRPC.

        Lists issue models.

        Returns:
            Callable[[~.ListIssueModelsRequest],
                    ~.ListIssueModelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_issue_models" not in self._stubs:
            self._stubs["list_issue_models"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListIssueModels",
                request_serializer=contact_center_insights.ListIssueModelsRequest.serialize,
                response_deserializer=contact_center_insights.ListIssueModelsResponse.deserialize,
            )
        return self._stubs["list_issue_models"]

    @property
    def delete_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete issue model method over gRPC.

        Deletes an issue model.

        Returns:
            Callable[[~.DeleteIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_issue_model" not in self._stubs:
            self._stubs["delete_issue_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeleteIssueModel",
                request_serializer=contact_center_insights.DeleteIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_issue_model"]

    @property
    def deploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeployIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the deploy issue model method over gRPC.

        Deploys an issue model. Returns an error if a model
        is already deployed. An issue model can only be used in
        analysis after it has been deployed.

        Returns:
            Callable[[~.DeployIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_issue_model" not in self._stubs:
            self._stubs["deploy_issue_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeployIssueModel",
                request_serializer=contact_center_insights.DeployIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_issue_model"]

    @property
    def undeploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployIssueModelRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the undeploy issue model method over gRPC.

        Undeploys an issue model.
        An issue model can not be used in analysis after it has
        been undeployed.

        Returns:
            Callable[[~.UndeployIssueModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_issue_model" not in self._stubs:
            self._stubs["undeploy_issue_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UndeployIssueModel",
                request_serializer=contact_center_insights.UndeployIssueModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undeploy_issue_model"]

    @property
    def get_issue(
        self,
    ) -> Callable[[contact_center_insights.GetIssueRequest], resources.Issue]:
        r"""Return a callable for the get issue method over gRPC.

        Gets an issue.

        Returns:
            Callable[[~.GetIssueRequest],
                    ~.Issue]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_issue" not in self._stubs:
            self._stubs["get_issue"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetIssue",
                request_serializer=contact_center_insights.GetIssueRequest.serialize,
                response_deserializer=resources.Issue.deserialize,
            )
        return self._stubs["get_issue"]

    @property
    def list_issues(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssuesRequest],
        contact_center_insights.ListIssuesResponse,
    ]:
        r"""Return a callable for the list issues method over gRPC.

        Lists issues.

        Returns:
            Callable[[~.ListIssuesRequest],
                    ~.ListIssuesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_issues" not in self._stubs:
            self._stubs["list_issues"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListIssues",
                request_serializer=contact_center_insights.ListIssuesRequest.serialize,
                response_deserializer=contact_center_insights.ListIssuesResponse.deserialize,
            )
        return self._stubs["list_issues"]

    @property
    def update_issue(
        self,
    ) -> Callable[[contact_center_insights.UpdateIssueRequest], resources.Issue]:
        r"""Return a callable for the update issue method over gRPC.

        Updates an issue.

        Returns:
            Callable[[~.UpdateIssueRequest],
                    ~.Issue]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_issue" not in self._stubs:
            self._stubs["update_issue"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateIssue",
                request_serializer=contact_center_insights.UpdateIssueRequest.serialize,
                response_deserializer=resources.Issue.deserialize,
            )
        return self._stubs["update_issue"]

    @property
    def calculate_issue_model_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateIssueModelStatsRequest],
        contact_center_insights.CalculateIssueModelStatsResponse,
    ]:
        r"""Return a callable for the calculate issue model stats method over gRPC.

        Gets an issue model's statistics.

        Returns:
            Callable[[~.CalculateIssueModelStatsRequest],
                    ~.CalculateIssueModelStatsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "calculate_issue_model_stats" not in self._stubs:
            self._stubs["calculate_issue_model_stats"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CalculateIssueModelStats",
                request_serializer=contact_center_insights.CalculateIssueModelStatsRequest.serialize,
                response_deserializer=contact_center_insights.CalculateIssueModelStatsResponse.deserialize,
            )
        return self._stubs["calculate_issue_model_stats"]

    @property
    def create_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.CreatePhraseMatcherRequest], resources.PhraseMatcher
    ]:
        r"""Return a callable for the create phrase matcher method over gRPC.

        Creates a phrase matcher.

        Returns:
            Callable[[~.CreatePhraseMatcherRequest],
                    ~.PhraseMatcher]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_phrase_matcher" not in self._stubs:
            self._stubs["create_phrase_matcher"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CreatePhraseMatcher",
                request_serializer=contact_center_insights.CreatePhraseMatcherRequest.serialize,
                response_deserializer=resources.PhraseMatcher.deserialize,
            )
        return self._stubs["create_phrase_matcher"]

    @property
    def get_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.GetPhraseMatcherRequest], resources.PhraseMatcher
    ]:
        r"""Return a callable for the get phrase matcher method over gRPC.

        Gets a phrase matcher.

        Returns:
            Callable[[~.GetPhraseMatcherRequest],
                    ~.PhraseMatcher]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_phrase_matcher" not in self._stubs:
            self._stubs["get_phrase_matcher"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetPhraseMatcher",
                request_serializer=contact_center_insights.GetPhraseMatcherRequest.serialize,
                response_deserializer=resources.PhraseMatcher.deserialize,
            )
        return self._stubs["get_phrase_matcher"]

    @property
    def list_phrase_matchers(
        self,
    ) -> Callable[
        [contact_center_insights.ListPhraseMatchersRequest],
        contact_center_insights.ListPhraseMatchersResponse,
    ]:
        r"""Return a callable for the list phrase matchers method over gRPC.

        Lists phrase matchers.

        Returns:
            Callable[[~.ListPhraseMatchersRequest],
                    ~.ListPhraseMatchersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_phrase_matchers" not in self._stubs:
            self._stubs["list_phrase_matchers"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/ListPhraseMatchers",
                request_serializer=contact_center_insights.ListPhraseMatchersRequest.serialize,
                response_deserializer=contact_center_insights.ListPhraseMatchersResponse.deserialize,
            )
        return self._stubs["list_phrase_matchers"]

    @property
    def delete_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.DeletePhraseMatcherRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete phrase matcher method over gRPC.

        Deletes a phrase matcher.

        Returns:
            Callable[[~.DeletePhraseMatcherRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_phrase_matcher" not in self._stubs:
            self._stubs["delete_phrase_matcher"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/DeletePhraseMatcher",
                request_serializer=contact_center_insights.DeletePhraseMatcherRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_phrase_matcher"]

    @property
    def calculate_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateStatsRequest],
        contact_center_insights.CalculateStatsResponse,
    ]:
        r"""Return a callable for the calculate stats method over gRPC.

        Gets conversation statistics.

        Returns:
            Callable[[~.CalculateStatsRequest],
                    ~.CalculateStatsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "calculate_stats" not in self._stubs:
            self._stubs["calculate_stats"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/CalculateStats",
                request_serializer=contact_center_insights.CalculateStatsRequest.serialize,
                response_deserializer=contact_center_insights.CalculateStatsResponse.deserialize,
            )
        return self._stubs["calculate_stats"]

    @property
    def get_settings(
        self,
    ) -> Callable[[contact_center_insights.GetSettingsRequest], resources.Settings]:
        r"""Return a callable for the get settings method over gRPC.

        Gets project-level settings.

        Returns:
            Callable[[~.GetSettingsRequest],
                    ~.Settings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_settings" not in self._stubs:
            self._stubs["get_settings"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/GetSettings",
                request_serializer=contact_center_insights.GetSettingsRequest.serialize,
                response_deserializer=resources.Settings.deserialize,
            )
        return self._stubs["get_settings"]

    @property
    def update_settings(
        self,
    ) -> Callable[[contact_center_insights.UpdateSettingsRequest], resources.Settings]:
        r"""Return a callable for the update settings method over gRPC.

        Updates project-level settings.

        Returns:
            Callable[[~.UpdateSettingsRequest],
                    ~.Settings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_settings" not in self._stubs:
            self._stubs["update_settings"] = self.grpc_channel.unary_unary(
                "/google.cloud.contactcenterinsights.v1.ContactCenterInsights/UpdateSettings",
                request_serializer=contact_center_insights.UpdateSettingsRequest.serialize,
                response_deserializer=resources.Settings.deserialize,
            )
        return self._stubs["update_settings"]


__all__ = ("ContactCenterInsightsGrpcTransport",)

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'ChannelHlsIngest',
    'ChannelHlsIngestIngestEndpoint',
]

@pulumi.output_type
class ChannelHlsIngest(dict):
    def __init__(__self__, *,
                 ingest_endpoints: Optional[List['outputs.ChannelHlsIngestIngestEndpoint']] = None):
        """
        :param List['ChannelHlsIngestIngestEndpointArgs'] ingest_endpoints: A list of the ingest endpoints
        """
        if ingest_endpoints is not None:
            pulumi.set(__self__, "ingest_endpoints", ingest_endpoints)

    @property
    @pulumi.getter(name="ingestEndpoints")
    def ingest_endpoints(self) -> Optional[List['outputs.ChannelHlsIngestIngestEndpoint']]:
        """
        A list of the ingest endpoints
        """
        return pulumi.get(self, "ingest_endpoints")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ChannelHlsIngestIngestEndpoint(dict):
    def __init__(__self__, *,
                 password: Optional[str] = None,
                 url: Optional[str] = None,
                 username: Optional[str] = None):
        """
        :param str password: The password
        :param str url: The URL
        :param str username: The username
        """
        if password is not None:
            pulumi.set(__self__, "password", password)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        The password
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The URL
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        """
        The username
        """
        return pulumi.get(self, "username")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop



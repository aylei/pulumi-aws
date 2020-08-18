# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetSecretsResult',
    'AwaitableGetSecretsResult',
    'get_secrets',
]



@pulumi.output_type
class GetSecretsResult:
    """
    A collection of values returned by getSecrets.
    """
    def __init__(__self__, id=None, plaintext=None, secrets=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if plaintext and not isinstance(plaintext, dict):
            raise TypeError("Expected argument 'plaintext' to be a dict")
        pulumi.set(__self__, "plaintext", plaintext)
        if secrets and not isinstance(secrets, list):
            raise TypeError("Expected argument 'secrets' to be a list")
        pulumi.set(__self__, "secrets", secrets)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def plaintext(self) -> Mapping[str, str]:
        """
        Map containing each `secret` `name` as the key with its decrypted plaintext value
        """
        return pulumi.get(self, "plaintext")

    @property
    @pulumi.getter
    def secrets(self) -> List['outputs.GetSecretsSecretResult']:
        return pulumi.get(self, "secrets")



class AwaitableGetSecretsResult(GetSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretsResult(
            id=self.id,
            plaintext=self.plaintext,
            secrets=self.secrets)


def get_secrets(secrets: Optional[List[pulumi.InputType['GetSecretsSecretArgs']]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretsResult:
    """
    Decrypt multiple secrets from data encrypted with the AWS KMS service.


    :param List[pulumi.InputType['GetSecretsSecretArgs']] secrets: One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
    """
    __args__ = dict()
    __args__['secrets'] = secrets
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kms/getSecrets:getSecrets', __args__, opts=opts, typ=GetSecretsResult).value

    return AwaitableGetSecretsResult(
        id=__ret__.id,
        plaintext=__ret__.plaintext,
        secrets=__ret__.secrets)

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

__all__ = ['Grant']


class Grant(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 constraints: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]]] = None,
                 grant_creation_tokens: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 grantee_principal: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 retire_on_delete: Optional[pulumi.Input[bool]] = None,
                 retiring_principal: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource-based access control mechanism for a KMS customer master key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.kms.Key("key")
        role = aws.iam.Role("role", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "lambda.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        grant = aws.kms.Grant("grant",
            constraints=[{
                "encryptionContextEquals": {
                    "Department": "Finance",
                },
            }],
            grantee_principal=role.arn,
            key_id=key.key_id,
            operations=[
                "Encrypt",
                "Decrypt",
                "GenerateDataKey",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[List[pulumi.Input[str]]] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[List[pulumi.Input[str]]] operations: A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`
        :param pulumi.Input[bool] retire_on_delete: -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['constraints'] = constraints
            __props__['grant_creation_tokens'] = grant_creation_tokens
            if grantee_principal is None:
                raise TypeError("Missing required property 'grantee_principal'")
            __props__['grantee_principal'] = grantee_principal
            if key_id is None:
                raise TypeError("Missing required property 'key_id'")
            __props__['key_id'] = key_id
            __props__['name'] = name
            if operations is None:
                raise TypeError("Missing required property 'operations'")
            __props__['operations'] = operations
            __props__['retire_on_delete'] = retire_on_delete
            __props__['retiring_principal'] = retiring_principal
            __props__['grant_id'] = None
            __props__['grant_token'] = None
        super(Grant, __self__).__init__(
            'aws:kms/grant:Grant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            constraints: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]]] = None,
            grant_creation_tokens: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            grant_id: Optional[pulumi.Input[str]] = None,
            grant_token: Optional[pulumi.Input[str]] = None,
            grantee_principal: Optional[pulumi.Input[str]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            operations: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            retire_on_delete: Optional[pulumi.Input[bool]] = None,
            retiring_principal: Optional[pulumi.Input[str]] = None) -> 'Grant':
        """
        Get an existing Grant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[List[pulumi.Input[str]]] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grant_id: The unique identifier for the grant.
        :param pulumi.Input[str] grant_token: The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[List[pulumi.Input[str]]] operations: A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`
        :param pulumi.Input[bool] retire_on_delete: -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["constraints"] = constraints
        __props__["grant_creation_tokens"] = grant_creation_tokens
        __props__["grant_id"] = grant_id
        __props__["grant_token"] = grant_token
        __props__["grantee_principal"] = grantee_principal
        __props__["key_id"] = key_id
        __props__["name"] = name
        __props__["operations"] = operations
        __props__["retire_on_delete"] = retire_on_delete
        __props__["retiring_principal"] = retiring_principal
        return Grant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def constraints(self) -> Optional[List['outputs.GrantConstraint']]:
        """
        A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        """
        return pulumi.get(self, "constraints")

    @property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(self) -> Optional[List[str]]:
        """
        A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        """
        return pulumi.get(self, "grant_creation_tokens")

    @property
    @pulumi.getter(name="grantId")
    def grant_id(self) -> str:
        """
        The unique identifier for the grant.
        """
        return pulumi.get(self, "grant_id")

    @property
    @pulumi.getter(name="grantToken")
    def grant_token(self) -> str:
        """
        The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        """
        return pulumi.get(self, "grant_token")

    @property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> str:
        """
        The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "grantee_principal")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        """
        The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A friendly name for identifying the grant.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operations(self) -> List[str]:
        """
        A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`
        """
        return pulumi.get(self, "operations")

    @property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> Optional[bool]:
        """
        -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
        See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        """
        return pulumi.get(self, "retire_on_delete")

    @property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> Optional[str]:
        """
        The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "retiring_principal")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Key']


class Key(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_master_key_spec: Optional[pulumi.Input[str]] = None,
                 deletion_window_in_days: Optional[pulumi.Input[float]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_key_rotation: Optional[pulumi.Input[bool]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 key_usage: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a KMS customer master key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.kms.Key("key",
            deletion_window_in_days=10,
            description="KMS key 1")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] customer_master_key_spec: Specifies whether the key contains a symmetric key or an asymmetric key pair and the encryption algorithms or signing algorithms that the key supports.
               Valid values: `SYMMETRIC_DEFAULT`,  `RSA_2048`, `RSA_3072`, `RSA_4096`, `ECC_NIST_P256`, `ECC_NIST_P384`, `ECC_NIST_P521`, or `ECC_SECG_P256K1`. Defaults to `SYMMETRIC_DEFAULT`. For help with choosing a key spec, see the [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html).
        :param pulumi.Input[float] deletion_window_in_days: Duration in days after which the key is deleted
               after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.
        :param pulumi.Input[str] description: The description of the key as viewed in AWS console.
        :param pulumi.Input[bool] enable_key_rotation: Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
               is enabled. Defaults to false.
        :param pulumi.Input[bool] is_enabled: Specifies whether the key is enabled. Defaults to true.
        :param pulumi.Input[str] key_usage: Specifies the intended use of the key. Valid values: `ENCRYPT_DECRYPT` or `SIGN_VERIFY`.
               Defaults to `ENCRYPT_DECRYPT`.
        :param pulumi.Input[str] policy: A valid policy JSON document.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the object.
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

            __props__['customer_master_key_spec'] = customer_master_key_spec
            __props__['deletion_window_in_days'] = deletion_window_in_days
            __props__['description'] = description
            __props__['enable_key_rotation'] = enable_key_rotation
            __props__['is_enabled'] = is_enabled
            __props__['key_usage'] = key_usage
            __props__['policy'] = policy
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['key_id'] = None
        super(Key, __self__).__init__(
            'aws:kms/key:Key',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            customer_master_key_spec: Optional[pulumi.Input[str]] = None,
            deletion_window_in_days: Optional[pulumi.Input[float]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable_key_rotation: Optional[pulumi.Input[bool]] = None,
            is_enabled: Optional[pulumi.Input[bool]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            key_usage: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Key':
        """
        Get an existing Key resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the key.
        :param pulumi.Input[str] customer_master_key_spec: Specifies whether the key contains a symmetric key or an asymmetric key pair and the encryption algorithms or signing algorithms that the key supports.
               Valid values: `SYMMETRIC_DEFAULT`,  `RSA_2048`, `RSA_3072`, `RSA_4096`, `ECC_NIST_P256`, `ECC_NIST_P384`, `ECC_NIST_P521`, or `ECC_SECG_P256K1`. Defaults to `SYMMETRIC_DEFAULT`. For help with choosing a key spec, see the [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html).
        :param pulumi.Input[float] deletion_window_in_days: Duration in days after which the key is deleted
               after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.
        :param pulumi.Input[str] description: The description of the key as viewed in AWS console.
        :param pulumi.Input[bool] enable_key_rotation: Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
               is enabled. Defaults to false.
        :param pulumi.Input[bool] is_enabled: Specifies whether the key is enabled. Defaults to true.
        :param pulumi.Input[str] key_id: The globally unique identifier for the key.
        :param pulumi.Input[str] key_usage: Specifies the intended use of the key. Valid values: `ENCRYPT_DECRYPT` or `SIGN_VERIFY`.
               Defaults to `ENCRYPT_DECRYPT`.
        :param pulumi.Input[str] policy: A valid policy JSON document.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the object.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["customer_master_key_spec"] = customer_master_key_spec
        __props__["deletion_window_in_days"] = deletion_window_in_days
        __props__["description"] = description
        __props__["enable_key_rotation"] = enable_key_rotation
        __props__["is_enabled"] = is_enabled
        __props__["key_id"] = key_id
        __props__["key_usage"] = key_usage
        __props__["policy"] = policy
        __props__["tags"] = tags
        return Key(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the key.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="customerMasterKeySpec")
    def customer_master_key_spec(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether the key contains a symmetric key or an asymmetric key pair and the encryption algorithms or signing algorithms that the key supports.
        Valid values: `SYMMETRIC_DEFAULT`,  `RSA_2048`, `RSA_3072`, `RSA_4096`, `ECC_NIST_P256`, `ECC_NIST_P384`, `ECC_NIST_P521`, or `ECC_SECG_P256K1`. Defaults to `SYMMETRIC_DEFAULT`. For help with choosing a key spec, see the [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html).
        """
        return pulumi.get(self, "customer_master_key_spec")

    @property
    @pulumi.getter(name="deletionWindowInDays")
    def deletion_window_in_days(self) -> pulumi.Output[Optional[float]]:
        """
        Duration in days after which the key is deleted
        after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.
        """
        return pulumi.get(self, "deletion_window_in_days")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the key as viewed in AWS console.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableKeyRotation")
    def enable_key_rotation(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
        is enabled. Defaults to false.
        """
        return pulumi.get(self, "enable_key_rotation")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the key is enabled. Defaults to true.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        """
        The globally unique identifier for the key.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the intended use of the key. Valid values: `ENCRYPT_DECRYPT` or `SIGN_VERIFY`.
        Defaults to `ENCRYPT_DECRYPT`.
        """
        return pulumi.get(self, "key_usage")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        A valid policy JSON document.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the object.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


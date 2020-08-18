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

__all__ = ['Gateway']


class Gateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activation_key: Optional[pulumi.Input[str]] = None,
                 cloudwatch_log_group_arn: Optional[pulumi.Input[str]] = None,
                 gateway_ip_address: Optional[pulumi.Input[str]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 gateway_timezone: Optional[pulumi.Input[str]] = None,
                 gateway_type: Optional[pulumi.Input[str]] = None,
                 gateway_vpc_endpoint: Optional[pulumi.Input[str]] = None,
                 medium_changer_type: Optional[pulumi.Input[str]] = None,
                 smb_active_directory_settings: Optional[pulumi.Input[pulumi.InputType['GatewaySmbActiveDirectorySettingsArgs']]] = None,
                 smb_guest_password: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tape_drive_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.

        > NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving `The specified gateway is not connected` errors during resource creation (gateway activation), ensure your gateway instance meets the [Storage Gateway requirements](https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html).

        ## Example Usage
        ### File Gateway

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.Gateway("example",
            gateway_ip_address="1.2.3.4",
            gateway_name="example",
            gateway_timezone="GMT",
            gateway_type="FILE_S3")
        ```
        ### Volume Gateway (Cached)

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.Gateway("example",
            gateway_ip_address="1.2.3.4",
            gateway_name="example",
            gateway_timezone="GMT",
            gateway_type="CACHED")
        ```
        ### Volume Gateway (Stored)

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.Gateway("example",
            gateway_ip_address="1.2.3.4",
            gateway_name="example",
            gateway_timezone="GMT",
            gateway_type="STORED")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] activation_key: Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).
        :param pulumi.Input[str] cloudwatch_log_group_arn: The Amazon Resource Name (ARN) of the Amazon CloudWatch log group to use to monitor and log events in the gateway.
        :param pulumi.Input[str] gateway_ip_address: Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where this provider is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).
        :param pulumi.Input[str] gateway_name: Name of the gateway.
        :param pulumi.Input[str] gateway_timezone: Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.
        :param pulumi.Input[str] gateway_type: Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.
        :param pulumi.Input[str] gateway_vpc_endpoint: VPC endpoint address to be used when activating your gateway. This should be used when your instance is in a private subnet. Requires HTTP access from client computer running Pulumi. More info on what ports are required by your VPC Endpoint Security group in [Activating a Gateway in a Virtual Private Cloud](https://docs.aws.amazon.com/storagegateway/latest/userguide/gateway-private-link.html).
        :param pulumi.Input[pulumi.InputType['GatewaySmbActiveDirectorySettingsArgs']] smb_active_directory_settings: Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.
        :param pulumi.Input[str] smb_guest_password: Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. This provider can only detect drift of the existence of a guest password, not its actual value from the gateway. This provider can however update the password with changing the argument.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags
        :param pulumi.Input[str] tape_drive_type: Type of tape drive to use for tape gateway. This provider cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.
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

            __props__['activation_key'] = activation_key
            __props__['cloudwatch_log_group_arn'] = cloudwatch_log_group_arn
            __props__['gateway_ip_address'] = gateway_ip_address
            if gateway_name is None:
                raise TypeError("Missing required property 'gateway_name'")
            __props__['gateway_name'] = gateway_name
            if gateway_timezone is None:
                raise TypeError("Missing required property 'gateway_timezone'")
            __props__['gateway_timezone'] = gateway_timezone
            __props__['gateway_type'] = gateway_type
            __props__['gateway_vpc_endpoint'] = gateway_vpc_endpoint
            __props__['medium_changer_type'] = medium_changer_type
            __props__['smb_active_directory_settings'] = smb_active_directory_settings
            __props__['smb_guest_password'] = smb_guest_password
            __props__['tags'] = tags
            __props__['tape_drive_type'] = tape_drive_type
            __props__['arn'] = None
            __props__['gateway_id'] = None
        super(Gateway, __self__).__init__(
            'aws:storagegateway/gateway:Gateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            activation_key: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cloudwatch_log_group_arn: Optional[pulumi.Input[str]] = None,
            gateway_id: Optional[pulumi.Input[str]] = None,
            gateway_ip_address: Optional[pulumi.Input[str]] = None,
            gateway_name: Optional[pulumi.Input[str]] = None,
            gateway_timezone: Optional[pulumi.Input[str]] = None,
            gateway_type: Optional[pulumi.Input[str]] = None,
            gateway_vpc_endpoint: Optional[pulumi.Input[str]] = None,
            medium_changer_type: Optional[pulumi.Input[str]] = None,
            smb_active_directory_settings: Optional[pulumi.Input[pulumi.InputType['GatewaySmbActiveDirectorySettingsArgs']]] = None,
            smb_guest_password: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tape_drive_type: Optional[pulumi.Input[str]] = None) -> 'Gateway':
        """
        Get an existing Gateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] activation_key: Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the gateway.
        :param pulumi.Input[str] cloudwatch_log_group_arn: The Amazon Resource Name (ARN) of the Amazon CloudWatch log group to use to monitor and log events in the gateway.
        :param pulumi.Input[str] gateway_id: Identifier of the gateway.
        :param pulumi.Input[str] gateway_ip_address: Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where this provider is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).
        :param pulumi.Input[str] gateway_name: Name of the gateway.
        :param pulumi.Input[str] gateway_timezone: Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.
        :param pulumi.Input[str] gateway_type: Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.
        :param pulumi.Input[str] gateway_vpc_endpoint: VPC endpoint address to be used when activating your gateway. This should be used when your instance is in a private subnet. Requires HTTP access from client computer running Pulumi. More info on what ports are required by your VPC Endpoint Security group in [Activating a Gateway in a Virtual Private Cloud](https://docs.aws.amazon.com/storagegateway/latest/userguide/gateway-private-link.html).
        :param pulumi.Input[pulumi.InputType['GatewaySmbActiveDirectorySettingsArgs']] smb_active_directory_settings: Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.
        :param pulumi.Input[str] smb_guest_password: Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. This provider can only detect drift of the existence of a guest password, not its actual value from the gateway. This provider can however update the password with changing the argument.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags
        :param pulumi.Input[str] tape_drive_type: Type of tape drive to use for tape gateway. This provider cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["activation_key"] = activation_key
        __props__["arn"] = arn
        __props__["cloudwatch_log_group_arn"] = cloudwatch_log_group_arn
        __props__["gateway_id"] = gateway_id
        __props__["gateway_ip_address"] = gateway_ip_address
        __props__["gateway_name"] = gateway_name
        __props__["gateway_timezone"] = gateway_timezone
        __props__["gateway_type"] = gateway_type
        __props__["gateway_vpc_endpoint"] = gateway_vpc_endpoint
        __props__["medium_changer_type"] = medium_changer_type
        __props__["smb_active_directory_settings"] = smb_active_directory_settings
        __props__["smb_guest_password"] = smb_guest_password
        __props__["tags"] = tags
        __props__["tape_drive_type"] = tape_drive_type
        return Gateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> str:
        """
        Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).
        """
        return pulumi.get(self, "activation_key")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the gateway.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon CloudWatch log group to use to monitor and log events in the gateway.
        """
        return pulumi.get(self, "cloudwatch_log_group_arn")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> str:
        """
        Identifier of the gateway.
        """
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> str:
        """
        Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where this provider is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).
        """
        return pulumi.get(self, "gateway_ip_address")

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> str:
        """
        Name of the gateway.
        """
        return pulumi.get(self, "gateway_name")

    @property
    @pulumi.getter(name="gatewayTimezone")
    def gateway_timezone(self) -> str:
        """
        Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.
        """
        return pulumi.get(self, "gateway_timezone")

    @property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> Optional[str]:
        """
        Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.
        """
        return pulumi.get(self, "gateway_type")

    @property
    @pulumi.getter(name="gatewayVpcEndpoint")
    def gateway_vpc_endpoint(self) -> Optional[str]:
        """
        VPC endpoint address to be used when activating your gateway. This should be used when your instance is in a private subnet. Requires HTTP access from client computer running Pulumi. More info on what ports are required by your VPC Endpoint Security group in [Activating a Gateway in a Virtual Private Cloud](https://docs.aws.amazon.com/storagegateway/latest/userguide/gateway-private-link.html).
        """
        return pulumi.get(self, "gateway_vpc_endpoint")

    @property
    @pulumi.getter(name="mediumChangerType")
    def medium_changer_type(self) -> Optional[str]:
        return pulumi.get(self, "medium_changer_type")

    @property
    @pulumi.getter(name="smbActiveDirectorySettings")
    def smb_active_directory_settings(self) -> Optional['outputs.GatewaySmbActiveDirectorySettings']:
        """
        Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.
        """
        return pulumi.get(self, "smb_active_directory_settings")

    @property
    @pulumi.getter(name="smbGuestPassword")
    def smb_guest_password(self) -> Optional[str]:
        """
        Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. This provider can only detect drift of the existence of a guest password, not its actual value from the gateway. This provider can however update the password with changing the argument.
        """
        return pulumi.get(self, "smb_guest_password")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value mapping of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tapeDriveType")
    def tape_drive_type(self) -> Optional[str]:
        """
        Type of tape drive to use for tape gateway. This provider cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.
        """
        return pulumi.get(self, "tape_drive_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


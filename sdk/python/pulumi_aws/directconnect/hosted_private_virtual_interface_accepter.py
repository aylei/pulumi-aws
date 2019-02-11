# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class HostedPrivateVirtualInterfaceAccepter(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the virtual interface.
    """
    dx_gateway_id: pulumi.Output[str]
    """
    The ID of the Direct Connect gateway to which to connect the virtual interface.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    virtual_interface_id: pulumi.Output[str]
    """
    The ID of the Direct Connect virtual interface to accept.
    """
    vpn_gateway_id: pulumi.Output[str]
    """
    The ID of the virtual private gateway to which to connect the virtual interface.
    """
    def __init__(__self__, resource_name, opts=None, dx_gateway_id=None, tags=None, virtual_interface_id=None, vpn_gateway_id=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage the accepter's side of a Direct Connect hosted private virtual interface.
        This resource accepts ownership of a private virtual interface created by another AWS account.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dx_gateway_id: The ID of the Direct Connect gateway to which to connect the virtual interface.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface to accept.
        :param pulumi.Input[str] vpn_gateway_id: The ID of the virtual private gateway to which to connect the virtual interface.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['dx_gateway_id'] = dx_gateway_id

        __props__['tags'] = tags

        if virtual_interface_id is None:
            raise TypeError('Missing required property virtual_interface_id')
        __props__['virtual_interface_id'] = virtual_interface_id

        __props__['vpn_gateway_id'] = vpn_gateway_id

        __props__['arn'] = None

        super(HostedPrivateVirtualInterfaceAccepter, __self__).__init__(
            'aws:directconnect/hostedPrivateVirtualInterfaceAccepter:HostedPrivateVirtualInterfaceAccepter',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


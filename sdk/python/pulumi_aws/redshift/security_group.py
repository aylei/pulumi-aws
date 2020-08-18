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

__all__ = ['SecurityGroup']


class SecurityGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ingress: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.redshift.SecurityGroup("default", ingress=[{
            "cidr": "10.0.0.0/24",
        }])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Redshift security group. Defaults to "Managed by Pulumi".
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]] ingress: A list of ingress rules.
        :param pulumi.Input[str] name: The name of the Redshift security group.
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

            if description is None:
                description = 'Managed by Pulumi'
            __props__['description'] = description
            if ingress is None:
                raise TypeError("Missing required property 'ingress'")
            __props__['ingress'] = ingress
            __props__['name'] = name
        super(SecurityGroup, __self__).__init__(
            'aws:redshift/securityGroup:SecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            ingress: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'SecurityGroup':
        """
        Get an existing SecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Redshift security group. Defaults to "Managed by Pulumi".
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['SecurityGroupIngressArgs']]]] ingress: A list of ingress rules.
        :param pulumi.Input[str] name: The name of the Redshift security group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["ingress"] = ingress
        __props__["name"] = name
        return SecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the Redshift security group. Defaults to "Managed by Pulumi".
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def ingress(self) -> List['outputs.SecurityGroupIngress']:
        """
        A list of ingress rules.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Redshift security group.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


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

__all__ = ['OrganizationalUnit']


class OrganizationalUnit(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to create an organizational unit.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.organizations.OrganizationalUnit("example", parent_id=aws_organizations_organization["example"]["roots"][0]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name for the organizational unit
        :param pulumi.Input[str] parent_id: ID of the parent organizational unit, which may be the root
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

            __props__['name'] = name
            if parent_id is None:
                raise TypeError("Missing required property 'parent_id'")
            __props__['parent_id'] = parent_id
            __props__['accounts'] = None
            __props__['arn'] = None
        super(OrganizationalUnit, __self__).__init__(
            'aws:organizations/organizationalUnit:OrganizationalUnit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            accounts: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['OrganizationalUnitAccountArgs']]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None) -> 'OrganizationalUnit':
        """
        Get an existing OrganizationalUnit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['OrganizationalUnitAccountArgs']]]] accounts: List of child accounts for this Organizational Unit. Does not return account information for child Organizational Units. All elements have these attributes:
        :param pulumi.Input[str] arn: ARN of the organizational unit
        :param pulumi.Input[str] name: The name for the organizational unit
        :param pulumi.Input[str] parent_id: ID of the parent organizational unit, which may be the root
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["accounts"] = accounts
        __props__["arn"] = arn
        __props__["name"] = name
        __props__["parent_id"] = parent_id
        return OrganizationalUnit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accounts(self) -> List['outputs.OrganizationalUnitAccount']:
        """
        List of child accounts for this Organizational Unit. Does not return account information for child Organizational Units. All elements have these attributes:
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name for the organizational unit
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> str:
        """
        ID of the parent organizational unit, which may be the root
        """
        return pulumi.get(self, "parent_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


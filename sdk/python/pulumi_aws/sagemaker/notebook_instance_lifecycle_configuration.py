# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['NotebookInstanceLifecycleConfiguration']


class NotebookInstanceLifecycleConfiguration(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_create: Optional[pulumi.Input[str]] = None,
                 on_start: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a lifecycle configuration for SageMaker Notebook Instances.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the lifecycle configuration (must be unique). If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[str] on_create: A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.
        :param pulumi.Input[str] on_start: A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it's created.
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
            __props__['on_create'] = on_create
            __props__['on_start'] = on_start
            __props__['arn'] = None
        super(NotebookInstanceLifecycleConfiguration, __self__).__init__(
            'aws:sagemaker/notebookInstanceLifecycleConfiguration:NotebookInstanceLifecycleConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            on_create: Optional[pulumi.Input[str]] = None,
            on_start: Optional[pulumi.Input[str]] = None) -> 'NotebookInstanceLifecycleConfiguration':
        """
        Get an existing NotebookInstanceLifecycleConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this lifecycle configuration.
        :param pulumi.Input[str] name: The name of the lifecycle configuration (must be unique). If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[str] on_create: A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.
        :param pulumi.Input[str] on_start: A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it's created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["name"] = name
        __props__["on_create"] = on_create
        __props__["on_start"] = on_start
        return NotebookInstanceLifecycleConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) assigned by AWS to this lifecycle configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the lifecycle configuration (must be unique). If omitted, this provider will assign a random, unique name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onCreate")
    def on_create(self) -> pulumi.Output[Optional[str]]:
        """
        A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.
        """
        return pulumi.get(self, "on_create")

    @property
    @pulumi.getter(name="onStart")
    def on_start(self) -> pulumi.Output[Optional[str]]:
        """
        A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it's created.
        """
        return pulumi.get(self, "on_start")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class DeploymentConfig(pulumi.CustomResource):
    compute_platform: pulumi.Output[str]
    """
    The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
    """
    deployment_config_id: pulumi.Output[str]
    """
    The AWS Assigned deployment config id
    """
    deployment_config_name: pulumi.Output[str]
    """
    The name of the deployment config.
    """
    minimum_healthy_hosts: pulumi.Output[dict]
    """
    A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.
    """
    traffic_routing_config: pulumi.Output[dict]
    """
    A traffic_routing_config block. Traffic Routing Config is documented below.
    """
    def __init__(__self__, resource_name, opts=None, compute_platform=None, deployment_config_name=None, minimum_healthy_hosts=None, traffic_routing_config=None, __name__=None, __opts__=None):
        """
        Provides a CodeDeploy deployment config for an application
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
        :param pulumi.Input[str] deployment_config_name: The name of the deployment config.
        :param pulumi.Input[dict] minimum_healthy_hosts: A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.
        :param pulumi.Input[dict] traffic_routing_config: A traffic_routing_config block. Traffic Routing Config is documented below.
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

        __props__['compute_platform'] = compute_platform

        if deployment_config_name is None:
            raise TypeError('Missing required property deployment_config_name')
        __props__['deployment_config_name'] = deployment_config_name

        __props__['minimum_healthy_hosts'] = minimum_healthy_hosts

        __props__['traffic_routing_config'] = traffic_routing_config

        __props__['deployment_config_id'] = None

        super(DeploymentConfig, __self__).__init__(
            'aws:codedeploy/deploymentConfig:DeploymentConfig',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


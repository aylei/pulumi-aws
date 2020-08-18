# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Dashboard']


class Dashboard(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_body: Optional[pulumi.Input[str]] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CloudWatch Dashboard resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        main = aws.cloudwatch.Dashboard("main",
            dashboard_body=\"\"\" {
           "widgets": [
               {
                  "type":"metric",
                  "x":0,
                  "y":0,
                  "width":12,
                  "height":6,
                  "properties":{
                     "metrics":[
                        [
                           "AWS/EC2",
                           "CPUUtilization",
                           "InstanceId",
                           "i-012345"
                        ]
                     ],
                     "period":300,
                     "stat":"Average",
                     "region":"us-east-1",
                     "title":"EC2 Instance CPU"
                  }
               },
               {
                  "type":"text",
                  "x":0,
                  "y":7,
                  "width":3,
                  "height":3,
                  "properties":{
                     "markdown":"Hello world"
                  }
               }
           ]
         }
         
        \"\"\",
            dashboard_name="my-dashboard")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_body: The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).
        :param pulumi.Input[str] dashboard_name: The name of the dashboard.
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

            if dashboard_body is None:
                raise TypeError("Missing required property 'dashboard_body'")
            __props__['dashboard_body'] = dashboard_body
            if dashboard_name is None:
                raise TypeError("Missing required property 'dashboard_name'")
            __props__['dashboard_name'] = dashboard_name
            __props__['dashboard_arn'] = None
        super(Dashboard, __self__).__init__(
            'aws:cloudwatch/dashboard:Dashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_arn: Optional[pulumi.Input[str]] = None,
            dashboard_body: Optional[pulumi.Input[str]] = None,
            dashboard_name: Optional[pulumi.Input[str]] = None) -> 'Dashboard':
        """
        Get an existing Dashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_arn: The Amazon Resource Name (ARN) of the dashboard.
        :param pulumi.Input[str] dashboard_body: The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).
        :param pulumi.Input[str] dashboard_name: The name of the dashboard.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["dashboard_arn"] = dashboard_arn
        __props__["dashboard_body"] = dashboard_body
        __props__["dashboard_name"] = dashboard_name
        return Dashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardArn")
    def dashboard_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the dashboard.
        """
        return pulumi.get(self, "dashboard_arn")

    @property
    @pulumi.getter(name="dashboardBody")
    def dashboard_body(self) -> str:
        """
        The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html).
        """
        return pulumi.get(self, "dashboard_body")

    @property
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> str:
        """
        The name of the dashboard.
        """
        return pulumi.get(self, "dashboard_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


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

__all__ = ['RateBasedRule']


class RateBasedRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 predicates: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['RateBasedRulePredicateArgs']]]]] = None,
                 rate_key: Optional[pulumi.Input[str]] = None,
                 rate_limit: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a WAF Rate Based Rule Resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        ipset = aws.wafregional.IpSet("ipset", ip_set_descriptors=[aws.wafregional.IpSetIpSetDescriptorArgs(
            type="IPV4",
            value="192.0.7.0/24",
        )])
        wafrule = aws.wafregional.RateBasedRule("wafrule",
            metric_name="tfWAFRule",
            rate_key="IP",
            rate_limit=100,
            predicates=[aws.wafregional.RateBasedRulePredicateArgs(
                data_id=ipset.id,
                negated=False,
                type="IPMatch",
            )],
            opts=ResourceOptions(depends_on=[ipset]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['RateBasedRulePredicateArgs']]]] predicates: The objects to include in a rule (documented below).
        :param pulumi.Input[str] rate_key: Valid value is IP.
        :param pulumi.Input[float] rate_limit: The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
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

            if metric_name is None:
                raise TypeError("Missing required property 'metric_name'")
            __props__['metric_name'] = metric_name
            __props__['name'] = name
            __props__['predicates'] = predicates
            if rate_key is None:
                raise TypeError("Missing required property 'rate_key'")
            __props__['rate_key'] = rate_key
            if rate_limit is None:
                raise TypeError("Missing required property 'rate_limit'")
            __props__['rate_limit'] = rate_limit
            __props__['tags'] = tags
            __props__['arn'] = None
        super(RateBasedRule, __self__).__init__(
            'aws:wafregional/rateBasedRule:RateBasedRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            metric_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            predicates: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['RateBasedRulePredicateArgs']]]]] = None,
            rate_key: Optional[pulumi.Input[str]] = None,
            rate_limit: Optional[pulumi.Input[float]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'RateBasedRule':
        """
        Get an existing RateBasedRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the WAF Regional Rate Based Rule.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['RateBasedRulePredicateArgs']]]] predicates: The objects to include in a rule (documented below).
        :param pulumi.Input[str] rate_key: Valid value is IP.
        :param pulumi.Input[float] rate_limit: The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["metric_name"] = metric_name
        __props__["name"] = name
        __props__["predicates"] = predicates
        __props__["rate_key"] = rate_key
        __props__["rate_limit"] = rate_limit
        __props__["tags"] = tags
        return RateBasedRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the WAF Regional Rate Based Rule.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Output[str]:
        """
        The name or description for the Amazon CloudWatch metric of this rule.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name or description of the rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def predicates(self) -> pulumi.Output[Optional[List['outputs.RateBasedRulePredicate']]]:
        """
        The objects to include in a rule (documented below).
        """
        return pulumi.get(self, "predicates")

    @property
    @pulumi.getter(name="rateKey")
    def rate_key(self) -> pulumi.Output[str]:
        """
        Valid value is IP.
        """
        return pulumi.get(self, "rate_key")

    @property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> pulumi.Output[float]:
        """
        The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 100.
        """
        return pulumi.get(self, "rate_limit")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


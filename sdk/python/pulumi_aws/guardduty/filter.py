# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Filter']


class Filter(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 finding_criteria: Optional[pulumi.Input[pulumi.InputType['FilterFindingCriteriaArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rank: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage a GuardDuty filter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_filter = aws.guardduty.Filter("myFilter",
            action="ARCHIVE",
            detector_id=aws_guardduty_detector["example"]["id"],
            rank=1,
            finding_criteria=aws.guardduty.FilterFindingCriteriaArgs(
                criterions=[
                    aws.guardduty.FilterFindingCriteriaCriterionArgs(
                        field="region",
                        equals=["eu-west-1"],
                    ),
                    aws.guardduty.FilterFindingCriteriaCriterionArgs(
                        field="service.additionalInfo.threatListName",
                        not_equals=[
                            "some-threat",
                            "another-threat",
                        ],
                    ),
                    aws.guardduty.FilterFindingCriteriaCriterionArgs(
                        field="updatedAt",
                        greater_than="2020-01-01T00:00:00Z",
                        less_than="2020-02-01T00:00:00Z",
                    ),
                    aws.guardduty.FilterFindingCriteriaCriterionArgs(
                        field="severity",
                        greater_than_or_equal="4",
                    ),
                ],
            ))
        ```

        ## Import

        GuardDuty filters can be imported using the detector ID and filter's name separated by a colon, e.g.

        ```sh
         $ pulumi import aws:guardduty/filter:Filter MyFilter 00b00fd5aecc0ab60a708659477e9617:MyFilter
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
        :param pulumi.Input[str] description: Description of the filter.
        :param pulumi.Input[str] detector_id: ID of a GuardDuty detector, attached to your account.
        :param pulumi.Input[pulumi.InputType['FilterFindingCriteriaArgs']] finding_criteria: Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
        :param pulumi.Input[str] name: The name of your filter.
        :param pulumi.Input[int] rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags that you want to add to the Filter resource. A tag consists of a key and a value.
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

            if action is None:
                raise TypeError("Missing required property 'action'")
            __props__['action'] = action
            __props__['description'] = description
            if detector_id is None:
                raise TypeError("Missing required property 'detector_id'")
            __props__['detector_id'] = detector_id
            if finding_criteria is None:
                raise TypeError("Missing required property 'finding_criteria'")
            __props__['finding_criteria'] = finding_criteria
            __props__['name'] = name
            if rank is None:
                raise TypeError("Missing required property 'rank'")
            __props__['rank'] = rank
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Filter, __self__).__init__(
            'aws:guardduty/filter:Filter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            detector_id: Optional[pulumi.Input[str]] = None,
            finding_criteria: Optional[pulumi.Input[pulumi.InputType['FilterFindingCriteriaArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rank: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Filter':
        """
        Get an existing Filter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
        :param pulumi.Input[str] arn: The ARN of the GuardDuty filter.
        :param pulumi.Input[str] description: Description of the filter.
        :param pulumi.Input[str] detector_id: ID of a GuardDuty detector, attached to your account.
        :param pulumi.Input[pulumi.InputType['FilterFindingCriteriaArgs']] finding_criteria: Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
        :param pulumi.Input[str] name: The name of your filter.
        :param pulumi.Input[int] rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags that you want to add to the Filter resource. A tag consists of a key and a value.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["action"] = action
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["detector_id"] = detector_id
        __props__["finding_criteria"] = finding_criteria
        __props__["name"] = name
        __props__["rank"] = rank
        __props__["tags"] = tags
        return Filter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the GuardDuty filter.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the filter.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[str]:
        """
        ID of a GuardDuty detector, attached to your account.
        """
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter(name="findingCriteria")
    def finding_criteria(self) -> pulumi.Output['outputs.FilterFindingCriteria']:
        """
        Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
        """
        return pulumi.get(self, "finding_criteria")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of your filter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rank(self) -> pulumi.Output[int]:
        """
        Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
        """
        return pulumi.get(self, "rank")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags that you want to add to the Filter resource. A tag consists of a key and a value.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


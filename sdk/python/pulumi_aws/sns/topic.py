# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Topic']


class Topic(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 application_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 application_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
                 delivery_policy: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 http_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 http_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 http_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
                 kms_master_key_id: Optional[pulumi.Input[str]] = None,
                 lambda_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 lambda_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 lambda_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 sqs_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 sqs_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
                 sqs_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an SNS topic resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        user_updates = aws.sns.Topic("userUpdates")
        ```
        ## Example with Delivery Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        user_updates = aws.sns.Topic("userUpdates", delivery_policy=\"\"\"{
          "http": {
            "defaultHealthyRetryPolicy": {
              "minDelayTarget": 20,
              "maxDelayTarget": 20,
              "numRetries": 3,
              "numMaxDelayRetries": 0,
              "numNoDelayRetries": 0,
              "numMinDelayRetries": 0,
              "backoffFunction": "linear"
            },
            "disableSubscriptionOverrides": false,
            "defaultThrottlePolicy": {
              "maxReceivesPerSecond": 1
            }
          }
        }

        \"\"\")
        ```

        ## Example with Server-side encryption (SSE)

        ```python
        import pulumi
        import pulumi_aws as aws

        user_updates = aws.sns.Topic("userUpdates", kms_master_key_id="alias/aws/sns")
        ```

        ## Message Delivery Status Arguments

        The `<endpoint>_success_feedback_role_arn` and `<endpoint>_failure_feedback_role_arn` arguments are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The `<endpoint>_success_feedback_sample_rate` argument is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the  `<endpoint>_failure_feedback_role_arn` argument, then all failed message deliveries generate CloudWatch Logs.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] application_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] application_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[str] delivery_policy: The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        :param pulumi.Input[str] display_name: The display name for the SNS topic
        :param pulumi.Input[str] http_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] http_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] http_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[str] kms_master_key_id: The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
        :param pulumi.Input[str] lambda_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] lambda_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] lambda_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[str] name: The friendly name for the SNS topic. By default generated by this provider.
        :param pulumi.Input[str] name_prefix: The friendly name for the SNS topic. Conflicts with `name`.
        :param pulumi.Input[str] policy: The fully-formed AWS policy as JSON.
        :param pulumi.Input[str] sqs_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] sqs_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] sqs_success_feedback_sample_rate: Percentage of success to sample
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

            __props__['application_failure_feedback_role_arn'] = application_failure_feedback_role_arn
            __props__['application_success_feedback_role_arn'] = application_success_feedback_role_arn
            __props__['application_success_feedback_sample_rate'] = application_success_feedback_sample_rate
            __props__['delivery_policy'] = delivery_policy
            __props__['display_name'] = display_name
            __props__['http_failure_feedback_role_arn'] = http_failure_feedback_role_arn
            __props__['http_success_feedback_role_arn'] = http_success_feedback_role_arn
            __props__['http_success_feedback_sample_rate'] = http_success_feedback_sample_rate
            __props__['kms_master_key_id'] = kms_master_key_id
            __props__['lambda_failure_feedback_role_arn'] = lambda_failure_feedback_role_arn
            __props__['lambda_success_feedback_role_arn'] = lambda_success_feedback_role_arn
            __props__['lambda_success_feedback_sample_rate'] = lambda_success_feedback_sample_rate
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['policy'] = policy
            __props__['sqs_failure_feedback_role_arn'] = sqs_failure_feedback_role_arn
            __props__['sqs_success_feedback_role_arn'] = sqs_success_feedback_role_arn
            __props__['sqs_success_feedback_sample_rate'] = sqs_success_feedback_sample_rate
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Topic, __self__).__init__(
            'aws:sns/topic:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            application_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            application_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            delivery_policy: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            http_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            http_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            http_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
            kms_master_key_id: Optional[pulumi.Input[str]] = None,
            lambda_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            lambda_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            lambda_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            sqs_failure_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            sqs_success_feedback_role_arn: Optional[pulumi.Input[str]] = None,
            sqs_success_feedback_sample_rate: Optional[pulumi.Input[float]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Topic':
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] application_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] application_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[str] arn: The ARN of the SNS topic, as a more obvious property (clone of id)
        :param pulumi.Input[str] delivery_policy: The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        :param pulumi.Input[str] display_name: The display name for the SNS topic
        :param pulumi.Input[str] http_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] http_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] http_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[str] kms_master_key_id: The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
        :param pulumi.Input[str] lambda_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] lambda_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] lambda_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[str] name: The friendly name for the SNS topic. By default generated by this provider.
        :param pulumi.Input[str] name_prefix: The friendly name for the SNS topic. Conflicts with `name`.
        :param pulumi.Input[str] policy: The fully-formed AWS policy as JSON.
        :param pulumi.Input[str] sqs_failure_feedback_role_arn: IAM role for failure feedback
        :param pulumi.Input[str] sqs_success_feedback_role_arn: The IAM role permitted to receive success feedback for this topic
        :param pulumi.Input[float] sqs_success_feedback_sample_rate: Percentage of success to sample
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_failure_feedback_role_arn"] = application_failure_feedback_role_arn
        __props__["application_success_feedback_role_arn"] = application_success_feedback_role_arn
        __props__["application_success_feedback_sample_rate"] = application_success_feedback_sample_rate
        __props__["arn"] = arn
        __props__["delivery_policy"] = delivery_policy
        __props__["display_name"] = display_name
        __props__["http_failure_feedback_role_arn"] = http_failure_feedback_role_arn
        __props__["http_success_feedback_role_arn"] = http_success_feedback_role_arn
        __props__["http_success_feedback_sample_rate"] = http_success_feedback_sample_rate
        __props__["kms_master_key_id"] = kms_master_key_id
        __props__["lambda_failure_feedback_role_arn"] = lambda_failure_feedback_role_arn
        __props__["lambda_success_feedback_role_arn"] = lambda_success_feedback_role_arn
        __props__["lambda_success_feedback_sample_rate"] = lambda_success_feedback_sample_rate
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["policy"] = policy
        __props__["sqs_failure_feedback_role_arn"] = sqs_failure_feedback_role_arn
        __props__["sqs_success_feedback_role_arn"] = sqs_success_feedback_role_arn
        __props__["sqs_success_feedback_sample_rate"] = sqs_success_feedback_sample_rate
        __props__["tags"] = tags
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationFailureFeedbackRoleArn")
    def application_failure_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        IAM role for failure feedback
        """
        return pulumi.get(self, "application_failure_feedback_role_arn")

    @property
    @pulumi.getter(name="applicationSuccessFeedbackRoleArn")
    def application_success_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The IAM role permitted to receive success feedback for this topic
        """
        return pulumi.get(self, "application_success_feedback_role_arn")

    @property
    @pulumi.getter(name="applicationSuccessFeedbackSampleRate")
    def application_success_feedback_sample_rate(self) -> pulumi.Output[Optional[float]]:
        """
        Percentage of success to sample
        """
        return pulumi.get(self, "application_success_feedback_sample_rate")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the SNS topic, as a more obvious property (clone of id)
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        """
        return pulumi.get(self, "delivery_policy")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name for the SNS topic
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="httpFailureFeedbackRoleArn")
    def http_failure_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        IAM role for failure feedback
        """
        return pulumi.get(self, "http_failure_feedback_role_arn")

    @property
    @pulumi.getter(name="httpSuccessFeedbackRoleArn")
    def http_success_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The IAM role permitted to receive success feedback for this topic
        """
        return pulumi.get(self, "http_success_feedback_role_arn")

    @property
    @pulumi.getter(name="httpSuccessFeedbackSampleRate")
    def http_success_feedback_sample_rate(self) -> pulumi.Output[Optional[float]]:
        """
        Percentage of success to sample
        """
        return pulumi.get(self, "http_success_feedback_sample_rate")

    @property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
        """
        return pulumi.get(self, "kms_master_key_id")

    @property
    @pulumi.getter(name="lambdaFailureFeedbackRoleArn")
    def lambda_failure_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        IAM role for failure feedback
        """
        return pulumi.get(self, "lambda_failure_feedback_role_arn")

    @property
    @pulumi.getter(name="lambdaSuccessFeedbackRoleArn")
    def lambda_success_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The IAM role permitted to receive success feedback for this topic
        """
        return pulumi.get(self, "lambda_success_feedback_role_arn")

    @property
    @pulumi.getter(name="lambdaSuccessFeedbackSampleRate")
    def lambda_success_feedback_sample_rate(self) -> pulumi.Output[Optional[float]]:
        """
        Percentage of success to sample
        """
        return pulumi.get(self, "lambda_success_feedback_sample_rate")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The friendly name for the SNS topic. By default generated by this provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The friendly name for the SNS topic. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        The fully-formed AWS policy as JSON.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="sqsFailureFeedbackRoleArn")
    def sqs_failure_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        IAM role for failure feedback
        """
        return pulumi.get(self, "sqs_failure_feedback_role_arn")

    @property
    @pulumi.getter(name="sqsSuccessFeedbackRoleArn")
    def sqs_success_feedback_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The IAM role permitted to receive success feedback for this topic
        """
        return pulumi.get(self, "sqs_success_feedback_role_arn")

    @property
    @pulumi.getter(name="sqsSuccessFeedbackSampleRate")
    def sqs_success_feedback_sample_rate(self) -> pulumi.Output[Optional[float]]:
        """
        Percentage of success to sample
        """
        return pulumi.get(self, "sqs_success_feedback_sample_rate")

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


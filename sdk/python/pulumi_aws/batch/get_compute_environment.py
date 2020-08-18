# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetComputeEnvironmentResult',
    'AwaitableGetComputeEnvironmentResult',
    'get_compute_environment',
]



@pulumi.output_type
class GetComputeEnvironmentResult:
    """
    A collection of values returned by getComputeEnvironment.
    """
    def __init__(__self__, arn=None, compute_environment_name=None, ecs_cluster_arn=None, id=None, service_role=None, state=None, status=None, status_reason=None, type=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if compute_environment_name and not isinstance(compute_environment_name, str):
            raise TypeError("Expected argument 'compute_environment_name' to be a str")
        pulumi.set(__self__, "compute_environment_name", compute_environment_name)
        if ecs_cluster_arn and not isinstance(ecs_cluster_arn, str):
            raise TypeError("Expected argument 'ecs_cluster_arn' to be a str")
        pulumi.set(__self__, "ecs_cluster_arn", ecs_cluster_arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if service_role and not isinstance(service_role, str):
            raise TypeError("Expected argument 'service_role' to be a str")
        pulumi.set(__self__, "service_role", service_role)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_reason and not isinstance(status_reason, str):
            raise TypeError("Expected argument 'status_reason' to be a str")
        pulumi.set(__self__, "status_reason", status_reason)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the compute environment.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="computeEnvironmentName")
    def compute_environment_name(self) -> str:
        return pulumi.get(self, "compute_environment_name")

    @property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> str:
        """
        The ARN of the underlying Amazon ECS cluster used by the compute environment.
        """
        return pulumi.get(self, "ecs_cluster_arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> str:
        """
        The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
        """
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the compute environment (for example, `ENABLED` or `DISABLED`). If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the compute environment (for example, `CREATING` or `VALID`).
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> str:
        """
        A short, human-readable string to provide additional details about the current status of the compute environment.
        """
        return pulumi.get(self, "status_reason")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the compute environment (for example, `MANAGED` or `UNMANAGED`).
        """
        return pulumi.get(self, "type")



class AwaitableGetComputeEnvironmentResult(GetComputeEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputeEnvironmentResult(
            arn=self.arn,
            compute_environment_name=self.compute_environment_name,
            ecs_cluster_arn=self.ecs_cluster_arn,
            id=self.id,
            service_role=self.service_role,
            state=self.state,
            status=self.status,
            status_reason=self.status_reason,
            type=self.type)


def get_compute_environment(compute_environment_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComputeEnvironmentResult:
    """
    The Batch Compute Environment data source allows access to details of a specific
    compute environment within AWS Batch.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    batch_mongo = aws.batch.get_compute_environment(compute_environment_name="batch-mongo-production")
    ```


    :param str compute_environment_name: The name of the Batch Compute Environment
    """
    __args__ = dict()
    __args__['computeEnvironmentName'] = compute_environment_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:batch/getComputeEnvironment:getComputeEnvironment', __args__, opts=opts, typ=GetComputeEnvironmentResult).value

    return AwaitableGetComputeEnvironmentResult(
        arn=__ret__.arn,
        compute_environment_name=__ret__.compute_environment_name,
        ecs_cluster_arn=__ret__.ecs_cluster_arn,
        id=__ret__.id,
        service_role=__ret__.service_role,
        state=__ret__.state,
        status=__ret__.status,
        status_reason=__ret__.status_reason,
        type=__ret__.type)

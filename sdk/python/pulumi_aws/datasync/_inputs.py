# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'EfsLocationEc2ConfigArgs',
    'LocationSmbMountOptionsArgs',
    'NfsLocationOnPremConfigArgs',
    'S3LocationS3ConfigArgs',
    'TaskOptionsArgs',
]

@pulumi.input_type
class EfsLocationEc2ConfigArgs:
    def __init__(__self__, *,
                 security_group_arns: pulumi.Input[List[pulumi.Input[str]]],
                 subnet_arn: pulumi.Input[str]):
        """
        :param pulumi.Input[List[pulumi.Input[str]]] security_group_arns: List of Amazon Resource Names (ARNs) of the EC2 Security Groups that are associated with the EFS Mount Target.
        :param pulumi.Input[str] subnet_arn: Amazon Resource Name (ARN) of the EC2 Subnet that is associated with the EFS Mount Target.
        """
        pulumi.set(__self__, "security_group_arns", security_group_arns)
        pulumi.set(__self__, "subnet_arn", subnet_arn)

    @property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Input[List[pulumi.Input[str]]]:
        """
        List of Amazon Resource Names (ARNs) of the EC2 Security Groups that are associated with the EFS Mount Target.
        """
        return pulumi.get(self, "security_group_arns")

    @security_group_arns.setter
    def security_group_arns(self, value: pulumi.Input[List[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_arns", value)

    @property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Name (ARN) of the EC2 Subnet that is associated with the EFS Mount Target.
        """
        return pulumi.get(self, "subnet_arn")

    @subnet_arn.setter
    def subnet_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_arn", value)


@pulumi.input_type
class LocationSmbMountOptionsArgs:
    def __init__(__self__, *,
                 version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] version: The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: `AUTOMATIC`, `SMB2`, and `SMB3`. Default: `AUTOMATIC`
        """
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The specific SMB version that you want DataSync to use for mounting your SMB share. Valid values: `AUTOMATIC`, `SMB2`, and `SMB3`. Default: `AUTOMATIC`
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class NfsLocationOnPremConfigArgs:
    def __init__(__self__, *,
                 agent_arns: pulumi.Input[List[pulumi.Input[str]]]):
        """
        :param pulumi.Input[List[pulumi.Input[str]]] agent_arns: List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.
        """
        pulumi.set(__self__, "agent_arns", agent_arns)

    @property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Input[List[pulumi.Input[str]]]:
        """
        List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.
        """
        return pulumi.get(self, "agent_arns")

    @agent_arns.setter
    def agent_arns(self, value: pulumi.Input[List[pulumi.Input[str]]]):
        pulumi.set(self, "agent_arns", value)


@pulumi.input_type
class S3LocationS3ConfigArgs:
    def __init__(__self__, *,
                 bucket_access_role_arn: pulumi.Input[str]):
        """
        :param pulumi.Input[str] bucket_access_role_arn: Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.
        """
        pulumi.set(__self__, "bucket_access_role_arn", bucket_access_role_arn)

    @property
    @pulumi.getter(name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> pulumi.Input[str]:
        """
        Amazon Resource Names (ARN) of the IAM Role used to connect to the S3 Bucket.
        """
        return pulumi.get(self, "bucket_access_role_arn")

    @bucket_access_role_arn.setter
    def bucket_access_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_access_role_arn", value)


@pulumi.input_type
class TaskOptionsArgs:
    def __init__(__self__, *,
                 atime: Optional[pulumi.Input[str]] = None,
                 bytes_per_second: Optional[pulumi.Input[float]] = None,
                 gid: Optional[pulumi.Input[str]] = None,
                 mtime: Optional[pulumi.Input[str]] = None,
                 posix_permissions: Optional[pulumi.Input[str]] = None,
                 preserve_deleted_files: Optional[pulumi.Input[str]] = None,
                 preserve_devices: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 verify_mode: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] atime: A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to `BEST_EFFORT`, the DataSync Task attempts to preserve the original (that is, the version before sync `PREPARING` phase) `atime` attribute on all source files. Valid values: `BEST_EFFORT`, `NONE`. Default: `BEST_EFFORT`.
        :param pulumi.Input[float] bytes_per_second: Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to `1048576`. Value values: `-1` or greater. Default: `-1` (unlimited).
        :param pulumi.Input[str] gid: Group identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
        :param pulumi.Input[str] mtime: A file metadata that indicates the last time a file was modified (written to) before the sync `PREPARING` phase. Value values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
        :param pulumi.Input[str] posix_permissions: Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
        :param pulumi.Input[str] preserve_deleted_files: Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: `PRESERVE`, `REMOVE`. Default: `PRESERVE`.
        :param pulumi.Input[str] preserve_devices: Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: `NONE`, `PRESERVE`. Default: `NONE` (ignore special devices).
        :param pulumi.Input[str] uid: User identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
        :param pulumi.Input[str] verify_mode: Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: `NONE`, `POINT_IN_TIME_CONSISTENT`, `ONLY_FILES_TRANSFERRED`. Default: `POINT_IN_TIME_CONSISTENT`.
        """
        if atime is not None:
            pulumi.set(__self__, "atime", atime)
        if bytes_per_second is not None:
            pulumi.set(__self__, "bytes_per_second", bytes_per_second)
        if gid is not None:
            pulumi.set(__self__, "gid", gid)
        if mtime is not None:
            pulumi.set(__self__, "mtime", mtime)
        if posix_permissions is not None:
            pulumi.set(__self__, "posix_permissions", posix_permissions)
        if preserve_deleted_files is not None:
            pulumi.set(__self__, "preserve_deleted_files", preserve_deleted_files)
        if preserve_devices is not None:
            pulumi.set(__self__, "preserve_devices", preserve_devices)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if verify_mode is not None:
            pulumi.set(__self__, "verify_mode", verify_mode)

    @property
    @pulumi.getter
    def atime(self) -> Optional[pulumi.Input[str]]:
        """
        A file metadata that shows the last time a file was accessed (that is when the file was read or written to). If set to `BEST_EFFORT`, the DataSync Task attempts to preserve the original (that is, the version before sync `PREPARING` phase) `atime` attribute on all source files. Valid values: `BEST_EFFORT`, `NONE`. Default: `BEST_EFFORT`.
        """
        return pulumi.get(self, "atime")

    @atime.setter
    def atime(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "atime", value)

    @property
    @pulumi.getter(name="bytesPerSecond")
    def bytes_per_second(self) -> Optional[pulumi.Input[float]]:
        """
        Limits the bandwidth utilized. For example, to set a maximum of 1 MB, set this value to `1048576`. Value values: `-1` or greater. Default: `-1` (unlimited).
        """
        return pulumi.get(self, "bytes_per_second")

    @bytes_per_second.setter
    def bytes_per_second(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "bytes_per_second", value)

    @property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[str]]:
        """
        Group identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
        """
        return pulumi.get(self, "gid")

    @gid.setter
    def gid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gid", value)

    @property
    @pulumi.getter
    def mtime(self) -> Optional[pulumi.Input[str]]:
        """
        A file metadata that indicates the last time a file was modified (written to) before the sync `PREPARING` phase. Value values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
        """
        return pulumi.get(self, "mtime")

    @mtime.setter
    def mtime(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mtime", value)

    @property
    @pulumi.getter(name="posixPermissions")
    def posix_permissions(self) -> Optional[pulumi.Input[str]]:
        """
        Determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file. Valid values: `NONE`, `PRESERVE`. Default: `PRESERVE`.
        """
        return pulumi.get(self, "posix_permissions")

    @posix_permissions.setter
    def posix_permissions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "posix_permissions", value)

    @property
    @pulumi.getter(name="preserveDeletedFiles")
    def preserve_deleted_files(self) -> Optional[pulumi.Input[str]]:
        """
        Whether files deleted in the source should be removed or preserved in the destination file system. Valid values: `PRESERVE`, `REMOVE`. Default: `PRESERVE`.
        """
        return pulumi.get(self, "preserve_deleted_files")

    @preserve_deleted_files.setter
    def preserve_deleted_files(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preserve_deleted_files", value)

    @property
    @pulumi.getter(name="preserveDevices")
    def preserve_devices(self) -> Optional[pulumi.Input[str]]:
        """
        Whether the DataSync Task should preserve the metadata of block and character devices in the source files system, and recreate the files with that device name and metadata on the destination. The DataSync Task can’t sync the actual contents of such devices, because many of the devices are non-terminal and don’t return an end of file (EOF) marker. Valid values: `NONE`, `PRESERVE`. Default: `NONE` (ignore special devices).
        """
        return pulumi.get(self, "preserve_devices")

    @preserve_devices.setter
    def preserve_devices(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preserve_devices", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        User identifier of the file's owners. Valid values: `BOTH`, `INT_VALUE`, `NAME`, `NONE`. Default: `INT_VALUE` (preserve integer value of the ID).
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter(name="verifyMode")
    def verify_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred. Valid values: `NONE`, `POINT_IN_TIME_CONSISTENT`, `ONLY_FILES_TRANSFERRED`. Default: `POINT_IN_TIME_CONSISTENT`.
        """
        return pulumi.get(self, "verify_mode")

    @verify_mode.setter
    def verify_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verify_mode", value)



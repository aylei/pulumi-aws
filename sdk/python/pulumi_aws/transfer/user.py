# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['User']


class User(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the `transfer.SshKey` resource.

        ```python
        import pulumi
        import pulumi_aws as aws

        foo_server = aws.transfer.Server("fooServer",
            identity_provider_type="SERVICE_MANAGED",
            tags={
                "NAME": "tf-acc-test-transfer-server",
            })
        foo_role = aws.iam.Role("fooRole", assume_role_policy=\"\"\"{
        	"Version": "2012-10-17",
        	"Statement": [
        		{
        		"Effect": "Allow",
        		"Principal": {
        			"Service": "transfer.amazonaws.com"
        		},
        		"Action": "sts:AssumeRole"
        		}
        	]
        }
        \"\"\")
        foo_role_policy = aws.iam.RolePolicy("fooRolePolicy",
            role=foo_role.id,
            policy=\"\"\"{
        	"Version": "2012-10-17",
        	"Statement": [
        		{
        			"Sid": "AllowFullAccesstoS3",
        			"Effect": "Allow",
        			"Action": [
        				"s3:*"
        			],
        			"Resource": "*"
        		}
        	]
        }
        \"\"\")
        foo_user = aws.transfer.User("fooUser",
            server_id=foo_server.id,
            user_name="tftestuser",
            role=foo_role.arn)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] home_directory: The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        :param pulumi.Input[str] policy: An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. These are evaluated on-the-fly when navigating the bucket.
        :param pulumi.Input[str] role: Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] user_name: The name used for log in to your SFTP server.
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

            __props__['home_directory'] = home_directory
            __props__['policy'] = policy
            if role is None:
                raise TypeError("Missing required property 'role'")
            __props__['role'] = role
            if server_id is None:
                raise TypeError("Missing required property 'server_id'")
            __props__['server_id'] = server_id
            __props__['tags'] = tags
            if user_name is None:
                raise TypeError("Missing required property 'user_name'")
            __props__['user_name'] = user_name
            __props__['arn'] = None
        super(User, __self__).__init__(
            'aws:transfer/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            home_directory: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user_name: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Transfer User
        :param pulumi.Input[str] home_directory: The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        :param pulumi.Input[str] policy: An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. These are evaluated on-the-fly when navigating the bucket.
        :param pulumi.Input[str] role: Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        :param pulumi.Input[str] server_id: The Server ID of the Transfer Server (e.g. `s-12345678`)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] user_name: The name used for log in to your SFTP server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["home_directory"] = home_directory
        __props__["policy"] = policy
        __props__["role"] = role
        __props__["server_id"] = server_id
        __props__["tags"] = tags
        __props__["user_name"] = user_name
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of Transfer User
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[str]]:
        """
        The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
        """
        return pulumi.get(self, "home_directory")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[str]]:
        """
        An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. These are evaluated on-the-fly when navigating the bucket.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The Server ID of the Transfer Server (e.g. `s-12345678`)
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        The name used for log in to your SFTP server.
        """
        return pulumi.get(self, "user_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


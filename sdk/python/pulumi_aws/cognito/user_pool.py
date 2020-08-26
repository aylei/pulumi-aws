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

__all__ = ['UserPool']


class UserPool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_create_user_config: Optional[pulumi.Input[pulumi.InputType['UserPoolAdminCreateUserConfigArgs']]] = None,
                 alias_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 auto_verified_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 device_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolDeviceConfigurationArgs']]] = None,
                 email_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolEmailConfigurationArgs']]] = None,
                 email_verification_message: Optional[pulumi.Input[str]] = None,
                 email_verification_subject: Optional[pulumi.Input[str]] = None,
                 lambda_config: Optional[pulumi.Input[pulumi.InputType['UserPoolLambdaConfigArgs']]] = None,
                 mfa_configuration: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password_policy: Optional[pulumi.Input[pulumi.InputType['UserPoolPasswordPolicyArgs']]] = None,
                 schemas: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['UserPoolSchemaArgs']]]]] = None,
                 sms_authentication_message: Optional[pulumi.Input[str]] = None,
                 sms_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolSmsConfigurationArgs']]] = None,
                 sms_verification_message: Optional[pulumi.Input[str]] = None,
                 software_token_mfa_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolSoftwareTokenMfaConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_pool_add_ons: Optional[pulumi.Input[pulumi.InputType['UserPoolUserPoolAddOnsArgs']]] = None,
                 username_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 username_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolUsernameConfigurationArgs']]] = None,
                 verification_message_template: Optional[pulumi.Input[pulumi.InputType['UserPoolVerificationMessageTemplateArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Cognito User Pool resource.

        ## Example Usage
        ### Basic configuration

        ```python
        import pulumi
        import pulumi_aws as aws

        pool = aws.cognito.UserPool("pool")
        ```
        ### Enabling SMS and Software Token Multi-Factor Authentication

        ```python
        import pulumi
        import pulumi_aws as aws

        # ... other configuration ...
        example = aws.cognito.UserPool("example",
            mfa_configuration="ON",
            sms_authentication_message="Your code is {####}",
            sms_configuration=aws.cognito.UserPoolSmsConfigurationArgs(
                external_id="example",
                sns_caller_arn=aws_iam_role["example"]["arn"],
            ),
            software_token_mfa_configuration=aws.cognito.UserPoolSoftwareTokenMfaConfigurationArgs(
                enabled=True,
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['UserPoolAdminCreateUserConfigArgs']] admin_create_user_config: The configuration for AdminCreateUser requests.
        :param pulumi.Input[List[pulumi.Input[str]]] alias_attributes: Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
        :param pulumi.Input[List[pulumi.Input[str]]] auto_verified_attributes: The attributes to be auto-verified. Possible values: email, phone_number.
        :param pulumi.Input[pulumi.InputType['UserPoolDeviceConfigurationArgs']] device_configuration: The configuration for the user pool's device tracking.
        :param pulumi.Input[pulumi.InputType['UserPoolEmailConfigurationArgs']] email_configuration: The Email Configuration.
        :param pulumi.Input[str] email_verification_message: A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
        :param pulumi.Input[str] email_verification_subject: A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
        :param pulumi.Input[pulumi.InputType['UserPoolLambdaConfigArgs']] lambda_config: A container for the AWS Lambda triggers associated with the user pool.
        :param pulumi.Input[str] mfa_configuration: Multi-Factor Authentication (MFA) configuration for the User Pool. Defaults of `OFF`. Valid values:
        :param pulumi.Input[str] name: The name of the attribute.
        :param pulumi.Input[pulumi.InputType['UserPoolPasswordPolicyArgs']] password_policy: A container for information about the user pool password policy.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['UserPoolSchemaArgs']]]] schemas: A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
        :param pulumi.Input[str] sms_authentication_message: A string representing the SMS authentication message. The message must contain the `{####}` placeholder, which will be replaced with the code.
        :param pulumi.Input[pulumi.InputType['UserPoolSmsConfigurationArgs']] sms_configuration: Configuration block for Short Message Service (SMS) settings. Detailed below. These settings apply to SMS user verification and SMS Multi-Factor Authentication (MFA). Due to Cognito API restrictions, the SMS configuration cannot be removed without recreating the Cognito User Pool. For user data safety, this resource will ignore the removal of this configuration by disabling drift detection. To force resource recreation after this configuration has been applied, see the [`up` command and use --replace](https://www.pulumi.com/docs/reference/cli/pulumi_up/).
        :param pulumi.Input[str] sms_verification_message: A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
        :param pulumi.Input[pulumi.InputType['UserPoolSoftwareTokenMfaConfigurationArgs']] software_token_mfa_configuration: Configuration block for software token Mult-Factor Authentication (MFA) settings. Detailed below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the User Pool.
        :param pulumi.Input[pulumi.InputType['UserPoolUserPoolAddOnsArgs']] user_pool_add_ons: Configuration block for user pool add-ons to enable user pool advanced security mode features.
        :param pulumi.Input[List[pulumi.Input[str]]] username_attributes: Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
        :param pulumi.Input[pulumi.InputType['UserPoolUsernameConfigurationArgs']] username_configuration: The Username Configuration.
        :param pulumi.Input[pulumi.InputType['UserPoolVerificationMessageTemplateArgs']] verification_message_template: The verification message templates configuration.
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

            __props__['admin_create_user_config'] = admin_create_user_config
            __props__['alias_attributes'] = alias_attributes
            __props__['auto_verified_attributes'] = auto_verified_attributes
            __props__['device_configuration'] = device_configuration
            __props__['email_configuration'] = email_configuration
            __props__['email_verification_message'] = email_verification_message
            __props__['email_verification_subject'] = email_verification_subject
            __props__['lambda_config'] = lambda_config
            __props__['mfa_configuration'] = mfa_configuration
            __props__['name'] = name
            __props__['password_policy'] = password_policy
            __props__['schemas'] = schemas
            __props__['sms_authentication_message'] = sms_authentication_message
            __props__['sms_configuration'] = sms_configuration
            __props__['sms_verification_message'] = sms_verification_message
            __props__['software_token_mfa_configuration'] = software_token_mfa_configuration
            __props__['tags'] = tags
            __props__['user_pool_add_ons'] = user_pool_add_ons
            __props__['username_attributes'] = username_attributes
            __props__['username_configuration'] = username_configuration
            __props__['verification_message_template'] = verification_message_template
            __props__['arn'] = None
            __props__['creation_date'] = None
            __props__['endpoint'] = None
            __props__['last_modified_date'] = None
        super(UserPool, __self__).__init__(
            'aws:cognito/userPool:UserPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_create_user_config: Optional[pulumi.Input[pulumi.InputType['UserPoolAdminCreateUserConfigArgs']]] = None,
            alias_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            auto_verified_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            creation_date: Optional[pulumi.Input[str]] = None,
            device_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolDeviceConfigurationArgs']]] = None,
            email_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolEmailConfigurationArgs']]] = None,
            email_verification_message: Optional[pulumi.Input[str]] = None,
            email_verification_subject: Optional[pulumi.Input[str]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            lambda_config: Optional[pulumi.Input[pulumi.InputType['UserPoolLambdaConfigArgs']]] = None,
            last_modified_date: Optional[pulumi.Input[str]] = None,
            mfa_configuration: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password_policy: Optional[pulumi.Input[pulumi.InputType['UserPoolPasswordPolicyArgs']]] = None,
            schemas: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['UserPoolSchemaArgs']]]]] = None,
            sms_authentication_message: Optional[pulumi.Input[str]] = None,
            sms_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolSmsConfigurationArgs']]] = None,
            sms_verification_message: Optional[pulumi.Input[str]] = None,
            software_token_mfa_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolSoftwareTokenMfaConfigurationArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user_pool_add_ons: Optional[pulumi.Input[pulumi.InputType['UserPoolUserPoolAddOnsArgs']]] = None,
            username_attributes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            username_configuration: Optional[pulumi.Input[pulumi.InputType['UserPoolUsernameConfigurationArgs']]] = None,
            verification_message_template: Optional[pulumi.Input[pulumi.InputType['UserPoolVerificationMessageTemplateArgs']]] = None) -> 'UserPool':
        """
        Get an existing UserPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['UserPoolAdminCreateUserConfigArgs']] admin_create_user_config: The configuration for AdminCreateUser requests.
        :param pulumi.Input[List[pulumi.Input[str]]] alias_attributes: Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
        :param pulumi.Input[str] arn: The ARN of the user pool.
        :param pulumi.Input[List[pulumi.Input[str]]] auto_verified_attributes: The attributes to be auto-verified. Possible values: email, phone_number.
        :param pulumi.Input[str] creation_date: The date the user pool was created.
        :param pulumi.Input[pulumi.InputType['UserPoolDeviceConfigurationArgs']] device_configuration: The configuration for the user pool's device tracking.
        :param pulumi.Input[pulumi.InputType['UserPoolEmailConfigurationArgs']] email_configuration: The Email Configuration.
        :param pulumi.Input[str] email_verification_message: A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
        :param pulumi.Input[str] email_verification_subject: A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
        :param pulumi.Input[str] endpoint: The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
        :param pulumi.Input[pulumi.InputType['UserPoolLambdaConfigArgs']] lambda_config: A container for the AWS Lambda triggers associated with the user pool.
        :param pulumi.Input[str] last_modified_date: The date the user pool was last modified.
        :param pulumi.Input[str] mfa_configuration: Multi-Factor Authentication (MFA) configuration for the User Pool. Defaults of `OFF`. Valid values:
        :param pulumi.Input[str] name: The name of the attribute.
        :param pulumi.Input[pulumi.InputType['UserPoolPasswordPolicyArgs']] password_policy: A container for information about the user pool password policy.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['UserPoolSchemaArgs']]]] schemas: A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
        :param pulumi.Input[str] sms_authentication_message: A string representing the SMS authentication message. The message must contain the `{####}` placeholder, which will be replaced with the code.
        :param pulumi.Input[pulumi.InputType['UserPoolSmsConfigurationArgs']] sms_configuration: Configuration block for Short Message Service (SMS) settings. Detailed below. These settings apply to SMS user verification and SMS Multi-Factor Authentication (MFA). Due to Cognito API restrictions, the SMS configuration cannot be removed without recreating the Cognito User Pool. For user data safety, this resource will ignore the removal of this configuration by disabling drift detection. To force resource recreation after this configuration has been applied, see the [`up` command and use --replace](https://www.pulumi.com/docs/reference/cli/pulumi_up/).
        :param pulumi.Input[str] sms_verification_message: A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
        :param pulumi.Input[pulumi.InputType['UserPoolSoftwareTokenMfaConfigurationArgs']] software_token_mfa_configuration: Configuration block for software token Mult-Factor Authentication (MFA) settings. Detailed below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the User Pool.
        :param pulumi.Input[pulumi.InputType['UserPoolUserPoolAddOnsArgs']] user_pool_add_ons: Configuration block for user pool add-ons to enable user pool advanced security mode features.
        :param pulumi.Input[List[pulumi.Input[str]]] username_attributes: Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
        :param pulumi.Input[pulumi.InputType['UserPoolUsernameConfigurationArgs']] username_configuration: The Username Configuration.
        :param pulumi.Input[pulumi.InputType['UserPoolVerificationMessageTemplateArgs']] verification_message_template: The verification message templates configuration.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_create_user_config"] = admin_create_user_config
        __props__["alias_attributes"] = alias_attributes
        __props__["arn"] = arn
        __props__["auto_verified_attributes"] = auto_verified_attributes
        __props__["creation_date"] = creation_date
        __props__["device_configuration"] = device_configuration
        __props__["email_configuration"] = email_configuration
        __props__["email_verification_message"] = email_verification_message
        __props__["email_verification_subject"] = email_verification_subject
        __props__["endpoint"] = endpoint
        __props__["lambda_config"] = lambda_config
        __props__["last_modified_date"] = last_modified_date
        __props__["mfa_configuration"] = mfa_configuration
        __props__["name"] = name
        __props__["password_policy"] = password_policy
        __props__["schemas"] = schemas
        __props__["sms_authentication_message"] = sms_authentication_message
        __props__["sms_configuration"] = sms_configuration
        __props__["sms_verification_message"] = sms_verification_message
        __props__["software_token_mfa_configuration"] = software_token_mfa_configuration
        __props__["tags"] = tags
        __props__["user_pool_add_ons"] = user_pool_add_ons
        __props__["username_attributes"] = username_attributes
        __props__["username_configuration"] = username_configuration
        __props__["verification_message_template"] = verification_message_template
        return UserPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminCreateUserConfig")
    def admin_create_user_config(self) -> pulumi.Output['outputs.UserPoolAdminCreateUserConfig']:
        """
        The configuration for AdminCreateUser requests.
        """
        return pulumi.get(self, "admin_create_user_config")

    @property
    @pulumi.getter(name="aliasAttributes")
    def alias_attributes(self) -> pulumi.Output[Optional[List[str]]]:
        """
        Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
        """
        return pulumi.get(self, "alias_attributes")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the user pool.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoVerifiedAttributes")
    def auto_verified_attributes(self) -> pulumi.Output[Optional[List[str]]]:
        """
        The attributes to be auto-verified. Possible values: email, phone_number.
        """
        return pulumi.get(self, "auto_verified_attributes")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The date the user pool was created.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(self) -> pulumi.Output[Optional['outputs.UserPoolDeviceConfiguration']]:
        """
        The configuration for the user pool's device tracking.
        """
        return pulumi.get(self, "device_configuration")

    @property
    @pulumi.getter(name="emailConfiguration")
    def email_configuration(self) -> pulumi.Output[Optional['outputs.UserPoolEmailConfiguration']]:
        """
        The Email Configuration.
        """
        return pulumi.get(self, "email_configuration")

    @property
    @pulumi.getter(name="emailVerificationMessage")
    def email_verification_message(self) -> pulumi.Output[str]:
        """
        A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
        """
        return pulumi.get(self, "email_verification_message")

    @property
    @pulumi.getter(name="emailVerificationSubject")
    def email_verification_subject(self) -> pulumi.Output[str]:
        """
        A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
        """
        return pulumi.get(self, "email_verification_subject")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> pulumi.Output['outputs.UserPoolLambdaConfig']:
        """
        A container for the AWS Lambda triggers associated with the user pool.
        """
        return pulumi.get(self, "lambda_config")

    @property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> pulumi.Output[str]:
        """
        The date the user pool was last modified.
        """
        return pulumi.get(self, "last_modified_date")

    @property
    @pulumi.getter(name="mfaConfiguration")
    def mfa_configuration(self) -> pulumi.Output[Optional[str]]:
        """
        Multi-Factor Authentication (MFA) configuration for the User Pool. Defaults of `OFF`. Valid values:
        """
        return pulumi.get(self, "mfa_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the attribute.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> pulumi.Output['outputs.UserPoolPasswordPolicy']:
        """
        A container for information about the user pool password policy.
        """
        return pulumi.get(self, "password_policy")

    @property
    @pulumi.getter
    def schemas(self) -> pulumi.Output[Optional[List['outputs.UserPoolSchema']]]:
        """
        A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter(name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> pulumi.Output[Optional[str]]:
        """
        A string representing the SMS authentication message. The message must contain the `{####}` placeholder, which will be replaced with the code.
        """
        return pulumi.get(self, "sms_authentication_message")

    @property
    @pulumi.getter(name="smsConfiguration")
    def sms_configuration(self) -> pulumi.Output['outputs.UserPoolSmsConfiguration']:
        """
        Configuration block for Short Message Service (SMS) settings. Detailed below. These settings apply to SMS user verification and SMS Multi-Factor Authentication (MFA). Due to Cognito API restrictions, the SMS configuration cannot be removed without recreating the Cognito User Pool. For user data safety, this resource will ignore the removal of this configuration by disabling drift detection. To force resource recreation after this configuration has been applied, see the [`up` command and use --replace](https://www.pulumi.com/docs/reference/cli/pulumi_up/).
        """
        return pulumi.get(self, "sms_configuration")

    @property
    @pulumi.getter(name="smsVerificationMessage")
    def sms_verification_message(self) -> pulumi.Output[str]:
        """
        A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
        """
        return pulumi.get(self, "sms_verification_message")

    @property
    @pulumi.getter(name="softwareTokenMfaConfiguration")
    def software_token_mfa_configuration(self) -> pulumi.Output[Optional['outputs.UserPoolSoftwareTokenMfaConfiguration']]:
        """
        Configuration block for software token Mult-Factor Authentication (MFA) settings. Detailed below.
        """
        return pulumi.get(self, "software_token_mfa_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the User Pool.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userPoolAddOns")
    def user_pool_add_ons(self) -> pulumi.Output[Optional['outputs.UserPoolUserPoolAddOns']]:
        """
        Configuration block for user pool add-ons to enable user pool advanced security mode features.
        """
        return pulumi.get(self, "user_pool_add_ons")

    @property
    @pulumi.getter(name="usernameAttributes")
    def username_attributes(self) -> pulumi.Output[Optional[List[str]]]:
        """
        Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
        """
        return pulumi.get(self, "username_attributes")

    @property
    @pulumi.getter(name="usernameConfiguration")
    def username_configuration(self) -> pulumi.Output[Optional['outputs.UserPoolUsernameConfiguration']]:
        """
        The Username Configuration.
        """
        return pulumi.get(self, "username_configuration")

    @property
    @pulumi.getter(name="verificationMessageTemplate")
    def verification_message_template(self) -> pulumi.Output['outputs.UserPoolVerificationMessageTemplate']:
        """
        The verification message templates configuration.
        """
        return pulumi.get(self, "verification_message_template")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


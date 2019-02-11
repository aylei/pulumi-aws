# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class MethodResponse(pulumi.CustomResource):
    http_method: pulumi.Output[str]
    """
    The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
    """
    resource_id: pulumi.Output[str]
    """
    The API resource ID
    """
    response_models: pulumi.Output[dict]
    """
    A map of the API models used for the response's content type
    """
    response_parameters: pulumi.Output[dict]
    """
    A map of response parameters that can be sent to the caller.
    For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
    would define that the header `X-Some-Header` can be provided on the response.
    """
    response_parameters_in_json: pulumi.Output[str]
    """
    **Deprecated**, use `response_parameters` instead.
    """
    rest_api: pulumi.Output[str]
    """
    The ID of the associated REST API
    """
    status_code: pulumi.Output[str]
    """
    The HTTP status code
    """
    def __init__(__self__, resource_name, opts=None, http_method=None, resource_id=None, response_models=None, response_parameters=None, response_parameters_in_json=None, rest_api=None, status_code=None, __name__=None, __opts__=None):
        """
        Provides an HTTP Method Response for an API Gateway Resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] http_method: The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
        :param pulumi.Input[str] resource_id: The API resource ID
        :param pulumi.Input[dict] response_models: A map of the API models used for the response's content type
        :param pulumi.Input[dict] response_parameters: A map of response parameters that can be sent to the caller.
               For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
               would define that the header `X-Some-Header` can be provided on the response.
        :param pulumi.Input[str] response_parameters_in_json: **Deprecated**, use `response_parameters` instead.
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] status_code: The HTTP status code
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

        if http_method is None:
            raise TypeError('Missing required property http_method')
        __props__['http_method'] = http_method

        if resource_id is None:
            raise TypeError('Missing required property resource_id')
        __props__['resource_id'] = resource_id

        __props__['response_models'] = response_models

        __props__['response_parameters'] = response_parameters

        __props__['response_parameters_in_json'] = response_parameters_in_json

        if rest_api is None:
            raise TypeError('Missing required property rest_api')
        __props__['rest_api'] = rest_api

        if status_code is None:
            raise TypeError('Missing required property status_code')
        __props__['status_code'] = status_code

        super(MethodResponse, __self__).__init__(
            'aws:apigateway/methodResponse:MethodResponse',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


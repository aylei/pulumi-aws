# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ApiCorsConfiguration',
    'AuthorizerJwtConfiguration',
    'DomainNameDomainNameConfiguration',
    'StageAccessLogSettings',
    'StageDefaultRouteSettings',
    'StageRouteSetting',
]

@pulumi.output_type
class ApiCorsConfiguration(dict):
    def __init__(__self__, *,
                 allow_credentials: Optional[bool] = None,
                 allow_headers: Optional[List[str]] = None,
                 allow_methods: Optional[List[str]] = None,
                 allow_origins: Optional[List[str]] = None,
                 expose_headers: Optional[List[str]] = None,
                 max_age: Optional[float] = None):
        """
        :param bool allow_credentials: Whether credentials are included in the CORS request.
        :param List[str] allow_headers: The set of allowed HTTP headers.
        :param List[str] allow_methods: The set of allowed HTTP methods.
        :param List[str] allow_origins: The set of allowed origins.
        :param List[str] expose_headers: The set of exposed HTTP headers.
        :param float max_age: The number of seconds that the browser should cache preflight request results.
        """
        if allow_credentials is not None:
            pulumi.set(__self__, "allow_credentials", allow_credentials)
        if allow_headers is not None:
            pulumi.set(__self__, "allow_headers", allow_headers)
        if allow_methods is not None:
            pulumi.set(__self__, "allow_methods", allow_methods)
        if allow_origins is not None:
            pulumi.set(__self__, "allow_origins", allow_origins)
        if expose_headers is not None:
            pulumi.set(__self__, "expose_headers", expose_headers)
        if max_age is not None:
            pulumi.set(__self__, "max_age", max_age)

    @property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[bool]:
        """
        Whether credentials are included in the CORS request.
        """
        return pulumi.get(self, "allow_credentials")

    @property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[List[str]]:
        """
        The set of allowed HTTP headers.
        """
        return pulumi.get(self, "allow_headers")

    @property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[List[str]]:
        """
        The set of allowed HTTP methods.
        """
        return pulumi.get(self, "allow_methods")

    @property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[List[str]]:
        """
        The set of allowed origins.
        """
        return pulumi.get(self, "allow_origins")

    @property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[List[str]]:
        """
        The set of exposed HTTP headers.
        """
        return pulumi.get(self, "expose_headers")

    @property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[float]:
        """
        The number of seconds that the browser should cache preflight request results.
        """
        return pulumi.get(self, "max_age")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AuthorizerJwtConfiguration(dict):
    def __init__(__self__, *,
                 audiences: Optional[List[str]] = None,
                 issuer: Optional[str] = None):
        """
        :param List[str] audiences: A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.
        :param str issuer: The base domain of the identity provider that issues JSON Web Tokens, such as the `endpoint` attribute of the `cognito.UserPool` resource.
        """
        if audiences is not None:
            pulumi.set(__self__, "audiences", audiences)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[List[str]]:
        """
        A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.
        """
        return pulumi.get(self, "audiences")

    @property
    @pulumi.getter
    def issuer(self) -> Optional[str]:
        """
        The base domain of the identity provider that issues JSON Web Tokens, such as the `endpoint` attribute of the `cognito.UserPool` resource.
        """
        return pulumi.get(self, "issuer")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainNameDomainNameConfiguration(dict):
    def __init__(__self__, *,
                 certificate_arn: str,
                 endpoint_type: str,
                 security_policy: str,
                 hosted_zone_id: Optional[str] = None,
                 target_domain_name: Optional[str] = None):
        """
        :param str certificate_arn: The ARN of an AWS-managed certificate that will be used by the endpoint for the domain name. AWS Certificate Manager is the only supported source.
               Use the `acm.Certificate` resource to configure an ACM certificate.
        :param str endpoint_type: The endpoint type. Valid values: `REGIONAL`.
        :param str security_policy: The Transport Layer Security (TLS) version of the [security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) for the domain name. Valid values: `TLS_1_2`.
        :param str hosted_zone_id: The Amazon Route 53 Hosted Zone ID of the endpoint.
        :param str target_domain_name: The target domain name.
        """
        pulumi.set(__self__, "certificate_arn", certificate_arn)
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        pulumi.set(__self__, "security_policy", security_policy)
        if hosted_zone_id is not None:
            pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if target_domain_name is not None:
            pulumi.set(__self__, "target_domain_name", target_domain_name)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> str:
        """
        The ARN of an AWS-managed certificate that will be used by the endpoint for the domain name. AWS Certificate Manager is the only supported source.
        Use the `acm.Certificate` resource to configure an ACM certificate.
        """
        return pulumi.get(self, "certificate_arn")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        The endpoint type. Valid values: `REGIONAL`.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> str:
        """
        The Transport Layer Security (TLS) version of the [security policy](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) for the domain name. Valid values: `TLS_1_2`.
        """
        return pulumi.get(self, "security_policy")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[str]:
        """
        The Amazon Route 53 Hosted Zone ID of the endpoint.
        """
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="targetDomainName")
    def target_domain_name(self) -> Optional[str]:
        """
        The target domain name.
        """
        return pulumi.get(self, "target_domain_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class StageAccessLogSettings(dict):
    def __init__(__self__, *,
                 destination_arn: str,
                 format: str):
        """
        :param str destination_arn: The ARN of the CloudWatch Logs log group to receive access logs. Any trailing `:*` is trimmed from the ARN.
        :param str format: A single line [format](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#apigateway-cloudwatch-log-formats) of the access logs of data, as specified by [selected $context variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html).
        """
        pulumi.set(__self__, "destination_arn", destination_arn)
        pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> str:
        """
        The ARN of the CloudWatch Logs log group to receive access logs. Any trailing `:*` is trimmed from the ARN.
        """
        return pulumi.get(self, "destination_arn")

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        A single line [format](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#apigateway-cloudwatch-log-formats) of the access logs of data, as specified by [selected $context variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html).
        """
        return pulumi.get(self, "format")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class StageDefaultRouteSettings(dict):
    def __init__(__self__, *,
                 data_trace_enabled: Optional[bool] = None,
                 detailed_metrics_enabled: Optional[bool] = None,
                 logging_level: Optional[str] = None,
                 throttling_burst_limit: Optional[float] = None,
                 throttling_rate_limit: Optional[float] = None):
        """
        :param bool data_trace_enabled: Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
               Defaults to `false`. Supported only for WebSocket APIs.
        :param bool detailed_metrics_enabled: Whether detailed metrics are enabled for the default route. Defaults to `false`.
        :param str logging_level: The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
               Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs.
        :param float throttling_burst_limit: The throttling burst limit for the default route.
        :param float throttling_rate_limit: The throttling rate limit for the default route.
        """
        if data_trace_enabled is not None:
            pulumi.set(__self__, "data_trace_enabled", data_trace_enabled)
        if detailed_metrics_enabled is not None:
            pulumi.set(__self__, "detailed_metrics_enabled", detailed_metrics_enabled)
        if logging_level is not None:
            pulumi.set(__self__, "logging_level", logging_level)
        if throttling_burst_limit is not None:
            pulumi.set(__self__, "throttling_burst_limit", throttling_burst_limit)
        if throttling_rate_limit is not None:
            pulumi.set(__self__, "throttling_rate_limit", throttling_rate_limit)

    @property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[bool]:
        """
        Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
        Defaults to `false`. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "data_trace_enabled")

    @property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[bool]:
        """
        Whether detailed metrics are enabled for the default route. Defaults to `false`.
        """
        return pulumi.get(self, "detailed_metrics_enabled")

    @property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[str]:
        """
        The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
        Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "logging_level")

    @property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[float]:
        """
        The throttling burst limit for the default route.
        """
        return pulumi.get(self, "throttling_burst_limit")

    @property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[float]:
        """
        The throttling rate limit for the default route.
        """
        return pulumi.get(self, "throttling_rate_limit")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class StageRouteSetting(dict):
    def __init__(__self__, *,
                 route_key: str,
                 data_trace_enabled: Optional[bool] = None,
                 detailed_metrics_enabled: Optional[bool] = None,
                 logging_level: Optional[str] = None,
                 throttling_burst_limit: Optional[float] = None,
                 throttling_rate_limit: Optional[float] = None):
        """
        :param str route_key: Route key.
        :param bool data_trace_enabled: Whether data trace logging is enabled for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
               Defaults to `false`. Supported only for WebSocket APIs.
        :param bool detailed_metrics_enabled: Whether detailed metrics are enabled for the route. Defaults to `false`.
        :param str logging_level: The logging level for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
               Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs.
        :param float throttling_burst_limit: The throttling burst limit for the route.
        :param float throttling_rate_limit: The throttling rate limit for the route.
        """
        pulumi.set(__self__, "route_key", route_key)
        if data_trace_enabled is not None:
            pulumi.set(__self__, "data_trace_enabled", data_trace_enabled)
        if detailed_metrics_enabled is not None:
            pulumi.set(__self__, "detailed_metrics_enabled", detailed_metrics_enabled)
        if logging_level is not None:
            pulumi.set(__self__, "logging_level", logging_level)
        if throttling_burst_limit is not None:
            pulumi.set(__self__, "throttling_burst_limit", throttling_burst_limit)
        if throttling_rate_limit is not None:
            pulumi.set(__self__, "throttling_rate_limit", throttling_rate_limit)

    @property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> str:
        """
        Route key.
        """
        return pulumi.get(self, "route_key")

    @property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[bool]:
        """
        Whether data trace logging is enabled for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
        Defaults to `false`. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "data_trace_enabled")

    @property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[bool]:
        """
        Whether detailed metrics are enabled for the route. Defaults to `false`.
        """
        return pulumi.get(self, "detailed_metrics_enabled")

    @property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[str]:
        """
        The logging level for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
        Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs.
        """
        return pulumi.get(self, "logging_level")

    @property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[float]:
        """
        The throttling burst limit for the route.
        """
        return pulumi.get(self, "throttling_burst_limit")

    @property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[float]:
        """
        The throttling rate limit for the route.
        """
        return pulumi.get(self, "throttling_rate_limit")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop



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

__all__ = ['VpnConnection']


class VpnConnection(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_gateway_id: Optional[pulumi.Input[str]] = None,
                 static_routes_only: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 tunnel1_inside_cidr: Optional[pulumi.Input[str]] = None,
                 tunnel1_preshared_key: Optional[pulumi.Input[str]] = None,
                 tunnel2_inside_cidr: Optional[pulumi.Input[str]] = None,
                 tunnel2_preshared_key: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EC2 VPN connection. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and Amazon.

        > **Note:** All arguments including `tunnel1_preshared_key` and `tunnel2_preshared_key` will be stored in the raw state as plain-text.

        > **Note:** The CIDR blocks in the arguments `tunnel1_inside_cidr` and `tunnel2_inside_cidr` must have a prefix of /30 and be a part of a specific range.
        [Read more about this in the AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html).

        ## Example Usage
        ### EC2 Transit Gateway

        ```python
        import pulumi
        import pulumi_aws as aws

        example_transit_gateway = aws.ec2transitgateway.TransitGateway("exampleTransitGateway")
        example_customer_gateway = aws.ec2.CustomerGateway("exampleCustomerGateway",
            bgp_asn="65000",
            ip_address="172.0.0.1",
            type="ipsec.1")
        example_vpn_connection = aws.ec2.VpnConnection("exampleVpnConnection",
            customer_gateway_id=example_customer_gateway.id,
            transit_gateway_id=example_transit_gateway.id,
            type=example_customer_gateway.type)
        ```
        ### Virtual Private Gateway

        ```python
        import pulumi
        import pulumi_aws as aws

        vpc = aws.ec2.Vpc("vpc", cidr_block="10.0.0.0/16")
        vpn_gateway = aws.ec2.VpnGateway("vpnGateway", vpc_id=vpc.id)
        customer_gateway = aws.ec2.CustomerGateway("customerGateway",
            bgp_asn="65000",
            ip_address="172.0.0.1",
            type="ipsec.1")
        main = aws.ec2.VpnConnection("main",
            customer_gateway_id=customer_gateway.id,
            static_routes_only=True,
            type="ipsec.1",
            vpn_gateway_id=vpn_gateway.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
        :param pulumi.Input[bool] static_routes_only: Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to apply to the connection.
        :param pulumi.Input[str] transit_gateway_id: The ID of the EC2 Transit Gateway.
        :param pulumi.Input[str] tunnel1_inside_cidr: The CIDR block of the inside IP addresses for the first VPN tunnel.
        :param pulumi.Input[str] tunnel1_preshared_key: The preshared key of the first VPN tunnel.
        :param pulumi.Input[str] tunnel2_inside_cidr: The CIDR block of the inside IP addresses for the second VPN tunnel.
        :param pulumi.Input[str] tunnel2_preshared_key: The preshared key of the second VPN tunnel.
        :param pulumi.Input[str] type: The type of VPN connection. The only type AWS supports at this time is "ipsec.1".
        :param pulumi.Input[str] vpn_gateway_id: The ID of the Virtual Private Gateway.
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

            if customer_gateway_id is None:
                raise TypeError("Missing required property 'customer_gateway_id'")
            __props__['customer_gateway_id'] = customer_gateway_id
            __props__['static_routes_only'] = static_routes_only
            __props__['tags'] = tags
            __props__['transit_gateway_id'] = transit_gateway_id
            __props__['tunnel1_inside_cidr'] = tunnel1_inside_cidr
            __props__['tunnel1_preshared_key'] = tunnel1_preshared_key
            __props__['tunnel2_inside_cidr'] = tunnel2_inside_cidr
            __props__['tunnel2_preshared_key'] = tunnel2_preshared_key
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['vpn_gateway_id'] = vpn_gateway_id
            __props__['arn'] = None
            __props__['customer_gateway_configuration'] = None
            __props__['routes'] = None
            __props__['transit_gateway_attachment_id'] = None
            __props__['tunnel1_address'] = None
            __props__['tunnel1_bgp_asn'] = None
            __props__['tunnel1_bgp_holdtime'] = None
            __props__['tunnel1_cgw_inside_address'] = None
            __props__['tunnel1_vgw_inside_address'] = None
            __props__['tunnel2_address'] = None
            __props__['tunnel2_bgp_asn'] = None
            __props__['tunnel2_bgp_holdtime'] = None
            __props__['tunnel2_cgw_inside_address'] = None
            __props__['tunnel2_vgw_inside_address'] = None
            __props__['vgw_telemetries'] = None
        super(VpnConnection, __self__).__init__(
            'aws:ec2/vpnConnection:VpnConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            customer_gateway_configuration: Optional[pulumi.Input[str]] = None,
            customer_gateway_id: Optional[pulumi.Input[str]] = None,
            routes: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['VpnConnectionRouteArgs']]]]] = None,
            static_routes_only: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
            transit_gateway_id: Optional[pulumi.Input[str]] = None,
            tunnel1_address: Optional[pulumi.Input[str]] = None,
            tunnel1_bgp_asn: Optional[pulumi.Input[str]] = None,
            tunnel1_bgp_holdtime: Optional[pulumi.Input[float]] = None,
            tunnel1_cgw_inside_address: Optional[pulumi.Input[str]] = None,
            tunnel1_inside_cidr: Optional[pulumi.Input[str]] = None,
            tunnel1_preshared_key: Optional[pulumi.Input[str]] = None,
            tunnel1_vgw_inside_address: Optional[pulumi.Input[str]] = None,
            tunnel2_address: Optional[pulumi.Input[str]] = None,
            tunnel2_bgp_asn: Optional[pulumi.Input[str]] = None,
            tunnel2_bgp_holdtime: Optional[pulumi.Input[float]] = None,
            tunnel2_cgw_inside_address: Optional[pulumi.Input[str]] = None,
            tunnel2_inside_cidr: Optional[pulumi.Input[str]] = None,
            tunnel2_preshared_key: Optional[pulumi.Input[str]] = None,
            tunnel2_vgw_inside_address: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vgw_telemetries: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['VpnConnectionVgwTelemetryArgs']]]]] = None,
            vpn_gateway_id: Optional[pulumi.Input[str]] = None) -> 'VpnConnection':
        """
        Get an existing VpnConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the VPN Connection.
        :param pulumi.Input[str] customer_gateway_configuration: The configuration information for the VPN connection's customer gateway (in the native XML format).
        :param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
        :param pulumi.Input[bool] static_routes_only: Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to apply to the connection.
        :param pulumi.Input[str] transit_gateway_attachment_id: When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
        :param pulumi.Input[str] transit_gateway_id: The ID of the EC2 Transit Gateway.
        :param pulumi.Input[str] tunnel1_address: The public IP address of the first VPN tunnel.
        :param pulumi.Input[str] tunnel1_bgp_asn: The bgp asn number of the first VPN tunnel.
        :param pulumi.Input[float] tunnel1_bgp_holdtime: The bgp holdtime of the first VPN tunnel.
        :param pulumi.Input[str] tunnel1_cgw_inside_address: The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
        :param pulumi.Input[str] tunnel1_inside_cidr: The CIDR block of the inside IP addresses for the first VPN tunnel.
        :param pulumi.Input[str] tunnel1_preshared_key: The preshared key of the first VPN tunnel.
        :param pulumi.Input[str] tunnel1_vgw_inside_address: The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
        :param pulumi.Input[str] tunnel2_address: The public IP address of the second VPN tunnel.
        :param pulumi.Input[str] tunnel2_bgp_asn: The bgp asn number of the second VPN tunnel.
        :param pulumi.Input[float] tunnel2_bgp_holdtime: The bgp holdtime of the second VPN tunnel.
        :param pulumi.Input[str] tunnel2_cgw_inside_address: The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
        :param pulumi.Input[str] tunnel2_inside_cidr: The CIDR block of the inside IP addresses for the second VPN tunnel.
        :param pulumi.Input[str] tunnel2_preshared_key: The preshared key of the second VPN tunnel.
        :param pulumi.Input[str] tunnel2_vgw_inside_address: The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
        :param pulumi.Input[str] type: The type of VPN connection. The only type AWS supports at this time is "ipsec.1".
        :param pulumi.Input[str] vpn_gateway_id: The ID of the Virtual Private Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["customer_gateway_configuration"] = customer_gateway_configuration
        __props__["customer_gateway_id"] = customer_gateway_id
        __props__["routes"] = routes
        __props__["static_routes_only"] = static_routes_only
        __props__["tags"] = tags
        __props__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        __props__["transit_gateway_id"] = transit_gateway_id
        __props__["tunnel1_address"] = tunnel1_address
        __props__["tunnel1_bgp_asn"] = tunnel1_bgp_asn
        __props__["tunnel1_bgp_holdtime"] = tunnel1_bgp_holdtime
        __props__["tunnel1_cgw_inside_address"] = tunnel1_cgw_inside_address
        __props__["tunnel1_inside_cidr"] = tunnel1_inside_cidr
        __props__["tunnel1_preshared_key"] = tunnel1_preshared_key
        __props__["tunnel1_vgw_inside_address"] = tunnel1_vgw_inside_address
        __props__["tunnel2_address"] = tunnel2_address
        __props__["tunnel2_bgp_asn"] = tunnel2_bgp_asn
        __props__["tunnel2_bgp_holdtime"] = tunnel2_bgp_holdtime
        __props__["tunnel2_cgw_inside_address"] = tunnel2_cgw_inside_address
        __props__["tunnel2_inside_cidr"] = tunnel2_inside_cidr
        __props__["tunnel2_preshared_key"] = tunnel2_preshared_key
        __props__["tunnel2_vgw_inside_address"] = tunnel2_vgw_inside_address
        __props__["type"] = type
        __props__["vgw_telemetries"] = vgw_telemetries
        __props__["vpn_gateway_id"] = vpn_gateway_id
        return VpnConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the VPN Connection.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="customerGatewayConfiguration")
    def customer_gateway_configuration(self) -> str:
        """
        The configuration information for the VPN connection's customer gateway (in the native XML format).
        """
        return pulumi.get(self, "customer_gateway_configuration")

    @property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> str:
        """
        The ID of the customer gateway.
        """
        return pulumi.get(self, "customer_gateway_id")

    @property
    @pulumi.getter
    def routes(self) -> List['outputs.VpnConnectionRoute']:
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter(name="staticRoutesOnly")
    def static_routes_only(self) -> bool:
        """
        Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.
        """
        return pulumi.get(self, "static_routes_only")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags to apply to the connection.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> str:
        """
        When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[str]:
        """
        The ID of the EC2 Transit Gateway.
        """
        return pulumi.get(self, "transit_gateway_id")

    @property
    @pulumi.getter(name="tunnel1Address")
    def tunnel1_address(self) -> str:
        """
        The public IP address of the first VPN tunnel.
        """
        return pulumi.get(self, "tunnel1_address")

    @property
    @pulumi.getter(name="tunnel1BgpAsn")
    def tunnel1_bgp_asn(self) -> str:
        """
        The bgp asn number of the first VPN tunnel.
        """
        return pulumi.get(self, "tunnel1_bgp_asn")

    @property
    @pulumi.getter(name="tunnel1BgpHoldtime")
    def tunnel1_bgp_holdtime(self) -> float:
        """
        The bgp holdtime of the first VPN tunnel.
        """
        return pulumi.get(self, "tunnel1_bgp_holdtime")

    @property
    @pulumi.getter(name="tunnel1CgwInsideAddress")
    def tunnel1_cgw_inside_address(self) -> str:
        """
        The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
        """
        return pulumi.get(self, "tunnel1_cgw_inside_address")

    @property
    @pulumi.getter(name="tunnel1InsideCidr")
    def tunnel1_inside_cidr(self) -> str:
        """
        The CIDR block of the inside IP addresses for the first VPN tunnel.
        """
        return pulumi.get(self, "tunnel1_inside_cidr")

    @property
    @pulumi.getter(name="tunnel1PresharedKey")
    def tunnel1_preshared_key(self) -> str:
        """
        The preshared key of the first VPN tunnel.
        """
        return pulumi.get(self, "tunnel1_preshared_key")

    @property
    @pulumi.getter(name="tunnel1VgwInsideAddress")
    def tunnel1_vgw_inside_address(self) -> str:
        """
        The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
        """
        return pulumi.get(self, "tunnel1_vgw_inside_address")

    @property
    @pulumi.getter(name="tunnel2Address")
    def tunnel2_address(self) -> str:
        """
        The public IP address of the second VPN tunnel.
        """
        return pulumi.get(self, "tunnel2_address")

    @property
    @pulumi.getter(name="tunnel2BgpAsn")
    def tunnel2_bgp_asn(self) -> str:
        """
        The bgp asn number of the second VPN tunnel.
        """
        return pulumi.get(self, "tunnel2_bgp_asn")

    @property
    @pulumi.getter(name="tunnel2BgpHoldtime")
    def tunnel2_bgp_holdtime(self) -> float:
        """
        The bgp holdtime of the second VPN tunnel.
        """
        return pulumi.get(self, "tunnel2_bgp_holdtime")

    @property
    @pulumi.getter(name="tunnel2CgwInsideAddress")
    def tunnel2_cgw_inside_address(self) -> str:
        """
        The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
        """
        return pulumi.get(self, "tunnel2_cgw_inside_address")

    @property
    @pulumi.getter(name="tunnel2InsideCidr")
    def tunnel2_inside_cidr(self) -> str:
        """
        The CIDR block of the inside IP addresses for the second VPN tunnel.
        """
        return pulumi.get(self, "tunnel2_inside_cidr")

    @property
    @pulumi.getter(name="tunnel2PresharedKey")
    def tunnel2_preshared_key(self) -> str:
        """
        The preshared key of the second VPN tunnel.
        """
        return pulumi.get(self, "tunnel2_preshared_key")

    @property
    @pulumi.getter(name="tunnel2VgwInsideAddress")
    def tunnel2_vgw_inside_address(self) -> str:
        """
        The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
        """
        return pulumi.get(self, "tunnel2_vgw_inside_address")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of VPN connection. The only type AWS supports at this time is "ipsec.1".
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vgwTelemetries")
    def vgw_telemetries(self) -> List['outputs.VpnConnectionVgwTelemetry']:
        return pulumi.get(self, "vgw_telemetries")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[str]:
        """
        The ID of the Virtual Private Gateway.
        """
        return pulumi.get(self, "vpn_gateway_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['BgpPeer']


class BgpPeer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_family: Optional[pulumi.Input[str]] = None,
                 amazon_address: Optional[pulumi.Input[str]] = None,
                 bgp_asn: Optional[pulumi.Input[float]] = None,
                 bgp_auth_key: Optional[pulumi.Input[str]] = None,
                 customer_address: Optional[pulumi.Input[str]] = None,
                 virtual_interface_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Direct Connect BGP peer resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        peer = aws.directconnect.BgpPeer("peer",
            virtual_interface_id=aws_dx_private_virtual_interface["foo"]["id"],
            address_family="ipv6",
            bgp_asn=65351)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[float] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface on which to create the BGP peer.
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

            if address_family is None:
                raise TypeError("Missing required property 'address_family'")
            __props__['address_family'] = address_family
            __props__['amazon_address'] = amazon_address
            if bgp_asn is None:
                raise TypeError("Missing required property 'bgp_asn'")
            __props__['bgp_asn'] = bgp_asn
            __props__['bgp_auth_key'] = bgp_auth_key
            __props__['customer_address'] = customer_address
            if virtual_interface_id is None:
                raise TypeError("Missing required property 'virtual_interface_id'")
            __props__['virtual_interface_id'] = virtual_interface_id
            __props__['aws_device'] = None
            __props__['bgp_peer_id'] = None
            __props__['bgp_status'] = None
        super(BgpPeer, __self__).__init__(
            'aws:directconnect/bgpPeer:BgpPeer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_family: Optional[pulumi.Input[str]] = None,
            amazon_address: Optional[pulumi.Input[str]] = None,
            aws_device: Optional[pulumi.Input[str]] = None,
            bgp_asn: Optional[pulumi.Input[float]] = None,
            bgp_auth_key: Optional[pulumi.Input[str]] = None,
            bgp_peer_id: Optional[pulumi.Input[str]] = None,
            bgp_status: Optional[pulumi.Input[str]] = None,
            customer_address: Optional[pulumi.Input[str]] = None,
            virtual_interface_id: Optional[pulumi.Input[str]] = None) -> 'BgpPeer':
        """
        Get an existing BgpPeer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[str] aws_device: The Direct Connect endpoint on which the BGP peer terminates.
        :param pulumi.Input[float] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] bgp_peer_id: The ID of the BGP peer.
        :param pulumi.Input[str] bgp_status: The Up/Down state of the BGP peer.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface on which to create the BGP peer.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address_family"] = address_family
        __props__["amazon_address"] = amazon_address
        __props__["aws_device"] = aws_device
        __props__["bgp_asn"] = bgp_asn
        __props__["bgp_auth_key"] = bgp_auth_key
        __props__["bgp_peer_id"] = bgp_peer_id
        __props__["bgp_status"] = bgp_status
        __props__["customer_address"] = customer_address
        __props__["virtual_interface_id"] = virtual_interface_id
        return BgpPeer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[str]:
        """
        The address family for the BGP peer. `ipv4 ` or `ipv6`.
        """
        return pulumi.get(self, "address_family")

    @property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> pulumi.Output[str]:
        """
        The IPv4 CIDR address to use to send traffic to Amazon.
        Required for IPv4 BGP peers on public virtual interfaces.
        """
        return pulumi.get(self, "amazon_address")

    @property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> pulumi.Output[str]:
        """
        The Direct Connect endpoint on which the BGP peer terminates.
        """
        return pulumi.get(self, "aws_device")

    @property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[float]:
        """
        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        """
        return pulumi.get(self, "bgp_asn")

    @property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> pulumi.Output[str]:
        """
        The authentication key for BGP configuration.
        """
        return pulumi.get(self, "bgp_auth_key")

    @property
    @pulumi.getter(name="bgpPeerId")
    def bgp_peer_id(self) -> pulumi.Output[str]:
        """
        The ID of the BGP peer.
        """
        return pulumi.get(self, "bgp_peer_id")

    @property
    @pulumi.getter(name="bgpStatus")
    def bgp_status(self) -> pulumi.Output[str]:
        """
        The Up/Down state of the BGP peer.
        """
        return pulumi.get(self, "bgp_status")

    @property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> pulumi.Output[str]:
        """
        The IPv4 CIDR destination address to which Amazon should send traffic.
        Required for IPv4 BGP peers on public virtual interfaces.
        """
        return pulumi.get(self, "customer_address")

    @property
    @pulumi.getter(name="virtualInterfaceId")
    def virtual_interface_id(self) -> pulumi.Output[str]:
        """
        The ID of the Direct Connect virtual interface on which to create the BGP peer.
        """
        return pulumi.get(self, "virtual_interface_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


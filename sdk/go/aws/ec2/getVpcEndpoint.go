// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The VPC Endpoint data source provides details about
// a specific VPC endpoint.
func LookupVpcEndpoint(ctx *pulumi.Context, args *GetVpcEndpointArgs) (*GetVpcEndpointResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["id"] = args.Id
		inputs["serviceName"] = args.ServiceName
		inputs["state"] = args.State
		inputs["vpcId"] = args.VpcId
	}
	outputs, err := ctx.Invoke("aws:ec2/getVpcEndpoint:getVpcEndpoint", inputs)
	if err != nil {
		return nil, err
	}
	return &GetVpcEndpointResult{
		CidrBlocks: outputs["cidrBlocks"],
	}
		DnsEntries: outputs["dnsEntries"],
	}
		Id: outputs["id"],
	}
		NetworkInterfaceIds: outputs["networkInterfaceIds"],
	}
		Policy: outputs["policy"],
	}
		PrefixListId: outputs["prefixListId"],
	}
		PrivateDnsEnabled: outputs["privateDnsEnabled"],
	}
		RouteTableIds: outputs["routeTableIds"],
	}
		SecurityGroupIds: outputs["securityGroupIds"],
	}
		ServiceName: outputs["serviceName"],
	}
		State: outputs["state"],
	}
		SubnetIds: outputs["subnetIds"],
	}
		VpcEndpointType: outputs["vpcEndpointType"],
	}
		VpcId: outputs["vpcId"],
	}
	}, nil
}

// A collection of arguments for invoking getVpcEndpoint.
type GetVpcEndpointArgs struct {
	// The ID of the specific VPC Endpoint to retrieve.
	Id interface{}
	// The AWS service name of the specific VPC Endpoint to retrieve.
	ServiceName interface{}
	// The state of the specific VPC Endpoint to retrieve.
	State interface{}
	// The ID of the VPC in which the specific VPC Endpoint is used.
	VpcId interface{}
}

// A collection of values returned by getVpcEndpoint.
type GetVpcEndpointResult struct {
	// The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
	CidrBlocks interface{}
	// The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.
	DnsEntries interface{}
	Id interface{}
	// One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
	NetworkInterfaceIds interface{}
	// The policy document associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
	Policy interface{}
	// The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
	PrefixListId interface{}
	// Whether or not the VPC is associated with a private hosted zone - `true` or `false`. Applicable for endpoints of type `Interface`.
	PrivateDnsEnabled interface{}
	// One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
	RouteTableIds interface{}
	// One or more security groups associated with the network interfaces. Applicable for endpoints of type `Interface`.
	SecurityGroupIds interface{}
	ServiceName interface{}
	State interface{}
	// One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type `Interface`.
	SubnetIds interface{}
	// The VPC Endpoint type, `Gateway` or `Interface`.
	VpcEndpointType interface{}
	VpcId interface{}
}

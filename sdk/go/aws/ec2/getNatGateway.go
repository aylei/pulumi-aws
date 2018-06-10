// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides details about a specific Nat Gateway.
func LookupNatGateway(ctx *pulumi.Context, args *GetNatGatewayArgs) (*GetNatGatewayResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["filters"] = args.Filters
		inputs["id"] = args.Id
		inputs["state"] = args.State
		inputs["subnetId"] = args.SubnetId
		inputs["tags"] = args.Tags
		inputs["vpcId"] = args.VpcId
	}
	outputs, err := ctx.Invoke("aws:ec2/getNatGateway:getNatGateway", inputs)
	if err != nil {
		return nil, err
	}
	return &GetNatGatewayResult{
		AllocationId: outputs["allocationId"],
	}
		Id: outputs["id"],
	}
		NetworkInterfaceId: outputs["networkInterfaceId"],
	}
		PrivateIp: outputs["privateIp"],
	}
		PublicIp: outputs["publicIp"],
	}
		State: outputs["state"],
	}
		SubnetId: outputs["subnetId"],
	}
		Tags: outputs["tags"],
	}
		VpcId: outputs["vpcId"],
	}
	}, nil
}

// A collection of arguments for invoking getNatGateway.
type GetNatGatewayArgs struct {
	// Custom filter block as described below.
	// More complex filters can be expressed using one or more `filter` sub-blocks,
	// which take the following arguments:
	Filters interface{}
	// The id of the specific Nat Gateway to retrieve.
	Id interface{}
	// The state of the NAT gateway (pending | failed | available | deleting | deleted ).
	State interface{}
	// The id of subnet that the Nat Gateway resides in.
	SubnetId interface{}
	Tags interface{}
	// The id of the VPC that the Nat Gateway resides in.
	VpcId interface{}
}

// A collection of values returned by getNatGateway.
type GetNatGatewayResult struct {
	// The Id of the EIP allocated to the selected Nat Gateway.
	AllocationId interface{}
	Id interface{}
	// The Id of the ENI allocated to the selected Nat Gateway.
	NetworkInterfaceId interface{}
	// The private Ip address of the selected Nat Gateway.
	PrivateIp interface{}
	// The public Ip (EIP) address of the selected Nat Gateway.
	PublicIp interface{}
	State interface{}
	SubnetId interface{}
	Tags interface{}
	VpcId interface{}
}

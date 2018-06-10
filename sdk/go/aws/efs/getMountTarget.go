// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package efs

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides information about an Elastic File System Mount Target (EFS).
func LookupMountTarget(ctx *pulumi.Context, args *GetMountTargetArgs) (*GetMountTargetResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["mountTargetId"] = args.MountTargetId
	}
	outputs, err := ctx.Invoke("aws:efs/getMountTarget:getMountTarget", inputs)
	if err != nil {
		return nil, err
	}
	return &GetMountTargetResult{
		DnsName: outputs["dnsName"],
	}
		FileSystemId: outputs["fileSystemId"],
	}
		IpAddress: outputs["ipAddress"],
	}
		NetworkInterfaceId: outputs["networkInterfaceId"],
	}
		SecurityGroups: outputs["securityGroups"],
	}
		SubnetId: outputs["subnetId"],
	}
	}, nil
}

// A collection of arguments for invoking getMountTarget.
type GetMountTargetArgs struct {
	// ID of the mount target that you want to have described
	MountTargetId interface{}
}

// A collection of values returned by getMountTarget.
type GetMountTargetResult struct {
	// The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
	DnsName interface{}
	// ID of the file system for which the mount target is intended.
	FileSystemId interface{}
	// Address at which the file system may be mounted via the mount target.
	IpAddress interface{}
	// The ID of the network interface that Amazon EFS created when it created the mount target.
	NetworkInterfaceId interface{}
	// List of VPC security group IDs attached to the mount target.
	SecurityGroups interface{}
	// ID of the mount target's subnet.
	SubnetId interface{}
}

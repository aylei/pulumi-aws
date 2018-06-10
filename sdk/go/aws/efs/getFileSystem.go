// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package efs

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides information about an Elastic File System (EFS).
func LookupFileSystem(ctx *pulumi.Context, args *GetFileSystemArgs) (*GetFileSystemResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["creationToken"] = args.CreationToken
		inputs["fileSystemId"] = args.FileSystemId
		inputs["tags"] = args.Tags
	}
	outputs, err := ctx.Invoke("aws:efs/getFileSystem:getFileSystem", inputs)
	if err != nil {
		return nil, err
	}
	return &GetFileSystemResult{
		CreationToken: outputs["creationToken"],
	}
		DnsName: outputs["dnsName"],
	}
		Encrypted: outputs["encrypted"],
	}
		FileSystemId: outputs["fileSystemId"],
	}
		KmsKeyId: outputs["kmsKeyId"],
	}
		PerformanceMode: outputs["performanceMode"],
	}
		Tags: outputs["tags"],
	}
	}, nil
}

// A collection of arguments for invoking getFileSystem.
type GetFileSystemArgs struct {
	// Restricts the list to the file system with this creation token.
	CreationToken interface{}
	// The ID that identifies the file system (e.g. fs-ccfc0d65).
	FileSystemId interface{}
	Tags interface{}
}

// A collection of values returned by getFileSystem.
type GetFileSystemResult struct {
	CreationToken interface{}
	// The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
	DnsName interface{}
	// Whether EFS is encrypted.
	Encrypted interface{}
	FileSystemId interface{}
	// The ARN for the KMS encryption key.
	KmsKeyId interface{}
	// The PerformanceMode of the file system.
	PerformanceMode interface{}
	// The list of tags assigned to the file system.
	Tags interface{}
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticloadbalancing

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the Account ID of the [AWS Elastic Load Balancing Service Account](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html#attach-bucket-policy)
// in a given region for the purpose of whitelisting in S3 bucket policy.
func LookupServiceAccount(ctx *pulumi.Context, args *GetServiceAccountArgs) (*GetServiceAccountResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["region"] = args.Region
	}
	outputs, err := ctx.Invoke("aws:elasticloadbalancing/getServiceAccount:getServiceAccount", inputs)
	if err != nil {
		return nil, err
	}
	return &GetServiceAccountResult{
		Arn: outputs["arn"],
	}
	}, nil
}

// A collection of arguments for invoking getServiceAccount.
type GetServiceAccountArgs struct {
	// Name of the region whose AWS ELB account ID is desired.
	// Defaults to the region from the AWS provider configuration.
	Region interface{}
}

// A collection of values returned by getServiceAccount.
type GetServiceAccountResult struct {
	// The ARN of the AWS ELB service account in the selected region.
	Arn interface{}
}

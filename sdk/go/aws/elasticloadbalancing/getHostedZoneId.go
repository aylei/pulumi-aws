// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticloadbalancing

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the HostedZoneId of the AWS Elastic Load Balancing HostedZoneId
// in a given region for the purpose of using in an AWS Route53 Alias.
func LookupHostedZoneId(ctx *pulumi.Context, args *GetHostedZoneIdArgs) error {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["region"] = args.Region
	}
	_, err := ctx.Invoke("aws:elasticloadbalancing/getHostedZoneId:getHostedZoneId", inputs)
	return err
}

// A collection of arguments for invoking getHostedZoneId.
type GetHostedZoneIdArgs struct {
	// Name of the region whose AWS ELB HostedZoneId is desired.
	// Defaults to the region from the AWS provider configuration.
	Region interface{}
}

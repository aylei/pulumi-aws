// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The IAM Account Alias data source allows access to the account alias
// for the effective account in which Terraform is working.
func LookupAccountAlias(ctx *pulumi.Context) (*GetAccountAliasResult, error) {
	outputs, err := ctx.Invoke("aws:iam/getAccountAlias:getAccountAlias", nil)
	if err != nil {
		return nil, err
	}
	return &GetAccountAliasResult{
		AccountAlias: outputs["accountAlias"],
	}
	}, nil
}

// A collection of values returned by getAccountAlias.
type GetAccountAliasResult struct {
	// The alias associated with the AWS account.
	AccountAlias interface{}
}

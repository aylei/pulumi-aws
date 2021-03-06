// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package signer

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides information about a Signer Signing Profile.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/signer"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := signer.LookupSigningProfile(ctx, &signer.LookupSigningProfileArgs{
// 			Name: "prod_profile_DdW3Mk1foYL88fajut4mTVFGpuwfd4ACO6ANL0D1uIj7lrn8adK",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupSigningProfile(ctx *pulumi.Context, args *LookupSigningProfileArgs, opts ...pulumi.InvokeOption) (*LookupSigningProfileResult, error) {
	var rv LookupSigningProfileResult
	err := ctx.Invoke("aws:signer/getSigningProfile:getSigningProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSigningProfile.
type LookupSigningProfileArgs struct {
	// The name of the target signing profile.
	Name string `pulumi:"name"`
	// A list of tags associated with the signing profile.
	Tags map[string]string `pulumi:"tags"`
}

// A collection of values returned by getSigningProfile.
type LookupSigningProfileResult struct {
	// The Amazon Resource Name (ARN) for the signing profile.
	Arn string `pulumi:"arn"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
	// A human-readable name for the signing platform associated with the signing profile.
	PlatformDisplayName string `pulumi:"platformDisplayName"`
	// The ID of the platform that is used by the target signing profile.
	PlatformId string `pulumi:"platformId"`
	// Revocation information for a signing profile.
	RevocationRecords []GetSigningProfileRevocationRecord `pulumi:"revocationRecords"`
	// The validity period for a signing job.
	SignatureValidityPeriods []GetSigningProfileSignatureValidityPeriod `pulumi:"signatureValidityPeriods"`
	// The status of the target signing profile.
	Status string `pulumi:"status"`
	// A list of tags associated with the signing profile.
	Tags map[string]string `pulumi:"tags"`
	// The current version of the signing profile.
	Version string `pulumi:"version"`
	// The signing profile ARN, including the profile version.
	VersionArn string `pulumi:"versionArn"`
}

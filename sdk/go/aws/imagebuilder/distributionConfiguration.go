// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package imagebuilder

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an Image Builder Distribution Configuration.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/imagebuilder"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := imagebuilder.NewDistributionConfiguration(ctx, "example", &imagebuilder.DistributionConfigurationArgs{
// 			Distributions: imagebuilder.DistributionConfigurationDistributionArray{
// 				&imagebuilder.DistributionConfigurationDistributionArgs{
// 					AmiDistributionConfiguration: &imagebuilder.DistributionConfigurationDistributionAmiDistributionConfigurationArgs{
// 						AmiTags: pulumi.StringMap{
// 							"CostCenter": pulumi.String("IT"),
// 						},
// 						LaunchPermission: &imagebuilder.DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgs{
// 							UserIds: pulumi.StringArray{
// 								pulumi.String("123456789012"),
// 							},
// 						},
// 						Name: pulumi.String("example-{{ imagebuilder:buildDate }}"),
// 					},
// 					Region: pulumi.String("us-east-1"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// `aws_imagebuilder_distribution_configurations` resources can be imported by using the Amazon Resource Name (ARN), e.g.
//
// ```sh
//  $ pulumi import aws:imagebuilder/distributionConfiguration:DistributionConfiguration example arn:aws:imagebuilder:us-east-1:123456789012:distribution-configuration/example
// ```
type DistributionConfiguration struct {
	pulumi.CustomResourceState

	// (Required) Amazon Resource Name (ARN) of the distribution configuration.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Date the distribution configuration was created.
	DateCreated pulumi.StringOutput `pulumi:"dateCreated"`
	// Date the distribution configuration was updated.
	DateUpdated pulumi.StringOutput `pulumi:"dateUpdated"`
	// Description to apply to the distributed AMI.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// One or more configuration blocks with distribution settings. Detailed below.
	Distributions DistributionConfigurationDistributionArrayOutput `pulumi:"distributions"`
	// Name to apply to the distributed AMI.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key-value map of resource tags for the distribution configuration.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewDistributionConfiguration registers a new resource with the given unique name, arguments, and options.
func NewDistributionConfiguration(ctx *pulumi.Context,
	name string, args *DistributionConfigurationArgs, opts ...pulumi.ResourceOption) (*DistributionConfiguration, error) {
	if args == nil || args.Distributions == nil {
		return nil, errors.New("missing required argument 'Distributions'")
	}
	if args == nil {
		args = &DistributionConfigurationArgs{}
	}
	var resource DistributionConfiguration
	err := ctx.RegisterResource("aws:imagebuilder/distributionConfiguration:DistributionConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDistributionConfiguration gets an existing DistributionConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDistributionConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DistributionConfigurationState, opts ...pulumi.ResourceOption) (*DistributionConfiguration, error) {
	var resource DistributionConfiguration
	err := ctx.ReadResource("aws:imagebuilder/distributionConfiguration:DistributionConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DistributionConfiguration resources.
type distributionConfigurationState struct {
	// (Required) Amazon Resource Name (ARN) of the distribution configuration.
	Arn *string `pulumi:"arn"`
	// Date the distribution configuration was created.
	DateCreated *string `pulumi:"dateCreated"`
	// Date the distribution configuration was updated.
	DateUpdated *string `pulumi:"dateUpdated"`
	// Description to apply to the distributed AMI.
	Description *string `pulumi:"description"`
	// One or more configuration blocks with distribution settings. Detailed below.
	Distributions []DistributionConfigurationDistribution `pulumi:"distributions"`
	// Name to apply to the distributed AMI.
	Name *string `pulumi:"name"`
	// Key-value map of resource tags for the distribution configuration.
	Tags map[string]string `pulumi:"tags"`
}

type DistributionConfigurationState struct {
	// (Required) Amazon Resource Name (ARN) of the distribution configuration.
	Arn pulumi.StringPtrInput
	// Date the distribution configuration was created.
	DateCreated pulumi.StringPtrInput
	// Date the distribution configuration was updated.
	DateUpdated pulumi.StringPtrInput
	// Description to apply to the distributed AMI.
	Description pulumi.StringPtrInput
	// One or more configuration blocks with distribution settings. Detailed below.
	Distributions DistributionConfigurationDistributionArrayInput
	// Name to apply to the distributed AMI.
	Name pulumi.StringPtrInput
	// Key-value map of resource tags for the distribution configuration.
	Tags pulumi.StringMapInput
}

func (DistributionConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*distributionConfigurationState)(nil)).Elem()
}

type distributionConfigurationArgs struct {
	// Description to apply to the distributed AMI.
	Description *string `pulumi:"description"`
	// One or more configuration blocks with distribution settings. Detailed below.
	Distributions []DistributionConfigurationDistribution `pulumi:"distributions"`
	// Name to apply to the distributed AMI.
	Name *string `pulumi:"name"`
	// Key-value map of resource tags for the distribution configuration.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a DistributionConfiguration resource.
type DistributionConfigurationArgs struct {
	// Description to apply to the distributed AMI.
	Description pulumi.StringPtrInput
	// One or more configuration blocks with distribution settings. Detailed below.
	Distributions DistributionConfigurationDistributionArrayInput
	// Name to apply to the distributed AMI.
	Name pulumi.StringPtrInput
	// Key-value map of resource tags for the distribution configuration.
	Tags pulumi.StringMapInput
}

func (DistributionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*distributionConfigurationArgs)(nil)).Elem()
}

type DistributionConfigurationInput interface {
	pulumi.Input

	ToDistributionConfigurationOutput() DistributionConfigurationOutput
	ToDistributionConfigurationOutputWithContext(ctx context.Context) DistributionConfigurationOutput
}

func (DistributionConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*DistributionConfiguration)(nil)).Elem()
}

func (i DistributionConfiguration) ToDistributionConfigurationOutput() DistributionConfigurationOutput {
	return i.ToDistributionConfigurationOutputWithContext(context.Background())
}

func (i DistributionConfiguration) ToDistributionConfigurationOutputWithContext(ctx context.Context) DistributionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DistributionConfigurationOutput)
}

type DistributionConfigurationOutput struct {
	*pulumi.OutputState
}

func (DistributionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DistributionConfigurationOutput)(nil)).Elem()
}

func (o DistributionConfigurationOutput) ToDistributionConfigurationOutput() DistributionConfigurationOutput {
	return o
}

func (o DistributionConfigurationOutput) ToDistributionConfigurationOutputWithContext(ctx context.Context) DistributionConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DistributionConfigurationOutput{})
}

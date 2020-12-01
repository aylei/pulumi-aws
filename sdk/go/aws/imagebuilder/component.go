// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package imagebuilder

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an Image Builder Component.
//
// ## Example Usage
// ### URI Document
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/imagebuilder"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := imagebuilder.NewComponent(ctx, "example", &imagebuilder.ComponentArgs{
// 			Platform: pulumi.String("Linux"),
// 			Uri:      pulumi.String(fmt.Sprintf("%v%v%v%v", "s3://", aws_s3_bucket_object.Example.Bucket, "/", aws_s3_bucket_object.Example.Key)),
// 			Version:  pulumi.String("1.0.0"),
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
// `aws_imagebuilder_components` resources can be imported by using the Amazon Resource Name (ARN), e.g.
//
// ```sh
//  $ pulumi import aws:imagebuilder/component:Component example arn:aws:imagebuilder:us-east-1:123456789012:component/example/1.0.0/1
// ```
//
//  Certain resource arguments, such as `uri`, cannot be read via the API and imported into Terraform. Terraform will display a difference for these arguments the first run after import if declared in the Terraform configuration for an imported resource.
type Component struct {
	pulumi.CustomResourceState

	// (Required) Amazon Resource Name (ARN) of the component.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Change description of the component.
	ChangeDescription pulumi.StringPtrOutput `pulumi:"changeDescription"`
	Data              pulumi.StringOutput    `pulumi:"data"`
	// Date the component was created.
	DateCreated pulumi.StringOutput `pulumi:"dateCreated"`
	// Description of the component.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Encryption status of the component.
	Encrypted pulumi.BoolOutput `pulumi:"encrypted"`
	// Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// Name of the component.
	Name pulumi.StringOutput `pulumi:"name"`
	// Owner of the component.
	Owner pulumi.StringOutput `pulumi:"owner"`
	// Platform of the component.
	Platform pulumi.StringOutput `pulumi:"platform"`
	// Set of Operating Systems (OS) supported by the component.
	SupportedOsVersions pulumi.StringArrayOutput `pulumi:"supportedOsVersions"`
	// Key-value map of resource tags for the component.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// Type of the component.
	Type pulumi.StringOutput `pulumi:"type"`
	// S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
	Uri pulumi.StringPtrOutput `pulumi:"uri"`
	// Version of the component.
	Version pulumi.StringOutput `pulumi:"version"`
}

// NewComponent registers a new resource with the given unique name, arguments, and options.
func NewComponent(ctx *pulumi.Context,
	name string, args *ComponentArgs, opts ...pulumi.ResourceOption) (*Component, error) {
	if args == nil || args.Platform == nil {
		return nil, errors.New("missing required argument 'Platform'")
	}
	if args == nil || args.Version == nil {
		return nil, errors.New("missing required argument 'Version'")
	}
	if args == nil {
		args = &ComponentArgs{}
	}
	var resource Component
	err := ctx.RegisterResource("aws:imagebuilder/component:Component", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComponent gets an existing Component resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComponent(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComponentState, opts ...pulumi.ResourceOption) (*Component, error) {
	var resource Component
	err := ctx.ReadResource("aws:imagebuilder/component:Component", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Component resources.
type componentState struct {
	// (Required) Amazon Resource Name (ARN) of the component.
	Arn *string `pulumi:"arn"`
	// Change description of the component.
	ChangeDescription *string `pulumi:"changeDescription"`
	Data              *string `pulumi:"data"`
	// Date the component was created.
	DateCreated *string `pulumi:"dateCreated"`
	// Description of the component.
	Description *string `pulumi:"description"`
	// Encryption status of the component.
	Encrypted *bool `pulumi:"encrypted"`
	// Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Name of the component.
	Name *string `pulumi:"name"`
	// Owner of the component.
	Owner *string `pulumi:"owner"`
	// Platform of the component.
	Platform *string `pulumi:"platform"`
	// Set of Operating Systems (OS) supported by the component.
	SupportedOsVersions []string `pulumi:"supportedOsVersions"`
	// Key-value map of resource tags for the component.
	Tags map[string]string `pulumi:"tags"`
	// Type of the component.
	Type *string `pulumi:"type"`
	// S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
	Uri *string `pulumi:"uri"`
	// Version of the component.
	Version *string `pulumi:"version"`
}

type ComponentState struct {
	// (Required) Amazon Resource Name (ARN) of the component.
	Arn pulumi.StringPtrInput
	// Change description of the component.
	ChangeDescription pulumi.StringPtrInput
	Data              pulumi.StringPtrInput
	// Date the component was created.
	DateCreated pulumi.StringPtrInput
	// Description of the component.
	Description pulumi.StringPtrInput
	// Encryption status of the component.
	Encrypted pulumi.BoolPtrInput
	// Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
	KmsKeyId pulumi.StringPtrInput
	// Name of the component.
	Name pulumi.StringPtrInput
	// Owner of the component.
	Owner pulumi.StringPtrInput
	// Platform of the component.
	Platform pulumi.StringPtrInput
	// Set of Operating Systems (OS) supported by the component.
	SupportedOsVersions pulumi.StringArrayInput
	// Key-value map of resource tags for the component.
	Tags pulumi.StringMapInput
	// Type of the component.
	Type pulumi.StringPtrInput
	// S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
	Uri pulumi.StringPtrInput
	// Version of the component.
	Version pulumi.StringPtrInput
}

func (ComponentState) ElementType() reflect.Type {
	return reflect.TypeOf((*componentState)(nil)).Elem()
}

type componentArgs struct {
	// Change description of the component.
	ChangeDescription *string `pulumi:"changeDescription"`
	Data              *string `pulumi:"data"`
	// Description of the component.
	Description *string `pulumi:"description"`
	// Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Name of the component.
	Name *string `pulumi:"name"`
	// Platform of the component.
	Platform string `pulumi:"platform"`
	// Set of Operating Systems (OS) supported by the component.
	SupportedOsVersions []string `pulumi:"supportedOsVersions"`
	// Key-value map of resource tags for the component.
	Tags map[string]string `pulumi:"tags"`
	// S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
	Uri *string `pulumi:"uri"`
	// Version of the component.
	Version string `pulumi:"version"`
}

// The set of arguments for constructing a Component resource.
type ComponentArgs struct {
	// Change description of the component.
	ChangeDescription pulumi.StringPtrInput
	Data              pulumi.StringPtrInput
	// Description of the component.
	Description pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
	KmsKeyId pulumi.StringPtrInput
	// Name of the component.
	Name pulumi.StringPtrInput
	// Platform of the component.
	Platform pulumi.StringInput
	// Set of Operating Systems (OS) supported by the component.
	SupportedOsVersions pulumi.StringArrayInput
	// Key-value map of resource tags for the component.
	Tags pulumi.StringMapInput
	// S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
	Uri pulumi.StringPtrInput
	// Version of the component.
	Version pulumi.StringInput
}

func (ComponentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*componentArgs)(nil)).Elem()
}

type ComponentInput interface {
	pulumi.Input

	ToComponentOutput() ComponentOutput
	ToComponentOutputWithContext(ctx context.Context) ComponentOutput
}

func (Component) ElementType() reflect.Type {
	return reflect.TypeOf((*Component)(nil)).Elem()
}

func (i Component) ToComponentOutput() ComponentOutput {
	return i.ToComponentOutputWithContext(context.Background())
}

func (i Component) ToComponentOutputWithContext(ctx context.Context) ComponentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComponentOutput)
}

type ComponentOutput struct {
	*pulumi.OutputState
}

func (ComponentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ComponentOutput)(nil)).Elem()
}

func (o ComponentOutput) ToComponentOutput() ComponentOutput {
	return o
}

func (o ComponentOutput) ToComponentOutputWithContext(ctx context.Context) ComponentOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ComponentOutput{})
}
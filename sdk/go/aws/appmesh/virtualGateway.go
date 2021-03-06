// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appmesh

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AWS App Mesh virtual gateway resource.
//
// ## Example Usage
// ### Basic
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/appmesh"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := appmesh.NewVirtualGateway(ctx, "example", &appmesh.VirtualGatewayArgs{
// 			MeshName: pulumi.String("example-service-mesh"),
// 			Spec: &appmesh.VirtualGatewaySpecArgs{
// 				Listener: &appmesh.VirtualGatewaySpecListenerArgs{
// 					PortMapping: &appmesh.VirtualGatewaySpecListenerPortMappingArgs{
// 						Port:     pulumi.Int(8080),
// 						Protocol: pulumi.String("http"),
// 					},
// 				},
// 			},
// 			Tags: pulumi.StringMap{
// 				"Environment": pulumi.String("test"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Access Logs and TLS
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/appmesh"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := appmesh.NewVirtualGateway(ctx, "example", &appmesh.VirtualGatewayArgs{
// 			MeshName: pulumi.String("example-service-mesh"),
// 			Spec: &appmesh.VirtualGatewaySpecArgs{
// 				Listener: &appmesh.VirtualGatewaySpecListenerArgs{
// 					PortMapping: &appmesh.VirtualGatewaySpecListenerPortMappingArgs{
// 						Port:     pulumi.Int(8080),
// 						Protocol: pulumi.String("http"),
// 					},
// 					Tls: &appmesh.VirtualGatewaySpecListenerTlsArgs{
// 						Certificate: &appmesh.VirtualGatewaySpecListenerTlsCertificateArgs{
// 							Acm: &appmesh.VirtualGatewaySpecListenerTlsCertificateAcmArgs{
// 								CertificateArn: pulumi.Any(aws_acm_certificate.Example.Arn),
// 							},
// 						},
// 						Mode: pulumi.String("STRICT"),
// 					},
// 				},
// 				Logging: &appmesh.VirtualGatewaySpecLoggingArgs{
// 					AccessLog: &appmesh.VirtualGatewaySpecLoggingAccessLogArgs{
// 						File: &appmesh.VirtualGatewaySpecLoggingAccessLogFileArgs{
// 							Path: pulumi.String("/var/log/access.log"),
// 						},
// 					},
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
// App Mesh virtual gateway can be imported using `mesh_name` together with the virtual gateway's `name`, e.g.
//
// ```sh
//  $ pulumi import aws:appmesh/virtualGateway:VirtualGateway example mesh/gw1
// ```
//
//  [1]/docs/providers/aws/index.html
type VirtualGateway struct {
	pulumi.CustomResourceState

	// The ARN of the virtual gateway.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The creation date of the virtual gateway.
	CreatedDate pulumi.StringOutput `pulumi:"createdDate"`
	// The last update date of the virtual gateway.
	LastUpdatedDate pulumi.StringOutput `pulumi:"lastUpdatedDate"`
	// The name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
	MeshName pulumi.StringOutput `pulumi:"meshName"`
	// The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
	MeshOwner pulumi.StringOutput `pulumi:"meshOwner"`
	// The name to use for the virtual gateway. Must be between 1 and 255 characters in length.
	Name pulumi.StringOutput `pulumi:"name"`
	// The resource owner's AWS account ID.
	ResourceOwner pulumi.StringOutput `pulumi:"resourceOwner"`
	// The virtual gateway specification to apply.
	Spec VirtualGatewaySpecOutput `pulumi:"spec"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewVirtualGateway registers a new resource with the given unique name, arguments, and options.
func NewVirtualGateway(ctx *pulumi.Context,
	name string, args *VirtualGatewayArgs, opts ...pulumi.ResourceOption) (*VirtualGateway, error) {
	if args == nil || args.MeshName == nil {
		return nil, errors.New("missing required argument 'MeshName'")
	}
	if args == nil || args.Spec == nil {
		return nil, errors.New("missing required argument 'Spec'")
	}
	if args == nil {
		args = &VirtualGatewayArgs{}
	}
	var resource VirtualGateway
	err := ctx.RegisterResource("aws:appmesh/virtualGateway:VirtualGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVirtualGateway gets an existing VirtualGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VirtualGatewayState, opts ...pulumi.ResourceOption) (*VirtualGateway, error) {
	var resource VirtualGateway
	err := ctx.ReadResource("aws:appmesh/virtualGateway:VirtualGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VirtualGateway resources.
type virtualGatewayState struct {
	// The ARN of the virtual gateway.
	Arn *string `pulumi:"arn"`
	// The creation date of the virtual gateway.
	CreatedDate *string `pulumi:"createdDate"`
	// The last update date of the virtual gateway.
	LastUpdatedDate *string `pulumi:"lastUpdatedDate"`
	// The name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
	MeshName *string `pulumi:"meshName"`
	// The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
	MeshOwner *string `pulumi:"meshOwner"`
	// The name to use for the virtual gateway. Must be between 1 and 255 characters in length.
	Name *string `pulumi:"name"`
	// The resource owner's AWS account ID.
	ResourceOwner *string `pulumi:"resourceOwner"`
	// The virtual gateway specification to apply.
	Spec *VirtualGatewaySpec `pulumi:"spec"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

type VirtualGatewayState struct {
	// The ARN of the virtual gateway.
	Arn pulumi.StringPtrInput
	// The creation date of the virtual gateway.
	CreatedDate pulumi.StringPtrInput
	// The last update date of the virtual gateway.
	LastUpdatedDate pulumi.StringPtrInput
	// The name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
	MeshName pulumi.StringPtrInput
	// The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
	MeshOwner pulumi.StringPtrInput
	// The name to use for the virtual gateway. Must be between 1 and 255 characters in length.
	Name pulumi.StringPtrInput
	// The resource owner's AWS account ID.
	ResourceOwner pulumi.StringPtrInput
	// The virtual gateway specification to apply.
	Spec VirtualGatewaySpecPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (VirtualGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualGatewayState)(nil)).Elem()
}

type virtualGatewayArgs struct {
	// The name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
	MeshName string `pulumi:"meshName"`
	// The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
	MeshOwner *string `pulumi:"meshOwner"`
	// The name to use for the virtual gateway. Must be between 1 and 255 characters in length.
	Name *string `pulumi:"name"`
	// The virtual gateway specification to apply.
	Spec VirtualGatewaySpec `pulumi:"spec"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a VirtualGateway resource.
type VirtualGatewayArgs struct {
	// The name of the service mesh in which to create the virtual gateway. Must be between 1 and 255 characters in length.
	MeshName pulumi.StringInput
	// The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
	MeshOwner pulumi.StringPtrInput
	// The name to use for the virtual gateway. Must be between 1 and 255 characters in length.
	Name pulumi.StringPtrInput
	// The virtual gateway specification to apply.
	Spec VirtualGatewaySpecInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (VirtualGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualGatewayArgs)(nil)).Elem()
}

type VirtualGatewayInput interface {
	pulumi.Input

	ToVirtualGatewayOutput() VirtualGatewayOutput
	ToVirtualGatewayOutputWithContext(ctx context.Context) VirtualGatewayOutput
}

func (VirtualGateway) ElementType() reflect.Type {
	return reflect.TypeOf((*VirtualGateway)(nil)).Elem()
}

func (i VirtualGateway) ToVirtualGatewayOutput() VirtualGatewayOutput {
	return i.ToVirtualGatewayOutputWithContext(context.Background())
}

func (i VirtualGateway) ToVirtualGatewayOutputWithContext(ctx context.Context) VirtualGatewayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VirtualGatewayOutput)
}

type VirtualGatewayOutput struct {
	*pulumi.OutputState
}

func (VirtualGatewayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VirtualGatewayOutput)(nil)).Elem()
}

func (o VirtualGatewayOutput) ToVirtualGatewayOutput() VirtualGatewayOutput {
	return o
}

func (o VirtualGatewayOutput) ToVirtualGatewayOutputWithContext(ctx context.Context) VirtualGatewayOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(VirtualGatewayOutput{})
}

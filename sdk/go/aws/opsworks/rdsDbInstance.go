// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package opsworks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an OpsWorks RDS DB Instance resource.
//
// > **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/opsworks"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := opsworks.NewRdsDbInstance(ctx, "myInstance", &opsworks.RdsDbInstanceArgs{
// 			StackId:          pulumi.Any(aws_opsworks_stack.My_stack.Id),
// 			RdsDbInstanceArn: pulumi.Any(aws_db_instance.My_instance.Arn),
// 			DbUser:           pulumi.String("someUser"),
// 			DbPassword:       pulumi.String("somePass"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type RdsDbInstance struct {
	pulumi.CustomResourceState

	// A db password
	DbPassword pulumi.StringOutput `pulumi:"dbPassword"`
	// A db username
	DbUser pulumi.StringOutput `pulumi:"dbUser"`
	// The db instance to register for this stack. Changing this will force a new resource.
	RdsDbInstanceArn pulumi.StringOutput `pulumi:"rdsDbInstanceArn"`
	// The stack to register a db instance for. Changing this will force a new resource.
	StackId pulumi.StringOutput `pulumi:"stackId"`
}

// NewRdsDbInstance registers a new resource with the given unique name, arguments, and options.
func NewRdsDbInstance(ctx *pulumi.Context,
	name string, args *RdsDbInstanceArgs, opts ...pulumi.ResourceOption) (*RdsDbInstance, error) {
	if args == nil || args.DbPassword == nil {
		return nil, errors.New("missing required argument 'DbPassword'")
	}
	if args == nil || args.DbUser == nil {
		return nil, errors.New("missing required argument 'DbUser'")
	}
	if args == nil || args.RdsDbInstanceArn == nil {
		return nil, errors.New("missing required argument 'RdsDbInstanceArn'")
	}
	if args == nil || args.StackId == nil {
		return nil, errors.New("missing required argument 'StackId'")
	}
	if args == nil {
		args = &RdsDbInstanceArgs{}
	}
	var resource RdsDbInstance
	err := ctx.RegisterResource("aws:opsworks/rdsDbInstance:RdsDbInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRdsDbInstance gets an existing RdsDbInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRdsDbInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RdsDbInstanceState, opts ...pulumi.ResourceOption) (*RdsDbInstance, error) {
	var resource RdsDbInstance
	err := ctx.ReadResource("aws:opsworks/rdsDbInstance:RdsDbInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RdsDbInstance resources.
type rdsDbInstanceState struct {
	// A db password
	DbPassword *string `pulumi:"dbPassword"`
	// A db username
	DbUser *string `pulumi:"dbUser"`
	// The db instance to register for this stack. Changing this will force a new resource.
	RdsDbInstanceArn *string `pulumi:"rdsDbInstanceArn"`
	// The stack to register a db instance for. Changing this will force a new resource.
	StackId *string `pulumi:"stackId"`
}

type RdsDbInstanceState struct {
	// A db password
	DbPassword pulumi.StringPtrInput
	// A db username
	DbUser pulumi.StringPtrInput
	// The db instance to register for this stack. Changing this will force a new resource.
	RdsDbInstanceArn pulumi.StringPtrInput
	// The stack to register a db instance for. Changing this will force a new resource.
	StackId pulumi.StringPtrInput
}

func (RdsDbInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*rdsDbInstanceState)(nil)).Elem()
}

type rdsDbInstanceArgs struct {
	// A db password
	DbPassword string `pulumi:"dbPassword"`
	// A db username
	DbUser string `pulumi:"dbUser"`
	// The db instance to register for this stack. Changing this will force a new resource.
	RdsDbInstanceArn string `pulumi:"rdsDbInstanceArn"`
	// The stack to register a db instance for. Changing this will force a new resource.
	StackId string `pulumi:"stackId"`
}

// The set of arguments for constructing a RdsDbInstance resource.
type RdsDbInstanceArgs struct {
	// A db password
	DbPassword pulumi.StringInput
	// A db username
	DbUser pulumi.StringInput
	// The db instance to register for this stack. Changing this will force a new resource.
	RdsDbInstanceArn pulumi.StringInput
	// The stack to register a db instance for. Changing this will force a new resource.
	StackId pulumi.StringInput
}

func (RdsDbInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rdsDbInstanceArgs)(nil)).Elem()
}

type RdsDbInstanceInput interface {
	pulumi.Input

	ToRdsDbInstanceOutput() RdsDbInstanceOutput
	ToRdsDbInstanceOutputWithContext(ctx context.Context) RdsDbInstanceOutput
}

func (RdsDbInstance) ElementType() reflect.Type {
	return reflect.TypeOf((*RdsDbInstance)(nil)).Elem()
}

func (i RdsDbInstance) ToRdsDbInstanceOutput() RdsDbInstanceOutput {
	return i.ToRdsDbInstanceOutputWithContext(context.Background())
}

func (i RdsDbInstance) ToRdsDbInstanceOutputWithContext(ctx context.Context) RdsDbInstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RdsDbInstanceOutput)
}

type RdsDbInstanceOutput struct {
	*pulumi.OutputState
}

func (RdsDbInstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RdsDbInstanceOutput)(nil)).Elem()
}

func (o RdsDbInstanceOutput) ToRdsDbInstanceOutput() RdsDbInstanceOutput {
	return o
}

func (o RdsDbInstanceOutput) ToRdsDbInstanceOutputWithContext(ctx context.Context) RdsDbInstanceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RdsDbInstanceOutput{})
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type CodeRepository struct {
	pulumi.CustomResourceState

	Arn                pulumi.StringOutput           `pulumi:"arn"`
	CodeRepositoryName pulumi.StringOutput           `pulumi:"codeRepositoryName"`
	GitConfig          CodeRepositoryGitConfigOutput `pulumi:"gitConfig"`
}

// NewCodeRepository registers a new resource with the given unique name, arguments, and options.
func NewCodeRepository(ctx *pulumi.Context,
	name string, args *CodeRepositoryArgs, opts ...pulumi.ResourceOption) (*CodeRepository, error) {
	if args == nil || args.CodeRepositoryName == nil {
		return nil, errors.New("missing required argument 'CodeRepositoryName'")
	}
	if args == nil || args.GitConfig == nil {
		return nil, errors.New("missing required argument 'GitConfig'")
	}
	if args == nil {
		args = &CodeRepositoryArgs{}
	}
	var resource CodeRepository
	err := ctx.RegisterResource("aws:sagemaker/codeRepository:CodeRepository", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCodeRepository gets an existing CodeRepository resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCodeRepository(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CodeRepositoryState, opts ...pulumi.ResourceOption) (*CodeRepository, error) {
	var resource CodeRepository
	err := ctx.ReadResource("aws:sagemaker/codeRepository:CodeRepository", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CodeRepository resources.
type codeRepositoryState struct {
	Arn                *string                  `pulumi:"arn"`
	CodeRepositoryName *string                  `pulumi:"codeRepositoryName"`
	GitConfig          *CodeRepositoryGitConfig `pulumi:"gitConfig"`
}

type CodeRepositoryState struct {
	Arn                pulumi.StringPtrInput
	CodeRepositoryName pulumi.StringPtrInput
	GitConfig          CodeRepositoryGitConfigPtrInput
}

func (CodeRepositoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*codeRepositoryState)(nil)).Elem()
}

type codeRepositoryArgs struct {
	CodeRepositoryName string                  `pulumi:"codeRepositoryName"`
	GitConfig          CodeRepositoryGitConfig `pulumi:"gitConfig"`
}

// The set of arguments for constructing a CodeRepository resource.
type CodeRepositoryArgs struct {
	CodeRepositoryName pulumi.StringInput
	GitConfig          CodeRepositoryGitConfigInput
}

func (CodeRepositoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*codeRepositoryArgs)(nil)).Elem()
}

type CodeRepositoryInput interface {
	pulumi.Input

	ToCodeRepositoryOutput() CodeRepositoryOutput
	ToCodeRepositoryOutputWithContext(ctx context.Context) CodeRepositoryOutput
}

func (CodeRepository) ElementType() reflect.Type {
	return reflect.TypeOf((*CodeRepository)(nil)).Elem()
}

func (i CodeRepository) ToCodeRepositoryOutput() CodeRepositoryOutput {
	return i.ToCodeRepositoryOutputWithContext(context.Background())
}

func (i CodeRepository) ToCodeRepositoryOutputWithContext(ctx context.Context) CodeRepositoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CodeRepositoryOutput)
}

type CodeRepositoryOutput struct {
	*pulumi.OutputState
}

func (CodeRepositoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CodeRepositoryOutput)(nil)).Elem()
}

func (o CodeRepositoryOutput) ToCodeRepositoryOutput() CodeRepositoryOutput {
	return o
}

func (o CodeRepositoryOutput) ToCodeRepositoryOutputWithContext(ctx context.Context) CodeRepositoryOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CodeRepositoryOutput{})
}

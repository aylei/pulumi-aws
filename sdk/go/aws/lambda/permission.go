// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Gives an external source (like a CloudWatch Event Rule, SNS, or S3) permission to access the Lambda function.
//
// ## Example Usage
// ### Specify Lambda permissions for API Gateway REST API
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/apigateway"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lambda"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		myDemoAPI, err := apigateway.NewRestApi(ctx, "myDemoAPI", &apigateway.RestApiArgs{
// 			Description: pulumi.String("This is my API for demonstration purposes"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = lambda.NewPermission(ctx, "lambdaPermission", &lambda.PermissionArgs{
// 			Action:    pulumi.String("lambda:InvokeFunction"),
// 			Function:  pulumi.String("MyDemoFunction"),
// 			Principal: pulumi.String("apigateway.amazonaws.com"),
// 			SourceArn: myDemoAPI.ExecutionArn.ApplyT(func(executionArn string) (string, error) {
// 				return fmt.Sprintf("%v%v", executionArn, "/*/*/*"), nil
// 			}).(pulumi.StringOutput),
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
// Lambda permission statements can be imported using function_name/statement_id, with an optional qualifier, e.g.
//
// ```sh
//  $ pulumi import aws:lambda/permission:Permission test_lambda_permission my_test_lambda_function/AllowExecutionFromCloudWatch
// ```
//
// ```sh
//  $ pulumi import aws:lambda/permission:Permission test_lambda_permission my_test_lambda_function:qualifier_name/AllowExecutionFromCloudWatch
// ```
type Permission struct {
	pulumi.CustomResourceState

	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action pulumi.StringOutput `pulumi:"action"`
	// The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
	EventSourceToken pulumi.StringPtrOutput `pulumi:"eventSourceToken"`
	// Name of the Lambda function whose resource policy you are updating
	Function pulumi.StringOutput `pulumi:"function"`
	// The principal who is getting this permission. e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal pulumi.StringOutput `pulumi:"principal"`
	// Query parameter to specify function version or alias name. The permission will then apply to the specific qualified ARN. e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier pulumi.StringPtrOutput `pulumi:"qualifier"`
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount pulumi.StringPtrOutput `pulumi:"sourceAccount"`
	// When the principal is an AWS service, the ARN of the specific resource within that service to grant permission to.
	// Without this, any resource from `principal` will be granted permission – even if that resource is from another account.
	// For S3, this should be the ARN of the S3 Bucket.
	// For CloudWatch Events, this should be the ARN of the CloudWatch Events Rule.
	// For API Gateway, this should be the ARN of the API, as described [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn pulumi.StringPtrOutput `pulumi:"sourceArn"`
	// A unique statement identifier. By default generated by this provider.
	StatementId pulumi.StringOutput `pulumi:"statementId"`
	// A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statementId`.
	StatementIdPrefix pulumi.StringPtrOutput `pulumi:"statementIdPrefix"`
}

// NewPermission registers a new resource with the given unique name, arguments, and options.
func NewPermission(ctx *pulumi.Context,
	name string, args *PermissionArgs, opts ...pulumi.ResourceOption) (*Permission, error) {
	if args == nil || args.Action == nil {
		return nil, errors.New("missing required argument 'Action'")
	}
	if args == nil || args.Function == nil {
		return nil, errors.New("missing required argument 'Function'")
	}
	if args == nil || args.Principal == nil {
		return nil, errors.New("missing required argument 'Principal'")
	}
	if args == nil {
		args = &PermissionArgs{}
	}
	var resource Permission
	err := ctx.RegisterResource("aws:lambda/permission:Permission", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPermission gets an existing Permission resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPermission(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PermissionState, opts ...pulumi.ResourceOption) (*Permission, error) {
	var resource Permission
	err := ctx.ReadResource("aws:lambda/permission:Permission", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Permission resources.
type permissionState struct {
	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action *string `pulumi:"action"`
	// The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
	EventSourceToken *string `pulumi:"eventSourceToken"`
	// Name of the Lambda function whose resource policy you are updating
	Function *string `pulumi:"function"`
	// The principal who is getting this permission. e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal *string `pulumi:"principal"`
	// Query parameter to specify function version or alias name. The permission will then apply to the specific qualified ARN. e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier *string `pulumi:"qualifier"`
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount *string `pulumi:"sourceAccount"`
	// When the principal is an AWS service, the ARN of the specific resource within that service to grant permission to.
	// Without this, any resource from `principal` will be granted permission – even if that resource is from another account.
	// For S3, this should be the ARN of the S3 Bucket.
	// For CloudWatch Events, this should be the ARN of the CloudWatch Events Rule.
	// For API Gateway, this should be the ARN of the API, as described [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn *string `pulumi:"sourceArn"`
	// A unique statement identifier. By default generated by this provider.
	StatementId *string `pulumi:"statementId"`
	// A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statementId`.
	StatementIdPrefix *string `pulumi:"statementIdPrefix"`
}

type PermissionState struct {
	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action pulumi.StringPtrInput
	// The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
	EventSourceToken pulumi.StringPtrInput
	// Name of the Lambda function whose resource policy you are updating
	Function pulumi.StringPtrInput
	// The principal who is getting this permission. e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal pulumi.StringPtrInput
	// Query parameter to specify function version or alias name. The permission will then apply to the specific qualified ARN. e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier pulumi.StringPtrInput
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount pulumi.StringPtrInput
	// When the principal is an AWS service, the ARN of the specific resource within that service to grant permission to.
	// Without this, any resource from `principal` will be granted permission – even if that resource is from another account.
	// For S3, this should be the ARN of the S3 Bucket.
	// For CloudWatch Events, this should be the ARN of the CloudWatch Events Rule.
	// For API Gateway, this should be the ARN of the API, as described [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn pulumi.StringPtrInput
	// A unique statement identifier. By default generated by this provider.
	StatementId pulumi.StringPtrInput
	// A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statementId`.
	StatementIdPrefix pulumi.StringPtrInput
}

func (PermissionState) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionState)(nil)).Elem()
}

type permissionArgs struct {
	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action string `pulumi:"action"`
	// The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
	EventSourceToken *string `pulumi:"eventSourceToken"`
	// Name of the Lambda function whose resource policy you are updating
	Function interface{} `pulumi:"function"`
	// The principal who is getting this permission. e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal string `pulumi:"principal"`
	// Query parameter to specify function version or alias name. The permission will then apply to the specific qualified ARN. e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier *string `pulumi:"qualifier"`
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount *string `pulumi:"sourceAccount"`
	// When the principal is an AWS service, the ARN of the specific resource within that service to grant permission to.
	// Without this, any resource from `principal` will be granted permission – even if that resource is from another account.
	// For S3, this should be the ARN of the S3 Bucket.
	// For CloudWatch Events, this should be the ARN of the CloudWatch Events Rule.
	// For API Gateway, this should be the ARN of the API, as described [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn *string `pulumi:"sourceArn"`
	// A unique statement identifier. By default generated by this provider.
	StatementId *string `pulumi:"statementId"`
	// A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statementId`.
	StatementIdPrefix *string `pulumi:"statementIdPrefix"`
}

// The set of arguments for constructing a Permission resource.
type PermissionArgs struct {
	// The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)
	Action pulumi.StringInput
	// The Event Source Token to validate.  Used with [Alexa Skills](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#use-aws-cli).
	EventSourceToken pulumi.StringPtrInput
	// Name of the Lambda function whose resource policy you are updating
	Function pulumi.Input
	// The principal who is getting this permission. e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal such as `events.amazonaws.com` or `sns.amazonaws.com`.
	Principal pulumi.StringInput
	// Query parameter to specify function version or alias name. The permission will then apply to the specific qualified ARN. e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`
	Qualifier pulumi.StringPtrInput
	// This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.
	SourceAccount pulumi.StringPtrInput
	// When the principal is an AWS service, the ARN of the specific resource within that service to grant permission to.
	// Without this, any resource from `principal` will be granted permission – even if that resource is from another account.
	// For S3, this should be the ARN of the S3 Bucket.
	// For CloudWatch Events, this should be the ARN of the CloudWatch Events Rule.
	// For API Gateway, this should be the ARN of the API, as described [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).
	SourceArn pulumi.StringPtrInput
	// A unique statement identifier. By default generated by this provider.
	StatementId pulumi.StringPtrInput
	// A statement identifier prefix. This provider will generate a unique suffix. Conflicts with `statementId`.
	StatementIdPrefix pulumi.StringPtrInput
}

func (PermissionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionArgs)(nil)).Elem()
}

type PermissionInput interface {
	pulumi.Input

	ToPermissionOutput() PermissionOutput
	ToPermissionOutputWithContext(ctx context.Context) PermissionOutput
}

func (Permission) ElementType() reflect.Type {
	return reflect.TypeOf((*Permission)(nil)).Elem()
}

func (i Permission) ToPermissionOutput() PermissionOutput {
	return i.ToPermissionOutputWithContext(context.Background())
}

func (i Permission) ToPermissionOutputWithContext(ctx context.Context) PermissionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionOutput)
}

type PermissionOutput struct {
	*pulumi.OutputState
}

func (PermissionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PermissionOutput)(nil)).Elem()
}

func (o PermissionOutput) ToPermissionOutput() PermissionOutput {
	return o
}

func (o PermissionOutput) ToPermissionOutputWithContext(ctx context.Context) PermissionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(PermissionOutput{})
}

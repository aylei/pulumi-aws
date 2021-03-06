// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lex

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an Amazon Lex Bot Alias resource. For more information see
// [Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lex"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := lex.NewBotAlias(ctx, "orderFlowersProd", &lex.BotAliasArgs{
// 			BotName:     pulumi.String("OrderFlowers"),
// 			BotVersion:  pulumi.String("1"),
// 			Description: pulumi.String("Production Version of the OrderFlowers Bot."),
// 			Name:        pulumi.String("OrderFlowersProd"),
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
// Bot aliases can be imported using an ID with the format `bot_name:bot_alias_name`.
//
// ```sh
//  $ pulumi import aws:lex/botAlias:BotAlias order_flowers_prod OrderFlowers:OrderFlowersProd
// ```
type BotAlias struct {
	pulumi.CustomResourceState

	// The ARN of the bot alias.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the bot.
	BotName pulumi.StringOutput `pulumi:"botName"`
	// The name of the bot.
	BotVersion pulumi.StringOutput `pulumi:"botVersion"`
	// Checksum of the bot alias.
	Checksum pulumi.StringOutput `pulumi:"checksum"`
	// The settings that determine how Amazon Lex uses conversation logs for the alias. Attributes are documented under conversation_logs.
	ConversationLogs BotAliasConversationLogsPtrOutput `pulumi:"conversationLogs"`
	// The date that the bot alias was created.
	CreatedDate pulumi.StringOutput `pulumi:"createdDate"`
	// A description of the alias. Must be less than or equal to 200 characters in length.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.
	LastUpdatedDate pulumi.StringOutput `pulumi:"lastUpdatedDate"`
	// The name of the alias. The name is not case sensitive. Must be less than or equal to 100 characters in length.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewBotAlias registers a new resource with the given unique name, arguments, and options.
func NewBotAlias(ctx *pulumi.Context,
	name string, args *BotAliasArgs, opts ...pulumi.ResourceOption) (*BotAlias, error) {
	if args == nil || args.BotName == nil {
		return nil, errors.New("missing required argument 'BotName'")
	}
	if args == nil || args.BotVersion == nil {
		return nil, errors.New("missing required argument 'BotVersion'")
	}
	if args == nil {
		args = &BotAliasArgs{}
	}
	var resource BotAlias
	err := ctx.RegisterResource("aws:lex/botAlias:BotAlias", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBotAlias gets an existing BotAlias resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBotAlias(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BotAliasState, opts ...pulumi.ResourceOption) (*BotAlias, error) {
	var resource BotAlias
	err := ctx.ReadResource("aws:lex/botAlias:BotAlias", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BotAlias resources.
type botAliasState struct {
	// The ARN of the bot alias.
	Arn *string `pulumi:"arn"`
	// The name of the bot.
	BotName *string `pulumi:"botName"`
	// The name of the bot.
	BotVersion *string `pulumi:"botVersion"`
	// Checksum of the bot alias.
	Checksum *string `pulumi:"checksum"`
	// The settings that determine how Amazon Lex uses conversation logs for the alias. Attributes are documented under conversation_logs.
	ConversationLogs *BotAliasConversationLogs `pulumi:"conversationLogs"`
	// The date that the bot alias was created.
	CreatedDate *string `pulumi:"createdDate"`
	// A description of the alias. Must be less than or equal to 200 characters in length.
	Description *string `pulumi:"description"`
	// The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.
	LastUpdatedDate *string `pulumi:"lastUpdatedDate"`
	// The name of the alias. The name is not case sensitive. Must be less than or equal to 100 characters in length.
	Name *string `pulumi:"name"`
}

type BotAliasState struct {
	// The ARN of the bot alias.
	Arn pulumi.StringPtrInput
	// The name of the bot.
	BotName pulumi.StringPtrInput
	// The name of the bot.
	BotVersion pulumi.StringPtrInput
	// Checksum of the bot alias.
	Checksum pulumi.StringPtrInput
	// The settings that determine how Amazon Lex uses conversation logs for the alias. Attributes are documented under conversation_logs.
	ConversationLogs BotAliasConversationLogsPtrInput
	// The date that the bot alias was created.
	CreatedDate pulumi.StringPtrInput
	// A description of the alias. Must be less than or equal to 200 characters in length.
	Description pulumi.StringPtrInput
	// The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.
	LastUpdatedDate pulumi.StringPtrInput
	// The name of the alias. The name is not case sensitive. Must be less than or equal to 100 characters in length.
	Name pulumi.StringPtrInput
}

func (BotAliasState) ElementType() reflect.Type {
	return reflect.TypeOf((*botAliasState)(nil)).Elem()
}

type botAliasArgs struct {
	// The name of the bot.
	BotName string `pulumi:"botName"`
	// The name of the bot.
	BotVersion string `pulumi:"botVersion"`
	// The settings that determine how Amazon Lex uses conversation logs for the alias. Attributes are documented under conversation_logs.
	ConversationLogs *BotAliasConversationLogs `pulumi:"conversationLogs"`
	// A description of the alias. Must be less than or equal to 200 characters in length.
	Description *string `pulumi:"description"`
	// The name of the alias. The name is not case sensitive. Must be less than or equal to 100 characters in length.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a BotAlias resource.
type BotAliasArgs struct {
	// The name of the bot.
	BotName pulumi.StringInput
	// The name of the bot.
	BotVersion pulumi.StringInput
	// The settings that determine how Amazon Lex uses conversation logs for the alias. Attributes are documented under conversation_logs.
	ConversationLogs BotAliasConversationLogsPtrInput
	// A description of the alias. Must be less than or equal to 200 characters in length.
	Description pulumi.StringPtrInput
	// The name of the alias. The name is not case sensitive. Must be less than or equal to 100 characters in length.
	Name pulumi.StringPtrInput
}

func (BotAliasArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*botAliasArgs)(nil)).Elem()
}

type BotAliasInput interface {
	pulumi.Input

	ToBotAliasOutput() BotAliasOutput
	ToBotAliasOutputWithContext(ctx context.Context) BotAliasOutput
}

func (BotAlias) ElementType() reflect.Type {
	return reflect.TypeOf((*BotAlias)(nil)).Elem()
}

func (i BotAlias) ToBotAliasOutput() BotAliasOutput {
	return i.ToBotAliasOutputWithContext(context.Background())
}

func (i BotAlias) ToBotAliasOutputWithContext(ctx context.Context) BotAliasOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BotAliasOutput)
}

type BotAliasOutput struct {
	*pulumi.OutputState
}

func (BotAliasOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*BotAliasOutput)(nil)).Elem()
}

func (o BotAliasOutput) ToBotAliasOutput() BotAliasOutput {
	return o
}

func (o BotAliasOutput) ToBotAliasOutputWithContext(ctx context.Context) BotAliasOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(BotAliasOutput{})
}

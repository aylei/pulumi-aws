// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a DB event subscription resource.
// 
// ## Attributes
// 
// The following additional atttributes are provided:
// 
// * `id` - The name of the RDS event notification subscription
// * `arn` - The Amazon Resource Name of the RDS event notification subscription
// * `customer_aws_id` - The AWS customer account associated with the RDS event notification subscription
type EventSubscription struct {
	s *pulumi.ResourceState
}

// NewEventSubscription registers a new resource with the given unique name, arguments, and options.
func NewEventSubscription(ctx *pulumi.Context,
	name string, args *EventSubscriptionArgs, opts ...pulumi.ResourceOpt) (*EventSubscription, error) {
	if args == nil || args.SnsTopic == nil {
		return nil, errors.New("missing required argument 'SnsTopic'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["enabled"] = nil
		inputs["eventCategories"] = nil
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["snsTopic"] = nil
		inputs["sourceIds"] = nil
		inputs["sourceType"] = nil
		inputs["tags"] = nil
	} else {
		inputs["enabled"] = args.Enabled
		inputs["eventCategories"] = args.EventCategories
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["snsTopic"] = args.SnsTopic
		inputs["sourceIds"] = args.SourceIds
		inputs["sourceType"] = args.SourceType
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	inputs["customerAwsId"] = nil
	s, err := ctx.RegisterResource("aws:rds/eventSubscription:EventSubscription", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &EventSubscription{s: s}, nil
}

// GetEventSubscription gets an existing EventSubscription resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventSubscription(ctx *pulumi.Context,
	name string, id pulumi.ID, state *EventSubscriptionState, opts ...pulumi.ResourceOpt) (*EventSubscription, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["customerAwsId"] = state.CustomerAwsId
		inputs["enabled"] = state.Enabled
		inputs["eventCategories"] = state.EventCategories
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["snsTopic"] = state.SnsTopic
		inputs["sourceIds"] = state.SourceIds
		inputs["sourceType"] = state.SourceType
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:rds/eventSubscription:EventSubscription", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &EventSubscription{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *EventSubscription) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *EventSubscription) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *EventSubscription) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

func (r *EventSubscription) CustomerAwsId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["customerAwsId"])
}

// A boolean flag to enable/disable the subscription. Defaults to true.
func (r *EventSubscription) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

// A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.
func (r *EventSubscription) EventCategories() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["eventCategories"])
}

// The name of the DB event subscription. By default generated by Terraform.
func (r *EventSubscription) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the DB event subscription. Conflicts with `name`.
func (r *EventSubscription) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// The SNS topic to send events to.
func (r *EventSubscription) SnsTopic() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["snsTopic"])
}

// A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.
func (r *EventSubscription) SourceIds() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["sourceIds"])
}

// The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
func (r *EventSubscription) SourceType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sourceType"])
}

// A mapping of tags to assign to the resource.
func (r *EventSubscription) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering EventSubscription resources.
type EventSubscriptionState struct {
	Arn interface{}
	CustomerAwsId interface{}
	// A boolean flag to enable/disable the subscription. Defaults to true.
	Enabled interface{}
	// A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.
	EventCategories interface{}
	// The name of the DB event subscription. By default generated by Terraform.
	Name interface{}
	// The name of the DB event subscription. Conflicts with `name`.
	NamePrefix interface{}
	// The SNS topic to send events to.
	SnsTopic interface{}
	// A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.
	SourceIds interface{}
	// The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
	SourceType interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a EventSubscription resource.
type EventSubscriptionArgs struct {
	// A boolean flag to enable/disable the subscription. Defaults to true.
	Enabled interface{}
	// A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.
	EventCategories interface{}
	// The name of the DB event subscription. By default generated by Terraform.
	Name interface{}
	// The name of the DB event subscription. Conflicts with `name`.
	NamePrefix interface{}
	// The SNS topic to send events to.
	SnsTopic interface{}
	// A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.
	SourceIds interface{}
	// The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
	SourceType interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

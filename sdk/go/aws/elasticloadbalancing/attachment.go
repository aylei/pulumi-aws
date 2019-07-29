// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticloadbalancing

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elb_attachment_legacy.html.markdown.
type Attachment struct {
	s *pulumi.ResourceState
}

// NewAttachment registers a new resource with the given unique name, arguments, and options.
func NewAttachment(ctx *pulumi.Context,
	name string, args *AttachmentArgs, opts ...pulumi.ResourceOpt) (*Attachment, error) {
	if args == nil || args.Elb == nil {
		return nil, errors.New("missing required argument 'Elb'")
	}
	if args == nil || args.Instance == nil {
		return nil, errors.New("missing required argument 'Instance'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["elb"] = nil
		inputs["instance"] = nil
	} else {
		inputs["elb"] = args.Elb
		inputs["instance"] = args.Instance
	}
	s, err := ctx.RegisterResource("aws:elasticloadbalancing/attachment:Attachment", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Attachment{s: s}, nil
}

// GetAttachment gets an existing Attachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAttachment(ctx *pulumi.Context,
	name string, id pulumi.ID, state *AttachmentState, opts ...pulumi.ResourceOpt) (*Attachment, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["elb"] = state.Elb
		inputs["instance"] = state.Instance
	}
	s, err := ctx.ReadResource("aws:elasticloadbalancing/attachment:Attachment", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Attachment{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Attachment) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Attachment) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the ELB.
func (r *Attachment) Elb() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["elb"])
}

// Instance ID to place in the ELB pool.
func (r *Attachment) Instance() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instance"])
}

// Input properties used for looking up and filtering Attachment resources.
type AttachmentState struct {
	// The name of the ELB.
	Elb interface{}
	// Instance ID to place in the ELB pool.
	Instance interface{}
}

// The set of arguments for constructing a Attachment resource.
type AttachmentArgs struct {
	// The name of the ELB.
	Elb interface{}
	// Instance ID to place in the ELB pool.
	Instance interface{}
}

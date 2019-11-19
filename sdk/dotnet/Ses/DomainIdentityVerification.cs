// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ses
{
    /// <summary>
    /// Represents a successful verification of an SES domain identity.
    /// 
    /// Most commonly, this resource is used together with `aws.route53.Record` and
    /// `aws.ses.DomainIdentity` to request an SES domain identity,
    /// deploy the required DNS verification records, and wait for verification to complete.
    /// 
    /// &gt; **WARNING:** This resource implements a part of the verification workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_identity_verification.html.markdown.
    /// </summary>
    public partial class DomainIdentityVerification : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the domain identity.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The domain name of the SES domain identity to verify.
        /// </summary>
        [Output("domain")]
        public Output<string> Domain { get; private set; } = null!;


        /// <summary>
        /// Create a DomainIdentityVerification resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DomainIdentityVerification(string name, DomainIdentityVerificationArgs args, CustomResourceOptions? options = null)
            : base("aws:ses/domainIdentityVerification:DomainIdentityVerification", name, args, MakeResourceOptions(options, ""))
        {
        }

        private DomainIdentityVerification(string name, Input<string> id, DomainIdentityVerificationState? state = null, CustomResourceOptions? options = null)
            : base("aws:ses/domainIdentityVerification:DomainIdentityVerification", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DomainIdentityVerification resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DomainIdentityVerification Get(string name, Input<string> id, DomainIdentityVerificationState? state = null, CustomResourceOptions? options = null)
        {
            return new DomainIdentityVerification(name, id, state, options);
        }
    }

    public sealed class DomainIdentityVerificationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The domain name of the SES domain identity to verify.
        /// </summary>
        [Input("domain", required: true)]
        public Input<string> Domain { get; set; } = null!;

        public DomainIdentityVerificationArgs()
        {
        }
    }

    public sealed class DomainIdentityVerificationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the domain identity.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The domain name of the SES domain identity to verify.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        public DomainIdentityVerificationState()
        {
        }
    }
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Cfg.Inputs
{

    public sealed class RuleScopeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
        /// If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
        /// </summary>
        [Input("complianceResourceId")]
        public Input<string>? ComplianceResourceId { get; set; }

        [Input("complianceResourceTypes")]
        private InputList<string>? _complianceResourceTypes;

        /// <summary>
        /// A list of resource types of only those AWS resources that you want to trigger an
        /// evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
        /// a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
        /// </summary>
        public InputList<string> ComplianceResourceTypes
        {
            get => _complianceResourceTypes ?? (_complianceResourceTypes = new InputList<string>());
            set => _complianceResourceTypes = value;
        }

        /// <summary>
        /// The tag key that is applied to only those AWS resources that you want you
        /// want to trigger an evaluation for the rule.
        /// </summary>
        [Input("tagKey")]
        public Input<string>? TagKey { get; set; }

        /// <summary>
        /// The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.
        /// </summary>
        [Input("tagValue")]
        public Input<string>? TagValue { get; set; }

        public RuleScopeArgs()
        {
        }
    }
}
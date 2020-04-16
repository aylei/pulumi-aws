// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.CodeDeploy.Outputs
{

    [OutputType]
    public sealed class DeploymentConfigTrafficRoutingConfigTimeBasedCanary
    {
        /// <summary>
        /// The number of minutes between the first and second traffic shifts of a `TimeBasedCanary` deployment.
        /// </summary>
        public readonly int? Interval;
        /// <summary>
        /// The percentage of traffic to shift in the first increment of a `TimeBasedCanary` deployment.
        /// </summary>
        public readonly int? Percentage;

        [OutputConstructor]
        private DeploymentConfigTrafficRoutingConfigTimeBasedCanary(
            int? interval,

            int? percentage)
        {
            Interval = interval;
            Percentage = percentage;
        }
    }
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppAutoScaling.Inputs
{

    public sealed class PolicyStepScalingPolicyConfigurationGetArgs : Pulumi.ResourceArgs
    {
        [Input("adjustmentType")]
        public Input<string>? AdjustmentType { get; set; }

        [Input("cooldown")]
        public Input<int>? Cooldown { get; set; }

        [Input("metricAggregationType")]
        public Input<string>? MetricAggregationType { get; set; }

        [Input("minAdjustmentMagnitude")]
        public Input<int>? MinAdjustmentMagnitude { get; set; }

        [Input("stepAdjustments")]
        private InputList<Inputs.PolicyStepScalingPolicyConfigurationStepAdjustmentGetArgs>? _stepAdjustments;
        public InputList<Inputs.PolicyStepScalingPolicyConfigurationStepAdjustmentGetArgs> StepAdjustments
        {
            get => _stepAdjustments ?? (_stepAdjustments = new InputList<Inputs.PolicyStepScalingPolicyConfigurationStepAdjustmentGetArgs>());
            set => _stepAdjustments = value;
        }

        public PolicyStepScalingPolicyConfigurationGetArgs()
        {
        }
    }
}
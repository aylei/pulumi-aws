// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an AWS Config Remediation Configuration.
 *
 * > **Note:** Config Remediation Configuration requires an existing [Config Rule](https://www.terraform.io/docs/providers/aws/r/config_config_rule.html) to be present.
 *
 * ## Example Usage
 *
 * AWS managed rules can be used by setting the source owner to `AWS` and the source identifier to the name of the managed rule. More information about AWS managed rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const thisRule = new aws.cfg.Rule("thisRule", {source: {
 *     owner: "AWS",
 *     sourceIdentifier: "S3_BUCKET_VERSIONING_ENABLED",
 * }});
 * const thisRemediationConfiguration = new aws.cfg.RemediationConfiguration("thisRemediationConfiguration", {
 *     configRuleName: thisRule.name,
 *     resourceType: "AWS::S3::Bucket",
 *     targetType: "SSM_DOCUMENT",
 *     targetId: "AWS-EnableS3BucketEncryption",
 *     targetVersion: "1",
 *     parameters: [
 *         {
 *             name: "AutomationAssumeRole",
 *             staticValue: "arn:aws:iam::875924563244:role/security_config",
 *         },
 *         {
 *             name: "BucketName",
 *             resourceValue: "RESOURCE_ID",
 *         },
 *         {
 *             name: "SSEAlgorithm",
 *             staticValue: "AES256",
 *         },
 *     ],
 * });
 * ```
 */
export class RemediationConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing RemediationConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RemediationConfigurationState, opts?: pulumi.CustomResourceOptions): RemediationConfiguration {
        return new RemediationConfiguration(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:cfg/remediationConfiguration:RemediationConfiguration';

    /**
     * Returns true if the given object is an instance of RemediationConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RemediationConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RemediationConfiguration.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The name of the AWS Config rule
     */
    public readonly configRuleName!: pulumi.Output<string>;
    /**
     * Can be specified multiple times for each
     * parameter. Each parameter block supports fields documented below.
     */
    public readonly parameters!: pulumi.Output<outputs.cfg.RemediationConfigurationParameter[] | undefined>;
    /**
     * The type of a resource
     */
    public readonly resourceType!: pulumi.Output<string | undefined>;
    /**
     * Target ID is the name of the public document
     */
    public readonly targetId!: pulumi.Output<string>;
    /**
     * The type of the target. Target executes remediation. For example, SSM document
     */
    public readonly targetType!: pulumi.Output<string>;
    /**
     * Version of the target. For example, version of the SSM document
     */
    public readonly targetVersion!: pulumi.Output<string | undefined>;

    /**
     * Create a RemediationConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RemediationConfigurationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RemediationConfigurationArgs | RemediationConfigurationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RemediationConfigurationState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["configRuleName"] = state ? state.configRuleName : undefined;
            inputs["parameters"] = state ? state.parameters : undefined;
            inputs["resourceType"] = state ? state.resourceType : undefined;
            inputs["targetId"] = state ? state.targetId : undefined;
            inputs["targetType"] = state ? state.targetType : undefined;
            inputs["targetVersion"] = state ? state.targetVersion : undefined;
        } else {
            const args = argsOrState as RemediationConfigurationArgs | undefined;
            if (!args || args.configRuleName === undefined) {
                throw new Error("Missing required property 'configRuleName'");
            }
            if (!args || args.targetId === undefined) {
                throw new Error("Missing required property 'targetId'");
            }
            if (!args || args.targetType === undefined) {
                throw new Error("Missing required property 'targetType'");
            }
            inputs["configRuleName"] = args ? args.configRuleName : undefined;
            inputs["parameters"] = args ? args.parameters : undefined;
            inputs["resourceType"] = args ? args.resourceType : undefined;
            inputs["targetId"] = args ? args.targetId : undefined;
            inputs["targetType"] = args ? args.targetType : undefined;
            inputs["targetVersion"] = args ? args.targetVersion : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RemediationConfiguration.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RemediationConfiguration resources.
 */
export interface RemediationConfigurationState {
    readonly arn?: pulumi.Input<string>;
    /**
     * The name of the AWS Config rule
     */
    readonly configRuleName?: pulumi.Input<string>;
    /**
     * Can be specified multiple times for each
     * parameter. Each parameter block supports fields documented below.
     */
    readonly parameters?: pulumi.Input<pulumi.Input<inputs.cfg.RemediationConfigurationParameter>[]>;
    /**
     * The type of a resource
     */
    readonly resourceType?: pulumi.Input<string>;
    /**
     * Target ID is the name of the public document
     */
    readonly targetId?: pulumi.Input<string>;
    /**
     * The type of the target. Target executes remediation. For example, SSM document
     */
    readonly targetType?: pulumi.Input<string>;
    /**
     * Version of the target. For example, version of the SSM document
     */
    readonly targetVersion?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RemediationConfiguration resource.
 */
export interface RemediationConfigurationArgs {
    /**
     * The name of the AWS Config rule
     */
    readonly configRuleName: pulumi.Input<string>;
    /**
     * Can be specified multiple times for each
     * parameter. Each parameter block supports fields documented below.
     */
    readonly parameters?: pulumi.Input<pulumi.Input<inputs.cfg.RemediationConfigurationParameter>[]>;
    /**
     * The type of a resource
     */
    readonly resourceType?: pulumi.Input<string>;
    /**
     * Target ID is the name of the public document
     */
    readonly targetId: pulumi.Input<string>;
    /**
     * The type of the target. Target executes remediation. For example, SSM document
     */
    readonly targetType: pulumi.Input<string>;
    /**
     * Version of the target. For example, version of the SSM document
     */
    readonly targetVersion?: pulumi.Input<string>;
}

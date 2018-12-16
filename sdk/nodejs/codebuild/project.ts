// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {Tags} from "../index";

/**
 * Provides a CodeBuild Project resource. See also the [`aws_codebuild_webhook` resource](https://www.terraform.io/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).
 */
export class Project extends pulumi.CustomResource {
    /**
     * Get an existing Project resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState, opts?: pulumi.CustomResourceOptions): Project {
        return new Project(name, <any>state, { ...opts, id: id });
    }

    /**
     * The ARN of the CodeBuild project.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * Information about the project's build output artifacts. Artifact blocks are documented below.
     */
    public readonly artifacts: pulumi.Output<{ encryptionDisabled?: boolean, location?: string, name?: string, namespaceType?: string, packaging?: string, path?: string, type: string }>;
    /**
     * Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
     */
    public readonly badgeEnabled: pulumi.Output<boolean | undefined>;
    /**
     * The URL of the build badge when `badge_enabled` is enabled.
     */
    public /*out*/ readonly badgeUrl: pulumi.Output<string>;
    /**
     * How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
     */
    public readonly buildTimeout: pulumi.Output<number | undefined>;
    /**
     * Information about the cache storage for the project. Cache blocks are documented below.
     */
    public readonly cache: pulumi.Output<{ location?: string, type?: string } | undefined>;
    /**
     * A short description of the project.
     */
    public readonly description: pulumi.Output<string>;
    /**
     * The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.
     */
    public readonly encryptionKey: pulumi.Output<string>;
    /**
     * Information about the project's build environment. Environment blocks are documented below.
     */
    public readonly environment: pulumi.Output<{ certificate?: string, computeType: string, environmentVariables: { name: string, type?: string, value: string }[], image: string, privilegedMode?: boolean, type: string }>;
    /**
     * The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
     */
    public readonly name: pulumi.Output<string>;
    /**
     * A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
     */
    public readonly secondaryArtifacts: pulumi.Output<{ artifactIdentifier: string, encryptionDisabled?: boolean, location?: string, name?: string, namespaceType?: string, packaging?: string, path?: string, type: string }[] | undefined>;
    /**
     * A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
     */
    public readonly secondarySources: pulumi.Output<{ auths?: { resource?: string, type: string }[], buildspec?: string, gitCloneDepth?: number, insecureSsl?: boolean, location?: string, reportBuildStatus?: boolean, sourceIdentifier: string, type: string }[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
     */
    public readonly serviceRole: pulumi.Output<string>;
    /**
     * Information about the project's input source code. Source blocks are documented below.
     */
    public readonly source: pulumi.Output<{ auths?: { resource?: string, type: string }[], buildspec?: string, gitCloneDepth?: number, insecureSsl?: boolean, location?: string, reportBuildStatus?: boolean, type: string }>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<Tags | undefined>;
    /**
     * Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
     */
    public readonly vpcConfig: pulumi.Output<{ securityGroupIds: string[], subnets: string[], vpcId: string } | undefined>;

    /**
     * Create a Project resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProjectArgs | ProjectState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ProjectState = argsOrState as ProjectState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["artifacts"] = state ? state.artifacts : undefined;
            inputs["badgeEnabled"] = state ? state.badgeEnabled : undefined;
            inputs["badgeUrl"] = state ? state.badgeUrl : undefined;
            inputs["buildTimeout"] = state ? state.buildTimeout : undefined;
            inputs["cache"] = state ? state.cache : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["encryptionKey"] = state ? state.encryptionKey : undefined;
            inputs["environment"] = state ? state.environment : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["secondaryArtifacts"] = state ? state.secondaryArtifacts : undefined;
            inputs["secondarySources"] = state ? state.secondarySources : undefined;
            inputs["serviceRole"] = state ? state.serviceRole : undefined;
            inputs["source"] = state ? state.source : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcConfig"] = state ? state.vpcConfig : undefined;
        } else {
            const args = argsOrState as ProjectArgs | undefined;
            if (!args || args.artifacts === undefined) {
                throw new Error("Missing required property 'artifacts'");
            }
            if (!args || args.environment === undefined) {
                throw new Error("Missing required property 'environment'");
            }
            if (!args || args.serviceRole === undefined) {
                throw new Error("Missing required property 'serviceRole'");
            }
            if (!args || args.source === undefined) {
                throw new Error("Missing required property 'source'");
            }
            inputs["artifacts"] = args ? args.artifacts : undefined;
            inputs["badgeEnabled"] = args ? args.badgeEnabled : undefined;
            inputs["buildTimeout"] = args ? args.buildTimeout : undefined;
            inputs["cache"] = args ? args.cache : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["encryptionKey"] = args ? args.encryptionKey : undefined;
            inputs["environment"] = args ? args.environment : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["secondaryArtifacts"] = args ? args.secondaryArtifacts : undefined;
            inputs["secondarySources"] = args ? args.secondarySources : undefined;
            inputs["serviceRole"] = args ? args.serviceRole : undefined;
            inputs["source"] = args ? args.source : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcConfig"] = args ? args.vpcConfig : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["badgeUrl"] = undefined /*out*/;
        }
        super("aws:codebuild/project:Project", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Project resources.
 */
export interface ProjectState {
    /**
     * The ARN of the CodeBuild project.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * Information about the project's build output artifacts. Artifact blocks are documented below.
     */
    readonly artifacts?: pulumi.Input<{ encryptionDisabled?: pulumi.Input<boolean>, location?: pulumi.Input<string>, name?: pulumi.Input<string>, namespaceType?: pulumi.Input<string>, packaging?: pulumi.Input<string>, path?: pulumi.Input<string>, type: pulumi.Input<string> }>;
    /**
     * Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
     */
    readonly badgeEnabled?: pulumi.Input<boolean>;
    /**
     * The URL of the build badge when `badge_enabled` is enabled.
     */
    readonly badgeUrl?: pulumi.Input<string>;
    /**
     * How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
     */
    readonly buildTimeout?: pulumi.Input<number>;
    /**
     * Information about the cache storage for the project. Cache blocks are documented below.
     */
    readonly cache?: pulumi.Input<{ location?: pulumi.Input<string>, type?: pulumi.Input<string> }>;
    /**
     * A short description of the project.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.
     */
    readonly encryptionKey?: pulumi.Input<string>;
    /**
     * Information about the project's build environment. Environment blocks are documented below.
     */
    readonly environment?: pulumi.Input<{ certificate?: pulumi.Input<string>, computeType: pulumi.Input<string>, environmentVariables?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, type?: pulumi.Input<string>, value: pulumi.Input<string> }>[]>, image: pulumi.Input<string>, privilegedMode?: pulumi.Input<boolean>, type: pulumi.Input<string> }>;
    /**
     * The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
     */
    readonly secondaryArtifacts?: pulumi.Input<pulumi.Input<{ artifactIdentifier: pulumi.Input<string>, encryptionDisabled?: pulumi.Input<boolean>, location?: pulumi.Input<string>, name?: pulumi.Input<string>, namespaceType?: pulumi.Input<string>, packaging?: pulumi.Input<string>, path?: pulumi.Input<string>, type: pulumi.Input<string> }>[]>;
    /**
     * A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
     */
    readonly secondarySources?: pulumi.Input<pulumi.Input<{ auths?: pulumi.Input<pulumi.Input<{ resource?: pulumi.Input<string>, type: pulumi.Input<string> }>[]>, buildspec?: pulumi.Input<string>, gitCloneDepth?: pulumi.Input<number>, insecureSsl?: pulumi.Input<boolean>, location?: pulumi.Input<string>, reportBuildStatus?: pulumi.Input<boolean>, sourceIdentifier: pulumi.Input<string>, type: pulumi.Input<string> }>[]>;
    /**
     * The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
     */
    readonly serviceRole?: pulumi.Input<string>;
    /**
     * Information about the project's input source code. Source blocks are documented below.
     */
    readonly source?: pulumi.Input<{ auths?: pulumi.Input<pulumi.Input<{ resource?: pulumi.Input<string>, type: pulumi.Input<string> }>[]>, buildspec?: pulumi.Input<string>, gitCloneDepth?: pulumi.Input<number>, insecureSsl?: pulumi.Input<boolean>, location?: pulumi.Input<string>, reportBuildStatus?: pulumi.Input<boolean>, type: pulumi.Input<string> }>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
     */
    readonly vpcConfig?: pulumi.Input<{ securityGroupIds: pulumi.Input<pulumi.Input<string>[]>, subnets: pulumi.Input<pulumi.Input<string>[]>, vpcId: pulumi.Input<string> }>;
}

/**
 * The set of arguments for constructing a Project resource.
 */
export interface ProjectArgs {
    /**
     * Information about the project's build output artifacts. Artifact blocks are documented below.
     */
    readonly artifacts: pulumi.Input<{ encryptionDisabled?: pulumi.Input<boolean>, location?: pulumi.Input<string>, name?: pulumi.Input<string>, namespaceType?: pulumi.Input<string>, packaging?: pulumi.Input<string>, path?: pulumi.Input<string>, type: pulumi.Input<string> }>;
    /**
     * Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
     */
    readonly badgeEnabled?: pulumi.Input<boolean>;
    /**
     * How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
     */
    readonly buildTimeout?: pulumi.Input<number>;
    /**
     * Information about the cache storage for the project. Cache blocks are documented below.
     */
    readonly cache?: pulumi.Input<{ location?: pulumi.Input<string>, type?: pulumi.Input<string> }>;
    /**
     * A short description of the project.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.
     */
    readonly encryptionKey?: pulumi.Input<string>;
    /**
     * Information about the project's build environment. Environment blocks are documented below.
     */
    readonly environment: pulumi.Input<{ certificate?: pulumi.Input<string>, computeType: pulumi.Input<string>, environmentVariables?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, type?: pulumi.Input<string>, value: pulumi.Input<string> }>[]>, image: pulumi.Input<string>, privilegedMode?: pulumi.Input<boolean>, type: pulumi.Input<string> }>;
    /**
     * The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
     */
    readonly secondaryArtifacts?: pulumi.Input<pulumi.Input<{ artifactIdentifier: pulumi.Input<string>, encryptionDisabled?: pulumi.Input<boolean>, location?: pulumi.Input<string>, name?: pulumi.Input<string>, namespaceType?: pulumi.Input<string>, packaging?: pulumi.Input<string>, path?: pulumi.Input<string>, type: pulumi.Input<string> }>[]>;
    /**
     * A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
     */
    readonly secondarySources?: pulumi.Input<pulumi.Input<{ auths?: pulumi.Input<pulumi.Input<{ resource?: pulumi.Input<string>, type: pulumi.Input<string> }>[]>, buildspec?: pulumi.Input<string>, gitCloneDepth?: pulumi.Input<number>, insecureSsl?: pulumi.Input<boolean>, location?: pulumi.Input<string>, reportBuildStatus?: pulumi.Input<boolean>, sourceIdentifier: pulumi.Input<string>, type: pulumi.Input<string> }>[]>;
    /**
     * The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
     */
    readonly serviceRole: pulumi.Input<string>;
    /**
     * Information about the project's input source code. Source blocks are documented below.
     */
    readonly source: pulumi.Input<{ auths?: pulumi.Input<pulumi.Input<{ resource?: pulumi.Input<string>, type: pulumi.Input<string> }>[]>, buildspec?: pulumi.Input<string>, gitCloneDepth?: pulumi.Input<number>, insecureSsl?: pulumi.Input<boolean>, location?: pulumi.Input<string>, reportBuildStatus?: pulumi.Input<boolean>, type: pulumi.Input<string> }>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<Tags>;
    /**
     * Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
     */
    readonly vpcConfig?: pulumi.Input<{ securityGroupIds: pulumi.Input<pulumi.Input<string>[]>, subnets: pulumi.Input<pulumi.Input<string>[]>, vpcId: pulumi.Input<string> }>;
}

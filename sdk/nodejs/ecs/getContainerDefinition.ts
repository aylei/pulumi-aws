// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The ECS container definition data source allows access to details of
 * a specific container within an AWS ECS service.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const ecs_mongo = pulumi.output(aws.ecs.getContainerDefinition({
 *     containerName: "mongodb",
 *     taskDefinition: aws_ecs_task_definition_mongo.id,
 * }));
 * ```
 */
export function getContainerDefinition(args: GetContainerDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetContainerDefinitionResult> {
    return pulumi.runtime.invoke("aws:ecs/getContainerDefinition:getContainerDefinition", {
        "containerName": args.containerName,
        "taskDefinition": args.taskDefinition,
    }, opts);
}

/**
 * A collection of arguments for invoking getContainerDefinition.
 */
export interface GetContainerDefinitionArgs {
    /**
     * The name of the container definition
     */
    readonly containerName: string;
    /**
     * The ARN of the task definition which contains the container
     */
    readonly taskDefinition: string;
}

/**
 * A collection of values returned by getContainerDefinition.
 */
export interface GetContainerDefinitionResult {
    /**
     * The CPU limit for this container definition
     */
    readonly cpu: number;
    /**
     * Indicator if networking is disabled
     */
    readonly disableNetworking: boolean;
    /**
     * Set docker labels
     */
    readonly dockerLabels: {[key: string]: string};
    /**
     * The environment in use
     */
    readonly environment: {[key: string]: string};
    /**
     * The docker image in use, including the digest
     */
    readonly image: string;
    /**
     * The digest of the docker image in use
     */
    readonly imageDigest: string;
    /**
     * The memory limit for this container definition
     */
    readonly memory: number;
    /**
     * The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit
     */
    readonly memoryReservation: number;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}

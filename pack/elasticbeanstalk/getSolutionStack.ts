// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "pulumi";

/**
 * Use this data source to get the name of a elastic beanstalk solution stack.
 */
export function getSolutionStack(args: GetSolutionStackArgs): Promise<GetSolutionStackResult> {
    return pulumi.runtime.invoke("aws:elasticbeanstalk/getSolutionStack:getSolutionStack", {
        "mostRecent": args.mostRecent,
        "nameRegex": args.nameRegex,
    });
}

/**
 * A collection of arguments for invoking getSolutionStack.
 */
export interface GetSolutionStackArgs {
    /**
     * If more than one result is returned, use the most
     * recent solution stack.
     */
    mostRecent?: pulumi.ComputedValue<boolean>;
    /**
     * A regex string to apply to the solution stack list returned
     * by AWS.
     */
    nameRegex: pulumi.ComputedValue<string>;
}

/**
 * A collection of values returned by getSolutionStack.
 */
export interface GetSolutionStackResult {
    /**
     * The name of the solution stack.
     */
    name: string;
}

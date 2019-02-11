// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an EC2 Transit Gateway Route.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.ec2transitgateway.Route("example", {
 *     destinationCidrBlock: "0.0.0.0/0",
 *     transitGatewayAttachmentId: aws_ec2_transit_gateway_vpc_attachment_example.id,
 *     transitGatewayRouteTableId: aws_ec2_transit_gateway_example.associationDefaultRouteTableId,
 * });
 * ```
 */
export class Route extends pulumi.CustomResource {
    /**
     * Get an existing Route resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteState, opts?: pulumi.CustomResourceOptions): Route {
        return new Route(name, <any>state, { ...opts, id: id });
    }

    /**
     * IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
     */
    public readonly destinationCidrBlock: pulumi.Output<string>;
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    public readonly transitGatewayAttachmentId: pulumi.Output<string>;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    public readonly transitGatewayRouteTableId: pulumi.Output<string>;

    /**
     * Create a Route resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RouteArgs | RouteState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: RouteState = argsOrState as RouteState | undefined;
            inputs["destinationCidrBlock"] = state ? state.destinationCidrBlock : undefined;
            inputs["transitGatewayAttachmentId"] = state ? state.transitGatewayAttachmentId : undefined;
            inputs["transitGatewayRouteTableId"] = state ? state.transitGatewayRouteTableId : undefined;
        } else {
            const args = argsOrState as RouteArgs | undefined;
            if (!args || args.destinationCidrBlock === undefined) {
                throw new Error("Missing required property 'destinationCidrBlock'");
            }
            if (!args || args.transitGatewayAttachmentId === undefined) {
                throw new Error("Missing required property 'transitGatewayAttachmentId'");
            }
            if (!args || args.transitGatewayRouteTableId === undefined) {
                throw new Error("Missing required property 'transitGatewayRouteTableId'");
            }
            inputs["destinationCidrBlock"] = args ? args.destinationCidrBlock : undefined;
            inputs["transitGatewayAttachmentId"] = args ? args.transitGatewayAttachmentId : undefined;
            inputs["transitGatewayRouteTableId"] = args ? args.transitGatewayRouteTableId : undefined;
        }
        super("aws:ec2transitgateway/route:Route", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Route resources.
 */
export interface RouteState {
    /**
     * IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
     */
    readonly destinationCidrBlock?: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    readonly transitGatewayAttachmentId?: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    readonly transitGatewayRouteTableId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Route resource.
 */
export interface RouteArgs {
    /**
     * IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
     */
    readonly destinationCidrBlock: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Attachment.
     */
    readonly transitGatewayAttachmentId: pulumi.Input<string>;
    /**
     * Identifier of EC2 Transit Gateway Route Table.
     */
    readonly transitGatewayRouteTableId: pulumi.Input<string>;
}

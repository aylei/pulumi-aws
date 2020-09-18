// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Rds
{
    public partial class ProxyDefaultTargetGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) representing the target group.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The settings that determine the size and behavior of the connection pool for the target group.
        /// </summary>
        [Output("connectionPoolConfig")]
        public Output<Outputs.ProxyDefaultTargetGroupConnectionPoolConfig> ConnectionPoolConfig { get; private set; } = null!;

        /// <summary>
        /// Name of the RDS DB Proxy.
        /// </summary>
        [Output("dbProxyName")]
        public Output<string> DbProxyName { get; private set; } = null!;

        /// <summary>
        /// The name of the default target group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a ProxyDefaultTargetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProxyDefaultTargetGroup(string name, ProxyDefaultTargetGroupArgs args, CustomResourceOptions? options = null)
            : base("aws:rds/proxyDefaultTargetGroup:ProxyDefaultTargetGroup", name, args ?? new ProxyDefaultTargetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ProxyDefaultTargetGroup(string name, Input<string> id, ProxyDefaultTargetGroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:rds/proxyDefaultTargetGroup:ProxyDefaultTargetGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ProxyDefaultTargetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProxyDefaultTargetGroup Get(string name, Input<string> id, ProxyDefaultTargetGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new ProxyDefaultTargetGroup(name, id, state, options);
        }
    }

    public sealed class ProxyDefaultTargetGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The settings that determine the size and behavior of the connection pool for the target group.
        /// </summary>
        [Input("connectionPoolConfig", required: true)]
        public Input<Inputs.ProxyDefaultTargetGroupConnectionPoolConfigArgs> ConnectionPoolConfig { get; set; } = null!;

        /// <summary>
        /// Name of the RDS DB Proxy.
        /// </summary>
        [Input("dbProxyName", required: true)]
        public Input<string> DbProxyName { get; set; } = null!;

        public ProxyDefaultTargetGroupArgs()
        {
        }
    }

    public sealed class ProxyDefaultTargetGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) representing the target group.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The settings that determine the size and behavior of the connection pool for the target group.
        /// </summary>
        [Input("connectionPoolConfig")]
        public Input<Inputs.ProxyDefaultTargetGroupConnectionPoolConfigGetArgs>? ConnectionPoolConfig { get; set; }

        /// <summary>
        /// Name of the RDS DB Proxy.
        /// </summary>
        [Input("dbProxyName")]
        public Input<string>? DbProxyName { get; set; }

        /// <summary>
        /// The name of the default target group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ProxyDefaultTargetGroupState()
        {
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppMesh.Outputs
{

    [OutputType]
    public sealed class VirtualNodeSpecListenerTimeoutHttp2
    {
        /// <summary>
        /// The idle timeout. An idle timeout bounds the amount of time that a connection may be idle.
        /// </summary>
        public readonly Outputs.VirtualNodeSpecListenerTimeoutHttp2Idle? Idle;
        /// <summary>
        /// The per request timeout.
        /// </summary>
        public readonly Outputs.VirtualNodeSpecListenerTimeoutHttp2PerRequest? PerRequest;

        [OutputConstructor]
        private VirtualNodeSpecListenerTimeoutHttp2(
            Outputs.VirtualNodeSpecListenerTimeoutHttp2Idle? idle,

            Outputs.VirtualNodeSpecListenerTimeoutHttp2PerRequest? perRequest)
        {
            Idle = idle;
            PerRequest = perRequest;
        }
    }
}
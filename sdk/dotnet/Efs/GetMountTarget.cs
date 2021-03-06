// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Efs
{
    public static class GetMountTarget
    {
        /// <summary>
        /// Provides information about an Elastic File System Mount Target (EFS).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var config = new Config();
        ///         var mountTargetId = config.Get("mountTargetId") ?? "";
        ///         var byId = Output.Create(Aws.Efs.GetMountTarget.InvokeAsync(new Aws.Efs.GetMountTargetArgs
        ///         {
        ///             MountTargetId = mountTargetId,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetMountTargetResult> InvokeAsync(GetMountTargetArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetMountTargetResult>("aws:efs/getMountTarget:getMountTarget", args ?? new GetMountTargetArgs(), options.WithVersion());
    }


    public sealed class GetMountTargetArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the mount target that you want to have described
        /// </summary>
        [Input("mountTargetId", required: true)]
        public string MountTargetId { get; set; } = null!;

        public GetMountTargetArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetMountTargetResult
    {
        /// <summary>
        /// The unique and consistent identifier of the Availability Zone (AZ) that the mount target resides in.
        /// </summary>
        public readonly string AvailabilityZoneId;
        /// <summary>
        /// The name of the Availability Zone (AZ) that the mount target resides in.
        /// </summary>
        public readonly string AvailabilityZoneName;
        /// <summary>
        /// The DNS name for the EFS file system.
        /// </summary>
        public readonly string DnsName;
        /// <summary>
        /// Amazon Resource Name of the file system for which the mount target is intended.
        /// </summary>
        public readonly string FileSystemArn;
        /// <summary>
        /// ID of the file system for which the mount target is intended.
        /// </summary>
        public readonly string FileSystemId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Address at which the file system may be mounted via the mount target.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
        /// </summary>
        public readonly string MountTargetDnsName;
        public readonly string MountTargetId;
        /// <summary>
        /// The ID of the network interface that Amazon EFS created when it created the mount target.
        /// </summary>
        public readonly string NetworkInterfaceId;
        /// <summary>
        /// AWS account ID that owns the resource.
        /// </summary>
        public readonly string OwnerId;
        /// <summary>
        /// List of VPC security group IDs attached to the mount target.
        /// </summary>
        public readonly ImmutableArray<string> SecurityGroups;
        /// <summary>
        /// ID of the mount target's subnet.
        /// </summary>
        public readonly string SubnetId;

        [OutputConstructor]
        private GetMountTargetResult(
            string availabilityZoneId,

            string availabilityZoneName,

            string dnsName,

            string fileSystemArn,

            string fileSystemId,

            string id,

            string ipAddress,

            string mountTargetDnsName,

            string mountTargetId,

            string networkInterfaceId,

            string ownerId,

            ImmutableArray<string> securityGroups,

            string subnetId)
        {
            AvailabilityZoneId = availabilityZoneId;
            AvailabilityZoneName = availabilityZoneName;
            DnsName = dnsName;
            FileSystemArn = fileSystemArn;
            FileSystemId = fileSystemId;
            Id = id;
            IpAddress = ipAddress;
            MountTargetDnsName = mountTargetDnsName;
            MountTargetId = mountTargetId;
            NetworkInterfaceId = networkInterfaceId;
            OwnerId = ownerId;
            SecurityGroups = securityGroups;
            SubnetId = subnetId;
        }
    }
}

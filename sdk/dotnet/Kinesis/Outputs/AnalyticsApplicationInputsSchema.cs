// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Kinesis.Outputs
{

    [OutputType]
    public sealed class AnalyticsApplicationInputsSchema
    {
        /// <summary>
        /// The Record Column mapping for the streaming source data element.
        /// See Record Columns below for more details.
        /// </summary>
        public readonly ImmutableArray<Outputs.AnalyticsApplicationInputsSchemaRecordColumn> RecordColumns;
        /// <summary>
        /// The Encoding of the record in the streaming source.
        /// </summary>
        public readonly string? RecordEncoding;
        /// <summary>
        /// The Record Format and mapping information to schematize a record.
        /// See Record Format below for more details.
        /// </summary>
        public readonly Outputs.AnalyticsApplicationInputsSchemaRecordFormat RecordFormat;

        [OutputConstructor]
        private AnalyticsApplicationInputsSchema(
            ImmutableArray<Outputs.AnalyticsApplicationInputsSchemaRecordColumn> recordColumns,

            string? recordEncoding,

            Outputs.AnalyticsApplicationInputsSchemaRecordFormat recordFormat)
        {
            RecordColumns = recordColumns;
            RecordEncoding = recordEncoding;
            RecordFormat = recordFormat;
        }
    }
}
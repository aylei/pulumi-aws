# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Classifier']


class Classifier(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 csv_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierCsvClassifierArgs']]] = None,
                 grok_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierGrokClassifierArgs']]] = None,
                 json_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierJsonClassifierArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 xml_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierXmlClassifierArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Glue Classifier resource.

        > **NOTE:** It is only valid to create one type of classifier (csv, grok, JSON, or XML). Changing classifier types will recreate the classifier.

        ## Example Usage
        ### Csv Classifier

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Classifier("example", csv_classifier=aws.glue.ClassifierCsvClassifierArgs(
            allow_single_column=False,
            contains_header="PRESENT",
            delimiter=",",
            disable_value_trimming=False,
            headers=[
                "example1",
                "example2",
            ],
            quote_symbol="'",
        ))
        ```
        ### Grok Classifier

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Classifier("example", grok_classifier=aws.glue.ClassifierGrokClassifierArgs(
            classification="example",
            grok_pattern="example",
        ))
        ```
        ### JSON Classifier

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Classifier("example", json_classifier=aws.glue.ClassifierJsonClassifierArgs(
            json_path="example",
        ))
        ```
        ### XML Classifier

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Classifier("example", xml_classifier=aws.glue.ClassifierXmlClassifierArgs(
            classification="example",
            row_tag="example",
        ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClassifierCsvClassifierArgs']] csv_classifier: A classifier for Csv content. Defined below.
        :param pulumi.Input[pulumi.InputType['ClassifierGrokClassifierArgs']] grok_classifier: A classifier that uses grok patterns. Defined below.
        :param pulumi.Input[pulumi.InputType['ClassifierJsonClassifierArgs']] json_classifier: A classifier for JSON content. Defined below.
        :param pulumi.Input[str] name: The name of the classifier.
        :param pulumi.Input[pulumi.InputType['ClassifierXmlClassifierArgs']] xml_classifier: A classifier for XML content. Defined below.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['csv_classifier'] = csv_classifier
            __props__['grok_classifier'] = grok_classifier
            __props__['json_classifier'] = json_classifier
            __props__['name'] = name
            __props__['xml_classifier'] = xml_classifier
        super(Classifier, __self__).__init__(
            'aws:glue/classifier:Classifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            csv_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierCsvClassifierArgs']]] = None,
            grok_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierGrokClassifierArgs']]] = None,
            json_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierJsonClassifierArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            xml_classifier: Optional[pulumi.Input[pulumi.InputType['ClassifierXmlClassifierArgs']]] = None) -> 'Classifier':
        """
        Get an existing Classifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClassifierCsvClassifierArgs']] csv_classifier: A classifier for Csv content. Defined below.
        :param pulumi.Input[pulumi.InputType['ClassifierGrokClassifierArgs']] grok_classifier: A classifier that uses grok patterns. Defined below.
        :param pulumi.Input[pulumi.InputType['ClassifierJsonClassifierArgs']] json_classifier: A classifier for JSON content. Defined below.
        :param pulumi.Input[str] name: The name of the classifier.
        :param pulumi.Input[pulumi.InputType['ClassifierXmlClassifierArgs']] xml_classifier: A classifier for XML content. Defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["csv_classifier"] = csv_classifier
        __props__["grok_classifier"] = grok_classifier
        __props__["json_classifier"] = json_classifier
        __props__["name"] = name
        __props__["xml_classifier"] = xml_classifier
        return Classifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierCsvClassifier']]:
        """
        A classifier for Csv content. Defined below.
        """
        return pulumi.get(self, "csv_classifier")

    @property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierGrokClassifier']]:
        """
        A classifier that uses grok patterns. Defined below.
        """
        return pulumi.get(self, "grok_classifier")

    @property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierJsonClassifier']]:
        """
        A classifier for JSON content. Defined below.
        """
        return pulumi.get(self, "json_classifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the classifier.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> pulumi.Output[Optional['outputs.ClassifierXmlClassifier']]:
        """
        A classifier for XML content. Defined below.
        """
        return pulumi.get(self, "xml_classifier")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


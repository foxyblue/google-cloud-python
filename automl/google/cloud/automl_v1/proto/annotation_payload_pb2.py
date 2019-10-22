# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/annotation_payload.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_classification__pb2,
)
from google.cloud.automl_v1.proto import (
    detection_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_detection__pb2,
)
from google.cloud.automl_v1.proto import (
    text_extraction_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_text__extraction__pb2,
)
from google.cloud.automl_v1.proto import (
    text_sentiment_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_text__sentiment__pb2,
)
from google.cloud.automl_v1.proto import (
    translation_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2,
)
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/annotation_payload.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoML\\V1\352\002\031Google::Cloud::AutoML::V1"
    ),
    serialized_pb=_b(
        '\n5google/cloud/automl_v1/proto/annotation_payload.proto\x12\x16google.cloud.automl.v1\x1a\x31google/cloud/automl_v1/proto/classification.proto\x1a,google/cloud/automl_v1/proto/detection.proto\x1a\x32google/cloud/automl_v1/proto/text_extraction.proto\x1a\x31google/cloud/automl_v1/proto/text_sentiment.proto\x1a.google/cloud/automl_v1/proto/translation.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto"\xd3\x03\n\x11\x41nnotationPayload\x12\x44\n\x0btranslation\x18\x02 \x01(\x0b\x32-.google.cloud.automl.v1.TranslationAnnotationH\x00\x12J\n\x0e\x63lassification\x18\x03 \x01(\x0b\x32\x30.google.cloud.automl.v1.ClassificationAnnotationH\x00\x12X\n\x16image_object_detection\x18\x04 \x01(\x0b\x32\x36.google.cloud.automl.v1.ImageObjectDetectionAnnotationH\x00\x12K\n\x0ftext_extraction\x18\x06 \x01(\x0b\x32\x30.google.cloud.automl.v1.TextExtractionAnnotationH\x00\x12I\n\x0etext_sentiment\x18\x07 \x01(\x0b\x32/.google.cloud.automl.v1.TextSentimentAnnotationH\x00\x12\x1a\n\x12\x61nnotation_spec_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\tB\x08\n\x06\x64\x65tailB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoML\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_detection__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_text__extraction__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_text__sentiment__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_ANNOTATIONPAYLOAD = _descriptor.Descriptor(
    name="AnnotationPayload",
    full_name="google.cloud.automl.v1.AnnotationPayload",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="translation",
            full_name="google.cloud.automl.v1.AnnotationPayload.translation",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="classification",
            full_name="google.cloud.automl.v1.AnnotationPayload.classification",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="image_object_detection",
            full_name="google.cloud.automl.v1.AnnotationPayload.image_object_detection",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text_extraction",
            full_name="google.cloud.automl.v1.AnnotationPayload.text_extraction",
            index=3,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text_sentiment",
            full_name="google.cloud.automl.v1.AnnotationPayload.text_sentiment",
            index=4,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1.AnnotationPayload.annotation_spec_id",
            index=5,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.automl.v1.AnnotationPayload.display_name",
            index=6,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="detail",
            full_name="google.cloud.automl.v1.AnnotationPayload.detail",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=387,
    serialized_end=854,
)

_ANNOTATIONPAYLOAD.fields_by_name[
    "translation"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_translation__pb2._TRANSLATIONANNOTATION
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "classification"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_classification__pb2._CLASSIFICATIONANNOTATION
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "image_object_detection"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_detection__pb2._IMAGEOBJECTDETECTIONANNOTATION
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "text_extraction"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_text__extraction__pb2._TEXTEXTRACTIONANNOTATION
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "text_sentiment"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_text__sentiment__pb2._TEXTSENTIMENTANNOTATION
)
_ANNOTATIONPAYLOAD.oneofs_by_name["detail"].fields.append(
    _ANNOTATIONPAYLOAD.fields_by_name["translation"]
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "translation"
].containing_oneof = _ANNOTATIONPAYLOAD.oneofs_by_name["detail"]
_ANNOTATIONPAYLOAD.oneofs_by_name["detail"].fields.append(
    _ANNOTATIONPAYLOAD.fields_by_name["classification"]
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "classification"
].containing_oneof = _ANNOTATIONPAYLOAD.oneofs_by_name["detail"]
_ANNOTATIONPAYLOAD.oneofs_by_name["detail"].fields.append(
    _ANNOTATIONPAYLOAD.fields_by_name["image_object_detection"]
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "image_object_detection"
].containing_oneof = _ANNOTATIONPAYLOAD.oneofs_by_name["detail"]
_ANNOTATIONPAYLOAD.oneofs_by_name["detail"].fields.append(
    _ANNOTATIONPAYLOAD.fields_by_name["text_extraction"]
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "text_extraction"
].containing_oneof = _ANNOTATIONPAYLOAD.oneofs_by_name["detail"]
_ANNOTATIONPAYLOAD.oneofs_by_name["detail"].fields.append(
    _ANNOTATIONPAYLOAD.fields_by_name["text_sentiment"]
)
_ANNOTATIONPAYLOAD.fields_by_name[
    "text_sentiment"
].containing_oneof = _ANNOTATIONPAYLOAD.oneofs_by_name["detail"]
DESCRIPTOR.message_types_by_name["AnnotationPayload"] = _ANNOTATIONPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnnotationPayload = _reflection.GeneratedProtocolMessageType(
    "AnnotationPayload",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANNOTATIONPAYLOAD,
        __module__="google.cloud.automl_v1.proto.annotation_payload_pb2",
        __doc__="""Contains annotation information that is relevant to AutoML.
  
  
  Attributes:
      detail:
          Output only . Additional information about the annotation
          specific to the AutoML domain.
      translation:
          Annotation details for translation.
      classification:
          Annotation details for content or image classification.
      image_object_detection:
          Annotation details for image object detection.
      text_extraction:
          Annotation details for text extraction.
      text_sentiment:
          Annotation details for text sentiment.
      annotation_spec_id:
          Output only . The resource ID of the annotation spec that this
          annotation pertains to. The annotation spec comes from either
          an ancestor dataset, or the dataset that was used to train the
          model in use.
      display_name:
          Output only. The value of [display\_name][google.cloud.automl.
          v1p1beta.AnnotationSpec.display\_name] when the model was
          trained. Because this field returns a value at model training
          time, for different models trained using the same dataset, the
          returned value could be different as model owner could update
          the ``display_name`` between any two model training.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.AnnotationPayload)
    ),
)
_sym_db.RegisterMessage(AnnotationPayload)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

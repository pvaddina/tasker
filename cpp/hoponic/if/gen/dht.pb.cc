// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: dht.proto

#include "dht.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// This is a temporary google only hack
#ifdef GOOGLE_PROTOBUF_ENFORCE_UNIQUENESS
#include "third_party/protobuf/version.h"
#endif
// @@protoc_insertion_point(includes)

namespace protobuf_base_2eproto {
extern PROTOBUF_INTERNAL_EXPORT_protobuf_base_2eproto ::google::protobuf::internal::SCCInfo<0> scc_info_CHwInitReq;
}  // namespace protobuf_base_2eproto
namespace Dht {
class CDhtInitReqDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<CDhtInitReq>
      _instance;
} _CDhtInitReq_default_instance_;
}  // namespace Dht
namespace protobuf_dht_2eproto {
static void InitDefaultsCDhtInitReq() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::Dht::_CDhtInitReq_default_instance_;
    new (ptr) ::Dht::CDhtInitReq();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::Dht::CDhtInitReq::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<1> scc_info_CDhtInitReq =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 1, InitDefaultsCDhtInitReq}, {
      &protobuf_base_2eproto::scc_info_CHwInitReq.base,}};

void InitDefaults() {
  ::google::protobuf::internal::InitSCC(&scc_info_CDhtInitReq.base);
}

::google::protobuf::Metadata file_level_metadata[1];
const ::google::protobuf::EnumDescriptor* file_level_enum_descriptors[1];

const ::google::protobuf::uint32 TableStruct::offsets[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::Dht::CDhtInitReq, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::Dht::CDhtInitReq, base_init_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::Dht::CDhtInitReq, mtype_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::Dht::CDhtInitReq)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::Dht::_CDhtInitReq_default_instance_),
};

void protobuf_AssignDescriptors() {
  AddDescriptors();
  AssignDescriptors(
      "dht.proto", schemas, file_default_instances, TableStruct::offsets,
      file_level_metadata, file_level_enum_descriptors, NULL);
}

void protobuf_AssignDescriptorsOnce() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, protobuf_AssignDescriptors);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_PROTOBUF_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::internal::RegisterAllTypes(file_level_metadata, 1);
}

void AddDescriptorsImpl() {
  InitDefaults();
  static const char descriptor[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
      "\n\tdht.proto\022\003Dht\032\nbase.proto\"P\n\013CDhtInit"
      "Req\022#\n\tbase_init\030\001 \001(\0132\020.Base.CHwInitReq"
      "\022\034\n\005mType\030\002 \001(\0162\r.Dht.MeasType*G\n\010MeasTy"
      "pe\022\017\n\013TEMPERATURE\020\000\022\014\n\010HUMIDITY\020\001\022\034\n\030TEM"
      "PERATURE_AND_HUMIDITY\020\002b\006proto3"
  };
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
      descriptor, 191);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "dht.proto", &protobuf_RegisterTypes);
  ::protobuf_base_2eproto::AddDescriptors();
}

void AddDescriptors() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, AddDescriptorsImpl);
}
// Force AddDescriptors() to be called at dynamic initialization time.
struct StaticDescriptorInitializer {
  StaticDescriptorInitializer() {
    AddDescriptors();
  }
} static_descriptor_initializer;
}  // namespace protobuf_dht_2eproto
namespace Dht {
const ::google::protobuf::EnumDescriptor* MeasType_descriptor() {
  protobuf_dht_2eproto::protobuf_AssignDescriptorsOnce();
  return protobuf_dht_2eproto::file_level_enum_descriptors[0];
}
bool MeasType_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
    case 2:
      return true;
    default:
      return false;
  }
}


// ===================================================================

void CDhtInitReq::InitAsDefaultInstance() {
  ::Dht::_CDhtInitReq_default_instance_._instance.get_mutable()->base_init_ = const_cast< ::Base::CHwInitReq*>(
      ::Base::CHwInitReq::internal_default_instance());
}
void CDhtInitReq::clear_base_init() {
  if (GetArenaNoVirtual() == NULL && base_init_ != NULL) {
    delete base_init_;
  }
  base_init_ = NULL;
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int CDhtInitReq::kBaseInitFieldNumber;
const int CDhtInitReq::kMTypeFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

CDhtInitReq::CDhtInitReq()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  ::google::protobuf::internal::InitSCC(
      &protobuf_dht_2eproto::scc_info_CDhtInitReq.base);
  SharedCtor();
  // @@protoc_insertion_point(constructor:Dht.CDhtInitReq)
}
CDhtInitReq::CDhtInitReq(const CDhtInitReq& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(NULL) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  if (from.has_base_init()) {
    base_init_ = new ::Base::CHwInitReq(*from.base_init_);
  } else {
    base_init_ = NULL;
  }
  mtype_ = from.mtype_;
  // @@protoc_insertion_point(copy_constructor:Dht.CDhtInitReq)
}

void CDhtInitReq::SharedCtor() {
  ::memset(&base_init_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&mtype_) -
      reinterpret_cast<char*>(&base_init_)) + sizeof(mtype_));
}

CDhtInitReq::~CDhtInitReq() {
  // @@protoc_insertion_point(destructor:Dht.CDhtInitReq)
  SharedDtor();
}

void CDhtInitReq::SharedDtor() {
  if (this != internal_default_instance()) delete base_init_;
}

void CDhtInitReq::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ::google::protobuf::Descriptor* CDhtInitReq::descriptor() {
  ::protobuf_dht_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_dht_2eproto::file_level_metadata[kIndexInFileMessages].descriptor;
}

const CDhtInitReq& CDhtInitReq::default_instance() {
  ::google::protobuf::internal::InitSCC(&protobuf_dht_2eproto::scc_info_CDhtInitReq.base);
  return *internal_default_instance();
}


void CDhtInitReq::Clear() {
// @@protoc_insertion_point(message_clear_start:Dht.CDhtInitReq)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  if (GetArenaNoVirtual() == NULL && base_init_ != NULL) {
    delete base_init_;
  }
  base_init_ = NULL;
  mtype_ = 0;
  _internal_metadata_.Clear();
}

bool CDhtInitReq::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:Dht.CDhtInitReq)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // .Base.CHwInitReq base_init = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(10u /* 10 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessage(
               input, mutable_base_init()));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // .Dht.MeasType mType = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(16u /* 16 & 0xFF */)) {
          int value;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          set_mtype(static_cast< ::Dht::MeasType >(value));
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:Dht.CDhtInitReq)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:Dht.CDhtInitReq)
  return false;
#undef DO_
}

void CDhtInitReq::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:Dht.CDhtInitReq)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .Base.CHwInitReq base_init = 1;
  if (this->has_base_init()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, this->_internal_base_init(), output);
  }

  // .Dht.MeasType mType = 2;
  if (this->mtype() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      2, this->mtype(), output);
  }

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()), output);
  }
  // @@protoc_insertion_point(serialize_end:Dht.CDhtInitReq)
}

::google::protobuf::uint8* CDhtInitReq::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  (void)deterministic; // Unused
  // @@protoc_insertion_point(serialize_to_array_start:Dht.CDhtInitReq)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .Base.CHwInitReq base_init = 1;
  if (this->has_base_init()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageToArray(
        1, this->_internal_base_init(), deterministic, target);
  }

  // .Dht.MeasType mType = 2;
  if (this->mtype() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      2, this->mtype(), target);
  }

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:Dht.CDhtInitReq)
  return target;
}

size_t CDhtInitReq::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:Dht.CDhtInitReq)
  size_t total_size = 0;

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()));
  }
  // .Base.CHwInitReq base_init = 1;
  if (this->has_base_init()) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *base_init_);
  }

  // .Dht.MeasType mType = 2;
  if (this->mtype() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::EnumSize(this->mtype());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void CDhtInitReq::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:Dht.CDhtInitReq)
  GOOGLE_DCHECK_NE(&from, this);
  const CDhtInitReq* source =
      ::google::protobuf::internal::DynamicCastToGenerated<const CDhtInitReq>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:Dht.CDhtInitReq)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:Dht.CDhtInitReq)
    MergeFrom(*source);
  }
}

void CDhtInitReq::MergeFrom(const CDhtInitReq& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:Dht.CDhtInitReq)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.has_base_init()) {
    mutable_base_init()->::Base::CHwInitReq::MergeFrom(from.base_init());
  }
  if (from.mtype() != 0) {
    set_mtype(from.mtype());
  }
}

void CDhtInitReq::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:Dht.CDhtInitReq)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void CDhtInitReq::CopyFrom(const CDhtInitReq& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:Dht.CDhtInitReq)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool CDhtInitReq::IsInitialized() const {
  return true;
}

void CDhtInitReq::Swap(CDhtInitReq* other) {
  if (other == this) return;
  InternalSwap(other);
}
void CDhtInitReq::InternalSwap(CDhtInitReq* other) {
  using std::swap;
  swap(base_init_, other->base_init_);
  swap(mtype_, other->mtype_);
  _internal_metadata_.Swap(&other->_internal_metadata_);
}

::google::protobuf::Metadata CDhtInitReq::GetMetadata() const {
  protobuf_dht_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_dht_2eproto::file_level_metadata[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace Dht
namespace google {
namespace protobuf {
template<> GOOGLE_PROTOBUF_ATTRIBUTE_NOINLINE ::Dht::CDhtInitReq* Arena::CreateMaybeMessage< ::Dht::CDhtInitReq >(Arena* arena) {
  return Arena::CreateInternal< ::Dht::CDhtInitReq >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)

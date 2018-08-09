// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: base.proto

#ifndef PROTOBUF_INCLUDED_base_2eproto
#define PROTOBUF_INCLUDED_base_2eproto

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3005001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#define PROTOBUF_INTERNAL_EXPORT_protobuf_base_2eproto 

namespace protobuf_base_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[4];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
}  // namespace protobuf_base_2eproto
namespace Base {
class CHwInitCnf;
class CHwInitCnfDefaultTypeInternal;
extern CHwInitCnfDefaultTypeInternal _CHwInitCnf_default_instance_;
class CHwInitReq;
class CHwInitReqDefaultTypeInternal;
extern CHwInitReqDefaultTypeInternal _CHwInitReq_default_instance_;
class CHwShutdownCnf;
class CHwShutdownCnfDefaultTypeInternal;
extern CHwShutdownCnfDefaultTypeInternal _CHwShutdownCnf_default_instance_;
class CHwShutdownReq;
class CHwShutdownReqDefaultTypeInternal;
extern CHwShutdownReqDefaultTypeInternal _CHwShutdownReq_default_instance_;
}  // namespace Base
namespace google {
namespace protobuf {
template<> ::Base::CHwInitCnf* Arena::CreateMaybeMessage<::Base::CHwInitCnf>(Arena*);
template<> ::Base::CHwInitReq* Arena::CreateMaybeMessage<::Base::CHwInitReq>(Arena*);
template<> ::Base::CHwShutdownCnf* Arena::CreateMaybeMessage<::Base::CHwShutdownCnf>(Arena*);
template<> ::Base::CHwShutdownReq* Arena::CreateMaybeMessage<::Base::CHwShutdownReq>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace Base {

enum PowerState {
  INVALID = 0,
  ON = 1,
  OFF = 2,
  PowerState_INT_MIN_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32min,
  PowerState_INT_MAX_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32max
};
bool PowerState_IsValid(int value);
const PowerState PowerState_MIN = INVALID;
const PowerState PowerState_MAX = OFF;
const int PowerState_ARRAYSIZE = PowerState_MAX + 1;

const ::google::protobuf::EnumDescriptor* PowerState_descriptor();
inline const ::std::string& PowerState_Name(PowerState value) {
  return ::google::protobuf::internal::NameOfEnum(
    PowerState_descriptor(), value);
}
inline bool PowerState_Parse(
    const ::std::string& name, PowerState* value) {
  return ::google::protobuf::internal::ParseNamedEnum<PowerState>(
    PowerState_descriptor(), name, value);
}
enum Result {
  INVALID_RESULT = 0,
  SUCCESS = 1,
  FAILURE = 2,
  Result_INT_MIN_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32min,
  Result_INT_MAX_SENTINEL_DO_NOT_USE_ = ::google::protobuf::kint32max
};
bool Result_IsValid(int value);
const Result Result_MIN = INVALID_RESULT;
const Result Result_MAX = FAILURE;
const int Result_ARRAYSIZE = Result_MAX + 1;

const ::google::protobuf::EnumDescriptor* Result_descriptor();
inline const ::std::string& Result_Name(Result value) {
  return ::google::protobuf::internal::NameOfEnum(
    Result_descriptor(), value);
}
inline bool Result_Parse(
    const ::std::string& name, Result* value) {
  return ::google::protobuf::internal::ParseNamedEnum<Result>(
    Result_descriptor(), name, value);
}
// ===================================================================

class CHwInitReq : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Base.CHwInitReq) */ {
 public:
  CHwInitReq();
  virtual ~CHwInitReq();

  CHwInitReq(const CHwInitReq& from);

  inline CHwInitReq& operator=(const CHwInitReq& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  CHwInitReq(CHwInitReq&& from) noexcept
    : CHwInitReq() {
    *this = ::std::move(from);
  }

  inline CHwInitReq& operator=(CHwInitReq&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const CHwInitReq& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const CHwInitReq* internal_default_instance() {
    return reinterpret_cast<const CHwInitReq*>(
               &_CHwInitReq_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(CHwInitReq* other);
  friend void swap(CHwInitReq& a, CHwInitReq& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline CHwInitReq* New() const final {
    return CreateMaybeMessage<CHwInitReq>(NULL);
  }

  CHwInitReq* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<CHwInitReq>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const CHwInitReq& from);
  void MergeFrom(const CHwInitReq& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(CHwInitReq* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // .Base.PowerState powerState = 1;
  void clear_powerstate();
  static const int kPowerStateFieldNumber = 1;
  ::Base::PowerState powerstate() const;
  void set_powerstate(::Base::PowerState value);

  // @@protoc_insertion_point(class_scope:Base.CHwInitReq)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  int powerstate_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_base_2eproto::TableStruct;
};
// -------------------------------------------------------------------

class CHwInitCnf : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Base.CHwInitCnf) */ {
 public:
  CHwInitCnf();
  virtual ~CHwInitCnf();

  CHwInitCnf(const CHwInitCnf& from);

  inline CHwInitCnf& operator=(const CHwInitCnf& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  CHwInitCnf(CHwInitCnf&& from) noexcept
    : CHwInitCnf() {
    *this = ::std::move(from);
  }

  inline CHwInitCnf& operator=(CHwInitCnf&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const CHwInitCnf& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const CHwInitCnf* internal_default_instance() {
    return reinterpret_cast<const CHwInitCnf*>(
               &_CHwInitCnf_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  void Swap(CHwInitCnf* other);
  friend void swap(CHwInitCnf& a, CHwInitCnf& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline CHwInitCnf* New() const final {
    return CreateMaybeMessage<CHwInitCnf>(NULL);
  }

  CHwInitCnf* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<CHwInitCnf>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const CHwInitCnf& from);
  void MergeFrom(const CHwInitCnf& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(CHwInitCnf* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // .Base.Result result = 1;
  void clear_result();
  static const int kResultFieldNumber = 1;
  ::Base::Result result() const;
  void set_result(::Base::Result value);

  // @@protoc_insertion_point(class_scope:Base.CHwInitCnf)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  int result_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_base_2eproto::TableStruct;
};
// -------------------------------------------------------------------

class CHwShutdownReq : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Base.CHwShutdownReq) */ {
 public:
  CHwShutdownReq();
  virtual ~CHwShutdownReq();

  CHwShutdownReq(const CHwShutdownReq& from);

  inline CHwShutdownReq& operator=(const CHwShutdownReq& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  CHwShutdownReq(CHwShutdownReq&& from) noexcept
    : CHwShutdownReq() {
    *this = ::std::move(from);
  }

  inline CHwShutdownReq& operator=(CHwShutdownReq&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const CHwShutdownReq& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const CHwShutdownReq* internal_default_instance() {
    return reinterpret_cast<const CHwShutdownReq*>(
               &_CHwShutdownReq_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    2;

  void Swap(CHwShutdownReq* other);
  friend void swap(CHwShutdownReq& a, CHwShutdownReq& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline CHwShutdownReq* New() const final {
    return CreateMaybeMessage<CHwShutdownReq>(NULL);
  }

  CHwShutdownReq* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<CHwShutdownReq>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const CHwShutdownReq& from);
  void MergeFrom(const CHwShutdownReq& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(CHwShutdownReq* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // @@protoc_insertion_point(class_scope:Base.CHwShutdownReq)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_base_2eproto::TableStruct;
};
// -------------------------------------------------------------------

class CHwShutdownCnf : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Base.CHwShutdownCnf) */ {
 public:
  CHwShutdownCnf();
  virtual ~CHwShutdownCnf();

  CHwShutdownCnf(const CHwShutdownCnf& from);

  inline CHwShutdownCnf& operator=(const CHwShutdownCnf& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  CHwShutdownCnf(CHwShutdownCnf&& from) noexcept
    : CHwShutdownCnf() {
    *this = ::std::move(from);
  }

  inline CHwShutdownCnf& operator=(CHwShutdownCnf&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const CHwShutdownCnf& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const CHwShutdownCnf* internal_default_instance() {
    return reinterpret_cast<const CHwShutdownCnf*>(
               &_CHwShutdownCnf_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    3;

  void Swap(CHwShutdownCnf* other);
  friend void swap(CHwShutdownCnf& a, CHwShutdownCnf& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline CHwShutdownCnf* New() const final {
    return CreateMaybeMessage<CHwShutdownCnf>(NULL);
  }

  CHwShutdownCnf* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<CHwShutdownCnf>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const CHwShutdownCnf& from);
  void MergeFrom(const CHwShutdownCnf& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(CHwShutdownCnf* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // .Base.Result result = 1;
  void clear_result();
  static const int kResultFieldNumber = 1;
  ::Base::Result result() const;
  void set_result(::Base::Result value);

  // @@protoc_insertion_point(class_scope:Base.CHwShutdownCnf)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  int result_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_base_2eproto::TableStruct;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// CHwInitReq

// .Base.PowerState powerState = 1;
inline void CHwInitReq::clear_powerstate() {
  powerstate_ = 0;
}
inline ::Base::PowerState CHwInitReq::powerstate() const {
  // @@protoc_insertion_point(field_get:Base.CHwInitReq.powerState)
  return static_cast< ::Base::PowerState >(powerstate_);
}
inline void CHwInitReq::set_powerstate(::Base::PowerState value) {
  
  powerstate_ = value;
  // @@protoc_insertion_point(field_set:Base.CHwInitReq.powerState)
}

// -------------------------------------------------------------------

// CHwInitCnf

// .Base.Result result = 1;
inline void CHwInitCnf::clear_result() {
  result_ = 0;
}
inline ::Base::Result CHwInitCnf::result() const {
  // @@protoc_insertion_point(field_get:Base.CHwInitCnf.result)
  return static_cast< ::Base::Result >(result_);
}
inline void CHwInitCnf::set_result(::Base::Result value) {
  
  result_ = value;
  // @@protoc_insertion_point(field_set:Base.CHwInitCnf.result)
}

// -------------------------------------------------------------------

// CHwShutdownReq

// -------------------------------------------------------------------

// CHwShutdownCnf

// .Base.Result result = 1;
inline void CHwShutdownCnf::clear_result() {
  result_ = 0;
}
inline ::Base::Result CHwShutdownCnf::result() const {
  // @@protoc_insertion_point(field_get:Base.CHwShutdownCnf.result)
  return static_cast< ::Base::Result >(result_);
}
inline void CHwShutdownCnf::set_result(::Base::Result value) {
  
  result_ = value;
  // @@protoc_insertion_point(field_set:Base.CHwShutdownCnf.result)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------

// -------------------------------------------------------------------

// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace Base

namespace google {
namespace protobuf {

template <> struct is_proto_enum< ::Base::PowerState> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::Base::PowerState>() {
  return ::Base::PowerState_descriptor();
}
template <> struct is_proto_enum< ::Base::Result> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::Base::Result>() {
  return ::Base::Result_descriptor();
}

}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_INCLUDED_base_2eproto
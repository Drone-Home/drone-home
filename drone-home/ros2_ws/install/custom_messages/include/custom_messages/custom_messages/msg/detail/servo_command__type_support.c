// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from custom_messages:msg/ServoCommand.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "custom_messages/msg/detail/servo_command__rosidl_typesupport_introspection_c.h"
#include "custom_messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "custom_messages/msg/detail/servo_command__functions.h"
#include "custom_messages/msg/detail/servo_command__struct.h"


// Include directives for member types
// Member `servo_ids`
// Member `positions`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  custom_messages__msg__ServoCommand__init(message_memory);
}

void custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_fini_function(void * message_memory)
{
  custom_messages__msg__ServoCommand__fini(message_memory);
}

size_t custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__size_function__ServoCommand__servo_ids(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_const_function__ServoCommand__servo_ids(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_function__ServoCommand__servo_ids(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__fetch_function__ServoCommand__servo_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_const_function__ServoCommand__servo_ids(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__assign_function__ServoCommand__servo_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_function__ServoCommand__servo_ids(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__resize_function__ServoCommand__servo_ids(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__size_function__ServoCommand__positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_const_function__ServoCommand__positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_function__ServoCommand__positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__fetch_function__ServoCommand__positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_const_function__ServoCommand__positions(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__assign_function__ServoCommand__positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_function__ServoCommand__positions(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__resize_function__ServoCommand__positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_member_array[2] = {
  {
    "servo_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_messages__msg__ServoCommand, servo_ids),  // bytes offset in struct
    NULL,  // default value
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__size_function__ServoCommand__servo_ids,  // size() function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_const_function__ServoCommand__servo_ids,  // get_const(index) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_function__ServoCommand__servo_ids,  // get(index) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__fetch_function__ServoCommand__servo_ids,  // fetch(index, &value) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__assign_function__ServoCommand__servo_ids,  // assign(index, value) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__resize_function__ServoCommand__servo_ids  // resize(index) function pointer
  },
  {
    "positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_messages__msg__ServoCommand, positions),  // bytes offset in struct
    NULL,  // default value
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__size_function__ServoCommand__positions,  // size() function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_const_function__ServoCommand__positions,  // get_const(index) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__get_function__ServoCommand__positions,  // get(index) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__fetch_function__ServoCommand__positions,  // fetch(index, &value) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__assign_function__ServoCommand__positions,  // assign(index, value) function pointer
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__resize_function__ServoCommand__positions  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_members = {
  "custom_messages__msg",  // message namespace
  "ServoCommand",  // message name
  2,  // number of fields
  sizeof(custom_messages__msg__ServoCommand),
  custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_member_array,  // message members
  custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_init_function,  // function to initialize message memory (memory has to be allocated)
  custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_type_support_handle = {
  0,
  &custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_custom_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, custom_messages, msg, ServoCommand)() {
  if (!custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_type_support_handle.typesupport_identifier) {
    custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &custom_messages__msg__ServoCommand__rosidl_typesupport_introspection_c__ServoCommand_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_messages:msg/ServoCommand.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__STRUCT_H_
#define CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'servo_ids'
// Member 'positions'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/ServoCommand in the package custom_messages.
/**
  * List of servo IDs
 */
typedef struct custom_messages__msg__ServoCommand
{
  rosidl_runtime_c__int32__Sequence servo_ids;
  /// List of corresponding positions
  rosidl_runtime_c__float__Sequence positions;
} custom_messages__msg__ServoCommand;

// Struct for a sequence of custom_messages__msg__ServoCommand.
typedef struct custom_messages__msg__ServoCommand__Sequence
{
  custom_messages__msg__ServoCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__msg__ServoCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__STRUCT_H_

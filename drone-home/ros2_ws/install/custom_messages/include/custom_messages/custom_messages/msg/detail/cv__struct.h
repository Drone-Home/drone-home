// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_messages:msg/CV.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__CV__STRUCT_H_
#define CUSTOM_MESSAGES__MSG__DETAIL__CV__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/CV in the package custom_messages.
typedef struct custom_messages__msg__CV
{
  float x_pos;
  float y_pos;
  float x_size;
  float y_size;
  int64_t image_number;
} custom_messages__msg__CV;

// Struct for a sequence of custom_messages__msg__CV.
typedef struct custom_messages__msg__CV__Sequence
{
  custom_messages__msg__CV * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__msg__CV__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__CV__STRUCT_H_

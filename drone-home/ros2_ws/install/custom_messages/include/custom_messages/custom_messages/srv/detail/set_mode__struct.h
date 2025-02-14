// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_messages:srv/SetMode.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__SRV__DETAIL__SET_MODE__STRUCT_H_
#define CUSTOM_MESSAGES__SRV__DETAIL__SET_MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'mode'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SetMode in the package custom_messages.
typedef struct custom_messages__srv__SetMode_Request
{
  /// Set mode. "automatic" or "manual"
  rosidl_runtime_c__String mode;
} custom_messages__srv__SetMode_Request;

// Struct for a sequence of custom_messages__srv__SetMode_Request.
typedef struct custom_messages__srv__SetMode_Request__Sequence
{
  custom_messages__srv__SetMode_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__srv__SetMode_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetMode in the package custom_messages.
typedef struct custom_messages__srv__SetMode_Response
{
  /// indicate successful trigger
  bool success;
} custom_messages__srv__SetMode_Response;

// Struct for a sequence of custom_messages__srv__SetMode_Response.
typedef struct custom_messages__srv__SetMode_Response__Sequence
{
  custom_messages__srv__SetMode_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__srv__SetMode_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MESSAGES__SRV__DETAIL__SET_MODE__STRUCT_H_

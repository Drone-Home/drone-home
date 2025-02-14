// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_messages:srv/SetCoordinate.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__SRV__DETAIL__SET_COORDINATE__STRUCT_H_
#define CUSTOM_MESSAGES__SRV__DETAIL__SET_COORDINATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'new_coordinate'
#include "sensor_msgs/msg/detail/nav_sat_fix__struct.h"

/// Struct defined in srv/SetCoordinate in the package custom_messages.
typedef struct custom_messages__srv__SetCoordinate_Request
{
  /// coordinate read from NavSatFix and set
  sensor_msgs__msg__NavSatFix new_coordinate;
} custom_messages__srv__SetCoordinate_Request;

// Struct for a sequence of custom_messages__srv__SetCoordinate_Request.
typedef struct custom_messages__srv__SetCoordinate_Request__Sequence
{
  custom_messages__srv__SetCoordinate_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__srv__SetCoordinate_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetCoordinate in the package custom_messages.
typedef struct custom_messages__srv__SetCoordinate_Response
{
  /// indicate successful trigger
  bool success;
} custom_messages__srv__SetCoordinate_Response;

// Struct for a sequence of custom_messages__srv__SetCoordinate_Response.
typedef struct custom_messages__srv__SetCoordinate_Response__Sequence
{
  custom_messages__srv__SetCoordinate_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_messages__srv__SetCoordinate_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MESSAGES__SRV__DETAIL__SET_COORDINATE__STRUCT_H_

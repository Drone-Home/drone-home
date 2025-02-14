// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_messages:msg/ServoCommand.idl
// generated code does not contain a copyright notice
#include "custom_messages/msg/detail/servo_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `servo_ids`
// Member `positions`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
custom_messages__msg__ServoCommand__init(custom_messages__msg__ServoCommand * msg)
{
  if (!msg) {
    return false;
  }
  // servo_ids
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->servo_ids, 0)) {
    custom_messages__msg__ServoCommand__fini(msg);
    return false;
  }
  // positions
  if (!rosidl_runtime_c__float__Sequence__init(&msg->positions, 0)) {
    custom_messages__msg__ServoCommand__fini(msg);
    return false;
  }
  return true;
}

void
custom_messages__msg__ServoCommand__fini(custom_messages__msg__ServoCommand * msg)
{
  if (!msg) {
    return;
  }
  // servo_ids
  rosidl_runtime_c__int32__Sequence__fini(&msg->servo_ids);
  // positions
  rosidl_runtime_c__float__Sequence__fini(&msg->positions);
}

bool
custom_messages__msg__ServoCommand__are_equal(const custom_messages__msg__ServoCommand * lhs, const custom_messages__msg__ServoCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // servo_ids
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->servo_ids), &(rhs->servo_ids)))
  {
    return false;
  }
  // positions
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->positions), &(rhs->positions)))
  {
    return false;
  }
  return true;
}

bool
custom_messages__msg__ServoCommand__copy(
  const custom_messages__msg__ServoCommand * input,
  custom_messages__msg__ServoCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // servo_ids
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->servo_ids), &(output->servo_ids)))
  {
    return false;
  }
  // positions
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->positions), &(output->positions)))
  {
    return false;
  }
  return true;
}

custom_messages__msg__ServoCommand *
custom_messages__msg__ServoCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_messages__msg__ServoCommand * msg = (custom_messages__msg__ServoCommand *)allocator.allocate(sizeof(custom_messages__msg__ServoCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_messages__msg__ServoCommand));
  bool success = custom_messages__msg__ServoCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_messages__msg__ServoCommand__destroy(custom_messages__msg__ServoCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_messages__msg__ServoCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_messages__msg__ServoCommand__Sequence__init(custom_messages__msg__ServoCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_messages__msg__ServoCommand * data = NULL;

  if (size) {
    data = (custom_messages__msg__ServoCommand *)allocator.zero_allocate(size, sizeof(custom_messages__msg__ServoCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_messages__msg__ServoCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_messages__msg__ServoCommand__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_messages__msg__ServoCommand__Sequence__fini(custom_messages__msg__ServoCommand__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_messages__msg__ServoCommand__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_messages__msg__ServoCommand__Sequence *
custom_messages__msg__ServoCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_messages__msg__ServoCommand__Sequence * array = (custom_messages__msg__ServoCommand__Sequence *)allocator.allocate(sizeof(custom_messages__msg__ServoCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_messages__msg__ServoCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_messages__msg__ServoCommand__Sequence__destroy(custom_messages__msg__ServoCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_messages__msg__ServoCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_messages__msg__ServoCommand__Sequence__are_equal(const custom_messages__msg__ServoCommand__Sequence * lhs, const custom_messages__msg__ServoCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_messages__msg__ServoCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_messages__msg__ServoCommand__Sequence__copy(
  const custom_messages__msg__ServoCommand__Sequence * input,
  custom_messages__msg__ServoCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_messages__msg__ServoCommand);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_messages__msg__ServoCommand * data =
      (custom_messages__msg__ServoCommand *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_messages__msg__ServoCommand__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_messages__msg__ServoCommand__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_messages__msg__ServoCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

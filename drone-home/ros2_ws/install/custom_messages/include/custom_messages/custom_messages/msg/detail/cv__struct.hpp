// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_messages:msg/CV.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__CV__STRUCT_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__CV__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__custom_messages__msg__CV __attribute__((deprecated))
#else
# define DEPRECATED__custom_messages__msg__CV __declspec(deprecated)
#endif

namespace custom_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CV_
{
  using Type = CV_<ContainerAllocator>;

  explicit CV_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_pos = 0.0f;
      this->y_pos = 0.0f;
      this->x_size = 0.0f;
      this->y_size = 0.0f;
      this->image_number = 0ll;
    }
  }

  explicit CV_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_pos = 0.0f;
      this->y_pos = 0.0f;
      this->x_size = 0.0f;
      this->y_size = 0.0f;
      this->image_number = 0ll;
    }
  }

  // field types and members
  using _x_pos_type =
    float;
  _x_pos_type x_pos;
  using _y_pos_type =
    float;
  _y_pos_type y_pos;
  using _x_size_type =
    float;
  _x_size_type x_size;
  using _y_size_type =
    float;
  _y_size_type y_size;
  using _image_number_type =
    int64_t;
  _image_number_type image_number;

  // setters for named parameter idiom
  Type & set__x_pos(
    const float & _arg)
  {
    this->x_pos = _arg;
    return *this;
  }
  Type & set__y_pos(
    const float & _arg)
  {
    this->y_pos = _arg;
    return *this;
  }
  Type & set__x_size(
    const float & _arg)
  {
    this->x_size = _arg;
    return *this;
  }
  Type & set__y_size(
    const float & _arg)
  {
    this->y_size = _arg;
    return *this;
  }
  Type & set__image_number(
    const int64_t & _arg)
  {
    this->image_number = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_messages::msg::CV_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_messages::msg::CV_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_messages::msg::CV_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_messages::msg::CV_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_messages::msg::CV_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_messages::msg::CV_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_messages::msg::CV_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_messages::msg::CV_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_messages::msg::CV_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_messages::msg::CV_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_messages__msg__CV
    std::shared_ptr<custom_messages::msg::CV_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_messages__msg__CV
    std::shared_ptr<custom_messages::msg::CV_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CV_ & other) const
  {
    if (this->x_pos != other.x_pos) {
      return false;
    }
    if (this->y_pos != other.y_pos) {
      return false;
    }
    if (this->x_size != other.x_size) {
      return false;
    }
    if (this->y_size != other.y_size) {
      return false;
    }
    if (this->image_number != other.image_number) {
      return false;
    }
    return true;
  }
  bool operator!=(const CV_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CV_

// alias to use template instance with default allocator
using CV =
  custom_messages::msg::CV_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__CV__STRUCT_HPP_

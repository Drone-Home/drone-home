// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_messages:srv/SetCoordinate.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__SRV__DETAIL__SET_COORDINATE__STRUCT_HPP_
#define CUSTOM_MESSAGES__SRV__DETAIL__SET_COORDINATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'new_coordinate'
#include "sensor_msgs/msg/detail/nav_sat_fix__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__custom_messages__srv__SetCoordinate_Request __attribute__((deprecated))
#else
# define DEPRECATED__custom_messages__srv__SetCoordinate_Request __declspec(deprecated)
#endif

namespace custom_messages
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetCoordinate_Request_
{
  using Type = SetCoordinate_Request_<ContainerAllocator>;

  explicit SetCoordinate_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_coordinate(_init)
  {
    (void)_init;
  }

  explicit SetCoordinate_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_coordinate(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _new_coordinate_type =
    sensor_msgs::msg::NavSatFix_<ContainerAllocator>;
  _new_coordinate_type new_coordinate;

  // setters for named parameter idiom
  Type & set__new_coordinate(
    const sensor_msgs::msg::NavSatFix_<ContainerAllocator> & _arg)
  {
    this->new_coordinate = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_messages::srv::SetCoordinate_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_messages::srv::SetCoordinate_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_messages::srv::SetCoordinate_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_messages::srv::SetCoordinate_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_messages__srv__SetCoordinate_Request
    std::shared_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_messages__srv__SetCoordinate_Request
    std::shared_ptr<custom_messages::srv::SetCoordinate_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetCoordinate_Request_ & other) const
  {
    if (this->new_coordinate != other.new_coordinate) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetCoordinate_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetCoordinate_Request_

// alias to use template instance with default allocator
using SetCoordinate_Request =
  custom_messages::srv::SetCoordinate_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace custom_messages


#ifndef _WIN32
# define DEPRECATED__custom_messages__srv__SetCoordinate_Response __attribute__((deprecated))
#else
# define DEPRECATED__custom_messages__srv__SetCoordinate_Response __declspec(deprecated)
#endif

namespace custom_messages
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetCoordinate_Response_
{
  using Type = SetCoordinate_Response_<ContainerAllocator>;

  explicit SetCoordinate_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit SetCoordinate_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_messages::srv::SetCoordinate_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_messages::srv::SetCoordinate_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_messages::srv::SetCoordinate_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_messages::srv::SetCoordinate_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_messages__srv__SetCoordinate_Response
    std::shared_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_messages__srv__SetCoordinate_Response
    std::shared_ptr<custom_messages::srv::SetCoordinate_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetCoordinate_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetCoordinate_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetCoordinate_Response_

// alias to use template instance with default allocator
using SetCoordinate_Response =
  custom_messages::srv::SetCoordinate_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace custom_messages

namespace custom_messages
{

namespace srv
{

struct SetCoordinate
{
  using Request = custom_messages::srv::SetCoordinate_Request;
  using Response = custom_messages::srv::SetCoordinate_Response;
};

}  // namespace srv

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__SRV__DETAIL__SET_COORDINATE__STRUCT_HPP_

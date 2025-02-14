// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_messages:msg/ServoCommand.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__BUILDER_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_messages/msg/detail/servo_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_messages
{

namespace msg
{

namespace builder
{

class Init_ServoCommand_positions
{
public:
  explicit Init_ServoCommand_positions(::custom_messages::msg::ServoCommand & msg)
  : msg_(msg)
  {}
  ::custom_messages::msg::ServoCommand positions(::custom_messages::msg::ServoCommand::_positions_type arg)
  {
    msg_.positions = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_messages::msg::ServoCommand msg_;
};

class Init_ServoCommand_servo_ids
{
public:
  Init_ServoCommand_servo_ids()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ServoCommand_positions servo_ids(::custom_messages::msg::ServoCommand::_servo_ids_type arg)
  {
    msg_.servo_ids = std::move(arg);
    return Init_ServoCommand_positions(msg_);
  }

private:
  ::custom_messages::msg::ServoCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_messages::msg::ServoCommand>()
{
  return custom_messages::msg::builder::Init_ServoCommand_servo_ids();
}

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__BUILDER_HPP_

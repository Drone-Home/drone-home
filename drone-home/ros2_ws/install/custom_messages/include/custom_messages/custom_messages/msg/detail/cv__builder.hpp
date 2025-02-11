// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_messages:msg/CV.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__CV__BUILDER_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__CV__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_messages/msg/detail/cv__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_messages
{

namespace msg
{

namespace builder
{

class Init_CV_image_number
{
public:
  explicit Init_CV_image_number(::custom_messages::msg::CV & msg)
  : msg_(msg)
  {}
  ::custom_messages::msg::CV image_number(::custom_messages::msg::CV::_image_number_type arg)
  {
    msg_.image_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_messages::msg::CV msg_;
};

class Init_CV_y_size
{
public:
  explicit Init_CV_y_size(::custom_messages::msg::CV & msg)
  : msg_(msg)
  {}
  Init_CV_image_number y_size(::custom_messages::msg::CV::_y_size_type arg)
  {
    msg_.y_size = std::move(arg);
    return Init_CV_image_number(msg_);
  }

private:
  ::custom_messages::msg::CV msg_;
};

class Init_CV_x_size
{
public:
  explicit Init_CV_x_size(::custom_messages::msg::CV & msg)
  : msg_(msg)
  {}
  Init_CV_y_size x_size(::custom_messages::msg::CV::_x_size_type arg)
  {
    msg_.x_size = std::move(arg);
    return Init_CV_y_size(msg_);
  }

private:
  ::custom_messages::msg::CV msg_;
};

class Init_CV_y_pos
{
public:
  explicit Init_CV_y_pos(::custom_messages::msg::CV & msg)
  : msg_(msg)
  {}
  Init_CV_x_size y_pos(::custom_messages::msg::CV::_y_pos_type arg)
  {
    msg_.y_pos = std::move(arg);
    return Init_CV_x_size(msg_);
  }

private:
  ::custom_messages::msg::CV msg_;
};

class Init_CV_x_pos
{
public:
  Init_CV_x_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CV_y_pos x_pos(::custom_messages::msg::CV::_x_pos_type arg)
  {
    msg_.x_pos = std::move(arg);
    return Init_CV_y_pos(msg_);
  }

private:
  ::custom_messages::msg::CV msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_messages::msg::CV>()
{
  return custom_messages::msg::builder::Init_CV_x_pos();
}

}  // namespace custom_messages

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__CV__BUILDER_HPP_

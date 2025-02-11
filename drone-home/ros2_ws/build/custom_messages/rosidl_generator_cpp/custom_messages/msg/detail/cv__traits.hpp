// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_messages:msg/CV.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__CV__TRAITS_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__CV__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_messages/msg/detail/cv__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace custom_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const CV & msg,
  std::ostream & out)
{
  out << "{";
  // member: x_pos
  {
    out << "x_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.x_pos, out);
    out << ", ";
  }

  // member: y_pos
  {
    out << "y_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.y_pos, out);
    out << ", ";
  }

  // member: x_size
  {
    out << "x_size: ";
    rosidl_generator_traits::value_to_yaml(msg.x_size, out);
    out << ", ";
  }

  // member: y_size
  {
    out << "y_size: ";
    rosidl_generator_traits::value_to_yaml(msg.y_size, out);
    out << ", ";
  }

  // member: image_number
  {
    out << "image_number: ";
    rosidl_generator_traits::value_to_yaml(msg.image_number, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CV & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.x_pos, out);
    out << "\n";
  }

  // member: y_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.y_pos, out);
    out << "\n";
  }

  // member: x_size
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_size: ";
    rosidl_generator_traits::value_to_yaml(msg.x_size, out);
    out << "\n";
  }

  // member: y_size
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_size: ";
    rosidl_generator_traits::value_to_yaml(msg.y_size, out);
    out << "\n";
  }

  // member: image_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "image_number: ";
    rosidl_generator_traits::value_to_yaml(msg.image_number, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CV & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace custom_messages

namespace rosidl_generator_traits
{

[[deprecated("use custom_messages::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_messages::msg::CV & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const custom_messages::msg::CV & msg)
{
  return custom_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<custom_messages::msg::CV>()
{
  return "custom_messages::msg::CV";
}

template<>
inline const char * name<custom_messages::msg::CV>()
{
  return "custom_messages/msg/CV";
}

template<>
struct has_fixed_size<custom_messages::msg::CV>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_messages::msg::CV>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_messages::msg::CV>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__CV__TRAITS_HPP_

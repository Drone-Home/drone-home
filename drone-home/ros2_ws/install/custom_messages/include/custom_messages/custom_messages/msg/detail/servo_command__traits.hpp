// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_messages:msg/ServoCommand.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__TRAITS_HPP_
#define CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_messages/msg/detail/servo_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace custom_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const ServoCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: servo_ids
  {
    if (msg.servo_ids.size() == 0) {
      out << "servo_ids: []";
    } else {
      out << "servo_ids: [";
      size_t pending_items = msg.servo_ids.size();
      for (auto item : msg.servo_ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: positions
  {
    if (msg.positions.size() == 0) {
      out << "positions: []";
    } else {
      out << "positions: [";
      size_t pending_items = msg.positions.size();
      for (auto item : msg.positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ServoCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: servo_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.servo_ids.size() == 0) {
      out << "servo_ids: []\n";
    } else {
      out << "servo_ids:\n";
      for (auto item : msg.servo_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.positions.size() == 0) {
      out << "positions: []\n";
    } else {
      out << "positions:\n";
      for (auto item : msg.positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ServoCommand & msg, bool use_flow_style = false)
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
  const custom_messages::msg::ServoCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const custom_messages::msg::ServoCommand & msg)
{
  return custom_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<custom_messages::msg::ServoCommand>()
{
  return "custom_messages::msg::ServoCommand";
}

template<>
inline const char * name<custom_messages::msg::ServoCommand>()
{
  return "custom_messages/msg/ServoCommand";
}

template<>
struct has_fixed_size<custom_messages::msg::ServoCommand>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_messages::msg::ServoCommand>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_messages::msg::ServoCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MESSAGES__MSG__DETAIL__SERVO_COMMAND__TRAITS_HPP_

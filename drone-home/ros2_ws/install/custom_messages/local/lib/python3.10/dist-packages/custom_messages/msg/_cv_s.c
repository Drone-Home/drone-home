// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from custom_messages:msg/CV.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "custom_messages/msg/detail/cv__struct.h"
#include "custom_messages/msg/detail/cv__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool custom_messages__msg__cv__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[27];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("custom_messages.msg._cv.CV", full_classname_dest, 26) == 0);
  }
  custom_messages__msg__CV * ros_message = _ros_message;
  {  // x_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_pos = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_pos = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // x_size
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_size");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_size = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_size
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_size");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_size = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // image_number
    PyObject * field = PyObject_GetAttrString(_pymsg, "image_number");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->image_number = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * custom_messages__msg__cv__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CV */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("custom_messages.msg._cv");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "CV");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  custom_messages__msg__CV * ros_message = (custom_messages__msg__CV *)raw_ros_message;
  {  // x_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_size
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_size);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_size", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_size
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_size);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_size", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // image_number
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->image_number);
    {
      int rc = PyObject_SetAttrString(_pymessage, "image_number", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

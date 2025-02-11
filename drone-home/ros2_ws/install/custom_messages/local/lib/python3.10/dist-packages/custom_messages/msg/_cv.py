# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_messages:msg/CV.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CV(type):
    """Metaclass of message 'CV'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('custom_messages')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_messages.msg.CV')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__cv
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__cv
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__cv
            cls._TYPE_SUPPORT = module.type_support_msg__msg__cv
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__cv

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CV(metaclass=Metaclass_CV):
    """Message class 'CV'."""

    __slots__ = [
        '_x_pos',
        '_y_pos',
        '_x_size',
        '_y_size',
        '_image_number',
    ]

    _fields_and_field_types = {
        'x_pos': 'float',
        'y_pos': 'float',
        'x_size': 'float',
        'y_size': 'float',
        'image_number': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x_pos = kwargs.get('x_pos', float())
        self.y_pos = kwargs.get('y_pos', float())
        self.x_size = kwargs.get('x_size', float())
        self.y_size = kwargs.get('y_size', float())
        self.image_number = kwargs.get('image_number', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.x_pos != other.x_pos:
            return False
        if self.y_pos != other.y_pos:
            return False
        if self.x_size != other.x_size:
            return False
        if self.y_size != other.y_size:
            return False
        if self.image_number != other.image_number:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x_pos(self):
        """Message field 'x_pos'."""
        return self._x_pos

    @x_pos.setter
    def x_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_pos' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x_pos' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x_pos = value

    @builtins.property
    def y_pos(self):
        """Message field 'y_pos'."""
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_pos' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y_pos' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y_pos = value

    @builtins.property
    def x_size(self):
        """Message field 'x_size'."""
        return self._x_size

    @x_size.setter
    def x_size(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_size' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x_size' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x_size = value

    @builtins.property
    def y_size(self):
        """Message field 'y_size'."""
        return self._y_size

    @y_size.setter
    def y_size(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_size' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y_size' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y_size = value

    @builtins.property
    def image_number(self):
        """Message field 'image_number'."""
        return self._image_number

    @image_number.setter
    def image_number(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'image_number' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'image_number' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._image_number = value

#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "custom_messages::custom_messages__rosidl_generator_c" for configuration ""
set_property(TARGET custom_messages::custom_messages__rosidl_generator_c APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(custom_messages::custom_messages__rosidl_generator_c PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libcustom_messages__rosidl_generator_c.so"
  IMPORTED_SONAME_NOCONFIG "libcustom_messages__rosidl_generator_c.so"
  )

list(APPEND _cmake_import_check_targets custom_messages::custom_messages__rosidl_generator_c )
list(APPEND _cmake_import_check_files_for_custom_messages::custom_messages__rosidl_generator_c "${_IMPORT_PREFIX}/lib/libcustom_messages__rosidl_generator_c.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)

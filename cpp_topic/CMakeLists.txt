cmake_minimum_required(VERSION 3.8)
project(cpp_topic)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
# find_package(ament_cmake_auto REQUIRED)
# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclpy REQUIRED)

add_executable(talker_str src/talker_str.cpp)
ament_target_dependencies(
  talker_str
  "rclcpp"
  "std_msgs"
)

add_executable(listener_str src/listener_str.cpp)
ament_target_dependencies(
  listener_str
  "rclcpp"
  "std_msgs"
)

# ament_auto_find_build_dependencies()

install(TARGETS
  talker_str
  listener_str
  DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()



ament_package()


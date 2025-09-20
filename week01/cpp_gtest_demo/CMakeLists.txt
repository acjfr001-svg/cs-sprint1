include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
# Keep it light
set(BUILD_GMOCK OFF CACHE BOOL "" FORCE)
set(BUILD_GTEST ON  CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_library(sample STATIC sample.cpp)
add_executable(sample_test sample_test.cpp)
target_link_libraries(sample_test PRIVATE sample GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(sample_test)

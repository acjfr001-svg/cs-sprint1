#include <gtest/gtest.h>
int add(int,int);
TEST(Add, Works){ EXPECT_EQ(add(2,3), 5); }

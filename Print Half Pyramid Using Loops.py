# Write a Python program that prints a pyramid pattern made with asterisks.
#
# The number of rows should be determined by the value of the variable n. This value will be entered by the user.
#
# You may assume that the value of n is a positive integer.
#
# 🔹 Expected Output:
# If the value of n is 5, this is the expected output:
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# If the value of n is 10, this is the expected output:
#
#                   *
#
#                 * *
#
#               * * *
#
#             * * * *
#
#           * * * * *
#
#         * * * * * *
#
#       * * * * * * *
#
#     * * * * * * * *
#
#   * * * * * * * * *
#
# * * * * * * * * * *

n = int(input("Enter a Number :"))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (j >= 6 - i):
            print("*", end=" ")
    print(" ")

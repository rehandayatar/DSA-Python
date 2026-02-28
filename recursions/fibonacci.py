
# class Solution:
#     def func(self, num):
#         if num == 0:
#             return 0
#         if num == 1:
#             return 1
#         return self.func(num-1) + self.func(num-2)
#
#     def fib(self, n: int) -> int:
#         return self.func(n)
#
#
# sol = Solution()
# print(sol.fib(4))   # Output: 3
class Solution:
    def fib(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


obj = Solution()
print(obj.fib(7))
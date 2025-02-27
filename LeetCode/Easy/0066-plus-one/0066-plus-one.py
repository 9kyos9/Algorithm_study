
class Solution(object):
    def plusOne(self, digits):
        ans = []
        digits[-1] += 1
        carry = 0

        for i in range(len(digits)-1, -1, -1):
            dig = digits[i] + carry
            if dig >= 10:
                ans.insert(0, dig-10)
                carry = 1
            else:
                ans.insert(0, dig)
                carry = 0
        if carry != 0:
            ans.insert(0, carry)

        return ans
               
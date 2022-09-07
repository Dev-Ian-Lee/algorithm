# https://leetcode.com/problems/defanging-an-ip-address/
# defanged : (위험을) 제거한, 분리된

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = address.replace(".", "[.]")

        return defanged
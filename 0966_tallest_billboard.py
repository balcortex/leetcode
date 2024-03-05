from typing import List, Optional


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def can_sum(
            target: int, nums: List[int], ans: Optional[List[int]] = None
        ) -> bool:
            need = target - nums[0]
            ans.append(nums[0])
            nums = nums[1:]

            if need == 0:
                return ans

            if need in nums:
                ans.append(need)
                return ans

            if len(nums) >= 2:
                return can_sum(need, nums, ans=ans)
            else:
                return []

        def get_possible(target: int) -> Optional[List[int]]:
            possible = [can_sum(target, rods[i:], []) for i in range(len(rods))]
            possible = [p for p in possible if p]
            return possible

        def valid_combination(lst, sublst1, sublst2):
            # remaining = [s for s in lst if s not in sublst1]
            remaining = lst[:]
            temp = sublst1[:]

            while temp:
                t = temp.pop()
                if t in remaining:
                    remaining.remove(t)
                else:
                    return False

            temp = sublst2[:]

            while temp:
                t = temp.pop()
                if t in remaining:
                    remaining.remove(t)
                else:
                    return False
            return True

        def is_valid_rod(target: int) -> bool:
            pos = get_possible(target)
            print(target, pos)
            if len(pos) < 2:
                return False
            else:
                for j in range(len(pos)):
                    for i in range(j):
                        if valid_combination(rods, pos[j], pos[i]):
                            return True
                return False

        max_ = max(i if is_valid_rod(i) else 0 for i in range(1, sum(rods)))
        # print(max_)
        return max_


rods1 = [1, 2, 3, 6]
rods2 = [1, 2, 3, 4, 5, 6]
rods3 = [1, 2]
rods4 = [100, 100]
rods5 = [61, 45, 43, 54, 40, 53, 55, 47, 51, 59, 42]

sol = Solution()
# sol.tallestBillboard(rods1)
# sol.tallestBillboard(rods2)
# sol.tallestBillboard(rods3)
# sol.tallestBillboard(rods4)
sol.tallestBillboard(rods5)

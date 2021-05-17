class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        new_list = []
        sum_of_walth = 0
        for account in accounts:
            for money in account:
                sum_of_walth += money
            new_list.append(sum_of_walth)
            sum_of_walth = 0
        return max(new_list)
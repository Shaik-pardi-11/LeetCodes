class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result


solution = Solution()
print(solution.letterCombinations("23"))  
print(solution.letterCombinations("2")) 

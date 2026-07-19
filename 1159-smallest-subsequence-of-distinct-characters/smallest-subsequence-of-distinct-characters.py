class Solution:
    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        stack = []
        in_stack = set()
        
        for ch in s:
            freq[ch] -= 1
            if ch in in_stack:
                continue
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(ch)
            in_stack.add(ch)
        
        return "".join(stack)

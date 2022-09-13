class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        q = deque(sorted(tokens))
        current_score = 0
        max_score = 0
        
        while q:
            if power >= q[0]:
                first_token = q.popleft()
                power -= first_token
                current_score += 1
                max_score = max(current_score, max_score)
            
            elif current_score > 0:
                last_token = q.pop()
                power += last_token
                current_score -= 1
            
            else:
                break
                
        return max_score
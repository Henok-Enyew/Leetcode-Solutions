# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = {}
        answer = []
        
        for cp in cpdomains:
            domain = cp.split(' ')[1]
            count = int(cp.split(' ')[0])
            if domain in mp.keys():
                mp[domain] += count 
            else:
                mp[domain] = count 
            domain = domain[domain.find('.')+1:]
            if domain in mp.keys():
                mp[domain] += count 
            else:
                mp[domain] = count 
            if domain.find('.') != -1:
                domain = domain[domain.find('.')+1:]
                if domain in mp.keys():
                    mp[domain] += count 
                else:
                    mp[domain] = count 
        for dom in mp:
            answer.append(f"{mp[dom]} {dom}")
        return answer

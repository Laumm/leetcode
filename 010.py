cs = [chr(i) for i in range(97,123)]
class Solution:
    last = []
    def isMatch(self, s: str, p: str) -> bool:
        if p == s :
            return True
        if len(p) == 0 :
            return False
        # 对应字符匹配
        if p[0] in cs :
            self.last = p[0] 
            if len(p) > 1 and p[1] == "*" :
                return self.isMatch(s,p[1:])
            if len(s) > 0 and p[0] == s[0] :
                return self.isMatch(s[1:],p[1:])
            return False
        # . 对应任何字符
        if p[0] == "." :
            self.last = cs
            if len(p) > 1 and p[1] == "*" :
                return self.isMatch(s,p[1:])
            if len(s) > 0 :
                return self.isMatch(s[1:],p[1:])
            return False
        # * 匹配0个和多个 ，复杂
        # 贪吃匹配(不匹配回滚)
        if p[0] == "*" :
            last = self.last
            self.last = []
            mx = 0 
            for c in s :
                if c in last :
                    mx += 1
                break
            for i in range(mx+1 ) :
                if self.isMatch(s[mx-i:],p[1:]):
                    return True 
            return False
            


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("bacccabbaacaccabac",".*..*.*c*.a*bb*b*"))
    


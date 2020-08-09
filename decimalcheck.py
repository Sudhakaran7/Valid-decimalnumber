class Solution:
    def isNumber(self, s):

        s = s.strip()

        isDot, isDigit, isE = False, False, False 

        for i, x in enumerate(s):
            if x == "e":
                if not isDigit or isE:  
                    return False

                isDigit = False  
                isE = True
            elif x in "+-":
                if i != 0 and s[i-1] != "e":  
                    return False
            elif x == ".":
                if isDot or isE:  
                    return False
                isDot = True
            elif x.isdecimal():  
                isDigit = True
            else:
                return False

        return len(s) > 0 and isDigit


if __name__ == '__main__':
    solu = Solution()
    a=input()
    print(solu.isNumber(a))

def canConstruct( ransomNote: str, magazine: str) -> bool:
        dct = {}
        
        for a in ransomNote:
            print(a)
            if a in dct.keys():
                dct[a] += 1    
            else:
                dct[a] = 0
            print(dct)    

        for a in magazine:
            if a in dct.keys():
                dct[a] -= 1
                if dct[a] == 0:
                    dct.pop(a)  
            if dct == {}:
                return True
        return False                          
print(canConstruct("aaa", "abbb"))    

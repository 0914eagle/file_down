
import re
def golorp_food(name):
    parts = re.findall(r'\?(\([^)]+\))/(\([^)]+\))', name)
    if not parts:
        return "false"
    
    jaws, stomach = parts[0]
    jaws = re.findall(r'[_\-+*]', jaws)
    stomach = re.findall(r'[_\-+*]', stomach)
    
    var_count = len(jaws)
    
    def get_food(i):
        if i >= var_count:
            return ''
        for v in range(10):
            if str(v) in jaws[i] and str(v) in stomach[i]:
                return str(v) + get_food(i+1)
    
    return get_food(0)
    
print(golorp_food("?(_-_/___*__):-___>__."))
print(golorp_food("?(__-_+_/_____):-__>__,_____<__."))
print(golorp_food("?(______________________/____+_______*__-_____*______-___):-__<___,___<____,____<_____,_____<______,______<_______."))
print(golorp_food("?(__+___+__-___):-___>__."))


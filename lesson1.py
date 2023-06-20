def strcounter(s):
    print(set(s))
    for sym in s:
        counter = 0
        for sub_s in s:
            counter +=1
            print(sym, '-', counter)
#strcounter('abbbcc')

def strcounter2(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym,'-', count)
strcounter2('aabbbcccccccccccde')

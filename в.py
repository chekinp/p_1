"""def rer(d):
    for f in set(d):
        count = 0
        for f1 in d:
            if f == f1:
                count += 1
        print(f'{count} - {f}')
rer('abcnra')
"""


def rer(d):
    syms_con = {}
    for sym in d:
        syms_con[sym] = syms_con.get(sym, 0) + 1
    for sym, count in syms_con.items():
        print(sym, count)

rer('ageyerytogyuerwy')



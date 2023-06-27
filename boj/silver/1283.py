# https://www.acmicpc.net/problem/1283

import sys
import copy

n = int(sys.stdin.readline())

shortcuts = set()
options = []
for _ in range(n):
    options.append(sys.stdin.readline().rstrip())

new_options = []
for option in options:
    curr_options = copy.deepcopy(new_options)

    # 첫 번째 단어의 첫 문자를 단축키로 지정
    if option[0].lower() not in shortcuts:
        shortcuts.add(option[0].lower())
        new_options.append("[" + option[0] + "]" + option[1:])

    # 옵션이 여러 개의 단어로 구성된 경우
    elif ' ' in option:
        splitted = option.split()

        new = ""
        for i in range(len(splitted)):
            s = splitted[i]

            # 각 단어의 첫 글자로 단축키를 등록할 수 있는 경우
            if s[0].lower() not in shortcuts:
                shortcuts.add(s[0].lower())
                new += "[" + s[0] + "]" + s[1:]

                # 단축키 등록 이후의 단어는 모두 그대로 추가
                for j in range(i + 1, len(splitted)):
                    new += " "
                    new += splitted[j]

                break
                
            else:
                new += s
                new += " "

        if "[" in new:
            new_options.append(new)

    # 각 단어의 첫 문자를 단축키로 지정할 수 없는 경우, 앞에서부터 한 글자씩 검사해 단축키로 지정
    if len(curr_options) == len(new_options):
        for i in range(len(option)):
            if option[i].lower() not in shortcuts and option[i] != " ":
                shortcuts.add(option[i].lower())
                new_options.append(option[:i] + "[" + option[i] + "]" + option[i + 1:])
                break

    # 단축키를 지정할 수 없는 옵션의 경우, 그대로 추가
    if len(curr_options) == len(new_options):
        new_options.append(option)

for o in new_options:
    print(o)
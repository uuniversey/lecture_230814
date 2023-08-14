

# 1222. 계산기1

# import sys
# sys.stdin = open('input_1222.txt', 'r')
#
#
# def isp(s):
#     if s == '*' or s == '/':
#         return 2
#     elif s == '(':
#         return 0
#     else:
#         return 1
#
#
# def icp(s):
#     if s == '*' or s == '/':
#         return 2
#     elif s == '(':
#         return 3
#     else:
#         return 1
#
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     formula = input()
#     top = -1
#     stack = []
#     my_list = []
#
#     for i in formula:
#         if len(my_list) == 0:
#             my_list.append(int(i))
#
#         elif i == '+':
#             if len(stack) == 0:
#                 top += 1
#                 stack.append(i)
#             elif icp(i) > isp(stack[top]):
#                 top += 1
#                 stack.append(i)
#             else:
#                 top -= 1
#                 my_list.append(stack.pop())
#                 top += 1
#                 stack.append(i)
#
#         else:
#             if i != '+':
#                 my_list.append(int(i))
#
#     my_list.append(stack[top])
#     top -= 1
#     stack = []
#     # 후위표기법 만들기 끝
#
#     for j in my_list:
#         if type(j) is int:
#             top += 1
#             stack.append(j)
#         elif j == '+':
#             cal_B = stack.pop()
#             top -= 1
#             cal_A = stack.pop()
#             top -= 1
#             stack.append(cal_A + cal_B)
#             top += 1
#
#     print(f'#{tc} {stack[top]}')



# 18382. Forth

# import sys
# sys.stdin = open('input_18382.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     formula = list(map(str, input().split()))
#     stack = []
#     top = -1
#     result = 0
#     symbol_check = 0
#     int_check = 0
#
#     for check in formula:                               # 예외처리 - 부호가 숫자보다 많을경우
#         if check in '+-*/':
#             symbol_check += 1
#         elif check not in '+-*/' and check != '.':
#             int_check += 1
#
#     if int_check <= symbol_check:
#         print(f'#{tc} error')
#
#     elif int_check > symbol_check:
#         for i in formula:
#             if len(stack) == 0 and i in '+-/*.':
#                 print(f'#{tc} error')
#                 break
#
#             if i not in '+-/*.':
#                 top += 1
#                 stack.append(i)
#             elif i == '.':
#                 if len(stack) != 1:
#                     print(f'#{tc} error')
#                     break
#                 else:
#                     print(f'#{tc} {result}')
#                     break
#             else:
#                 if len(stack) <= 1:                 # 예외처리 - 숫자가 남은 경우
#                     print(f'#{tc} error')
#                     break
#                 else:
#                     val2 = int(stack.pop())
#                     top -= 1
#                     val1 = int(stack.pop())
#                     top -= 1
#                     if i == '+':
#                         result = val1 + val2
#                         stack.append(result)
#                         top += 1
#                     elif i == '-':
#                         result = val1 - val2
#                         stack.append(result)
#                         top += 1
#                     elif i == '*':
#                         result = val1 * val2
#                         stack.append(result)
#                         top += 1
#                     elif i == '/':
#                         result = int(val1 / val2)       # 예외처리 - .0으로 나오는 경우 제거
#                         stack.append(result)
#                         top += 1



# 18384. 미로

import sys
# sys.stdin = open('input_18384.txt', 'r')


# 18389. 후위 유사 표기법 연습

# import sys
# sys.stdin = open('input_18389.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     formula = input()
#     result = ''
#     box = []
#     stack = []
#     top = -1
#     icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
#     isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
#
#     for i in formula:
#         if i not in '(*/+-)':
#             box.append(i)
#
#         elif i == '(':
#             top += 1
#             stack.append(i)
#
#         elif i == ')':
#             while stack[top] != '(':
#                 box.append(stack[top])
#                 top -= 1
#
#         else:
#             if len(stack) == 0 or icp[i] >= isp[stack[top]]:
#                 top += 1
#                 stack.append(i)
#             elif icp[i] < isp[stack[top]]:
#                 top -= 1
#                 box.append(stack.pop())
#
#     while top >= 0:
#         box.append(stack[top])
#         top -= 1
#
#     for j in range(len(box)):
#         result += box[j]
#
#     print(f'#{tc} {result}')



# 18390. 후위 표기법

# import sys
# sys.stdin = open('input_18390.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     formula = input()
#     result = ''
#     box = []
#     stack = []
#     top = -1
#     icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
#     isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
#
#     for i in formula:
#         if i not in '(+-*/':
#             box.append(i)
#         else:
#             if len(stack) == 0 or icp[i] > isp[stack[top]]:
#                 top += 1
#                 stack.append(i)
#
#             elif icp[i] <= isp[stack[top]]:
#                 top -= 1
#                 box.append(stack.pop())
#                 top += 1
#                 stack.append(i)
#
#     while len(stack) != 0:
#         box.append(stack.pop())
#
#     for j in range(len(box)):
#         result += box[j]
#
#     print(f'#{tc} {result}')
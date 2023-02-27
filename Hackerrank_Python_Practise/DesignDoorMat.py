# Designer Door Mat
#
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#
# Mat size must be N X M  ( N is an odd natural number, and M is 3 times N)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
#
# Sample Designs
# Size: 7 x 21
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
#
# Size: 11 x 33
#         ---------------.|.---------------
#         ------------.|..|..|.------------
#         ---------.|..|..|..|..|.---------
#         ------.|..|..|..|..|..|..|.------
#         ---.|..|..|..|..|..|..|..|..|.---
#         -------------WELCOME-------------
#         ---.|..|..|..|..|..|..|..|..|.---
#         ------.|..|..|..|..|..|..|.------
#         ---------.|..|..|..|..|.---------
#         ------------.|..|..|.------------
#         ---------------.|.---------------
# Constraint : 5 < N < 101
#              15 < M < 303

# Sample Input
# try:
#     N = int(input())
#     while N % 2 == 0:
#         N = int(input("Enter an odd number ( 2..9 ) : "))
# except ValueError as e:
#     raise
#
# M = 3 * N
# top_gen_rows = ("".join(list(["-"] * M)) for i in range(1,N + 1))
# gen_colums = ("".join(list([".|."] * i)).center(M) for i in range(1,(M + 1)//3,2))

N, M = map(int,input().split())
# gen_rows = ("".join(list(["-"] * M)) for i in range(1,N + 1))
gen_top_half = ("".join(list([".|."] * i)).center(M,'-') for i in range(1,(M + 1)//3,2))
gen_bottom_half = ("".join(list([".|."] * i)).center(M,'-') for i in reversed(range(1,(M + 1)//3,2)))
middle_line = "WELCOME".center(M,'-')


for i in gen_top_half:
    print(i)

print("".join(list(middle_line)))

for i in gen_bottom_half:
    print(i)

#
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# # 11
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------

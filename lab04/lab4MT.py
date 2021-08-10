# Douglas Vieira
# @ansattz


# # 1 Manipulação de strings
# # 1.
# def concatenacao(a,b):
#     return a + b + b + a
# print(concatenacao('x', 'd'))


# # 2. 

# def substitui(s,x,i):
#     sub = s[:i] + x + s[1+i:]
#     return sub
# print(substitui('jogar','b',2))


# # 3.
# def hashtag(s):
#     n= len(s)//2 
#     frasehast='#' + s[:n] + '#' + s[n:] + '#'
#     return frasehast

# print(hashtag('abcde'))


# def colisao(tup,tup1):
#     if tup[2] < tup1[0] or tup1[2] < tup[0] or tup[3] < tup1[1] or tup1[3] < tup[1]:
#         return 2==3
#     else:
#         return 2==2
# print(colisao((4,8,9,9),(2,1,9,5)))



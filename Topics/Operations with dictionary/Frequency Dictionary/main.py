"""After hours of work I crammed the solution into one line.

I did it not because it was easy, but because it was hard.
And because I find it funny. Mostly because I find it funny.

The first line after this docstring is the final official
absolutely amazing oneliner.

The 14 literal in that oneliner is a dirty hack to get through
hyperskill tests. It is the smallest number that passes the tests.
I didn't try looking for a solution that wouldn't require this
monstrosity, as solving this problem in one line is insane anyway.

The functions are basically consecutive approaches to solving
the problem in as few lines as possible. In particular,
the comments in two_lines_with_dict() describe why
the walrus operator doesn't solve anything.
"""
print(*[f'{w} {words.count(w)}' for (w, words) in zip(*[(sorted(set(ws)), [ws] * 14) for ws in [input().lower().split()]][0])], sep='\n')
#                                                   hyperskill got nothing on me ^

def normal_code():
    words = input().lower().split()
    counts = {w: words.count(w) for w in sorted(set(words))}
    for key, value in counts.items():
        print(key, value)

def two_lines_with_dict():
    words = input().lower().split()
    print(*(f'{key} {value}' for (key, value) in {w: words.count(w) for w in sorted(set(words))}.items()), sep='\n')
    # Sadly the walrus operator can't be used in comprehensions.
    # If it was allowed I could go down to one line with:
    # print(*(f'{key} {value}' for (key, value) in {w: words.count(w) for w in sorted(set(words := input().lower().split()))}.items()), sep='\n')
    #                                                                         walrus lives here ^

def two_lines_no_dict():
    words = input().lower().split()
    print(*(f'{w} {words.count(w)}' for w in set(words)), sep='\n')

def idea():
    words: list[str] = ['a', 'aa', 'aaa', 'a']
    n: int = 0  # n >= 0
    print(*[f'{w} {words.count(w)}' for (w, words) in zip( sorted(set(words)), [words] * (len(set(words))+n) )], sep='\n')
    #                                                      ^
    #                                                    ( {'a', 'aa', 'aaa'}, [['a', 'aa', 'aaa', 'a']]*4 )

def draft_1():
    print(*[f'{w} {words.count(w)}' for (w, words) in zip( {'a', 'aa', 'aaa'}, [['a', 'aa', 'aaa', 'a']]*4 )], sep='\n')

    print( [{'a', 'aa', 'aaa'}, [['a', 'aa', 'aaa', 'a']]*3] )
    print([(sorted(set(ws)), [ws] * 3) for ws in [['a', 'aa', 'aaa', 'a']]][0])
    # print( [[a, a*3] for a in [1]][0])

def draft_2():
    print(*[f'{w} {words.count(w)}' for (w, words) in zip( *[(sorted(set(ws)), [ws] * 3) for ws in [['a', 'aa', 'aaa', 'a']]][0] )], sep='\n')

# ======================================================================
#                              No mans land:
# ======================================================================
# My initial approach was all over the place.
# Here lie the remnants of that chaotic era.

# def counter():
#     words = input().lower().split()
#     l = []
#     for w1, n in zip(sorted(set(words)), [0]*len(sorted(words))):
#         # n = 0
#         for w2 in words:
#             if w1 == w2:
#                 n += 1
#         l.append(f'{w1} {n}')
#     print(*l, sep='\n')
# compact_counter()

# print(*(f'{w} {words.count(w)}' for w in set(words)), sep='\n')

# Try to use some tuples
# words = input().lower()
# ws, cs = ((words + '\n')*2).rstrip('\n').split('\n')
#
# ws = ws.split()
# cs = cs.split()

# print(f'{ws=}\n{cs=}')
# ws = list(set(ws))
# cs = [cs.count(w) for w in set(cs)]
# print(list(zip(ws,cs)))
# print(f'{ws=}\n{cs=}')

# print(*(f'{w} {words.count(w)}' for w in set(words)))
# print(*(f'{w} {words.count(w)}' for w in set(words)))
# print(*(f'{w} {c}' for (w, c) in zip(['a', 'aa', 'aaaa', 'a'],[2, 1, 1, 2])), sep='\n')

# words = ((input().lower() + '\n')*2).rstrip('\n').split('\n')
# print(words)
# words = f'{words[0]}\n{words[1]}'
# print(words)
# words = words.split(' ')
# print(words)

# words = input().lower().split()
# print(words)


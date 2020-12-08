from collections import Counter
import math
word = ["abcdafcc"]


def anagram(word_list):
    for word in word_list:
        tot_len = len(word)
        if tot_len % 2 == 1:
            print(-1)
            return -1
        else:
            tot_count = 0
            s1 = Counter(word[tot_len // 2:])
            s2 = Counter(word[:tot_len // 2])
            for letter in s1:
                diff = s1[letter] - s2.get(letter, 0.0)
                if diff > 0:
                    tot_count += diff
            print(tot_count)
            return tot_count


anagram(word)


def find_sqrts(num):
    keep_going = True
    tot_count = 0
    temp_num = num
    while keep_going:
        temp_square = math.sqrt(temp_num)
        if temp_square != math.floor(temp_square):
            keep_going = False
        else:
            tot_count += 1
            temp_num = temp_square
    return tot_count


print(find_sqrts(9))

print(range(0, 20))
print(10 // 2)

print("new")
M = 5
count = [0] * (M + 1)
print(count)

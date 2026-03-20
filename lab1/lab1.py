#1
def analyze_text(text):
    vowels = "aeiou"
    text = text.lower()
    clean = ""
    for c in text:
        if c.isalpha() or c == " ":
            clean += c
    words = clean.split()
    v = set()
    res = []
    used = set()
    for w in words:
        for c in w:
            if c in vowels:
                v.add(c)
        if len(w) >= 5 and w[0] == w[-1] and w not in used:
            res.append(w)
            used.add(w)
    return (len(v), " ".join(res))
t = "level apple bread radar table"
print(analyze_text(t))
#2
f = lambda s: " ".join(
    filter(
        lambda w: len(w) % 2 == 0,
        map(
            lambda w: w[::-1],
            filter(lambda w: not any(c.isdigit() for c in w), s.split())
        )
    )
)

s = "book car12 table pen apple"
print(f(s))
#3
import string
def top_k_words(text, k):
    text = text.lower()
    clean = ""
    for c in text:
        if c not in string.punctuation:
            clean += c
    words = clean.split()
    d = {}
    for w in words:
        if w not in d:
            d[w] = 0
        d[w] += 1
    items = list(d.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    res = []
    for i in range(min(k, len(items))):
        res.append(items[i][0])
    return res
t = "cat dog cat milk dog cat bread"
print(top_k_words(t, 2))
#4
f = lambda s: " ".join(
    w.lower() for w in s.split()
    if sum(1 for c in w if c.isupper()) == 1
    and not w[0].isupper()
    and not w[-1].isupper()
)
s = "aBc abCde heLlo woRld"
print(f(s))
#5
def compress_text(text):
    if text == "":
        return ""
    res = ""
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i-1].lower():
            count += 1
        else:
            if count > 1:
                res += text[i-1] + str(count)
            else:
                res += text[i-1]

            count = 1
    if count > 1:
        res += text[-1] + str(count)
    else:
        res += text[-1]
    return res
print(compress_text("aaBBcDDD"))
#6
f = lambda s: [
    w for w in s.split()
    if len(w) >= 4
    and not any(c.isdigit() for c in w)
    and len(set(w)) == len(w)
]
s = "lamp door tree book1 milk"
print(f(s))
#7
import string
def palindrome_words(text):
    clean = ""
    for c in text:
        if c not in string.punctuation:
            clean += c
    words = clean.lower().split()
    p = set()
    for w in words:
        if len(w) >= 3 and w == w[::-1]:
            p.add(w)
    res = list(p)
    res.sort(key=lambda x: (-len(x), x))
    return res
t = "level radar cat civic noon apple"
print(palindrome_words(t))
#8
f = lambda s: " ".join(
    w if any(c.isdigit() for c in w)
    else ("VOWEL" if w[0].lower() in "aeiou" else "CONSONANT")
    for w in s.split()
)

s = "apple book egg table car7 orange"
print(f(s))
#9
def alternate_case_blocks(text, n):
    res = ""
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if (i // n) % 2 == 0:
            res += block.upper()
        else:
            res += block.lower()
    return res.replace(" ", "")
print(alternate_case_blocks("hello world python", 3))
#10
f = lambda s: sum(
    1 for w in s.split()
    if any(c.isdigit() for c in w)
    and not w[0].isdigit()
    and len(w) >= 5
)

s = "ab12cd 1test abcde9 book7 test"
print(f(s))
#11
def common_unique_chars(s1, s2):
    res = ""
    used = set()
    for c in s1:
        if c in s2 and c not in used and not c.isdigit() and c != " ":
            res += c
            used.add(c)
    return res
print(common_unique_chars("hello123", "worldhello"))
#12
f = lambda s: [
    w for w in s.split()
    if len(w) > 3 and w[0] == w[-1] and w != w[::-1]
]

s = "abca level testaa radar civic"
print(f(s))
#13
def replace_every_nth(text, n, ch):
    res = ""
    pos = 0
    words = text.split(" ")
    for w in words:
        new = ""
        for c in w:
            pos += 1
            if pos % n == 0 and not c.isdigit() and len(w) >= 3:
                new += ch
            else:
                new += c
        res += new + " "
    return res.strip()
print(replace_every_nth("hello my table book", 3, "*"))
#14
v = "aeiou"

f = lambda s: ",".join(
    w for w in s.split()
    if len(set(w)) > 3 and all(w.count(x) <= 1 for x in v)
)

s = "table bread moon light car apple"
print(f(s))
#15
def word_pattern_sort(text):
    v = "aeiou"
    words = text.split()
    groups = {}
    for w in words:
        l = len(w)
        if l not in groups:
            groups[l] = []
        groups[l].append(w)
    res = []
    for l in sorted(groups):
        g = groups[l]
        g.sort(key=lambda x: (-sum(1 for c in x if c in v), x))
        res.extend(g)
    return res
t = "table car apple bread tea moon"
print(word_pattern_sort(t))
#16
def transform_list(nums):
    res = []
    for n in nums:
        if n < 0:
            continue
        if n % 2 == 0:
            res.append(n*n)
        elif n > 10:
            s = 0
            for d in str(n):
                s += int(d)
            res.append(s)
        else:
            res.append(n)
    return res
print(transform_list([2, 5, 12, -3, 8, 15]))
#17
f = lambda a: [
    x*x for x in a
    if (x % 3 == 0 or x % 5 == 0)
    and x % 15 != 0
    and len(str(abs(x))) % 2 == 1
]

print(f([3,5,15,33,44,105]))
#18
def flatten_and_filter(lst):
    res = []
    for x in lst:
        if isinstance(x, list):
            res += flatten_and_filter(x)
        else:
            if isinstance(x, int) and x > 0 and x % 4 != 0 and len(str(x)) > 1:
                res.append(x)
    res.sort()
    return res
print(flatten_and_filter([1,[12,8],[33,[16,25]],5]))
#19
f = lambda a,b: [x for x,y in zip(a,b) if x==y and x%2==0]
print(f([2,3,4,6],[2,5,4,7]))
#20
def max_subarray_sum(nums, k):
    m = None
    for i in range(len(nums)-k+1):
        w = nums[i:i+k]
        ok = True
        for x in w:
            if x <= 0:
                ok = False
        if ok:
            s = sum(w)
        if m == None or s > m:
                m = s
    return m
print(max_subarray_sum([1,2,3,0,5,6],2))
#21
f = lambda a: [x.upper() for x in a if x.isalpha() and len(x)>4 and len(set(x))==len(x)]
print(f(["table","apple","book","lamp12","chair"]))
#22
def group_by_parity_and_sort(nums):
    e = []
    o = []
    for x in nums:
        if x % 2 == 0:
            e.append(x)
        else:
            o.append(x)
    e.sort()
    o.sort()
    return e + o
print(group_by_parity_and_sort([5,2,7,4,1,6]))
#23
f = lambda a: [
a[i] for i in range(len(a))
if i>1
and all(i%j!=0 for j in range(2,int(i**0.5)+1))
and a[i]%2==1
and a[i] > sum(a)/len(a)
]
print(f([3,7,5,9,11,2,15]))
#24
def longest_increasing_sublist(nums):
    best = []
    cur = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            cur.append(nums[i])
        else:
            if len(cur) > len(best):
                best = cur
            cur = [nums[i]]
    if len(cur) > len(best):
        best = cur
    return best
print(longest_increasing_sublist([1,2,3,1,2,5,6,0]))
#25
f = lambda a: [sum(x)/len(x) for x in a if len(x)>=3 and sum(x)%2==0]
print(f([[1,2,3],[2,4,6],[1,1],[5,5,5]]))
#26
def remove_duplicates_keep_last(nums):
    res = []
    seen = set()
    for x in reversed(nums):
        if x not in seen:
            res.append(x)
            seen.add(x)
    res.reverse()
    return res
print(remove_duplicates_keep_last([1,2,3,2,4,1,5]))
#27
f = lambda a: sorted(a,key=lambda x:(-len(x),x))[:5]
print(f(["table","car","apple","banana","dog","milk","chair"]))
#28
def moving_average(nums,k):
    res = []
    for i in range(len(nums)-k+1):
        w = nums[i:i+k]
        ok = True
        for x in w:
            if x < 0:
                ok = False
        if ok:
            res.append(sum(w)/k)
    return res

print(moving_average([1,2,3,-1,5,6],2))
#29
f = lambda a,b: [x for x in a if x not in b and x > sum(a)/len(a)]
print(f([1,5,7,10,3],[5,2,3]))
#30
def analyze_strings_list(words):
    res = []
    seen = set()
    for w in words:
        if any(c.isdigit() for c in w):
            continue
        if len(w)%2==0:
            new = w[::-1]
        else:
            new = w.upper()
        if new not in seen:
            res.append(new)
            seen.add(new)
    return res

print(analyze_strings_list(["table","apple","book2","milk","apple"]))

#set and dict
#1
def invert_unique(d):
    result = {}
    for k in d:
        v = d[k]
        if v not in result:
            result[v] = []
        if k not in result[v]:
            result[v].append(k)
    return result
d = {"a":1,"b":2,"c":1,"d":3}
print(invert_unique(d))
#2
filter_set = lambda s: {x for x in s if x > sum(s)/len(s) and x%2==1 and x%5!=0}

s = {1,3,7,9,10,15,21}
print(filter_set(s))
#3
def merge_dicts_sum(d1,d2):
    result = {}
    for k in d1:
        result[k] = d1[k]
    for k in d2:
        if k in result:
            result[k] += d2[k]
        else:
            result[k] = d2[k]
    return result
d1 = {"a":2,"b":3}
d2 = {"b":5,"c":4}
print(merge_dicts_sum(d1,d2))
#4
def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) > 3:
            has_negative = False
            has_even = False
            for x in s:
                if x < 0:
                    has_negative = True
                if x % 2 == 0:
                    has_even = True
                if not has_negative and has_even:
                   result.append(s)
    return result
sets_list = [{1,2,3,4},{1,3,5},{2,4,6,8},{1,-2,3,4}]
print(filter_sets(sets_list))
#5
top5 = lambda d: [k for k,v in sorted(d.items(), key=lambda x:(-x[1],x[0]))][:5]
d = {"a":5,"b":7,"c":7,"d":2,"e":10,"f":1}
print(top5(d))
#6
def deep_sum(d):
    total = 0
    for v in d.values():
        if isinstance(v,int):
            total += v
        elif isinstance(v,list):
            for x in v:
                total += x
        elif isinstance(v,dict):
            total += deep_sum(v)
    return total
d = {"a":5,"b":[1,2,3],"c":{"x":4,"y":[1,1]}}
print(deep_sum(d))
#7
even_unique = lambda a,b: {x for x in (a^b) if x%2==0}
a = {1,2,3,4}
b = {3,4,5,6}
print(even_unique(a,b))
#8
def sort_dict_by_value_length(d):
    items = list(d.items())
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if len(items[i][1]) > len(items[j][1]) or \
               (len(items[i][1]) == len(items[j][1]) and items[i][0] > items[j][0]):
                items[i],items[j] = items[j],items[i]
    return items
d = {"a":"apple","b":"hi","c":"banana","d":"cat"}
print(sort_dict_by_value_length(d))\
#9
def common_elements_all(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for s in sets_list[1:]:
        result = result.intersection(s)
    return result
sets_list = [{1,2,3},{2,3,4},{0,2,3,5}]
print(common_elements_all(sets_list))
#10
filter_dict = lambda d: {k:sorted([x for x in v if x%2==1]) for k,v in d.items() if [x for x in v if x%2==1]}
d = {"a":[1,2,3,4],"b":[2,4,6],"c":[5,7,8]}
print(filter_dict(d))
#11
def group_by_length(words):
    result = {}
    for w in words:
        l = len(w)
        if l not in result:
            result[l] = []
        if w not in result[l]:
            result[l].append(w)
    return result
words = ["cat","dog","apple","dog","hi","sun"]
print(group_by_length(words))
#12
filter_strings = lambda s: {x for x in s if x.isalpha() and len(x)>4 and len(set(x))==len(x)}
s = {"hello","world","apple","abcd","abcde","level"}
print(filter_strings(s))
#13
def invert_dict_strict(d):
    counts = {}
    result = {}
    for v in d.values():
        counts[v] = counts.get(v,0)+1
    for k,v in d.items():
        if counts[v] == 1:
            result[v] = k
    return result
d = {"a":1,"b":2,"c":1,"d":3}
print(invert_dict_strict(d))
#14
def top_k_frequent(nums,k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n,0)+1
    items = list(freq.items())
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if items[i][1] < items[j][1] or \
               (items[i][1]==items[j][1] and items[i][0] > items[j][0]):
                items[i],items[j] = items[j],items[i]
    result = set()
    for i in range(min(k,len(items))):
        result.add(items[i][0])
    return result
nums = [1,1,1,2,2,3,4,4,4,4]
print(top_k_frequent(nums,2))
#15
filter_dict2 = lambda d: {k:v for k,v in d.items() if v >= sum(d.values())/len(d) and v%2==1}
d = {"a":5,"b":2,"c":9,"d":4,"e":7}
print(filter_dict2(d))
#16
def update_counts(d,items):
    for x in items:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d
d = {"apple":2,"banana":1}
items = ["apple","banana","apple","orange"]
print(update_counts(d,items))
#17
set_func = lambda a,b,c: (a & b) - c
a = {1,2,3,4}
b = {2,3,5}
c = {3}
print(set_func(a,b,c))
#18
def sort_dict_by_value_sum(d):
    items = []
    for k in d:
        s = 0
        for x in d[k]:
            s += x
        items.append((k,s))
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if items[i][1] < items[j][1] or \
               (items[i][1] == items[j][1] and items[i][0] > items[j][0]):
                items[i],items[j] = items[j],items[i]
    return items
d = {
    "a":[1,2,3],
    "b":[5],
    "c":[2,2,2],
    "d":[10]
}
print(sort_dict_by_value_sum(d))
#19
def filter_by_digit_sum(nums):
    result = set()
    for n in nums:
        if n % 2 == 1:
            s = 0
            for digit in str(abs(n)):
                s += int(digit)
            if s % 2 == 0:
                result.add(n)
    return result
nums = {11,23,35,44,51,62}
print(filter_by_digit_sum(nums))
#20
func = lambda d: [k for k,v in sorted(d.items(), key=lambda x:(x[1],len(x[0])))][:3]
d = {
    "apple":5,
    "kiwi":2,
    "banana":2,
    "pear":1,
    "plum":3
}
print(func(d))

print("Lab1 Homework")

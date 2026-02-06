def analyze_text(text):
    vowels="aejouy"
    unique_vowels=set()
    clean=" "
    for ch in text:
        if ch.isalpha():
            clean +=ch.lower
        else:
            clean+=" "
    words=clean.split()
    result=[]
    used=set()
    for w in words:
        for ch in vowels:
            if ch in vowels:
                unique_vowels.add(ch)
        if len(w)>=5 and w[0]==w[-1]:
            if w not in used:
                result.append(w)
                used.add(w)
        return len(unique_vowels)," ".join(result)

#2
task2=lambda s: "" .join(
    filter(
        lambda w:len(w)%2==0,
        map(
            lambda w: w[::-1],
            filter(lambda w: not any(c.isdigit() for c in w),s.split())
        )
    )
)
print(task2("arulljdjnxh"))

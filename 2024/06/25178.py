def sol(s1, s2):
    def first(s1, s2):
        if sorted(s1) == sorted(s2):
            return True
        else:
            return False

    def second(s1, s2):
        if s1[0] == s2[0] and s1[-1] == s2[-1]:
            return True
        else:
            return False

    def third(s1, s2):
        new_s1 = new_s2 = ''
        vowel = 'aeiou'
        for i in s1:
            if i not in vowel:
                new_s1 += i
        for i in s2:
            if i not in vowel:
                new_s2 += i
        if new_s1 == new_s2:
            return True
        else:
            return False

    if first(s1, s2) and second(s1, s2) and third(s1, s2):
        return 'YES'
    else:
        return 'NO'


n = int(input())
s1 = input()
s2 = input()

print(sol(s1, s2))
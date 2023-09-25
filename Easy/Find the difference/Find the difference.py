def findTheDifference(s: str, t: str) -> str:
    if len(s) < len(t):
        for str1, str2 in zip(s, t):
            if str1 != str2:
                return str2
        return t[-1]
    if len(s) > len(t):
        for str1, str2 in zip(s, t):
            if str1 != str2:
                return str1
        return s[-1]


def findTheDifference2(s: str, t: str) -> str:
    if len(s) > len(t):
        for i in s:
            print(i)
            if s.count(i) > t.count(i):
                return i
                break
    if len(t) > len(s):
        for i in t:
            print(i, end=' ')
            print(t.count(i), end=' ')
            print(s.count(i))
            # print(i, end=' ')
            if t.count(i) > s.count(i):
                return i
                break


# this solution was generated by ChatGPT
def findTheDifference3(s: str, t: str) -> str:
    # Initialize dictionaries to store character counts
    s_count = {}
    t_count = {}

    # Count characters in string s
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1

    # Count characters in string t
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Compare character counts to find the added letter
    for char in t_count:
        if char not in s_count or t_count[char] > s_count[char]:
            return char


# My final solution
def findTheDifference4(s: str, t: str) -> str:
    result = 0
    for char in s + t:
        result ^= ord(char)
    return chr(result)


# My final solution
def findTheDifference5(s: str, t: str) -> str:
    return chr(sum(ord(char) for char in t) - sum(ord(char) for char in s))


first_string = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvl" \
               "fwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldp" \
               "rwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxcz" \
               "covrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofnc" \
               "bohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwx" \
               "pqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfh" \
               "tklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqr" \
               "cwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxg" \
               "djwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbx" \
               "oofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"

second_string = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbc" \
                "jhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwes" \
                "axsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqpt" \
                "rmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrk" \
                "eczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkri" \
                "srlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyaw" \
                "vkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluy" \
                "imkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpi" \
                "havligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzj" \
                "aetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"

print(findTheDifference2(first_string, second_string))

print(findTheDifference3(first_string, second_string))

print(findTheDifference4(first_string, second_string))

print(findTheDifference5(first_string, second_string))
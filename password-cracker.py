#!/bin/python3

# https://www.hackerrank.com/challenges/password-cracker

ip ="""10
10
the cake is a lie thec ak ei sal ie
thecakeisaliethecakeisalieakthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieathecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethethecakeisaliethecakeisaliethecakeisaliethecakeisaliethethecakeisalieakthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliesalthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliesalthecakeisaliethecakeisalielieakthecakeisalieliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieakthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieeithecakeisaliethecakeisalieeithecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieiethecakeisaliethecakeisaliethecakeisaliethecakeisalieisthecakeisaliethecakeisalieiscakeakthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieakcakethecakeisaliethecieiethecthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieeithecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieathecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieeithecakeisaliethecakeisaliethecakeisaliethecakeisalieacakethecakeisaliethecakeisaliesalthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalieakthecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisaliethecakeisalie
4
we web adaman barcod
webadaman
5
ends open stop vest love
vestloveendslovevestloveloveloveendslovevestendsopenloveopenstoploveopenendsopenopenstopvestopenloveloveendsvestopenlovevestopenlovestopendsvestveststopendsendsvestendsloveopenendsstopstopstopveststopveststoplovestoplovestopendsvestveststopopenstopveststoploveveststopstopopenvestveststopvestvestopenvestopenlovevestlovevestopenendslovevestvestlovevestvestendsopenopenopenstopopenendsloveopenopenendsstopopenstopstopstopendsendsstopveststoplovestopstopopenloveopenopenloveendsvestendsendsstopopenopenendsendsstopstoploveloveopenvestopenopenopenstopendslovestopendsstopopenopenstopvestloveendsloveveststopstopopenveststopstopvestlovevestendsveststopstopendsendsendslovestopstoplovelovestopopenendsloveloveloveendslovestopstopvestveststopopenvestvestendsvestopenendslovevestvestvestloveloveopenveststopopenendsendslovevestopenloveopenvestlovestoplovestopvestloveendsloveopenvestvestendsendsvestvestopenopenstopvestopenopenloveopenopenstopvestopenlovelovevestendsopenendsopenopenvestopenendsendsstoplovestopopenopenstopopenlovelovestopopenlovestopvestvestlovevestloveloveendsstopveststoplovestoploveloveloveveststopstoplovelovelovevestendslovestopvestvestvestlovelovestopopenveststopendsloveopenveststopopenvestloveendsvestvestvestlovestoploveopenendsendsendsstoploveopenendsvestveststopopenlovelovevestvestloveendsvestendsveststopopenveststopendsstoploveopenendsstoploveopenstopopenendsvestopenopenstopstopstopendsopenstoplovestoploveopenlovestopendsopenloveendsendsopenloveloveendsopenlovestopendsopenopenveststopopenopenloveendsendsopenendsendsopenvestvestendsopenendslovevestendsendsendslovestopendsstopopenendsloveopenvestopenendsloveendsstoplovevestveststopopenstopstopstopstopstopstopopenloveendsopenopenlovevestlovelovevestendsvestendsendslovestopopenvestendsvestlovestopopenopenopenopenendsopenopenopenstopopenopenopenendsstopstopstopendsendslovestopopenopenopenlovevestendsvestendsloveopenopenstoplovevestvestopenvestlovestopendsvestvestopenlovevestopenlovelovestopstopopenvestlovelovestopvest
7
solo love vest stop open ends dsso
solodssoopendssosoloopenendsstopendsvestdssodssostopstopstopopensolovestsolosolosolosolosolosolostoploveopenloveendssoloopenendssolostopopenvestvestlovestopstoplovestopveststopdssodssoendsstopendsvestendslovedssostopopenlovedssosolodssoopenendssoloopenlovestopstopstopsolodssostopdssovestsolovestopendssoopenendsopensolodssovestendslovelovesoloopenendssoloopenloveendsstopvestvestlovesolodssovestvestopenopenstopsolostopstopsolostopdssoveststopsololoveopenlovedssovestlovevestdssoendsendsstopendsvestendsvestlovestopdssoveststopsolovestopendssostopopenopenlovesolovestopendssoopenopenlovesolostoplovelovevestloveendsvestsololovesoloopensolovestopendssoopenopenstopopenendsopenlovevestdssoendsendslovesolostopsololovedssosololoveopenstopopenvestvestopenstopvestdssosolovestsolodssosolostopvestendsopensolodssostopdssoopenstopopenvestopenopensolosolosolodssostopstopendslovelovestopdssoendsendsdssoopenstopvestlovedssostoplovesololovestopopenvestlovestoplovevestsolovestopensololoveopensolovestopendssolovedssostopveststopdssoopensololovevestvestlovestoplovestopsoloendsopensololovevestsolovestopendssovestsololovesoloopensololovelovestopopenendslovesoloopenendssolovestdssostopopenopendssodssoendsopenendsendsopenvestvestsolovestopenlovevestopenendssoloendsstoplovedssoveststopopenopenvestdssoopenopensololoveloveendsopenopenopendssoveststopendsendsstopsolodssosoloopenlovestopsololoveloveloveendssolodssolovestopstopopendssoopensoloopenendssoloendsstopveststopdssoopenendslovevestopenstopdssodssostopendsdssostopendsdssovestdssovestsoloendssolosolosololovestopendsendsvestopendssodssostopendssololoveopenendssolovestlovevestlovesololovesoloveststoplovesoloendsvestveststopdssoendsopenopenendsopensoloopenopenstopsoloopendssostopsoloendsstoploveopenstopendsdssostopstopopendssoendsdssodssolovelovevestendsstoploveendsvestendssolodssosolosolosololovedssolovesolostopsoloendsstopopensolodssoloveloveloveendssolovestlovevestvestdssostopopensolovestopendssostopendsendsdssostopstopveststopendsendsdssoopen
3
aaaaaaaaab aaaaaaaaaa aaaaaaaab
aaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaabbaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabbaaaaaaaabaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabbaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaabbaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabbaaaaaaaaaaaaaaaaaaabbaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaab
5
strong hold stronghold holdhold holdstrong
strongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstrongholdstronghold
9
aba bab ababababab bababababa c d e f g
abababababeabababababbababababaababababababaabababababcfdbabceababababababadeabagecdbabababababababababacdgbababababageeebababababadfabababababdbabeebabbababababaabagbababababababbabbababaffffbababaababababababafbababababaddabacccbabgabababababeabaabababfcdbabebababababaabaebabdabadeababababababababababgabababababbababababababegfeeabaabababccabababababbababababagcegababababababafcgddfababababababafdbabbabdcfcababababababafggababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababddbababababfabacabababababababababababababababffegcabababababdababababab
10
a ab abc abcd abcde bcdef cdef def ef f
cdefabcdefbcdefbcdefbcdefbcdefefabcabcdabdefefcdefabbcdefabcaabcababcdefdefabcabcdabcdfbcdefababcabdefabcabcbcdefdefefacdefabcbcdefabcdefcdefababdefefabcdeabcdefbcdefabbcdefaabcabcdabcefabcabcfabcdefadefabfdeffabcdebcdefabfabccdeffcdefffdefaabcddefefefdefcdefdefbcdefabcfabcdaabcdeacdefaabdefababefababcdecdefabfbcdefabcdabcabcabefcdefabcefabcdeabcdeefefefabcabcdeffababcdabababcabcdedefabcdababcdefefbcdefaefababcdefefababcdeadefadefabcdefabcdeefabccdefadefbcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcabcdabcdefabcdefabccdefcdefbcdefbcdefabcdababcbcdeffabfcdefcdefabcabcdbcdefcdefefabbcdefbcdefaabcdefbcdefabcdefacdefbcdefadefcdeffababcdaefaacdefabcabcdabcfefabbcdefababcdefabcdeffabcababcdefcdefbcdefaaafabcabcbcdeffcdefabcdeaadefabcabcdabcdacdefabcdeababcfaabcabcdecdefabcbcdeffabcabfabcfcdefbcdefabcfbcdefababcdeabbcdefbcdefcdefabcd
10
bb aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaabbaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaabbaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaabaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
4
we web adaman barcod
webarcodwebadamanweb"""
import sys
import time

sys.setrecursionlimit(4000)

# def stringListToCharSet(stringList):
#     res = set()
#     for s in stringList:
#         res.update([c for c in s])
#     return res


# def passwordCracker(pwd, attempt, tracker):
#     global memo
#     if len(attempt) == 0:
#         return tracker
#     if attempt in memo:
#         print("Hello")
#         return []
#     qual_pwd = [x for x in pwd if len(x) <= len(attempt)]
#     attemptCharSet = stringListToCharSet([attempt])
#     qualPwdSet = stringListToCharSet(qual_pwd)
#     if len(attemptCharSet - qualPwdSet) > 0:
#         return []
#     qual_pwd.sort(key=lambda s: len(s), reverse=True)
#     if len(qual_pwd) == 0:
#         return []
#     for p in qual_pwd:
#         if attempt[:len(p)] == p:
#             memo.update(p)
#             res = passwordCracker(qual_pwd, attempt[len(p):], tracker[:]+[p])
#             if res: return res
#     return []


def crack(keys, password):
    res = []
    _crack(password, keys, res)
    print(*res) if len(res) > 0 else print("WRONG PASSWORD")


def _crack(password, keys, res):
    global memo
        
    if len(password) == 0:
        return True

    if password in memo:
        return False
    
    for key in keys:
        if password[:len(key)] == key:
            res.append(key)
            memo[password] = True
            
            if _crack(password[len(key):], keys, res):
                return True

            # remove last element
            del res[-1]

    return False


if __name__ == "__main__":
    # memo = set()
    memo = {}
    if len(sys.argv) > 1:
        ip_lines = ip.split('\n')
        t = int(ip_lines[0])
        for a0 in range(t):
            n = int(ip_lines[1+(a0*3)])
            pwd = ip_lines[2+(a0*3)].strip().split(' ')
            attempt = ip_lines[3+(a0*3)].strip()

            # start = time.time()
            # result = passwordCracker(pwd, attempt, [])
            crack(pwd, attempt)
            # end = time.time()
            # print(end - start)
            # if result:
            #     print(" ".join(result))
            # else:
            #     print("WRONG PASSWORD")
    else:
        t = int(input().strip())
        for a0 in range(t):
            n = int(input().strip())
            pwd = input().strip().split(' ')
            attempt = input().strip()
            crack(pwd, attempt)
            # result = passwordCracker(pwd, attempt, [])
            # if result:
            #     print(" ".join(result))
            # else:
            #     print("WRONG PASSWORD")
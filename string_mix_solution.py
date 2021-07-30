import string
def mix(s1, s2):
    log_dict = {}
    for lwr_chr in string.ascii_lowercase:
        first_val, second_val = s1.count(lwr_chr), s2.count(lwr_chr)
        if max(first_val, second_val) > 1:
            chosen = "1" if first_val > second_val else "2" if second_val > first_val else "="
            log_dict[lwr_chr] = (-max(first_val, second_val), chosen +
                                 ":" + lwr_chr * max(first_val, second_val))
    result = "/".join(log_dict[lwr_chr][1]
                      for lwr_chr in sorted(log_dict, key=lambda x: log_dict[x]))
    print(result)


mix("Are they here", "yes, they are here")
# "2:eeeee/2:yy/=:hh/=:rr"

mix("Sadus:cpms>orqn3zecwGvnznSgacs",
    "MynwdKizfd$lvse+gnbaGydxyXzayp")
# '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
mix("looping is fun but dangerous", "less dangerous than coding")
# "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg
mix(" In many languages", " there's a pair of functions")
# "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
mix("Lords of the Fallen", "gamekult")  # "1:ee/1:ll/1:oo"
mix("codewars", "codewars")  # ""
mix("A generation must confront the looming ",
    "codewarrs")
# "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"

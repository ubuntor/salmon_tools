from zhp import *

# not guaranteed to round-trip when going from serialized->parsed->serialized
# but it should round-trip when going parsed->serialized->parsed

s = open("crisp2.zhp","rb").read()
zhp = ZHP.parse(s)
s2 = zhp.serialize()
s3 = ZHP.parse(s2)
s3 = s3.serialize()
assert s2==s3
open("crisp2_new.zhp","wb").write(s2)

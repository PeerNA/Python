from konlpy.tag import Hannanum
import re

hannanum = Hannanum()

text = input()

nouns_list = hannanum.nouns(text)
kor_nouns = list(set(nouns_list))

eng_str = re.sub(r"[^a-zA-Z\s]", "", text).split()
for i in range(len(eng_str)):
  eng_str[i] = eng_str[i].lower()
eng_nouns = list(set(eng_str))
print(kor_nouns)
print(eng_nouns)
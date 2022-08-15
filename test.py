# import json
import translators as ts

#
# di = {}
#
# keys = ['start', 'stop', 'folder', 'history', 'settings', 'exit']
# dicts = ['Start', 'Stop', 'Open destination folder', 'History', 'Settings', 'Exit']
#
# di['en'] = dict(zip(keys, dicts))
# lang = ['AR', 'ru', 'uz', 'zh', 'de', 'fr', 'uk', 'BE', 'DA', 'ES', 'ET', 'FI', 'GA', 'HE', 'HI', 'IT', 'JA', 'KO', 'PL']
#
# for i in lang:
#     tm = []
#     try:
#         for j in dicts:
#             tm.append(ts.google(j, from_language='en', to_language=i.lower()))
#         di[i] = dict(zip(keys, tm))
#         print(di[i])
#     except:
#         pass
#
# w = open('language.json', 'w', encoding='utf-8')
# json.dump(di, w, ensure_ascii=False, indent=4)
# print(di)
lang = ['AR', 'ru', 'uz', 'zh', 'de', 'fr', 'uk', 'BE', 'DA', 'ES', 'ET', 'FI', 'GA', 'HE', 'HI', 'IT', 'JA', 'KO',
        'PL']

from iso639 import Lang

s = ""

for i in lang:
    try:
        s += f"#{i.lower()} - {ts.google(Lang(i.lower()).name, from_language='en', to_language=i.lower())}\n"
    except:
        pass
print(s)
"""
#ar - عربي
#ru - Русский
#uz - O'zbek tili
#zh - 中国人
#de - Deutsch
#fr - Français
#uk - Український
#be - Беларускі
#da - dansk
#es - Española Español
#et - Eestonian
#fi - Suomalainen
#ga - Gaeilge
#hi - हिन्दी
#it - Italiana Italiano
#ja - 日本
#ko - 한국인
#pl - Polski

"""
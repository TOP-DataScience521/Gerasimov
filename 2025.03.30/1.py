high_domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ಭಾರತ', '한국', 'ଭାରତ', 'ভাৰত', 'ভারত', 'ישראל', 'বাংলা', 'қаз', 'срб', 'бг', 'бел', 'சிங்கப்பூர்', 'мкд', 'ею', '中国', '中國', 'భారత్', 'ලංකා', 'ભારત', 'भारतम्', 'भारत', 'भारोत', 'укр', '香港', '台湾', '台灣', 'мон', 'الجزائر', 'عمان', 'ایران', 'امارات', 'موريتانيا', 'پاکستان', 'الاردن', 'بارت', 'بھارت', 'المغرب', 'البحرين', 'السعودية', 'ڀارت', 'سودان', 'عراق', 'مليسيا', '澳門', 'გე', 'ไทย', 'سورية', 'рф', 'تونس', 'ລາວ', 'ευ', 'ελ', 'ഭാരതം', 'ਭਾਰਤ', 'مصر', 'قطر', 'இலங்கை', 'இந்தியா', 'հայ', '新加坡', 'فلسطين', 'ye', 'yt', 'za', 'zm', 'zw']


email = input('Введите почту: ')


if '@' in email and '.' in email: # наличие точки и @
    part_1 = email.split('@')
    if len(part_1) == 2:  # проверяем наличие @
        part_2 = part_1[1].split('.')  # разбивка
        if len(part_2) >= 2:  # ищем точки
            tld = part_2[-1]  # берем 1 с конца
            if tld in high_domains: # наличие домена
                print('да')
            else:
                print('нет') # домена нету
        else:
            print('нет')  # нет точки
    else:
        print('нет')  # если нет или больше 2 @
else:
    print('нет')  # нет @ или точки


# Введите почту: asdad@jfjf.ru
# да

# Введите почту: gasgyya.ujsj@casc
# нет
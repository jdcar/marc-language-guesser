from guess_language import guess_language
from pymarc import MARCReader
from pymarc import Record, Field
import re


with open('\\\\library.northwestern.edu\cab\StaffDocs\jcs8769\Documents\ACPDB\\updated-language-country\\newsreview'
          '-from-alma-mrk-edited.mrk',
          'rb') as fh:

    reader = MARCReader(fh)
    for record in reader:

        langMarcCodeTranslate = {'ab': 'abk', 'aa': 'aar', 'af': 'afr', 'ak': 'aka', 'sq': 'alb', 'am': 'amh',
                                 'ar': 'ara', 'an': 'arg', 'hy': 'arm', 'as': 'asm', 'av': 'ava', 'ae': 'ave',
                                 'ay': 'aym', 'az': 'aze', 'bm': 'bam', 'ba': 'bak', 'eu': 'baq', 'be': 'bel',
                                 'bn': 'ben', 'bh': 'bih', 'bi': 'bis', 'bs': 'bos', 'br': 'bre', 'bg': 'bul',
                                 'my': 'bur', 'ca': 'cat', 'ch': 'cha', 'ce': 'che', 'ny': 'nya', 'zh': 'chi',
                                 'cv': 'chv', 'kw': 'cor', 'co': 'cos', 'cr': 'cre', 'hr': 'hrv', 'cs': 'cze',
                                 'da': 'dan', 'dv': 'div', 'nl': 'dut', 'dz': 'dzo', 'en': 'eng', 'eo': 'epo',
                                 'et': 'est', 'ee': 'ewe', 'fo': 'fao', 'fj': 'fij', 'fi': 'fin', 'fr': 'fre',
                                 'ff': 'ful', 'gl': 'glg', 'ka': 'geo', 'de': 'ger', 'el': 'gre', 'gn': 'grn',
                                 'gu': 'guj', 'ht': 'hat', 'ha': 'hau', 'he': 'heb', 'hz': 'her', 'hi': 'hin',
                                 'ho': 'hmo', 'hu': 'hun', 'ia': 'ina', 'id': 'ind', 'ie': 'ile', 'ga': 'gle',
                                 'ig': 'ibo', 'ik': 'ipk', 'io': 'ido', 'is': 'ice', 'it': 'ita', 'iu': 'iku',
                                 'ja': 'jpn', 'jv': 'jav', 'kl': 'kal', 'kn': 'kan', 'kr': 'kau', 'ks': 'kas',
                                 'kk': 'kaz', 'km': 'khm', 'ki': 'kik', 'rw': 'kin', 'ky': 'kir', 'kv': 'kom',
                                 'kg': 'kon', 'ko': 'kor', 'ku': 'kur', 'kj': 'kua', 'la': 'lat', 'lb': 'ltz',
                                 'lg': 'lug', 'li': 'lim', 'ln': 'lin', 'lo': 'lao', 'lt': 'lit', 'lu': 'lub',
                                 'lv': 'lav', 'gv': 'glv', 'mk': 'mac', 'mg': 'mlg', 'ms': 'may', 'ml': 'mal',
                                 'mt': 'mlt', 'mi': 'mao', 'mr': 'mar', 'mh': 'mah', 'mn': 'mon', 'na': 'nau',
                                 'nv': 'nav', 'nd': 'nde', 'ne': 'nep', 'ng': 'ndo', 'nb': 'nob', 'nn': 'nno',
                                 'no': 'nor', 'ii': 'iii', 'nr': 'nbl', 'oc': 'oci', 'oj': 'oji', 'cu': 'chu',
                                 'om': 'orm', 'or': 'ori', 'os': 'oss', 'pa': 'pan', 'pi': 'pli', 'fa': 'per',
                                 'pl': 'pol', 'ps': 'pus', 'pt': 'por', 'qu': 'que', 'rm': 'roh', 'rn': 'run',
                                 'ro': 'rum', 'ru': 'rus', 'sa': 'san', 'sc': 'srd', 'sd': 'snd', 'se': 'sme',
                                 'sm': 'smo', 'sg': 'sag', 'sr': 'srp', 'gd': 'gla', 'sn': 'sna', 'si': 'sin',
                                 'sk': 'slo', 'sl': 'slv', 'so': 'som', 'st': 'sot', 'es': 'spa', 'su': 'sun',
                                 'sw': 'swa', 'ss': 'ssw', 'sv': 'swe', 'ta': 'tam', 'te': 'tel', 'tg': 'tgk',
                                 'th': 'tha', 'ti': 'tir', 'bo': 'tib', 'tk': 'tuk', 'tl': 'tgl', 'tn': 'tsn',
                                 'to': 'ton', 'tr': 'tur', 'ts': 'tso', 'tt': 'tat', 'tw': 'twi', 'ty': 'tah',
                                 'ug': 'uig', 'uk': 'ukr', 'ur': 'urd', 'uz': 'uzb', 've': 'ven', 'vi': 'vie',
                                 'vo': 'vol', 'wa': 'wln', 'cy': 'wel', 'wo': 'wol', 'fy': 'fry', 'xh': 'xho',
                                 'yi': 'yid', 'yo': 'yor', 'za': 'zha', 'zu': 'zul'}

        mmsid = re.sub("=001  ", "", str(record['001']))

        # 008 work
        fixedfield = str(record['008'])


        longtitle = str(record["245"]["a"]) + " " + str(record["740"])
                    # + " " + str(record["245"]["b"]) + " " + str(record["740"]["a"])

        longtitle2 = re.sub("[\[\]\/\#\!\$\%\^\&\*\;\:\{\}\=_\`\~\(\)]", "", longtitle)

        longtitle3 = re.sub("None", " ", longtitle2)

        longtitle4 = re.sub("  ", ". ", longtitle3)

        languageguess = guess_language(longtitle4)

        languagemarc = re.sub(r"(^.{41})(...)(.+)", r"\2", str(record["008"]))

        if languagemarc == "|||" or languagemarc == "und":

            if languageguess in langMarcCodeTranslate:

                newFixedField = re.sub(r'(=008  .{35})(...)(..)', r'\1{}\3'.format(langMarcCodeTranslate[languageguess]), fixedfield)


                print (mmsid, ";", newFixedField)


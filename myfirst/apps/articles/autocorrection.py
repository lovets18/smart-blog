from django.conf import settings
import re

def correct(word):
    "Поиск лучшего исправления ошибки для данного слова."
    # предрассчитать edit_distance==0, затем 1, затем 2; в противном случае оставить слово "как есть".
    candidates = (known(edit_dist_0(word)) or
                  known(edit_dist_1(word)) or
                  known(edit_dist_2(word)) or
                  [word])
    return max(candidates, key=settings.COUNTS.get)

def known(words):
    "Вернуть подмножество слов, которое есть в нашем словаре."
    return {w for w in words if w in settings.COUNTS}

def edit_dist_0(word):
    "Вернуть все строки, которые находятся на edit_distance == 0 от word (т.е., просто само слово)."
    return {word}

def edit_dist_2(word):
    "Вернуть все строки, которые находятся на edit_distance == 2 от word."
    return {e2 for e1 in edit_dist_1(word) for e2 in edit_dist_1(e1)}


def edit_dist_1(word):
    "Возвращает список всех строк на расстоянии edit_distance == 1 от word."
    pairs      = splits(word)
    deletes    = [a+b[1:]           for (a, b) in pairs if b]
    transposes = [a+b[1]+b[0]+b[2:] for (a, b) in pairs if len(b) > 1]
    replaces   = [a+c+b[1:]         for (a, b) in pairs for c in settings.ALPHABET if b]
    inserts    = [a+c+b             for (a, b) in pairs for c in settings.ALPHABET]
    return set(deletes + transposes + replaces + inserts)

def splits(word):
    "Возвращает список всех возможных разбиений слова на пары (a, b)."
    return [(word[:i], word[i:]) for i in range(len(word)+1)]


def correct_text(text):
    "Исправить все слова с опечатками в тексте."
    return re.sub('[a-zA-Z]+', correct_match, text)


def correct_match(match):
    "Исправить слово word в match-группе, сохранив регистр: upper/lower/title."
    word = match.group()
    return case_of(word)(correct(word.lower()))


def case_of(text):
    "Возвращает функцию регистра по тексту: upper, lower, title, или str."
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.title if text.istitle() else
            str)

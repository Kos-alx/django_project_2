from django import template


register = template.Library()

obscene_words = [
    'дурак',
    'урод',
    'дебил',
    'тварь'
]

@register.filter()
def censor(value: str):
    txt = value.split()
    count = 0
    for i in txt:
        for word in obscene_words:
            if word in i.lower():
                cen = '*' * len(i)
                txt[count] = cen
        count += 1
    return ' '.join(txt)


def single_root_words(root_word, *other_words):
    same_words = []
    for x in other_words:
        a = list(other_words)
        a.remove(x)
        a.insert(0, x.lower())
        if (root_word.lower() in a[0]) or (a[0] in root_word.lower()):
            same_words.insert(0, x.lower())
    return print(same_words)

single_root_words('DisaBlement', 'AbLe', 'MAble', 'DiSable', 'BaGel')
single_root_words('riCh', 'ricHiest', 'orIchalcum', 'cheErs', 'Richies')

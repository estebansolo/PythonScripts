from collections import Counter


def is_anagram(word_a, word_b):
    if len(word_a) != len(word_b):
        return False

    return Counter(word_a) == Counter(word_b)


def search_anagrams(text):
    processed_keys, anagrams = [], []
    for main_key, main_word in enumerate(text):
        for new_key, new_word in enumerate(text):
            if main_key == new_key or new_key in processed_keys:
                continue

            if is_anagram(main_word, new_word):
                processed_keys += [main_key, new_key]
                anagrams.append(main_word)
                break

    return sorted(anagrams)


anagrams = [
    ["qwerty", "anagram", "aaangrm", "treyqw"],
    ["search", "teerh", "chears", "three"],
]

expected = [["anagram", "qwerty"], ["search", "teerh"]]

assert search_anagrams(anagrams[0]) == expected[0], f"Expected {', '.join(expected[0])}"
assert search_anagrams(anagrams[1]) == expected[1], f"Expected {', '.join(expected[1])}"


import re


def get_words_statistic(text):
    frequency = {}
    match_pattern = re.findall(r'\b[a-zA-Z]+\b', text)
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    return frequency

if __name__ == '__main__':
    print(get_words_statistic('asdfasdf'))
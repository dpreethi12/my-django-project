from collections import Counter
import heapq

def get_top_10_paragraphs(paragraphs, search_word):
    search_word = search_word.lower()
    result = []
    
    for para in paragraphs:
        words = para.lower().split()
        word_freq = Counter(words)
        freq = word_freq.get(search_word, 0)
        if freq > 0:
            result.append((freq, para))
    
    top_10 = heapq.nlargest(10, result, key=lambda x: x[0])
    return [para for freq, para in top_10]

from heapq import heappush, heappop, heapify
from collections import defaultdict

def readText(fname):
    txt = open(fname).read()
    nodes = defaultdict(int)
    for ch in txt:
        nodes[ch] += 1
    return nodes

def readText2(fname):
    txt = open(fname).read()
    nodes = defaultdict(int)
    for ch in txt:
        nodes[ch] = 1
    return nodes

def create_huffman(nodes):
    heap = [[wt, [sym, ""]] for sym, wt in nodes.items()]
    heapify(heap)
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def encode(huff, text):
    dict = {a[0]:a[1] for a in huff}
    text_encoded = ""
    for char in text:
        text_encoded += dict[char]
    return text_encoded

def decode(huff, text_encoded):
    dict = {a[1]:a[0] for a in huff}
    text = ""
    current_code = ""
    for c in text_encoded:
        current_code += c
        if current_code in dict:
            text += dict[current_code]
            current_code = ""
    return text

huff = create_huffman(readText2('text'))


print encode(huff, 'this is a test')
print len(encode(huff, open('text').read()))
print decode(huff, encode(huff, 'this is a test'))

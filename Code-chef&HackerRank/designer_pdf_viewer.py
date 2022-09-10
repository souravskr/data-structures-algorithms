def designer_pdf_viewer(h, word):
    word_size = len(word)
    height = 0
    for c in word:
        char_height = h[ord(c) - 97]
        if char_height >= height:
            height = char_height
    return height * word_size


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word ='abc'
print(designer_pdf_viewer(h, word))

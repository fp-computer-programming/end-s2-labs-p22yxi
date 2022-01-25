# Yongdong Xi
def removeConsecutiveDuplicates(sentence):
    p=""
    # A new string is used as the sentence after the repeated characters are removed
    for s in sentence:
        #Confirm whether the elements in the sentence have appeared
        if s not in p:
            p += s
    print(p)
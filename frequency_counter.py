from collections import Counter
import re

def freq_counter(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b',text)
    frequency=Counter(words)
    return frequency

if __name__=="__main__":
    text = input("Enter Text: ")
    frequency = freq_counter(text)
    for word,count in frequency.items():
        print (f"{word}:{count}")

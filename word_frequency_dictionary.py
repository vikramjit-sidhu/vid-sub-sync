import re

"""
  Takes a list as input and creates a dictionary with word - frequency.
  The dictionary is sorted on the basis of the most frequent word first
  Only words with a frequency of 2 or more are considered, the rest are 
  later discarded
"""


def create_freq_dictionary (listfiles):
  """
    This function creates word_freq which is the dictionary required
  """
  word_freq = {}
  
  for filename in listfiles:
    filename = filename [:filename.find ('.')]
    words = re.findall (r'([a-zA-Z0-9]+)', filename)
    
    for word in words:
      if word not in word_freq:
        word_freq [word] = 1
      else:
        word_freq [word] += 1
  
  
  word_freq = {k:v for k,v in word_freq.items () if v >= 2}
    
  return (word_freq)


def main ():
  return

if __name__ == '__main__':
  main ()
  
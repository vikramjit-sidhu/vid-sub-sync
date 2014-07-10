"""
  Changes the subtitle names to match the names of the video
  file corresponding to it
"""

import os
import re

def change_subname_tovideo (vidsubdict):
  """
    The method that takes as input the dictionary matching
    the videos to the corresponding subtitles, it then changes
    the subtitle name to match the video name
  """
  for vid, sub in vidsubdict.items ():
    ext = re.search (r'\.(\w+)', sub)
    vid = vid + '.' + ext.group (1)

    if vid != sub:
      os.rename (sub, vid)

  return



def main ():
  
  return
  

if __name__ ==  '__main__':
  main ()
  
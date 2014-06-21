import glob
import os
import re

"""
Given a list of the video files, finds the best subtitle match for it
in the given folder, forms a dictionary of video-subtitle pair
"""

list_sub_formats = ['srt', 'sub', 'txt']



def take_video_list ():
  """
    Takes a file path as input and creates a list of videos calling the function
    to map it to the subtitles. This function is purely for testing
  """
  #filename = input ('enter the file path where the video list can be found: ')  
  
  #file = open (filename, 'r')
  file = open ('list.txt', 'r')
  listvids = file.readlines ()  
  file.close ()
  
  #dirpath = input ('enter the directory to search for subtitles in')
  #os.chdir (dirpath)
  os.chdir ("C:\\Users\\vikram\\Downloads\\video lectures\\Computer Networks_University of Washington")
  
  match_subs (listvids)
  
  return


def match_subs (listvids):
  """
    Takes as input the list of all videos, matches the relevant subtitle to
    it, displaying the video and the match in the end for the user to approve
  """
  for video in listvids:
    
  
  

  return



def main ():
  take_video_list ()

  return


if __name__ == '__main__':
  main ()
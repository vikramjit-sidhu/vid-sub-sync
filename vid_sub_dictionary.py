"""
Given a list of the video files, finds the best subtitle match for it
in the given folder, forms a dictionary of video-subtitle pair
"""


import glob
import os
import re
import word_frequency_dictionary
import change_sub_name



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
  
  match_subs (listvids, [], 1)
  
  return


def match_subs (listvids, exclusionlist, iteration):
  """
    Takes as input the list of all videos, matches the relevant subtitle to
    it, displaying the video and the match in the end for the user to approve
  """
  if iteration == 5:
    return
  
  word_freq_dict = word_frequency_dictionary.create_freq_dictionary (listvids)
  
  video_sub_dict = {}
  sub_not_found = []
  
  for vidnameext in listvids:
    vidname = vidnameext [:vidnameext.find ('.')]
    vid_words = re.findall (r'([a-zA-Z0-9]+)', vidname)
    
    unique_words = []
    for word in vid_words:
      if word not in word_freq_dict:
        unique_words.append (word)
    
    search_str = ''
    found = False

    for word in unique_words:
      wordsearch = '*' + word + '*' + '[st][urx][tb]'
      listsubs = glob.glob (wordsearch)
      
      listsubs = [sub for sub in listsubs if sub not in exclusionlist]
      
      if len (listsubs) == 1:
        video_sub_dict [vidname] = listsubs[0]
        found = True
        break
      else:
        if search_str:
          search_str = search_str + word + '*'
          wordsearch = search_str + '[st][urx][tb]'
          listsubs = glob.glob (wordsearch)
          if len (listsubs) == 1:
            video_sub_dict [vidname] = listsubs[0]
            found = True
            break
        else:
          search_str = '*' + word + '*'

    
    if not found:
      sub_not_found.append (vidnameext)

  

  
#  for video, sub in video_sub_dict.items ():
    #print ('\n' + video + ' ==> ' + sub)

  #call program to change sub names
  change_sub_name.change_subname_tovideo (video_sub_dict)
  
  exclusionlist += video_sub_dict.values ()
  match_subs (sub_not_found, exclusionlist, iteration + 1)
  
  return



def main ():
  take_video_list ()

  return


if __name__ == '__main__':
  main ()
import sys
import os
import re
import glob
import check_windows
import vid_sub_dictionary

"""
Scans a folder and checks the various subtitle and video files in it.
Checks for minor differences in the subtitle and video files and changes
the subtitle file correspondingly to reflect the video file
"""

list_vid_formats = ['aaf', '3gp', 'asf', 'avchd', 'avi', 'dat', 'flv', 'fla', 'flr', 'sol', 'm4v', 'mkv', 'mov', 'mp4' ,'mpeg', 'mpg', 'mpe', 'wmv']



def take_dirpath ():
  """
    Takes user input of the directory path where the sub and vid files
    are skewed
  """
  
  print ('Enter the directory path where your video and subtitle files are not in synch')
  dirpath = input ('directory: ')
  
  get_video_list (dirpath)  


def get_video_list (dirpath):
  """
    Takes the dirpath and switches to that directory if it is valid.
    From the acceptable file formats, searches the dir and obtains 
    a list of video files which is passed on for further processing
  """
  
  if not os.path.exists (dirpath):
    print ('not a valid directory name given')
    take_dirpath ()
    
  os.chdir (dirpath)
   
  vid_formats_used ()
  
  listvids = []
  for format in list_vid_formats:
    listvids = listvids + glob.glob ('*.' + format)

  if not listvids:
    print ('there were no files found')
    newext = input ('do you want to continue, y/n?: ')
    while newext.lower() not in ['y', 'n']:
      print ('you have entered an invalid option')
      newext = input ('do you want to continue, y/n?: ')
    if newext.lower() == 'y':
      take_dirpath ()
      
  #create_vid_txtfile (listvids)
  
  return


def vid_formats_used ():
  """
    Informs the user of the various video file formats being searched for,
    the user is given the option to add another format
  """
  modified = False
  
  print ('\nThe following video formats are being searched for:')
  for ext in list_vid_formats:
    print (ext)
  
  addfmt = input ('\ndo you want to add any additional format? y/n: ')
  while addfmt.lower() not in ['y', 'n']:
    print ('you have entered an incorrect option')
    addfmt = input ('any other format, y/n?: ')
  
  if addfmt.lower () == 'y':
    modified = True
    userfmt = input ('enter an additional format, "exit" to finish:')
    while userfmt.lower () != 'exit':
      userfmt = re.search (r'([\w]+)', userfmt.lower())
      list_vid_formats.append (userfmt.group (1))
      userfmt = input ('enter an additional format, "exit" to finish:')
  else:
    return
      
  if modified:
    print ('\nso finally we are searching for the following formats:')
    for ext in list_vid_formats:
      print (ext)
      
  return

  
def create_vid_txtfile (listvids):
  
  file = open ('list.txt', 'w')
  
  for video in listvids:
    file.write (video + '\n')
    
  file.close ()

  return



def main ():
  if not check_windows.main ():
    print ('your os is not supported as yet')
    sys.exit (0)

  args = sys.argv [1:]  
  if not args:
    take_dirpath ()
  else:  
    get_video_list (args[0])
  
  return

if __name__ == '__main__':
  main ()
  
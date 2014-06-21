"""
Check which version of os is currently running in environment
Returns a lower case version of OS
eg: 'windows', 'linux'
"""
import platform

def main ():
  os = platform.system ()  
  if os.lower () == 'windows':
    return True
  else:
    return False
    
      

if __name__ == '__main__':
  main ()
  
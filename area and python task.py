//Task1: Python program which accepts the radius of a circle from the user and computes area.
from math import pi
r=float(input("Input the radius of the circle:"))
calculateArea=str(pi*r**2)
print("The area of the circle with radius"+str(r)+"is:"+calculateArea)

//Task2:Python program to accept a filename from the user and print the extension of that.
def fun():
  ext_dict = {'.py':'python',
              '.bat':'PC batch file',
              '.bin':'Binary compressed file',
              '.csv':'Comma-separated values fil',
              '.dll':'Dynamic Link Library file',
              '.doc':'Microsoft Word document before Word 2007',
              '.docm':'Microsoft Word macro-enabled document',
              '.docx':'Microsoft Word document',
              '.exe':'Executable program file',
              '.htm':'Hypertext markup language page',
              '.html':'Hypertext markup language page',
              '.iso':'ISO-9660 disc image',
              '.jpg':'Joint Photographic Experts Group photo file',
              '.jpeg':'Joint Photographic Experts Group photo file',
              '.mp3':'MPEG layer 3 audio file',
              '.mp4':'MPEG 4 video',
              '.msi':'Microsoft installer file',
              '.pdf':'Portable Document Format file',
              '.png':'Portable Network Graphics file',
              '.ppt':'Microsoft PowerPoint format before PowerPoint 2007',
              '.pptx':'Microsoft PowerPoint presentation',
              '.rar':'Roshal Archive compressed file',
              '.txt':'Unformatted text file',
              '.zip':'Compressed file',
              '.xps':'XML-based document',
              '.xltx':'Microsoft Excel template after Excel 2007'}
  f_name = input()
  if f_name.count('.') > 1:
    print('please enter a correct file name')
  else:
    indx = f_name.index('.')
    sl_w = f_name[indx:]
    # print(sl_w)
    if sl_w in ext_dict:
      print(ext_dict[sl_w])
    else:
      print('please enter a correct file name')
fun()

import os

for (dirpath, dirnames, filenames) in os.walk('media/'):
  print(dirpath)
  for re_dirpath in dirnames:
    print(f'\t{re_dirpath}')
  for re_filespath in filenames:
    print(f'\t{re_filespath}')
  print()

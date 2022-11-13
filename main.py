from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import os.path

## Global variables ##
URL = 'https://propedeutico-nektagt.github.io/CDN/'


#print(os.path.dirname(__file__))

## Jinja template ##
env = Environment(
  loader = FileSystemLoader("./templates/"),
  autoescape = select_autoescape()
)
template = env.get_template("template.html")

#print(template.render())

## Main thread ##
for (dirpath, dirnames, filenames) in os.walk('media/'):
  print(f"{dirpath}\n")
  for re_dirpath in dirnames:
    print(f'\t{re_dirpath}')
  for re_filespath in filenames:
    print(f'{URL}{dirpath}/{re_filespath}')
  print()

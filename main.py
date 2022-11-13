from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import os
import os.path

## Global variables ##
URL = 'https://propedeutico-nektagt.github.io/CDN/'
CWD = os.getcwd()
STYLE = 'https://propedeutico-nektagt.github.io/CDN/templates/style.css'

## Jinja template ##
env = Environment(
  loader = FileSystemLoader("./templates/"),
  autoescape = select_autoescape()
)
env.globals['getmtime'] = lambda z: datetime.fromtimestamp(os.path.getmtime(z))
env.globals['getsize'] = os.path.getsize
env.globals['toURLd'] = lambda d: URL + os.path.join(d)
env.globals['toURLf'] = lambda d,f: URL + os.path.join(d,f)
template = env.get_template("template.html")

## Main thread ##
for (dirpath, dirnames, filenames) in os.walk('media/'):
  print(dirpath)
  path = os.path.join(CWD,dirpath)
  os.chdir(path)
  with open('index.html', 'w') as html_f:
    html_f.write(template.render(
      style = STYLE,
      dirpath = dirpath,
      dirnames = dirnames,
      filenames = filenames
    ))
  print(dirnames)
  print(filenames)
  print()
  os.chdir(CWD)

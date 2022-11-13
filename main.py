from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import os.path

## Global variables ##
URL = 'https://propedeutico-nektagt.github.io/CDN/'
CWD = os.getcwd()
STYLE = os.path.join(CWD,'templates','style.css')

## Jinja template ##
env = Environment(
  loader = FileSystemLoader("./templates/"),
  autoescape = select_autoescape()
)
template = env.get_template("template.html")

## Main thread ##
for (dirpath, dirnames, filenames) in os.walk('media/'):
  path = os.path.join(CWD,dirpath)
  os.chdir(path)
  with open('index.html', 'w') as html_f:
    html_f.write(template.render(
      style = STYLE,
      dirnames = dirnames
    ))

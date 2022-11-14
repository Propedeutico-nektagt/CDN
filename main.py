from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import os
import os.path

## Extensions ##
def get_icon_ext(file):
  dictext = {
    '.aif':'fa-file-audio', '.mp3':'fa-file-audio', '.wav':'fa-file-audio',
    '.wpl':'fa-file-audio', '.rar':'fa-file-zipper', '.deb':'fa-file-zipper',
    '.pkg':'fa-file-zipper', '.z':'fa-file-zipper', '.zip':'fa-file-zipper',
    '.csv':'fa-floppy-disk', '.tsv':'fa-floppy-disk', '.dat':'fa-floppy-disk',
    '.db':'fa-floppy-disk', '.log':'fa-floppy-disk', '.sql':'fa-floppy-disk',
    '.tar':'fa-floppy-disk', '.xml':'fa-floppy-disk', '.py':'fa-file-code',
    '.nb':'fa-file-code', '.c':'fa-file-code', '.pl':'fa-file-code',
    '.class':'fa-file-code', '.cpp':'fa-file-code', '.h':'fa-file-code',
    '.php':'fa-file-code', '.sh':'fa-file-code', '.swift':'fa-file-code',
    '.r':'fa-file-code', '.html':'fa-file-code', '.css':'fa-file-code',
    '.js':'fa-file-code', '.tex':'fa-file-code', '.cls':'fa-file-code',
    '.sty':'fa-file-code', '.toml':'fa-file-code', '.yaml':'fa-file-code',
    '.bmp':'fa-file-image', '.gif':'fa-file-image', '.ico':'fa-file-image',
    '.jpg':'fa-file-image', '.jpeg':'fa-file-image', '.png':'fa-file-image',
    '.ps':'fa-file-image', '.svg':'fa-file-image', '.tiff':'fa-file-image',
    '.avi':'fa-file-video', '.mov':'fa-file-video', '.mp4':'fa-file-video',
    '.wmv':'fa-file-video', '.mpg':'fa-file-video', '.mpeg':'fa-file-video',
    '.doc':'fa-file-word', '.docx':'fa-file-word', '.odt':'fa-file-word',
    '.pdf':'fa-file-pdf', '.pdfa':'fa-file-pdf', '.pdfx':'fa-file-pdf',
    '.xlsx':'fa-file-excel', '.xls':'fa-file-excel', '.xml':'fa-file-excel',
    '.xlsm':'fa-file-excel', '.pptx':'fa-file-powerpoint', '.pptm':'fa-file-powerpoint',
    '.ppt':'fa-file-powerpoint'
  }
  name, ext = os.path.splitext(file)
  return dictext.get(ext,'fa-file')

## Global variables ##
URL = 'https://propedeutico-nektagt.github.io/CDN/'
CWD = os.getcwd()
STYLE = 'https://propedeutico-nektagt.github.io/CDN/templates/style.css'

## Jinja template ##
env = Environment(
  loader = FileSystemLoader("./templates/"),
  autoescape = select_autoescape()
)
env.globals['gicon'] = get_icon_ext
env.globals['getmtime'] = lambda z: datetime.fromtimestamp(os.path.getmtime(z))
env.globals['getsize'] = os.path.getsize
env.globals['toURLd'] = lambda d: URL + d
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

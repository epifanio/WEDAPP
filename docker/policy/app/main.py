
from jinja2 import Environment, FileSystemLoader
import panel as pn
pn.extension()



env = Environment(loader=FileSystemLoader('/app/static'))
jinja_template = env.get_template('template.html')
tmpl = pn.Template(jinja_template)

tmpl.add_panel('A', pn.Column(pn.pane.HTML('<center><h3>♥ ♥ ♥</h3></center>')))
tmpl.add_variable('app_title', '<center><h1>♥ Geno & Massi Sposi! ♥</h1></center>')
tmpl.servable('Geno & Massi Sposi!')
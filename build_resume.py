import yaml
from jinja2 import Environment, FileSystemLoader

with open("resume.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("resume.tex.j2")
rendered = template.render(**data)

with open("resume.tex", "w", encoding="utf-8") as f:
    f.write(rendered)

print("Generated resume.tex")

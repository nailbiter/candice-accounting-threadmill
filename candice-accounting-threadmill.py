#!/usr/bin/env python3
"""===============================================================================

        FILE: candice-accounting-threadmill.py

       USAGE: ./candice-accounting-threadmill.py

 DESCRIPTION: 

     OPTIONS: ---
REQUIREMENTS: ---
        BUGS: ---
       NOTES: ---
      AUTHOR: Alex Leontiev (alozz1991@gmail.com)
ORGANIZATION: 
     VERSION: ---
     CREATED: 2021-05-08T18:02:12.485922
    REVISION: ---

==============================================================================="""

from flask import Flask, request
from jinja2 import Template, Environment
from jinja2.loaders import FileSystemLoader
import markdown
import _common
from os import path

app = Flask(__name__)


def _get_env():
    return Environment(loader=FileSystemLoader("templates"))


@app.route("/grade/<path:question>")
def grade(question):
    fn = path.join("data/right_answers", question+".txt")
    if not path.isfile(fn):
        return f"no answer \"{question}\""
    with open(fn) as f:
        right_answers = f.read().strip()
    right_answers = [line.strip() for line in right_answers.split("\n")]
    print(right_answers)
    print(f"{len(right_answers)} right answers")
    wrong_items = []
    for i, a in enumerate(right_answers):
        got, expected = str(request.args.get(str(i+1))), str(a)
        if got != expected:
            wrong_items.append((i+1, got, expected))
    return "right" if len(wrong_items) == 0 else "<br>".join([f"wrong ({len(wrong_items)}/{len(right_answers)}={len(wrong_items)/len(right_answers)*100:.2f}%)", *[f"{i}: \"{got}\" != \"{expected}\"" for i, got, expected in wrong_items]])


@app.route('/')
@app.route('/<path:question>')
def hello_world(question="1"):
    fn = path.join("templates", question+".jinja.md")
    if not path.isfile(fn):
        return f"no question \"{question}\""
    with open(fn) as f:
        md = f.read()
#    jinja_env = _get_env()
#    md = jinja_env.get_template("question.jinja.md")
#    md_converter = markdown.Markdown(extension=["tables"])
#    html = md_converter.convert(md)
    html = markdown.markdown(md, extensions=["tables"])
#    print(html)
    input_ = _common.Input()
    html = Template(html).render({
        "html": {
            "input": input_.input,
            "dropdown": input_.dropdown,
        }
    })
    return f"""
    <form action="grade/{question}">
    <!--form action="cgi-bin/formmail.cgi" method="post"-->
    {html}
    <input type="submit" value="送信">
    <!--input type="reset" value="リセット"-->
    </form>
    """

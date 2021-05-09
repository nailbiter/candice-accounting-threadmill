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

app = Flask(__name__)


def _get_env():
    return Environment(loader=FileSystemLoader("templates"))


@app.route("/grade")
def grade():
    _RIGHT_ANSWER = [
        "X2/8/31",
        "普通",
        "28,800",
        "X2/4/1",
        "未払利息",
        "16,800",
        *"X3/2/28 普通預金 30,000 X3/3/31 損益 47,000".split(" "),
        *"X3/3/31 未払利息 5.000".split(" "),
        *(["63,800"]*2),
        "未払",
        *"X2/4/1 支払利息 16,.800 X2/4/1 前期 繰越 16.800".split(" "),
        *"X3/3/31 次期繰越 5.000 X3/3/31 支払利息 5,000".split(" "),
        *(["21,800"]*2),
    ]
    wrong_items = []
    for i, a in enumerate(_RIGHT_ANSWER):
        got,expected = str(request.args.get(str(i))), str(a)
        if got != expected:
            wrong_items.append((i+1,got,expected))
    return "right" if len(wrong_items)==0 else "<br>".join(["wrong",*[f"{i}: \"{got}\" != \"{expected}\"" for i,got,expected in wrong_items]])


@app.route('/')
def hello_world():
    with open("templates/question.jinja.md") as f:
        md = f.read()
#    jinja_env = _get_env()
#    md = jinja_env.get_template("question.jinja.md")
#    md_converter = markdown.Markdown(extension=["tables"])
#    html = md_converter.convert(md)
    html = markdown.markdown(md, extensions=["tables"])
    print(html)
    input_ = _common.Input()
    html = Template(html).render({
        "html": {
            **{k: getattr(input_, k) for k in "input,dropdown_1,dropdown_2".split(",")},
        }
    })
    return f"""
    <form action="grade">
    <!--form action="cgi-bin/formmail.cgi" method="post"-->
    {html}
    <input type="submit" value="送信">
    <!--input type="reset" value="リセット"-->
    </form>
    """

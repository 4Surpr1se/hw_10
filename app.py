from flask import Flask
import json

app = Flask(__name__)

with open('candidates.json', 'r', encoding="utf-8") as file:
    content = file.read()
    worker_list = json.loads(content)


@app.route("/")
def page_index():
    output_text = ''
    for i in worker_list:
        output_text += f' Имя кандидата - {i["name"]}\n Позиция кандидата - {i["position"]}\n Навыки через запятую - {i["skills"]}\n\n'
    return f'<pre>\n{output_text}\n<pre>'


@app.route('/candidate/<int:id>')
def profile(id):
    output_text = ''
    for i in worker_list:
        if i['id'] == id:
            output_text = f'<img src={i["picture"]}>\n\n<pre>\n Имя кандидата - {i["name"]}\n Позиция кандидата - {i["position"]}\n Навыки через запятую - {i["skills"]}<pre>'
            break
    if output_text == '':
        return '<pre>Кандидата с таким id не существует\n¯\_(ツ)_/¯<pre>'
    return output_text


@app.route('/skill/<uid>')
def profile_1(uid):
    output_text = ''
    for i in worker_list:
        if uid.lower() in i["skills"].lower().split(", "):
            output_text += f' Имя кандидата - {i["name"]}\n Позиция кандидата - {i["position"]}\n Навыки через запятую - {i["skills"]}\n\n'
    if output_text == '':
        return '<pre>Кандидатов с данными навыками нет\n¯\_(ツ)_/¯<pre>'
    print(output_text)
    return f'<pre>{output_text}<pre>'


app.run()

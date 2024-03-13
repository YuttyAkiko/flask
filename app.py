from flask import Flask, render_template

app = Flask(__name__)

# Lista simples de itens
items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'}
]

# Rota principal que renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html', items=items)

# Rota dinâmica que recebe um parâmetro na URL
@app.route('/item/<int:item_id>')
def item_detail(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return render_template('item_detail.html', item=item)
    else:
        return 'Item não encontrado', 404

if __name__ == '__main__':
    app.run(debug=True)
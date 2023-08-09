from flask import jsonify, Flask, request

twits = []

app = Flask(__name__)

# Тестовая штука
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


# Создать пост
@app.route('/twit', methods=['POST'])
def create_twit():
    ''' {'body':'Hello World', 'author': '@ague'}
    '''
    twit_json = request.get_json()
    twit = list([twit_json['body'], twit_json['author']])
    twits.append(twit)
    return jsonify({'status': 'success'})

# Прочитать пост
@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})


# Изменить пост
@app.route('/twit', methods=['PUT'])
def change_twit():
    twit_json = request.get_json()
    body = twit_json['body']
    author = twit_json['author']
    body_n = twit_json['body_n']
    for i in range(len(twits)):
        if twits[i] == [body, author]:
            twits[i] = [body_n, author]
    return jsonify({'Change': 'success'})


# Удалить пост
@app.route('/twit', methods=['delete'])
def del_twit():
    twit_json = request.get_json()
    body = twit_json['body']
    author = twit_json['author']
    twits.remove([body, author])
    return jsonify({'Delete': 'success'})


if __name__ == '__main__':
    app.run(debug=True)

from firebase import firebase

from flask import Flask, request, jsonify
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://bananacounter-60bb5-default-rtdb.firebaseio.com/', None)
COUNTERS_PATH = '/Counters'
BANANA_COUNT = 'BananaCount'

@app.route('/', methods=['GET', 'POST'])
def handle():
    counter_dict = firebase.get(COUNTERS_PATH, None)
    banana_count = counter_dict[BANANA_COUNT]
    if request.method == 'POST':
        banana_count += 1
        firebase.put(COUNTERS_PATH, BANANA_COUNT, banana_count)
    return jsonify({BANANA_COUNT: banana_count})


if __name__ == '__main__':
    app.run(debug=True)
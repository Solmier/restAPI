from flask import Flask, request, jsonify

app = Flask(__name__)

music_list = [
    {
    "id": 1,
    "group": "Nirvana",
    "song": "Smells Like Teen Spirit",
    "date": "10 сентября 1991 г."
  }, {
    "id": 2,
    "group": "Deep Purple",
    "song": "Smoke on the Water",
    "date": "4 декабря 1971 г."
  }, {
    "id": 3,
    "group": "Led Zeppelin",
    "song": "Kashmir",
    "date": "24 февраля 1975 г."
  }, {
    "id": 4,
    "group": "Queen",
    "song": "We Will Rock You",
    "date": "25 октября 1977 г."
  }, {
    "id": 5,
    "group": "AC/DC",
    "song": "Highway to Hell",
    "date": "27 июля 1979 г."
  }, {
    "id": 6,
    "group": "Metallica",
    "song": "Nothing Else Matters",
    "date": "20 апреля 1992 г."
  }, {
    "id": 7,
    "group": "Black Sabbath",
    "song": "Paranoid",
    "date": "18 сентября 1970 года"
  }, {
    "id": 8,
    "group": "Guns N’ Roses",
    "song": "Welcome To the Jungle",
    "date": "3 октября 1987 г."
  }, {
    "id": 9,
    "group": "Aerosmith",
    "song": "Dream On",
    "date": "27 июня 1973 г."
  }, {
    "id": 10,
    "group": "The Cranberries",
    "song": "Zombie",
    "date": "4 ноября 1994 г."
  }
]

@app.route('/music', methods=['GET', 'POST'])
def music():
    if request.method == 'GET':
        if len(music_list) > 0:
            return jsonify(music_list)
        else:
            'Not Found 404', 404

    if request.method == 'POST':
        new_group = request.form['group']
        new_song = request.form['song']
        new_date = request.form['date']
        id = music_list[-1]['id']+1

        new_obj = {
            'id': id,
            'group': new_group,
            'song': new_song,
            'date': new_date
        }
        music_list.append(new_obj)
        return jsonify(music_list), 201

@app.route('/song/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def song(id):
    if request.method == 'GET':
        for song in music_list:
            if song['id'] == id:
                return jsonify(song)
            pass
    if request.method == 'PUT':
        for song in music_list:
            if song['id'] == id:
                song['group']=request.form['group']
                song['song']=request.form['song']
                song['date']=request.form['date']
                updated_song = {
                    'id': id,
                    'group': song['group'],
                    'song': song['song'],
                    'date': song['date']
                }
                return jsonify(updated_song)
    if request.method == 'DELETE':
        for index, song in enumerate(music_list):
            if song['id']==id:
                music_list.pop(index)
                return jsonify(music_list)


if __name__ == '__main__':
    app.run()
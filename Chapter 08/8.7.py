def make_album(singer_name, album_name, number_of_tracks=None):
    album_information = {'singer': singer_name,
                         'album': album_name}
    if number_of_tracks:
        album_information['tracks'] = number_of_tracks
    return album_information


album_dictionary = make_album('Scooter', 'Age of love')
print(album_dictionary)

album_dictionary = make_album('System of a down', 'Mesmerise')
print(album_dictionary)

album_dictionary = make_album('Bon Jovi', 'Have a nice day')
print(album_dictionary)

album_dictionary = make_album('Korn', 'Untouchables', 14)
print(album_dictionary)

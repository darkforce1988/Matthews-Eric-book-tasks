def make_album(singer_name, album_name, number_of_tracks=None):
    album_information = {'singer': singer_name,
                         'album': album_name}
    if number_of_tracks:
        album_information['tracks'] = number_of_tracks
    return album_information


while True:
    singer_input = input("Enter a singer name (type 'quit' to exit): ")
    if singer_input == 'quit':
        break
    album_input = input("Enter an album name (type 'quit' to exit): ")
    if album_input == 'quit':
        break
    track_input = input("(Optional) Enter a number of tracks: ")

    album_dictionary = make_album(singer_input, album_input, track_input)
    print(album_dictionary)

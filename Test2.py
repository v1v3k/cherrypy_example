import cherrypy
import json


songs = {
    '1': {
        'title': 'Lumberjack Song',
        'artist': 'Canadian Guard Choir'
    },

    '2': {
        'title': 'Always Look On the Bright Side of Life',
        'artist': 'Eric Idle'
    },

    '3': {
        'title': 'Spam Spam Spam',
        'artist': 'Monty Python'
    }
}


class Songs:

    exposed = True

    def GET(self, id=None):

        if id is None:
            return(json.dumps(songs, sort_keys=True, indent=4, separators=(',', ': ')))
        elif id in songs:
            song = songs[id]

            return(json.dumps(song, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            return('No song with the ID %s :-(' % id)

    def POST(self, title, artist):

        id = str(max([int(_) for _ in songs.keys()]) + 1)

        songs[id] = {
            'title': title,
            'artist': artist
        }

        return ('Data entered')

    def PUT(self, id, title=None, artist=None):
        if id in songs:
            song = songs[id]

            song['title'] = title or song['title']
            song['artist'] = artist or song['artist']

            return(
                'Song with the ID %s is now called %s, '
                'and the artist is now %s' % (
                    id, song['title'], song['artist'])
            )
        else:
            return('No song with the ID %s :-(' % id)

    def DELETE(self, id):
        if id in songs:
            songs.pop(id)

            return('Song with the ID %s has been deleted.' % id)
        else:
            return('No song with the ID %s :-(' % id)

if __name__ == '__main__':

    cherrypy.tree.mount(
        Songs(), '/api/songs',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
         }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

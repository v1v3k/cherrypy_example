__author__ = 'george'
import cherrypy
import json


food = {
    '1111': {
        'Title': 'recipee1',
        'Instructions': 'Canadian Guard Choir',
        'Time': '10 mins',
        'Ingredients': 'apple,mango'
    },

    '2': {
        'Title': 'recipee2',
        'Instructions': 'Canadian Guard Choir',
        'Time': '10 mins',
        'Ingredients': 'apple,mango'
    },

    '3': {
        'Title': 'recipee3',
        'Instructions': 'Canadian Guard Choir',
        'Time': '10 mins',
        'Ingredients': 'apple,mango'
    }


}


class Food:

    exposed = True

    def GET(self, id=None):

        if id is None:
            return(json.dumps(food, sort_keys=True, indent=4, separators=(',', ': ')))
        elif id in food:
            food_item = food[id]

            return(json.dumps(food_item, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            return('No song with the ID %s :-(' % id)

    def POST(self, title, instruction,time,ingredients):

        id = str(max([int(_) for _ in food.keys()]) + 1)
        food[id] = {
        'Title': title,
        'Instructions': instruction,
        'Time': time,
        'Ingredients': ingredients
        }

        return ('Data entered')

    def PUT(self, id, title=None, instruction=None,time=None,ingredients=None):
        if id in food:
            food_1 = food[id]

            food_1['Title'] = title or food_1['Title']
            food_1['Instructions'] = instruction or food_1['Instructions']
            food_1['Time'] = time or food_1['Time']
            food_1['Ingredients'] = ingredients or food_1['Ingredients']

            return(json.dumps(food_1, sort_keys=True, indent=4, separators=(',', ': ')))

        else:
            return('No song with the ID %s' % id)

    def DELETE(self, id):
        if id in food:
            food.pop(id)

            return('Song with the ID %s has been deleted.' % id)
        else:
            return('No song with the ID %s :-(' % id)

if __name__ == '__main__':

    cherrypy.tree.mount(
        Food(), '/api/foods',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
         }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

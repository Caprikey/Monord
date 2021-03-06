from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Keyword, GeoPoint, Boolean, Integer

connections.create_connection(hosts=['localhost'])


class Gym(DocType):
    name = Text(analyzer='snowball', fields={'raw': Keyword()})
    location = GeoPoint()

    class Meta:
        index = 'gym'

    class Index:
        name = 'gym'

Gym.init()


class Pokemon(DocType):
    name = Text(analyzer='snowball', fields={'raw': Keyword()})

    class Meta:
        index = 'pokemon'

    class Index:
        name = 'pokemon'

Pokemon.init()


class Pokestop(DocType):
    name = Text(analyzer='snowball', fields={'raw': Keyword()})

    class Meta:
        index = 'pokestop'

    class Index:
        name = 'pokestop'

Pokestop.init()

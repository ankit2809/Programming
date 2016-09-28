import facebook
import json
import codecs
'''def pp(o):
        print(json.dumps(o,indent=1))
g=facebook.GraphAPI('EAACEdEose0cBADnJAxlvWCyHwHLdOGEgIWbZC3RpfyJopGZBIBi6BjYBVLe7AphcYqLjkr95IItMlP410QsS2HaQMopZByG15jTBGKk2zedbLawlarPDkajTuJQWJVhGTxtZCf1D6PPbuOIzIKFP78Gn8z1FUv1MNggnMxGxcwZDZD')
pepsi_id = '1431338237110781'
def int_format(n): return "{:,}".format(n)
print ("Pepsi likes:", int_format(g.get_object(pepsi_id)['likes']))
'''
from operator import itemgetter
from prettytable import PrettyTable
from collections import Counter
g=facebook.GraphAPI('EAACEdEose0cBADnJAxlvWCyHwHLdOGEgIWbZC3RpfyJopGZBIBi6BjYBVLe7AphcYqLjkr95IItMlP410QsS2HaQMopZByG15jTBGKk2zedbLawlarPDkajTuJQWJVhGTxtZCf1D6PPbuOIzIKFP78Gn8z1FUv1MNggnMxGxcwZDZD')
friends = g.get_connections("me", "friends")['data']
likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']
for friend in friends }
num_likes_by_friend = { friend : len(likes[friend])
for friend in likes }
my_likes = [ like['name']
friends_likes = Counter([like['name']
    for friend in likes
        for like in likes[friend]
            if like.get('name')])
for like in g.get_connections("me", "likes")['data'] ]
common_likes = list(set(my_likes) & set(friends_likes))
pt = PrettyTable(field_names=["Name"])
pt.align = 'l'
[ pt.add_row((cl,)) for cl in common_likes ]
print(pt.decode('utf-8'))

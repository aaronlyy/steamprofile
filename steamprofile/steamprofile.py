import requests
import xml.etree.ElementTree as et
import json

def get_profile(profile_url):
    # request xml as string
    res = requests.get(f"{profile_url}?xml=1")
    # parse string to xml tree
    tree = et.fromstring(res.text)
    # parse xml to dictionary
    d = {}
    for e in tree.iter():
        if e.tag != "groups":
            d[e.tag] = e.text
        else:
            break
    return Profile(d)

class Profile:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def json(self):
        return self.dictionary

    def __getattr__(self, attr):
        if attr in self.dictionary.keys():
            return self.dictionary[attr]
        else:
            return None
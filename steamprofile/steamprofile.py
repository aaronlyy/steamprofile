import requests
import xml.etree.ElementTree as et

def get_profile(profile_url):
    """Request a new Profile

    Args:
        profile_url (string): URL of a Steamprofile

    Returns:
        Profile: Profile object containing all information
    """
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
    """Profile Class containing information about a Steamprofile.
    """
    def __init__(self, info):
        self.info = info

    def json(self):
        return self.info

    def __getattr__(self, attr):
        if attr in self.info.keys():
            return self.info[attr]
        else:
            return None
import requests

def get_profile(profile_url, format="json"):
    """request info about a profile

    Args:
        profile_url (str): url of a steamprofile
    """

    # request xml of a user
    res = requests.get(f"{profile_url}/?xml=1")

    print(res.text)

get_profile("https://steamcommunity.com/id/speedkonsum")
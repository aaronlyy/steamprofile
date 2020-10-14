# example.py
from steamprofile import get_profile
import json

profile = get_profile("https://steamcommunity.com/id/guccigirl")

print(json.dumps(profile.json()))
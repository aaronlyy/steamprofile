# example.py
from steamprofile import get_profile

profile = get_profile("https://steamcommunity.com/id/speedkonsum")

print(profile.steamID, profile.memberSince)
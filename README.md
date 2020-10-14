# steamprofile: Collect information about Profiles on Steam 🕹

## Install

Use pip to install
```
pip install steamprofile
```

## Example
```python
from steamprofile import get_profile

profile = get_profile("https://steamcommunity.com/id/speedkonsum")
print(profile.steamID, profile.memberSince)

# >> aaron December 28, 2017
```
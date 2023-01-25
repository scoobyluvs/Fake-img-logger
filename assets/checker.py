import robloxpy
import requests

class roblox:
        
    def check(id: int):
        api = requests.get('https://www.roblox.com/avatar-thumbnails?params=[{userId:id}]').json()
        username = api['name']
        headshot = api['thumbnailUrl']
        nrap = robloxpy.User.External.GetRAP(id)
        rap = "{:,}".format(nrap)
        friends = robloxpy.User.Friends.External.GetCount(id)
        followers = robloxpy.User.Friends.External.GetFollowerCount(id)
        following = robloxpy.User.Friends.External.GetFollowingCount(id)
        return username,headshot,rap,friends,followers,following
    

import robloxpy
import requests

class roblox:
        
    def check(id: int):
        username = robloxpy.User.External.GetUserName(id)
        headshot = requests.get(f'https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={id}&size=48x48&format=Png&isCircular=false').json()['imageUrl']
        nrap = robloxpy.User.External.GetRAP(id)
        rap = "{:,}".format(nrap)
        friends = robloxpy.User.Friends.External.GetCount(id)
        followers = robloxpy.User.Friends.External.GetFollowerCount(id)
        following = robloxpy.User.Friends.External.GetFollowingCount(id)
        return username,headshot,rap,friends,followers,following
    

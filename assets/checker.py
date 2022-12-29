import robloxpy

class roblox:
        
    def check(id: int):
        username = robloxpy.User.External.GetUserName(id)
        headshot = robloxpy.User.External.GetHeadshot(id)
        nrap = robloxpy.User.External.GetRAP(id)
        rap = "{:,}".format(nrap)
        friends = robloxpy.User.Friends.External.GetCount(id)
        followers = robloxpy.User.Friends.External.GetFollowerCount(id)
        following = robloxpy.User.Friends.External.GetFollowingCount(id)
        return username,headshot,rap,friends,followers,following
    
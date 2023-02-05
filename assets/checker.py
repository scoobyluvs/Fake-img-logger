import requests


class Roblox:
    
    def check_user(user_id:int):        
        
        try:
            url = f'https://users.roblox.com/v1/users/{user_id}'
            user_data = requests.get(url).json()
            username = user_data['name']

            headshot_url = f'https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=48x48&format=Png&isCircular=false'
            headshot_data = requests.get(headshot_url).json()
            headshot = headshot_data['data'][0]['imageUrl']

            collectibles_url = f'https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100'
            collectibles_data = requests.get(collectibles_url).json()
            rap = sum(v['recentAveragePrice'] for v in collectibles_data['data'])

            friends_url = f'https://friends.roblox.com/v1/users/{user_id}/friends/count'
            friends_data = requests.get(friends_url).json()
            friends = friends_data['count']
            
            followers_url = f'https://friends.roblox.com/v1/users/{user_id}/followers/count'
            followers_data = requests.get(followers_url).json()
            followers = followers_data['count']

            following_url = f'https://friends.roblox.com/v1/users/{user_id}/followings/count'
            following_data = requests.get(following_url).json()
            following = following_data['count']
            
            return username,headshot,rap,friends,followers,following
            
        except requests.exceptions.RequestException as e:
            print(e)
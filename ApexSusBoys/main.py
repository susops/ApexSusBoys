from ApexApi import ApexApi
from ProcessData import ApexData

def main():
    client = ApexApi(*grab_user_info())
    user_input = options()
    
    if user_input == 1:
        results = client.get_player_stats()
    else:
        results = client.track_player()
        
    processed_data = ApexData(results, "test")
    processed_data.write_to_file()
        
def grab_user_info():
    api_key = "change_me"
    player = "change_me"
    platform = "change_me"
    uid = "change_me"
    return api_key, platform, player, uid
    
def options():
    user_input = int(
        input(
            '''
        Options:
        
            1 - Get Basic Stats by User
            2 - Get Player Match History
            3 - Query Player by UID
            
        >> '''
        )
    )
    return user_input
    

if __name__ == "__main__":
    main()
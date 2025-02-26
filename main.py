from src.functions import InstagramClient, UnfollowManager

def main():
    try:
        instagram = InstagramClient().login()
        unfollow_manager = UnfollowManager(instagram)
        unfollow_manager.unfollow_users()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

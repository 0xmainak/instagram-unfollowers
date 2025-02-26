import os
import random
import time
from dotenv import load_dotenv

class UnfollowManager:
    def __init__(self, instagram_client):
        load_dotenv()
        self.client = instagram_client.client
        self.user_id = instagram_client.user_id

    def get_non_followers(self):
        """Get list of users who don't follow back"""
        followers = self.client.user_followers(self.user_id)
        following = self.client.user_following(self.user_id)
        return set(following.keys()) - set(followers.keys())

    def unfollow_users(self):
        """Unfollow users who don't follow back"""
        non_followers = self.get_non_followers()
        print(f"Found {len(non_followers)} users who don't follow you back")

        for user_id in non_followers:
            user_info = self.client.user_info(user_id)
            print(f"Unfollowing {user_info.username}")
            self.client.user_unfollow(user_id)
            time.sleep(random.uniform(10, 15))

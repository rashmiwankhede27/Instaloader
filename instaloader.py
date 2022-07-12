import instaloader
ig= instaloader.Instaloader()
dp= input('Enter insta user name')
ig.download_profile(dp, profile_pic_only=True)

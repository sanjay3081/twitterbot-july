# Final Code
import time
import tweepy

consumer_key = 'OfACLAoErr4eaApF5Qpq8pA9n'
consumer_secret='YUePEBHRo1Yqlz0SGpndr1GHlz8pphcPEXHLfP1MZhPxnJjELr'
access_token='1297164703110582274-Cnwo9UBZwq8cFrQOIyH5pxCSLS2kbC'
access_token_secret='dTgX3l6DtDUq2EMtL4V6wxCmAmKyZcTQaQnJjVzgnka2t'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("Authentication approved")
while True:
  user = api.get_user('@Ameen91741779')
  u = user.followers_count
  api.update_profile(name=f'AMEER {u} Followers')
  print(f'AMEER {u} Followers')
  time.sleep(60)

import snscrape.modules.twitter as sntwitter
import tweepy
from geopy.geocoders import Nominatim
from uszipcode import SearchEngine
from facepplib import FacePP
import json
import os
import csv
import time

# Twitter Keys
consumer_key = "Qb8sBabv6T0Bsl0FBBkx5hbWk"
consumer_secret = "dkI4PaMw1f7Bwyggll3oXqvJra9Moh8jddrGlH6teedHjzlL9F"
access_token = "1408221286485037058-liNY6GrozCf7SL5F4UsQEize7Plcdg"
access_token_secret = "HdQ5Evgv8WrrqcEIJHtSLebBdNjqyuuMzqanUVuIjr4Pt"
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
# calling the api
api = tweepy.API(auth)

# Geocoder & USZipcode
gn = Nominatim(user_agent="geoapiExercises")
zipsearch = SearchEngine()

# FaceApp Auth
Face_API_Key = "2hG1Zouff9RJi60QDgo6PoH1Er1umTkE"
Face_API_Secret = "NDVjb-tjqyUf02V6Ts_r4blijPkFeo08"
faceapp = FacePP(api_key=Face_API_Key, api_secret=Face_API_Secret)

query = "the OR i OR to OR a OR and OR is OR in OR it OR you OR of OR for OR on OR my OR s OR that OR at OR with OR me OR do OR have OR just OR this OR be OR n’t OR so OR are OR m OR not OR was OR but OR out OR up OR what OR now OR new OR from OR your OR like"

useful_users = 0
all_users = set()

if not os.path.isfile("All_Users.csv"):
    with open("All_Users.csv", "w") as placeholder:
        pass
else:
    with open("All_Users.csv", "r", newline='') as f:
        reader = csv.reader(f)
        userdetails = list(reader)
        useful_users = int(userdetails[-1][0])
        all_users = set([str(entry[-1]) for entry in userdetails])

offset = useful_users


def json_saver(count, user, face, uszip):

    if uszip.land_area_in_sqmi == 0:
        water_level = 0.
    else:
        water_level = uszip.water_area_in_sqmi / uszip.land_area_in_sqmi

    user_dict = {
        'id': user.id,
        'id_str': user.id_str,
        'name': user.name,
        'screen_name': user.screen_name,
        'location': user.location,
        'profile_location': user.profile_location,
        'description': user.description,
        'url': user.url,
        'entities': user.entities,
        'protected': user.protected,
        'followers_count': user.followers_count,
        'friends_count': user.friends_count,
        'listed_count': user.listed_count,
        'created_at': str(user.created_at),
        'favourites_count': user.favourites_count,
        'utc_offset': user.utc_offset,
        'geo_enabled': user.geo_enabled,
        'verified': user.verified,
        'statuses_count': user.statuses_count,
        'lang': user.lang,
        'status_id': user.status.id,
        'contributors_enabled': user.contributors_enabled,
        'is_translator': user.is_translator,
        'is_translation_enabled': user.is_translation_enabled,
        'profile_background_color': user.profile_background_color,
        'profile_background_image_url': user.profile_background_image_url,
        'profile_background_image_url_https': user.profile_background_image_url_https,
        'profile_background_tile': user.profile_background_tile,
        'profile_image_url': user.profile_image_url,
        'profile_image_url_https': user.profile_image_url_https,
        # 'profile_banner_url': user.profile_banner_url,
        'profile_link_color': user.profile_link_color,
        'profile_sidebar_border_color': user.profile_sidebar_border_color,
        'profile_sidebar_fill_color': user.profile_sidebar_fill_color,
        'profile_text_color': user.profile_text_color,
        'profile_use_background_image': user.profile_use_background_image,
        'has_extended_profile': user.has_extended_profile,
        'default_profile': user.default_profile,
        'default_profile_image': user.default_profile_image,
        'following': user.following,
        'follow_request_sent': user.follow_request_sent,
        'notifications': user.notifications,
        'age': face.age,
        'gender': face.gender,
        'smile': face.smile['value'] > face.smile['threshold'],
        'zipcode': uszip.zipcode,
        'population': uszip.population,
        'population_density': uszip.population_density,
        'water_level': water_level,
        'median_household_income': uszip.median_household_income,
        'median_home_value': uszip.median_home_value
    }

    with open(f"User_Details/{count}.json", "w") as fp:
        json.dump(user_dict, fp)

    with open("All_Users.csv", "a", newline='') as fp:
        write = csv.writer(fp)
        write.writerow([count, user.id, user.screen_name])

except_count = 0
except_twice = 0

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(
            query + f" since:{int(useful_users // 250) + 2009}-07-01 until:{int(useful_users // 250) + 2010}-06-30").get_items()):
    # tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    # print([tweet.date, tweet.id, tweet.content, tweet.user.username])

    if useful_users >= 3000:
        break

    if tweet.user.username in all_users:
        continue

    # If API Call limit exceeds
    try:
        user = api.get_user(screen_name=tweet.user.username)
    except:
        while True:
            try:
                user = api.get_user(screen_name=tweet.user.username)
                break
            except:
                print("Tweepy API Limit Exceeded. Waiting for 60 seconds. . .")
                time.sleep(60)

    print(f"{useful_users} / {i + 1 + offset}")

    if user.profile_image_url is None:
        continue
    if user.location is None or user.location == "":
        continue

    # To suppress a no attribute error : 'User' object has no attribute 'status'
    if not hasattr(user, 'status'):
        continue

    # geo_code = gn.geocode(user.location)

    # If Geocode API times out
    try:
        geo_code = gn.geocode(user.location)
    except:
        # gn = Nominatim(user_agent="geoapiExercises")
        print("GeoCode API Called again.")
        try:
            geo_code = gn.geocode(user.location)
        except:
            print("GeoCode API Called Twice.")
            continue

    if geo_code is None:
        continue
    if "United States" not in geo_code[-2]:
        continue
    location = geo_code[-1]
    uszip = zipsearch.by_coordinates(location[0], location[1])
    if len(uszip) == 0:
        continue
    uszip = max(uszip, key=lambda x: x.population_density if x.population_density is not None else 0)

    face_url = ''.join(user.profile_image_url.split('_normal'))  # To get HQ Image

    try:
        image = faceapp.image.get(image_url=face_url, return_attributes=['smiling', 'age', 'gender'])
    except:
        except_count += 1
        print("Except_Count: ", except_count)
        try:
            image = faceapp.image.get(image_url=face_url, return_attributes=['smiling', 'age', 'gender'])
        except:
            except_twice += 1
            print("Except_Twice: ", except_twice)
            continue

    if len(image.faces) != 1:
        continue

    useful_users += 1
    print(user.screen_name, "|", user.name, "|", user.location)
    # print(user.name, "|", user.location, "|", geo_code, "|", uszip.zipcode, "|", uszip.population,
    #      uszip.population_density)
    # print(uszip)
    '''
    print("Number of faces =", len(image.faces))
    print("Age =", image.faces[0].age)
    print("Gender =", image.faces[0].gender)
    print("Smiling =", image.faces[0].smile)
    '''
    json_saver(useful_users, user, image.faces[0], uszip)
    all_users.add(user.screen_name)

    # print(f"{useful_users} / {i + 1}")

print("Scrape successfully completed")

from mongoengine import connect

connect(db="testDB", host="localhost", port=27017)

from mongoengine import *
class DateTimeTest(Document):#date_time_test

    id1 = IntField(db_field ="id",required=True,primary_key=True)
    join_date = DateTimeField(required=True)
    url = URLField(required=True)
    name = StringField(required=True)
    username = StringField(required=True)
    bio = StringField(required=True)
    location = StringField(required=True)
    tweets = IntField(required=True)
    following = IntField(required=True)
    followers = IntField(required=True)
    likes = IntField(required=True)
    media = IntField(required=True)
    private = BooleanField(required=True)
    verified = BooleanField(required=True)
    profile_image_url = URLField(required=True)
    background_image = StringField(required=True)

    def __init__(self,data):
        super().__init__()

        self.id1 = data.get("id",0)
        self.join_date = data.get('join_date','')
        self.url=data.get('url','')
        self.name = data.get('name','')
        self.username=data.get('username','')
        self.bio=data.get('bio','')
        self.location=data.get('location','')
        self.tweets=data.get('tweets',0)
        self.following=data.get('following',0)
        self.followers=data.get('followers',0)
        self.likes=data.get('likes',0)
        self.media=data.get('media',0)
        self.private=data.get('private',False)
        self.verified=data.get('verified',False)
        self.profile_image_url=data.get('profile_image_url','')
        self.background_image=data.get('background_image','')
        # self.date=d['date']
d={'id': '892072054148796416', 'name': 'Hindenburg Research', 'username': 'HindenburgRes', 'bio': 'Popping bubbles as we see them. We express strong opinions. Not investment advice.', 'location': 'United States', 'url': 'https://t.co/vrWOyYyUmI', 'tweets': 1566, 'following': 857, 'followers': 450035, 'likes': 10111, 'media': 734, 'private': False, 'verified': False, 'profile_image_url': 'https://pbs.twimg.com/profile_images/1167878460422836225/DG419RgJ_normal.jpg', 'background_image': '', 'join_date': '2017-07-31 17:18:46'}
tutorial1 = DateTimeTest(d)
tutorial1.save()

from instabot import Bot

bot = Bot(max_likes_to_like=1000000) # Creating Bot object
bot.login(username="username", password="password") # Logs bot in

# Posting Image
img = "Untitled.jpg"
bot.upload_photo(img, caption="lmao")

# Following User
bot.follow("spacex")

# Get Post ID
post = bot.get_media_id_from_link("https://www.instagram.com/p/CPtPcfSFJZl/")
bot.like(post)
bot.comment(post, "xd")

bot.logout() # Logs bot out



import praw
import config
import time
from oracleScrapper import *


# This function creates the connection between this script and reddit via PRAW
def bot_login():
    print("Logging " + config.username + " in...")
    credentials = praw.Reddit(username=config.username,
                              password=config.password,
                              client_id=config.client_id,
                              client_secret=config.client_secert,
                              user_agent="Programming Language Documentation Fetcher Bot v0.5")
    return credentials


# this function takes in all replied to comments from a file and inserts it into a list
def get_saved_comments():
    with open("comments_replied_to.txt", "a+") as f:
        f.seek(0)
        comments = f.read()
        comments = comments.split("\n")
        comments = list(filter(None, comments))
    return comments


# This function reads through reddit comments in a subreddit
# once a user calls the bot, it looks for keywords such as programming language names and searches for class
# the typical command should look like this "!DocFetcher <Language> <KeyWord>"
def run_bot(access, comments):
    for comment in access.subreddit('learnjava+javahelp').comments(limit=25):
        time.sleep(3)
        print("Searching for comments...")
        if ("!DocFetcher" in comment.body or "!df" in comment.body or "!DF" in comment.body) and\
                comment.id not in comments and not comment.author == access.user.me():
            print("Found Comment...")
            if "j11" in comment.body or "java11" in comment.body:
                com = comment.body.split()
                if len(com) == 3:
                    if (com[0] == "!DocFetcher" or com[0] == "!df" or com[0] == "!DF") and\
                            ("j" in com[1] and "11" in com[1]):
                        if "::" in com[-1]:
                            method_class = com[-1].split("::")
                            reply = get_method_information(method_class[1], get_j11_class(method_class[0]))
                        elif "." in com[-1]:
                            method_class = com[-1].split(".")
                            reply = get_method_information(method_class[1], get_j11_class(method_class[0]))
                        else:
                            # search_jdk is a method inside oracleScrapper
                            reply = search_jdk(com[1], com[-1])
                        print("Leaving Reply for " + comment.id + "...")
                        comment.reply(reply)
                        comments.append(comment.id)
                        # append the comment ID to the comments file so as not to spam comments already replied to
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
            elif "java7" in comment.body or "j7" in comment.body:
                com = comment.body.split()
                if len(com) == 3:
                    if (com[0] == "!DocFetcher" or com[0] == "!df" or com[0] == "!DF") and\
                            ("j" in com[1] and "7" in com[1]):
                        if "::" in com[-1]:
                            method_class = com[-1].split("::")
                            reply = get_method_information(method_class[1], get_j7_class(method_class[0]))
                        elif "." in com[-1]:
                            method_class = com[-1].split(".")
                            reply = get_method_information(method_class[1], get_j7_class(method_class[0]))
                        else:
                            # search_jdk is a method inside oracleScrapper
                            reply = search_jdk(com[1], com[-1])
                        print("Leaving Reply for " + comment.id + "...")
                        comment.reply(reply)
                        comments.append(comment.id)
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
            elif "java8" in comment.body or "j8" in comment.body or "java" in comment.body:
                com = comment.body.split()
                if len(com) == 3:
                    if (com[0] == "!DocFetcher" or com[0] == "!df" or com[0] == "!DF") and\
                            (com[1] == "j8" or com[1] == "java" or com[1] == "java8"):
                        if "::" in com[-1]:
                            method_class = com[-1].split("::")
                            reply = get_method_information(method_class[1], get_j8_class(method_class[0]))
                        elif "." in com[-1]:
                            method_class = com[-1].split(".")
                            reply = get_method_information(method_class[1], get_j8_class(method_class[0]))
                        else:
                            # search_jdk is a method inside oracleScrapper
                            reply = search_jdk(com[1], com[-1])
                        print("Leaving Reply for " + comment.id + "...")
                        comment.reply(reply)
                        comments.append(comment.id)
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
    print("sleeping...")
    time.sleep(60)


while True:
    comments_replied = get_saved_comments()
    login = bot_login()
    run_bot(login, comments_replied)

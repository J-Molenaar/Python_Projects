about_me = {"name": "Anna", "age": "101",
            "country of birth": "USA", "favorite language": "Python", }


def me(about_me):
    for key in about_me:
        print "My", about_me[key], "is", key


me(about_me)

from pathlib import Path


def generate_github_profile(theme, **kwargs):
    """
    Generate a Github Profile 
    """
    # read the theme file
    with open(f"src/themes/{theme}/profile.txt") as f:
        Readme = f.read()
    
    # replace the placeholders with user data
    for key, value in kwargs.items():
        item_path = Path(f"src/themes/{theme}/{key}.txt")
        if not item_path.exists():
            continue      
        
        with open(item_path) as f:
            profile_item = f.read()

        profile_item = profile_item.replace(f"{{ value }}", value)
        Readme = Readme.replace(f"{{ {key} }}", profile_item)
    
    return Readme


if __name__ == "__main__":
    #personal info
    name = "John Doe"
    email = "John@gmail.com"

    # social media
    twitter = "JohnDoe" 
    linkedin = "JohnDoe"      
    instagram = "JohnDoe"

    # select theme
    theme = "default"

    # generate readme
    Readme= generate_github_profile(theme, name=name, email=email, twitter=twitter, linkedin=linkedin, instagram=instagram)
    print(Readme)




    

﻿# The script of the game goes in this file.

init python:
    from discoIPC import ipc
    import time

    client_id = "641724281365069884"  # Put your Client ID in here
    client = ipc.DiscordIPC(client_id) # Initialize the Presence client

    print('Sending data ...')
    client.connect() # Start the handshake loop

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chode")

define pov = Character("[povname]")

label before_main_menu:
    call discordActivity()
    return

# The game starts here.

label start:

    $ save_name = "Highschool Entrance"
    $ date = 0

    call discordActivity("talking", "Highschool Entrance", "Chode")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chode back

    # These display lines of dialogue.

    c "Well hello there!"

    show chode happy
    with dissolve

    c "I'm chode, welcome to the Incel Highschool bro. What's your name?"

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Anon"

    pov "My name is [povname]!"

    c "Oh nice to-"

    python:
        if povname == "Chode":
            renpy.jump("choded")
        else:
            if povname == "Nigger":
                renpy.jump("Ending03")
            else:
                renpy.jump("end")

label choded:

    call discordActivity("talking", "Highschool Back Alley", "Chode")

    c "You can't be Chode, I'm Chode."

    "Chode grabs you by your school uniform and takes you to behind the school"

    scene school alleway

    c "Since your name is Chode, I might as well chode you with my chode bro."

    show chode happy
    with dissolve

    "Chode unzips his pants to reveal his smol chode"

    c "Here we go bro"

    jump Ending02

label end:

    c "Wait you're [povname]? You must be a first year bro."

    c "I don't hang out with first year incels"

    show chode back

    c "Get choded bro!"

    "As Chode turns around and walks away you feel like you've just been choded for life..."

    jump Ending02

label sleep:

    menu:
        "You slowly start closing your eyes."

        "Sleep":
            python:
                date += 1


    return

label Ending01:

    "Ending 1 - Get choded!"

    return

label Ending02:

    "Ending 2 - Get choded... ew..."

    return

label Ending03:

    "Ending 3 - Battle of Chode"

    return

label discordActivity(activity="main_menu",place="none",character="none",large_image="default"):

    python:
        print('Sending activity ...')
        if activity == "main_menu":
            client.update_activity({
                'state': 'Main Menu',
                'details': 'Deciding',
                'assets': {
                    'large_image': 'default',
                }
            }) # Updates our presence

        if activity == "talking":
            client.update_activity({
                'state': place,
                'details': 'Talking with ' + character,
                'assets': {
                    'large_image': large_image,
                    'large_text': 'Talking with ' + character,
                }
            }) # Updates our presence

    return

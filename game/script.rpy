# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chode")

define pov = Character("[povname]")


# The game starts here.

label start:

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
            renpy.jump("end")

label choded:

    c "You can't be Chode, I'm Chode."

    c "*Chode grabs you by your school uniform and takes you to behind the school*"

    scene school alleway

    c "Since your name is Chode, I might as well chode you with my chode bro."

    show chode happy
    with dissolve

    c "*Chode unzips his pants to reveal his smol chode*"

    c "Here we go bro"

    # This ends the game.

    return

label end:

    c "Wait you're [povname]? You must be a first year student."

    c "I don't hang out with first year incels"

    show chode back

    c "Get choded!"

    c "*walks away*"

    # This ends the game.

    return

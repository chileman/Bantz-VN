# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eesti', color="#1f88ff")
image bg eestiBG = "Eesti.jpg"

image Eesti normal = "Eesti_girl.png"
image Eesti mad = "Eesti_girl_mad.png"


# The game starts here.
label start:

    scene bg eestiBG

    "You wake up in a frozen wasteland"

    "You don't know what the fuck is going on"
    
    show Eesti normal
    
    e "Welcome to Estonia!"

    e "Haha now you are stuck in Estonia!!"
    
    "You want to die"
    
    e "Now, before we go any further, which is the most autistic balt?"
    
    menu:
        "Estonia":
            jump estonia
            
        "Latvia":
            jump latvia
            
        "Lithuania":
            jump lithuania
    
    label estonia:
        show Eesti mad
        e "Die"
        hide Eesti
        hide bg
        "You are kill"
        return
    
    label latvia:
        e "Right answer!"
        return
        
    label lithuania:
        e "Oh no, now you've done it"
        "You hear a gunshot in the distance"
        
    return

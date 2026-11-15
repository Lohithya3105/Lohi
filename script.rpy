
define e = Character("Slimeboy")
define c = Character("Spider")
define q = Character("Purple Slime")
define x = Character("Ending")
label start:


    scene bg n

    show slimeboy n at truecenter:
        zoom 2

    e "Wassup"
    play music "audio/Wow.mp3" volume 0.5
    e "Im Slimeboy, the greatest slime!"
    stop music 
    menu:
        "Hello slimeboy, what are you doing!":
            e "talking to you mate."
        "Wazup!":
            e "Wazzzzup"

    e "Anyways, I have a quest for you."

    menu:
        "What is it":
            e "To slay the evil purple slime"
        "Can I not do the quest?":
            hide slimeboy n
            show slimeboy angry at truecenter:
                zoom 2

            e "no, anyways our quest is to slay the evil purple slime"
    show slimeboy n at truecenter:
        zoom 2
    e "Oh no, Imma hide behind you"
    hide slimeboy n
    show spoder n at truecenter :
        zoom 2

    c "Have you seen a weird looking green slime anywhere?"

    menu:
        "No he is not behind me.":
            c "Okay buh bai."
            jump escape
        "Yeah, he's behind me all right.":
            c "you're getting slimed, hehe get it?"
            jump death

label death:
    show black
    scene black
    e "You died, but don't worry, I will bounce you back"
    
    scene bg n
    show slimeboy angry at truecenter:
        zoom 2
    e "Let battle the spider instead!"

    show slimeboy angry at left:
        zoom 2
    show spoder n at right:
        zoom 2

    c"How are you alive?"
    play music "audio/Wow.mp3" volume 0.5
    e"Cause of my magic! The power to bounce people back alive!"
    stop music

    menu:  
        "Slime the spider.":
            play music "audio/Oof.mp3" volume 2
            c "nooo"
    hide spoder n 

    show slimeboy n at truecenter:
        zoom 2
    e "By the way, don't betray me ever again. Now lets find purple slime!"

    show slimeboy n at left:
        zoom 2
    show purple slime at right
    q "Hello."
    
    menu:
        "Team with purple slime":
            q "As if I would work with you, weakling."
            jump death2
        "Fight purple slime":
            q "Bet."
            jump warrior
    return

label escape:

    scene bg n
    
    show slimeboy n at truecenter:
        zoom 2
    e "Thank you, my friend!"

    show slimeboy n at left:
        zoom 2
    show spoder n at right:
        zoom 2
    c "Wait hol up, you lied broski."

    menu: 
        "Slime the spider.":
            c "noo"
    hide spoder n
    show slimeboy n at truecenter:
        zoom 2
    e"Thanks, now lets find purple slime"
    show slimeboy n at left:
        zoom 2
    show purple slime at right
    q "Hello."
    
    menu:
        "Fight purple slime":
            q "Bet."
            jump warrior
    return

label death2:

    show black
    scene black

    e"Stop dying, work with me."

    scene bg n
    show slimeboy angry at left:
        zoom 2
    show purple slime at right

    q "So you do have the power to bounce people back alive- But can you bounce back?"

    menu:
        "Protect Slimeboy":
            e "Thank you for saving me."
            q "Really, you think you can beat me?"
            jump warrior
        "Watch Slimeboy die":
            hide slimeboy angry
            show purple slime at truecenter
            q "Now I can rule the world!"
            x "Bad Ending."
        
    return

label warrior:
    scene bg n 
    show purple slime at truecenter
    q "Take This attack!"
    show fire ball at right:
        zoom 3
    menu:
        "Redirect Shot.":
            q "It cant be..."
    show fire ball at truecenter
    play music "audio/Oof.mp3" volume 2
    q "I guess I lost."
    stop music
    hide purple slime
    hide fire ball
    show slimeboy n at truecenter 
    e "Thank you... I always knew you could... Bounce Back"
    x "Good Ending."
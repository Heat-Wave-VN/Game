# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define Bear = Character("Bear")
define Scorpion = Character("Scorpion")
define Unknown = Character("??")
define Bird = Character("Bird")
define Jaguar = Character("Jaguar")
define Flowercub = Character("Flowercub")


# The game starts here.
transform left_to_right:
    xalign 0.0
    linear 2.0 yalign 1.0
    repeat

transform jumpup:
    linear 0.5 yalign 1.5
    linear 1.0 yalign 1.5

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    label scene1:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

        show opening_scene
        with dissolve
        pause 2
        $ renpy.music.set_volume(0.5, delay=0, channel='music')
        play music opening_chant
        pause 4
        show opening_scene2
        pause 4
        show opening_scene3:
            subpixel True
            yalign 0.0
            easein 8.0 yalign 1.0
        with dissolve

        pause 6
    # These display lines of dialogue.
    # This ends the game.
    label scene2:
        
    # bear swirl
        show meditate01_scene1
        play music intro_background_music
        with dissolve
        pause 1.25
        show meditate02_scene2
        with dissolve
        pause 1.25
        show meditate03_scene3
        with dissolve
        pause 1.25
        with dissolve
        show meditate04_scene4
        pause 1.25
        with dissolve
        show meditate05_scene5
        pause 1.25
        stop music
        show drift
        with dissolve
        pause 5


    label scene3:
        show walking_scene1
        with dissolve
        Bear "Hmm..."
        Bear "..I wonder where I am.."
        window hide
        pause 2

        show trip_scene2
        with dissolve
        Bear "Aghh!Owaghhh$#@"
        window hide

        show trip_scene3
        with dissolve
        Bear "..."
        show trip_scene4
        pause 4

        play sound bird_laugh01
        Unknown " HEee HwEe, heee, Hee!! "
        pause 3
        
        menu:
            "Look Around":
                show lookaround_scene1
                with dissolve
                Unknown " Hee-hee-hee-hee!! "
                window hide
                show lookaround_scene2
                with dissolve
                pause 2
            "Continue walking":
                show walking_scene1
                play sound bird_laugh02
                show walking_scene1
                Unknown "Oh- my! EEhhhheehe! This Bear!! This Bear - fell - on - their - FACE! eeHHeee!"

    label scene4:
        show forest_scene4
        pause 1.0
        with dissolve
        show bear_annoyed at left, left_to_right
        pause .75
        
        with dissolve
        show bird_laugh at right
        Bear "Hey, that's not very nice."
        hide bear_annoyed
        show lookaround_scene2
        play sound bird_laugh01
        Bird "It - might - not - be - nice - EEEhhheeheehe.. But - it - is - very funny"

        play sound opening_chant
        hide bird_laugh
        hide lookaround_scene2
        with dissolve
        with dissolve
        show bear_meditate
        with dissolve
        pause 1
        with dissolve

        menu:
            "Own it":
                show forest
                with dissolve
                hide bear_meditate
                hide umm
                stop music
                show forest_scene4
                with dissolve
                show bear_thinking at left
                show bird_laugh at right
                Bear "You know... it wasn't that bad."
                play sound bird_single_laugh
                Bird "eheehee.."
                hide bird_laugh
                show bird_confused at right
                with dissolve
                hide bear_thinking
                show bear_thinking_happy at left
                with dissolve
                Bear "Yeah you know. the fall, it wasn't that bad."
                Bear "Besides which, I couldn't do much to stop that from happening."

                show bird_embarassed at right
                with dissolve
                Bird "EEhhhh, I guess you're right."
                Bird "Errr, umm. Sorry... for making fun of you then.. I guess."
                Bird "..."
                show bird_embarassed_sad at right
                with dissolve
                Bird "I'm sorry."

                hide bear_thinking_happy
                show bear_happy at left
                with dissolve

                Bear "It seems that we have switched positions!"
                hide bear_happy
                show bear_laughing at left
                with dissolve
                Bear "It's okay, you know? No Worries! I forgive you!"
                show bird_embarassed at right
                with dissolve
                Bird "Wait, really...?"
                hide bird_embarassed_sad
                hide bird_embarassed
                hide bear_laughing
                show bear_happy at left
                Bear "Yes, really, I forgive you. It's okay."

                #-Fade out- End of Act I

                #[ALTERNATIVELY]#

            "Run Off":

                show bear_running_woods
                Bear "I’ve already made such a fool of myself"
                Bear "If I stayed it would have only made it worse"
                Bear "Sometimes I can be so absent minded."
                show bear_happy
                hide bear_meditate
                hide umm
                hide bear_running_woods
                hide lookaround_scene2
                show forest_scene4
                Bear "I should have seen that tree root.  I could have avoided it!"
                Bear "I need to pay better attention in the future"
                Bear "I can’t believe I messed up so badly."
                Bear "I’ll watch where my feet go.  I won’t trip again!"



        hide bear_happy
        show bird_embarassed at right
        with dissolve
        Bird "You know, I want to apoligize, For being such a jerk."
        Bird "Maybe I can... Maybe I can give you something?"
        Bird "You know, as consolation! Eee!"

        show bear_happy
            #fux
        with dissolve
        Bear "you know you really don't have to"
        Bird "No, please! Take This! It's the least I could do in this situation"
        play sound heart_shard_appears
        hide bird_embarassed
        show bird_tada
            #fux
        hide bear_happy
        hide bird_tada
        show bird_confused at right
        show bear_thinking_happy at left

            #fux
        Bear "Er, umm.. what is This?"
        Bird "You don't recognise it It's a piece of your heart! eeHHee!"
            #play music confused
            #fux
        Bear "..."
        pause 4

        hide bird_confused
        hide bear_thinking_happy
        show bear_annoyed at left
        show bird_wave at right
        Bird "No, no no! you musn't be embarassed! Now look."
        Bird "I was flying around this forest one day and I saw something shiny."
        Bird "I was wondering what it was, so I swooped down and grabbed it."
        hide bear_annoyed
        show bear_happy at left


        hide bear_happy
        hide bird_wave

        pause 5

        with dissolve
        #show scorpion3 right
        show bear_happy at left
        show heart_shard01 at center
        with dissolve
        Bird "Beautiful"
        Bear "Yeah"
        hide heart_shard01 at center
        Scorpion "Oh no! I forgot! The tides! The full moon! Quick, back to the ship!"
        Bear "We can’t stay on the beach tonight"
        Scorpion "Agreed. Even on the ship, we’d be dragged out to open waters when we go to sleep"
        Bird "It was the most wonderous thing, it had a heartbeat and everything!"
        show bird_wave at right
        #show scorpion
        #fux
        Bird "Unfortunately, soon after I found it, it stopped beating…"
        Bird "Then, soon after that, it stopped shining too…"
        show black
        with dissolve
        pause(2)

        show bear_meditate at left
        #fux
        Bear "Oh, I hear it!  I hear the heartbeat!"
        hide bird_wave
        show bird_confused at right

            #fux
        Bird "You see?  How else would you explain it starting up again?  Just like magic."
        hide bear_meditate
        show bird_confused at left
        show bear_happy at right
            #fux
        Bird "I’m glad I held on to it!  Eeee!"
        hide window
            #- (I believe this is a repeat)

        Bear "Oh, wow!  Thank you for this!  It’s great…but…"
        "I’m not sure what to do with it!?"

        Bird "No, no!  My friend, do not be embarrassed!"
        show bear_happy
        Bird "You know, I’m not entirely sure.  But I bet…"
        "I bet if you held it up to your heart, it would probably slide right back in."
        Bird "The heart, you see, wants to be whole!"

        show bird_thinking at right
        hide bird_thinking
        Bear "So I would just…hold it up to my heart?"
        show bird_confused

        Bird "Yes, like this see!?"

        with dissolve
        show heart_shard0
        pause .2
        with dissolve
        show heart_shard1
        pause 3
        hide heart_shard1
        hide heart_shard0


        show forest_scene4
        show bird_laugh at right

        hide bird_laugh

        Bird "EEeehhheee, Ehhhhee, Eeehhhheee, Eeehhhheee!"
            #fux
        Bird "Yes, my friend!  You did it!"
        Bear "Wow, I guess it really was a part of me."
        hide bear_happy
        hide bird_laugh
        show bear_laughing left
        show bird_laugh right
        "I feel so much more whole, I feel better.  Thank you!"
        hide bird_confused
        show bird_laugh
        Bird "Eeehhhee, eehheee, ehheee, eehheee!  You see, we are good friends now!"
        "Unfortunate circumstances may have brought us together, but good came from it!"
        "Eheee, yay!"
        hide bird_laugh
        show bird_embarassed at left
        hide bear_happy
            #fux
            #fux
        pause 1.5
            #fux
            #fux


        show bear_thinking_happy at right
        Bear "Well, I suppose I should get going.  I have more to traverse.  More to find."
        hide bear_thinking_happy at right
        hide bird_embarassed

        show bird_wave at right

        Bird "Yes, I will not forget you, or the lessons learned."
        "Thank you for teaching them.  I will not be so cruel in the future."
        hide bird_wave at right
        show bear_meditate at right
        Bear "No, thank you for teaching me!  I will not take such cruelties to heart in my future!"
        hide bear_meditate

        show bear_laughing at right
        Bear "Goodbye for now, Bird!"
        hide bear_laughing at right
        show bird_tada at right
        Bird "Goodluck in your travels bear!"
        hide bird_tada
        #-Fade out- End of Act I –

        hide forest_scene4
        hide bear_happy
        show walking_scene1
        pause 1.5
        with dissolve
        Bear ".."
        show forest_scene4
        pause 2
        show walking_scene1
        pause 2


        label Act2:
        play music scene2_background_music
        show explanation_desert
        pause 2
        hide explanation_desert
        show scene03_overhead_hot_sun
        pause 2
        show scene03_sand_blowing_01
        pause 3
        show bear_thinking
        hide bear_thinking
        play sound scene3_wind
        Bear "It's so hot.. how long have I been out here?"
        pause 2
        show scene03_looking_left
        hide scene03_looking_left
        pause 1.0
        show scene03_looking_right
        pause 1.0

        menu:
            "Keep Walking":
                show scene03_sand_blowing_02
                Bear "I should not have kept walking it's so hot!"
                hide window
                pause 3
                play sound scorpion_appearing
                Unknown "Scuttle noises"
                pause 1.5
                show bear_scorpion_scene2
                pause .25
                show bear_scorpion_scene1
                pause 2
                Scorpion ".."
            "Stay put and find shelter, you investigate the wreckage":
                show scene03_bck03
                pause 1.5
                Bear "What's this doing all the way out here?"
                pause 3
                show scene03_bear_enters_ship
                Bear "How did this get here?"
                pause 2
                show scene03_inside_ship
                pause 2
                Unknown "scurrying noises"
                play sound scorpion_appearing
                pause 3
                show bear_scorpion_scene2
                pause 1.5
                Bear "Hello?!"

                show bear_scorpion_scene1
                show bear_scorpion_scene2
                

#--The desert--scorpion and bear are face to face, assessing each other

        Bear "Who are you? What do you want?"

#Scorpion: “Hmm I would ask you the same thing. What’s a bear doing all the way out here?”

        Bear "I got lost. But I’ll figure out a way to get out of here"
        Scorpion "Would you like some help?"

#[OPTION]
        menu:
            "Accept Help":
                Bear "That's very kind of you, Which way should I go?"
                Scorpion "Goodness, you look parched. Why not have some refreshments first?"

                

                Bear "Thank you very much. I would love that. But where?"
                show scene03_find_melons
                Bear "Thank you for this. I don't know what I would've done if you hand't shown up"
                Scorpion "You're welcome. It's not an easy terrain to walk alone. And without food or water!"
                Bear "Well, it seems even in this harsh enviornment, there's still food, shelter, and warmth from strangers. There is much here if you lok closer."

                Scorpion "It's getting darker. I can lead you out of here in the morning."
                Bear "Oh I musn't trouble you any longer. Just tell me the direction I should go and i'll go."
                #the clouds above you have built up without you noticing
                "**the clouds above you have built up without you noticing..**"

                
            "Refuse Help":
                Scorpion "Are you sure?!"

                Scorpion "Very well then. Before you go, take a melon with you."
                show scene03_looking_at_fruit
                
        Scorpion "This is my largest melon, it's different than all of the others, there is something that is quite shiney in side of it you can have it, it's yours."
        pause 2
        show heart_shard0
        pause 2
        show heart_shard1
        pause 1
        show heart_shard2
        pause 1
        "Drops of rain splatters on Bear's head. Scorpion scurries under some grass"
        show scene03_rain_starts
        play sound scene3_rain01
        pause 6
        
        pause 3
        hide window
        show scene03_melon_grass  
        "Scorpion scuttles to the grass"
        Scorpion "It hasn't rained here in a long time! What's going on?"
        Bear "I don't know! But I feel it's something good! My heart feels a little fuller now.. And so does my stomach."
        window hide
        pause 2
    
        pause 2
        "light magically levitates and reconstructs the ship pulling it's severed halves together."
        pause 2
        
        show float0
        pause 1.5
        with dissolve

        show float1
        pause 1.5
        with dissolve
        
        show float2
        pause 1.5
        with dissolve

        "Scorpion and the bear stand in awe. The water has risen up to Bear's waist."
        pause 1.5
        Bear "Come with me! I don't think the rain will stop for a while."
        pause 1.5
        with dissolve
        
        show float3
        pause 1.5
        with dissolve
    
        Bear "Come with me! I don't think the rain will stop for a while!"
        
        show scene04_part_ways
        Scorpion "Hurry Jump! Bear! Climb aboard"
        show scene03_bear_ladder
        show scene03_climb_aboard
        pause 3
        show float4
        Bear "So where to friend?"
        Scorpion "That-a way!"
        pause 4

        label Act3:
        play music scene3_background_music
        show float0
        Bear "What should we do Scorpion?"
        Scorpion "Whatever it is, we have to be careful. We can use the ship for shelter but we'll need food and freshwater soon"

        menu:
            "Stay on the beach on the ship":
                show island_first
                Scorpion "Beautiful"
                Bear "(Dreamily) Yeah"
                Scorpion "Oh no! I forgot! The tides! The Full moon! Quick, back to the ship!"
                "A large wave crashes in the side of the boat and carries it further down the beach"
                Bear "We can't stay on the beach tonight"
                show scene04_water_rising
                Scorpion "Agreed. Even on the ship, we'd be dragged out to open waters when we go to sleep"
                "Another wave approaches"
            "Go into the Forest":
                show scene04_background_dialog
                Scorpion "There's still some light left. We won't be in total darkness. We cacn at least go as far as we can to see if there's potential food and freshwater close by."
                Bear "All right. I guess it's worth a try. By the way (looks around the beach) did you notice there's barely any other animals here?"
                show scene04_bear_enters_jungle
                Scorpion "Yeah. that is a bit worrying, isn't it?"
                Bear "*Sniff* I smeel something sweet not far off."
                Scorpion "That something sweet will probably still be there in the morning"
                Bear "(Nodding) let's head back and we'll go at first daylight"
        
        Bear "This behind me, is the entrance to the jungle."
        play sound scene4_jungle_noises
        show scene04_background_dialog
        pause 3.0
        play sound jaguar_snap_branch
        "(rustling)"
        pause 2.0
        stop music
        show jaguar_snarl
        play sound bear_heartbeat
        Unknown " Rrrrr who are you? Rrrrr "
        Unknown "I said, who are you? Rrrrr"
        hide jaguar_snarl
        show bear_fussy
        Bear "We just landed here. We mean no harm. We were just looking for soemthing to eat and freshwater."
        hide bear_fussy
        show jaguar_snarl
        Unknown "Rrr.. is that so? Rrrr.."
        hide jaguar_snarl
        menu:
            "Stand your ground":
                show scene04_background_dialog
                show bear_fussy
                Bear "We mean no harm. We were just looking for something to eat"
                hide bear_fussy
                show jaguar_f
                Jaguar "You're a bear. You're dangerous. Why should I let you walk free through my island"
                Bear "I may be a bear, but I am not dangerous. There's nothing to be afraid of. At least with me. But you're a jaguar. Why should you be afraid of anything?"
                Jaguar "Rrr that is none of your concern. I would ask you twhat a bear has to be afraid of"
                Bear "Unknown things perhaps. But isn't it silly ot be afraid of something you haven't even seen yet?"
                hide bear_fussy
                pause .5
                hide jaguar_f
                show scorpion1
                Scorpion "Madame, pardon our intrusion, but bear is right. You mustn’t be afraid. We’re completely harmless and will leave your island as soon as we’re refreshed and rested."
                pause 2
                hide scorpion1
                show jaguar_happy
                Jaguar "All right rrrrr follow me."
                Jaguar "Drink!"
                hide jaguar_happy
                show bear_thinking_happy
                Bear "Thankyou!"
                hide bear_thinking_happy
                show scorpion2
                pause 1
                Scorpion "Yes! Thank you so much"
                hide scorpion2
                show bear_thinking
                Bear "Breakfast? That sweet smell from last night is nearby here"
                hide bear_thinking
                show scorpion1
                Scorpion "Let's go then"
                pause 2
                hide scorpion1
                show jaguar_happy
                Jaguar "I take it you ate already?"
                hide jaguar_happy
                show bear_happy
                Bear "It seems all three of you have too"
                hide bear_happy
                pause 2
                show scorpion1
                Scorpion "Fine cubs you have there"
                hide scorpion1
                pause 2
                show jaguar_happy
                Jaguar "(Proudly) Of course! And i'd do anything to keep them safe.."
                hide jaguar_happy
                show bear_happy
                Bear "(smiles) I try to be"
                hide bear_happy
                show jaguar_cubs
                pause 2
                hide jaguar_cubs
                pause 1
                show jaguar_cubs_tada
                Flowercub "Here. you can have this. For your bravery"
                play sound heart_shard_appears
                hide jaguar_cubs_tada
                pause 1.0
                show heart_shard4
                pause 1.75
                show heart_shard5
                pause 1.75
                show heart_shard6
                pause 1.75
                hide heart_shard4
                hide heart_shard5
                hide heart_shard6
                show bear_happy
                Bear "Thank you"
                pause 2
                hide bear_happy
                show jaguar_happy
                Jaguar "Rrr. in broad daylight you don't seem so threatneing"
                Scorpion "We need to get back to the ship soon"
                Jaguar "Ill show you the way"
                hide jaguar_happy

                #fade out end of act 3
            "Run away":
                Bear "AHHHHHH"
                Scorpion "AHHHHHH"

                Unknown "AND STAY OUT!"
                pause 5
        label ending:
        play sound finale_h
        show whiteroom1
        Bear "(Confused)"
        play music finale_background_music
        pause 3
        show showroom1
        pause .75
        with dissolve
        show showroom2
        pause .75
        with dissolve       
        show showroom3
        play sound finale_head_rises
        pause .75
        with dissolve
        show showroom4
        pause .75
        with dissolve
        show showroom5
        pause .5
        with dissolve        
        show showroom6
        pause .5
        with dissolve        
        show showroom7
        pause .5
        with dissolve
        show showroom8
        pause .75
        with dissolve   
        show showroom9
        pause .75
        with dissolve          
        Bear "...?"

        menu:
            "Push the button":
                ""

        pause 2
        show b1
        pause 1.0
        show b2
        pause 1.0
        show b3
        pause 1.0
        show b4
        pause 1.0
        show b7
        play sound finale_fail_button_push
        pause 1.0
        show b6
        pause 1.0
        show b5
        pause 1.0
        show b5
        pause 1.0
        show b6
        pause 1.0
        show b7
        show showroom11
        pause 1.0
        with dissolve
        show showroom10
        pause 1.0
        with dissolve
        show showroom12
        pause 1.0
        with dissolve
        show showroom13
        pause 2.0
        with dissolve
        show showroom14
        pause 1.0
        with dissolve
        show showroom15
        pause 2.0
        show scene05_ascendant



        pause 2.0
        with dissolve
        show showroom16
        pause 2.0
        with dissolve
        show showroom17
        pause 2.0
        with dissolve
        show showroom16
        pause 2.0
        with dissolve



        show showroom18
        pause 2.0
        with dissolve
        show showroom19
        pause 5.0
        show credits01
        pause 3.0
        show credits02
        pause 3.0
        show credits03
        pause 3.0
        show credits04
        pause 3.0
        show credits05
        pause 3.0
        show credits06
        "End"
        #bear pushes button

return

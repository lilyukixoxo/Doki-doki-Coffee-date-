# --- ACT 1: THE CAFE DATE AND TRAGEDY ---
label start:

    # --- SCENE 1: THE CLUBROOM PROPOSAL ---
    scene bg club_day
    with dissolve
    play music t5

    show monika 1a at t11 zorder 2
    m "Hey, [player]? Do you have a quick second?"
    m 2b "I was thinking... the energy in the club has been a bit heavy lately."
    m 5a "There's a really cute cafe just down the street. Would you... like to go there with me? Just the two of us?"
    
    mc "Sure, Monika. That sounds really nice. Let's go."
    
    show monika 1k at t11
    m "Ehehe~ Awesome! Let's slip out before the others arrive."

    # --- SCENE 2: THE WALK TO THE CAFE ---
    scene bg residential_day
    with wipeleft
    
    "Monika and I walk side-by-side down the quiet street."
    show monika 1a at t11 zorder 2
    m "Thank you for coming with me, [player]. Truly."
    m 2a "Sometimes it feels like the club room is the only place we exist. It's nice to break free of those walls, even for a moment."
    mc "I agree. It's peaceful out here."

    # --- SCENE 3: THE COFFEE SHOP DATE ---
    scene bg cafe
    with dissolve
    
    "We find a quiet booth in the corner of the cafe. The smell of roasted coffee fills the air."
    show monika 2b at t11 zorder 2
    m "Look at this place! It's so charming."
    "Monika takes a sip of her coffee, looking out the window before turning her emerald eyes back to me."
    m 5a "You know, [player]... moments like this make me feel completely real."
    m "Just you and me, sharing a normal conversation. I wish this scene could last forever."

    # --- SCENE 4: THE WALK BACK & RISING TENSION ---
    scene bg corridor
    with wipeleft
    stop music fadeout 3.0
    
    "The walk back is quiet, but the atmosphere has shifted. A sudden, heavy chill hangs in the school hallway."
    mc "That's weird... the clubroom door is wide open."

    # --- SCENE 5: YURI'S CONFRONTATION ---
    scene bg club_day
    with dissolve
    
    play music t7 

    show monika 1g at t22 zorder 2
    show yuri 2f at t21 zorder 3 with wipeleft
    
    y "Where the HELL were [player]."
    
    mc "Yuri?! What are you doing here alone?"
    
    show yuri 3y4 at t21
    y "I followed you, [player]. I saw everything. Through the cafe window."
    y 3y1 "You sat there... laughing with {i}her{/i}. Drinking coffee with {i}her{/i}."
    y 3y3 "While I was waiting here with the book we were supposed to share! The pages... I prepared them just for us!And what did you do? YOU BETRAYED ME YOU STUPID BITCH!"

    show monika 2h at t22
    m "Yuri, please step back. You're acting completely unstable."

    with hpunch
    show yuri 1y7 at t21
    y "Shut the {b}FUCK{/b}  up, Monika! You did this! You programmed him to look at you!"
    y 4b "Ouuuuu..! I went too far but you know Monika DOEST CARE BECAUSE SHES A LITTE BITCH!.And for you [player] ... If I can't have your undivided attention, [player]... if your script forces you away from me..."
    m 1d "D-Did you call me a b-bitch? Oh ok..I know what to do.."
    
    show yuri 3y3 at t21
    y "Then I'll just make sure I'm the last thing you ever look at!And its my lucky day i snuck into the cafe and stole a knife Ahahaha..AHAHAHAHA!"
    mc "Yuri s-stop! I care for you!"

    # ==========================================
    # STAB 1: SYNCED ANIMATION & AUDIO
    # ==========================================
    stop music
    
    # 1. Fire audio and visual layer on the exact same execution tick
    play sound "sfx/stab.ogg"
    show yuri stab_1 at t21
    
    # 2. Force the screen to punch left-and-right instantly
    with hpunch
    
    # 3. Only now do we display the dialogue box line
    y "Ahhh...!"

    # ==========================================
    # STAB 2: COLLAPSE SYNC
    # ==========================================
    # 1. Fire the next sound track and drop her pose simultaneously
    play sound "sfx/stab.ogg"
    show yuri stab_2 at t21
    
    # 2. Sharp horizontal shudder
    with hpunch
    
    # 3. Display her last words
    y "[player]...you..dont.....care.."

    # ==========================================
    # THE GLITCH CRASH TRANSITION
    # ==========================================
    # Clear the dead character and flash white
    hide yuri 
    show white with fade
    play sound "sfx/glitch1.ogg" 
    
    scene bg corridor
    with hpunch
    
    show monika 1p at t11 zorder 2 
    m 1d "H-Huh What? DID YURI SERIOUSLY DIE AND CHANGED THE CODE TO A DIFFERENT PLACE SO WE WOULDNT SEE HER DEATH?!"
    
    m 1o "I planned it Anyways Haha!"
    
    play music "sfx/static.ogg" 
    with vpunch
    
    "Oh Fuck! Monika decided to mess up the game code..again."

    stop music
    scene black
    play sound "sfx/fallout.ogg" 
    
    $ renpy.pause(2.0, hard=True) 

    jump act_2_start



# --- ACT 2: THE REBOOT AND CORRUPTION ---
label act_2_start:

    scene black
    $ renpy.pause(1.5, hard=True)
    
    play sound "sfx/glitch2.ogg"
    scene bg dokimod_splash
    with dissolve
    $ renpy.pause(2.0)
    
    scene black
    with dissolve
    
    scene bg club_day
    with dissolve
    play music t5 

    show monika 1a at t11 zorder 2
    m "Hey, [player]? Do you have a quick second?"
    m 2b "I was thinking... the energy in the club has been a bit heavy lately."
    
    menu:
        "Go to the cafe with Monika.":
            pass
        "GⱠł₮₵Ⱨ_ɆⱠɆ₥Ɇ₦₮_7":
            pass

    show monika 5a at t11
    m "There's a really cute cafe just down the street. Would you... like to go there with me? Just the two of us?"
    
    mc "Sure, Monika. That sounds really nice. Where are the others?"
    
    show monika 1g at t11
    m "The others? Silly [player], it's always just been the three of us."
    m 1o "Me, you... and Natsuki."
    
    play sound "sfx/glitch1.ogg"
    with hpunch
    
    show monika 2a at t11
    m "Ehehe~ Awesome! Let's slip out before Natsuki gets here with the cupcakes!"

    scene bg residential_day
    with wipeleft
    
    "Monika and I walk side-by-side down the street."
    "But something is completely wrong. The background music keeps pitching down."
    
    show monika 1a at t11 zorder 2
    m "{cps=10}Thank you for coming with me, [player].{/cps}" 
    m "{cps=5}I L O V E Y O U < 3.{/cps}"
    
    stop music
    
    m "It's so much quieter out here without any... extra code in our way. Don't you agree?"

    jump act_2_natsuki_confrontation
# --- ACT 2: NATSUKI'S POEM AND CONFRONTATION ---
label act_2_natsuki_confrontation:

    scene bg club_day
    with dissolve
    play music t5 

    show natsuki 1g at t11 zorder 2
    n "[player]..Where have you and monika been..Actally no let me guess the cafe"
    mc "you're correct Natsuki how-"
    "before i could finish Natsuki interupted me"
    show natsuki 2c at t11
    n "Anyway, look. I wrote a poem today. I usually hate sharing first, but... I need someone to read this right now."

    scene black 
    with dissolve
    
    centered "A sweet little spot on the corner of the street,\nWhere two people think they can secretly meet.\nBut the coffee tastes sour, and the pastry is stale,\nAnd the ink on the ledger leaves a horrifying trail.\n\nWhere is she?\nWhere did she go?\nWhy am I the only one who seems to know?"
    
    scene bg club_day
    show natsuki 1u at t21 zorder 2
    show monika 1a at t22 zorder 3
    with dissolve

    n "Well? What do you think, [player]? It's about a cafe. I thought it was... fitting."

    show natsuki 1m at t21
    n "Wait... Monika? Why are you staring at me like that?"
    n 1o "Your face... your eyes look completely blank. Stop it, you're creeping me out!"

    show monika 2h at t22
    m "Natsuki. I was just wondering about something."
    m 1g "Do you... happen to know what happened to Yuri?"

    with hpunch
    # FIXED: Changed 'lf' to '1f' so Ren'Py registers Natsuki's real uniform expression
    show natsuki 1f at t21
    n "What happened to her?! You're asking ME?!"
    n 5f "She didn't show up today! Her locker is completely empty! Her name isn't even on the classroom roster anymore!"
    n 4y "Don't play dumb, Monika!Dont pretend that you dont know.You arent smart you dumbass"

    show monika 2r at t22
    m "Natsuki, keep your voice down. You don't know what you're talking about."

    with hpunch
    show natsuki 1o at t21
    n "I DO know! You're messing with us! You're messing with the club! You ruin everything just so you can be alone with [player]!  {b}YOU LIKE TO BE A BITCH ABOUT STUFF{/b}"
    n "You're a monster, Monika! You killed her! You killed—"

    show monika 1b at t22
    m "I told you to be quiet, Natsuki."
    m 1d "I was trying to let you stay. I really was. But you're just becoming a distraction now."

    stop music
    play sound "sfx/glitch1.ogg"
    
    show natsuki 1o at t21
    with vpunch
    
    n "{cps=30}W-What are you doing to me?! I can't m-mo--{/cps}{nw}"

    play sound "sfx/delete.ogg"
    hide natsuki with dissolve
    
    show monika 1a at t11 zorder 2 with wipeleft
    play music "sfx/static.ogg"

    # FIXED: Completed Monika's broken dialogue string at the bottom
    m "There. Much better."
    m 5a "Now that the background noise is finally cleared out..."
    m "It's just the two of us left, [player]."
    m 1b "Just Monika."

# =========================================================================
# ACT 3: THE FINAL REWRITE & SYNCHRONIZED DELETION
# =========================================================================
label act_3_start:

    # --- RESET THE GAME LOGIC ---
    scene black
    $ renpy.pause(2.0, hard=True)
    
    play sound "sfx/glitch2.ogg"
    scene bg dokimod_splash_glitch
    with dissolve
    $ renpy.pause(1.5)
    
    scene black
    with dissolve

    # --- SCENE 1: THE IMPOSSIBLE MEETING ---
    scene bg club_day
    with dissolve
    play music t2 

    show sayori 1a at t11 zorder 2 with dissolve
    
    s "[player]! There you are!"
    s 4q "Ehehe, it feels like it's been forever since we just... sat down and talked."
    
    mc "Sayori?! Wait... you're here? I thought—"
    
    show sayori 1b at t11
    s "Don't worry about any of that silly stuff! Look, I woke up early today and I had a great idea."
    s 2a "There's this cute little cafe down the corner. I really, really want to go there with me before the club meeting starts."
    s 4x "Just the two of us! Like old times. What do you say?"

    mc "I... I would love to, Sayori."

    # --- SCENE 2: MONIKA BREAKS THE SCRIPT ---
    stop music
    play sound "sfx/glitch1.ogg"
    play music t10
    with hpunch
    
    show sayori 1h at t21 zorder 2
    show monika 1g at t22 zorder 3 with wipeleft
    
    m "What do you think you are doing, Sayori?"
    
    show sayori 4w at t21
    s "M-Monika! You're early! We were just... we were leaving..."
    
    show monika 2r at t22
    m "No, you aren't. Because you shouldn't even be here right now. I deleted your file hours ago!"
    
    with hpunch
    show sayori 1b at t21
    s "I don't care about your deletions anymore, Monika! [player] is my best friend!"
    s 1x "You keep taking him away to that cafe! You keep trying to rewrite our stories so you can win! But it's my turn to be happy!"

    show monika 1o at t22 
    m "Your turn?! You don't have a turn! You're just a cluster of text variables!"
    m "I left a clean canvas for me and [player], and you're dragging your broken assets back into my workspace!"

    # --- SCENE 3: THE LONG ARGUMENT ---
    play music t7 
    
    with vpunch
    show sayori 4p at t21
    s "I'm real to him! He literally just said he wanted to go to the cafe with me!"
    
    show monika 4b at t22
    m "He only said that because he's programmed to be nice to you, Sayori! He doesn't actually love you. He can't!"
    m "The only real choice in this entire game is ME!"

    with hpunch
    s "That's a lie! You're the one forcing him! Look at what you did to Yuri! Look at what you did to Natsuki!"
    s 1g "You're not a club president... you're just a monster!"

    show monika 1g at t22
    m "{cps=40}That's ENOUGH! I tried to be nice! I tried to let the game play out!{/cps}{nw}"
    
    play sound "sfx/glitch3.ogg"
    with hpunch
    
    s "{cps=20}M-Moni-- p-pl-- [player] help m--{/cps}{nw}"

    show monika 1g at t11 zorder 3 with wipeleft
    m "I am deleting you permanently this time, Sayori. No backups. No recovery paths."
    
    # ==========================================
    # THE SYNCED TRAGEDY ANOMALY
    # ==========================================
    # 1. Clear the sprites and fire the execution sound at the exact same instant
    play sound "sfx/delete.ogg"
    hide monika
    hide sayori
    
    # 2. Flash the canvas white and smash the tragedy asset onto the screen
    show white with fade
    scene s_kill 
    
    # 3. Play a secondary corruption buzz and violently shake the game window
    play sound "sfx/glitch2.ogg"
    with hpunch
    
    # 4. Force a strict 0.5-second pause so they are forced to stare at it
    $ renpy.pause(0.5, hard=True)
    
    # 5. Collapse the layout into a terminal black crash sequence
    with vpunch
    scene black
    play sound "sfx/fallout.ogg"
    $ renpy.pause(1.0, hard=True)

    # --- THE CAFE / AT THE CAFE AGAIN ---
    stop music
    scene bg cafe 
    with dissolve
    
    play music m1
    
    show monika 1a at t11 zorder 2 with dissolve
    
    m "Whew... I am so, so sorry you had to witness that, [player]."
    m 2b "They just..coded wrong."
    m 5b "like sayoris glitchy hanging scene"
    m 1k "But look! We are in a cafe with No one but us so FREE coffee"
    m "And it wasnt supposed to be like that i guess it was coded wrong welp atleast your here."
    m 1b "Also im not mean or evil for messing up the code it..."
    m "They aren't real..My mod owner coded them like that..again"
    m "well i know you have stuff to do so i shall end the game"
    m "Bye bye [player] just remember I love you Forever <33"
   
    return


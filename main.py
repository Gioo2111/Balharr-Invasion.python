import os
story = {
    "current_scene": "begin",
    "begin": {
        "story": """

            .     .       .  .   . .   .   . .    +  .
        .     .  :     .    .. :. .___---------___.
            .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
          .  :       .  .  .:../:            . .^  :.:\.
              .   . :: +. :.:/: .   .    .        . . .:\
      .  :    .     . _ :::/:               .  ^ .  . .:\
        .. . .   . - : :.:./.                        .  .:\
        .      .     . :..|:                    .  .  ^. .:|
          .       . : : ..||        .                . . !:|
        .     . . . ::. ::\(                           . :)/
      .   .     : . : .:.|. ######              .#######::|
        :.. .  :-  : .:  ::|.#######           ..########:|
      .  .  .  ..  .  .. :\ ########          :######## :/
        .        .+ :: : -.:\ ########       . ########.:/
          .  .+   . . . . :.:\. #######       #######..:/
            :: . . . . ::.:..:.\           .   .   ..:/
        .   .   .  .. :  -::::.\.       | |     . .:/
            .  :  .  .  .-:.":.::.\             ..:/
      .      -.   . . . .: .:::.:.\.           .:/
      .   .   .  :      : ....::_:..:\   ___.  :/
        .   .  .   .:. .. .  .: :.:.:\       :/
          +   .   .   : . ::. :.:. .:.|\  .:/|
          .         +   .  .  ...:: ..|  --.:|
      .      . . .   .  .  . ... :..:.."(  ..)"
      .   .       .      :  .   .: ::/  .  .::\


        Aliens invaded earth and started their world domination plans. You got caught but escaped and killed the Balharry that captured you.
        Now, you are stuck inside their mothership, but with an advantage: Nobody knows you are here.
        Your mission is to get to the navigation room and send them back to where they came from.
        But remember, each decision will take you to a completely different scenario, and acting carelessly may and will lead you to death.
        So be careful, and good luck.
        

        You are currently in the floor-level of the spaceship, in a small and cold room with only you and the dead Balharry. Will you:
        """,
        "choices": [
            {"choice": "Search the Body", "destination": "getGun"},
            {"choice": "Leave the room immediately", "destination": "noGun"},
            {"choice": "Explore the mothership through the ventilation system", "destination": "vent"},
        ],
    },
    "getGun": {
        "story": """
                                 __ 1      1 __        _.xxxxxx.
                 [xxxxxxxxxxxxxx|##|xxxxxxxx|##|xxxxxxXXXXXXXXX|
 ____            [XXXXXXXXXXXXXXXXXXXXX/.\||||||XXXXXXXXXXXXXXX|
|::: '-------.-.__+=========---___/::::|::::::|::::||X O^XXXXXX|
|::::::::::::|2|%%%%%%%%%%%%\::::::::::|::::::|::::||X /
|::::,-------|_|~~~~~~~~~~~~~'---=====-------------':||  5
 ~~~~                       |===|:::::|::::::::|::====:\O
                            |===|:::::|:.----.:|:||::||:|
                            |=3=|::4::''::::::'':||__||:|
                            |===|:::::::/  ))\:::'----':/
                            '===|::::::|  // //~'######b
                                '--------=====/  ######B
                                                 '######b
                                                  #######b
                                                  #######B
                                                  '#######b
                                                   #######P
                                                   '#####B


        You found a laser gun! Really lucky... Now, which way will you go?
        """,
        "choices": [
            {"choice": "Leave the room immediately", "destination": "leaveRoom"},
            {"choice": "Explore the mothership through the ventilation system", "destination": "ventGun"},
        ],
    },
    "leaveRoom": {
        "story": """
                     o   o                                         
                      )-( 
                     (O O)                                        
                      \\=/ 
                     .-"-. 
                    //\\ /\\ 
                  _// / \\ \\_ 
                 =./ {,-.} \\.= 
                     || || 
                     || ||    
                  _ _|| ||__   
                  '---" '---'


        You slowly open the door to a poorly lit hallway, it is really elongated and full of doors.
        They look all the same, and you take some time to think about where you should go first.
        Interrupting your thoughts, you hear two aliens approaching from the end of the hallway.
        """,
        "choices": [
            {"choice": "Aim at the end of the hallway with your laser gun", "destination": "gunFail"},
            {"choice": "Enter the closest door to you", "destination": "hallwayDoor"},
        ],
    },
    "gunFail": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  


        You aim confidently at the voices, and when the two Balharry appear, you pull the trigger.  
        The gun did not work, and you try desperately to shoot again and again and again,  
        but as your attempts fail, they quickly take their guns and shoot you.  
        You died with multiple laser beams ripping through your body.


        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "hallwayDoor": {
        "story": """
        You quickly open the first door you can and hide inside quietly. The room is completely dark,  
        but before looking around you sit in silence waiting for the aliens in the hallway to leave.  
        It doesn't take long, as they walk past you without saying a word to each other.  
        "Do they even talk?", you wonder as you try to feel the room for something useful.  
        You feel some kind of switch, wondering if you should pull it...
        """,
        "choices": [
            {"choice": "Yes", "destination": "labOnGun"},
            {"choice": "No", "destination": "labOffGun"},
        ],
    },
    "labOnGun": {
        "story": """
                                       ||              []
                                    __ ||              []
                                    || ||              []
                                  .-||-||-.            [] 
                                 _\\_______/_===========[]=(-o)
                                  )\\_____/(            []  
                                 /     ||  \\           []
                                /      ||   \\          []
                               /       ||    \\         []
                              /~~~~~~~~~~~~~~~\\        []
                             /         ::      \\       []
                            (          ::       )      []
                             '-----------------'       []
                                     )                 []
                                   (   )               []
                                     )( . (            []
                                  .) @@)   )           []
                               ' ) @@(@@)@             []
                                 (@@(@@)@              []
                                  @(@.@)@@             []
                                ' (@{__}@)'            []
                                    :__;               []
                ___                  {}+               []
               ( = )             .---''---.            []
                | |_            /          \\   ________[]____
             ___| |_|==========(____________)_/______________\\


        You pull it and the lights turn on to reveal what seems to look like a science lab, full of flasks filled with colorful liquids,
        weird rocks, plants and etcetera. You take a look around just to find two beds in the corner of the lab and two Balharry sleeping peacefully in it.
        Fortunately for you, they seem to be in a very heavy sleep completely undisturbed by your presence,
        but you decide to be more careful to not wake them up. Close to them, you find a table with four flasks containing each a different liquid.
        Knowing nothing about alien nor human chemistry, which one of them will you pick?
        """,
        "choices": [
            {"choice": "Purple Flask", "destination": "flaskGoodGun"},
            {"choice": "Green Flask", "destination": "flaskGoodGun"},
            {"choice": "Orange Flask", "destination": "flaskBadGun"},
            {"choice": "Blue Flask", "destination": "flaskBadGun"},
        ],
    },
    "flaskGoodGun": {
        "story": """
        You pick the flask and take another look around to see if there is anything else that can be useful.
        On one of the top shelves you see what looks like a syringe filled with a bright green liquid.
        It could be really useful, but to reach it you'll need to stand over the table and climb the shelves, which can be dangerous.


                                            |
                      ,------------=--------|___________|
     -=============%%%|         |  |______|_|___________|
                      | | | | | | ||| | | | |___________|
                      '------------=--------|           |
                                            |


        Will you attempt to reach the syringe?
        """,
        "choices": [
            {"choice": "No, it's too dangerous", "destination": "leaveSyringeGun"},
            {"choice": "A flask AND a syringe, why not?", "destination": "takeSyringeGG"},
        ],
    },
    "takeSyringeGG": {
        "story": """
        You balance yourself over the table and start climbing. You firmly grab the bottom shelves and start going up.
        Suddenly, one of the shelves breaks and everything else collapses and falls to the ground, including yourself, who fell on the table and broke it.

            .-****-.        .-****-.
           /        \\      /        \\
          /_        _\\    /_        _\\
         // \\      / \\\\  // \\      / \\\\
         |\\__\\    /__/|  |\\__\\    /__/|
          \\    ||    /    \\    ||    /
           \\        /      \\        /
            \\  __  /        \\  __  /
             '.__.'          '.__.'
              |  |            |  |
              |  |            |  |

        You stand up and anxiously look back to the sleeping scientists, thinking that no one could stay asleep after such a mess.
        They are, in fact, staring directly at you in a mix of confusion and fear. They appear to be unarmed, and the only gun you see is the one on the table.
        One of them quickly tries to reach for it. Now think fast and act faster!
        """,
        "choices": [
            {"choice": "Throw the flask at them", "destination": "labDeathThrow"},
            {"choice": "Drink the flask", "destination": "drinkFlask"},
            {"choice": "Shoot them", "destination": "gunFail2"},
        ],
    },
    "flaskBadGun": {
        "story": """
        You pick the flask and take another look around to see if there is anything else that can be useful.
        On one of the top shelves you see what looks like a syringe filled with a bright green liquid.
        It could be really useful, but to reach it you'll need to stand over the table and climb the shelves, which can be dangerous.


                                            |
                      ,------------=--------|___________|
     -=============%%%|         |  |______|_|___________|
                      | | | | | | ||| | | | |___________|
                      '------------=--------|           |
                                            |


        Will you attempt to reach the syringe?
        """,
        "choices": [
            {"choice": "No, it's too dangerous", "destination": "leaveSyringeGun"},
            {"choice": "A flask AND a syringe, why not?", "destination": "takeSyringeBG"},
        ],
    },
    "takeSyringeBG": {
        "story": """
        You balance yourself over the table and start climbing. You firmly grab the bottom shelves and start going up.
        Suddenly, one of the shelves breaks and everything else collapses and falls to the ground, including yourself, who fell on the table and broke it.


            .-****-.        .-****-.
           /        \\      /        \\
          /_        _\\    /_        _\\
         // \\      / \\\\  // \\      / \\\\
         |\\__\\    /__/|  |\\__\\    /__/|
          \\    ||    /    \\    ||    /
           \\        /      \\        /
            \\  __  /        \\  __  /
             '.__.'          '.__.'
              |  |            |  |
              |  |            |  |

              
        You stand up and anxiously look back to the sleeping scientists, thinking that no one could stay asleep after such a mess.
        They are, in fact, staring directly at you in a mix of confusion and fear. They appear to be unarmed, and the only gun you see is the one on the table.
        One of them quickly tries to reach for it. Now think fast and act faster!
        """,
        "choices": [
            {"choice": "Throw the flask at them", "destination": "throwFlask"},
            {"choice": "Drink the flask", "destination": "labDeathDrink"},
            {"choice": "Shoot them", "destination": "gunFail2"},
        ],
    },
    "gunFail2": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  


        You aim your gun at the alien and pull the trigger before he can reach the table,  
        but nothing comes out of it, and you realise the gun you've been carrying is not working.  
        That explains why the Balharry that had it is dead...  
        You died when the scientist reaches his gun and shoots your head, exploding your brain.


        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end_game"},
        ],
    },
    "labOffGun": {
        "story": """
        You decide that whatever is inside that room must be left alone.  
        After waiting a little more, you open the door and return to the hallway.  
        All the doors seem to look the same. You walk a little more, finding one with a different color than the others and decide to open it.  
        It looks like a security room, full of screens and cameras. You can see the corridor you were before,  
        the dark room you probably entered before, and all kinds of rooms.  
        You search for one that resembles a navigation room, but everything looks confusing, although three rooms catch your attention:  
        The first one is a room filled with cryogenic chambers with humans inside of it.  
        You really want to save them before leaving the ship and look around to find any other humans.  
        The second one is a room full of equipment, protective suits, bigger guns, and all sorts of technologic devices that could really help you right now.  
        The third one is a room with a flashing light, buttons, wires, and energy generators, probably an electricity room.  
        Unlike the other two, there are no aliens there.  
        There is also an entry to the ventilation system right behind you that can be useful to get to some of these rooms,  
        and you can see a dim red light coming from inside it.  
        So, which way are you going? 
        """,
        "choices": [
            {"choice": "Cryo room", "destination": "cryoRoom" },
            {"choice": "Tech room", "destination": "techRoom" },
            {"choice": "Electricity room", "destination": "electricRoom" },
            {"choice": "Go for the red light", "destination": "prisonCell" },
        ],
    },
    "vent": {
        "story": """
        You crawl inside the ventilation system. It is small but big enough to fit a human.  
        Inside, you can only go right, and then keep going forward. You can see what's going on under you from the gaps.  
        It looks like a dark hallway, and you haven't found anything that gives you a clue to where the navigation room is.  
        Completely clueless, the ventilation now only goes two ways:  
        To the right, where you can see a red light from a short distance,  
        while to the left, you see nothing but pure darkness.  
        Which way are you choosing?
        """,
        "choices": [
            {"choice": "Right", "destination": "prisonCell" },
            {"choice": "Left", "destination": "fanDeath" },
        ],
    },
    "prisonCell": {
        "story": """
                                   ###########                  /
                 \\                  #########                  /
                  \\                                           /
                   \\                                         /
                    \\                                       /
                     \\                                     /
                      \\                                   /
                       \\_________________________________/
                       |                                 |
                       |                                 |
                       |                                 |
                       |            _________            |
                       |           |         |           |
                       |           |   ___   |           |
                       |           I  |___|  |           |
                       |           |         |           |
                       |           |         |           |
                       |           |        _|           |
                       |           |       |#|           |  
               -- ___  |           |         |           |  
                 /   ' |           |         |      _____|    
               */     )|           I         |     \\_____\\    
               /___.,';|           |         |     \\\\     \\     
               |     ; |___________|_________|______\\\\     \\      
               | ._,'  /                             \\\\     \\      
               |,'    /                               \\\\     \\
               ||    /                                 \\\\_____\\
               ||   /                                   \\_____|
               ||  /              ___________                \\


        You follow until you reach the red light you've seen before. You look under you  
        to see a small room with a reinforced door, simple and few furniture, and an alien inside it.  
        From your perspective, it looks like a jail cell, and that alien must be the prisoner.  
        This one looks very different from the one that captured you, with different shape,  
        color, size, and features, probably from another planet.  
        He suddenly looks up directly at you and whispers something you cannot comprehend.
        Now, what will you do?
        """,
        "choices": [
            {"choice": "Ignore him and keep going", "destination": "cryoRoom" },
            {"choice": "Pull him up to the ventilation", "destination": "escapeCell" },
        ],
    },
    "escapeCell": {
        "story": """
        ______              ______
       /___   \\___\\ || /___/   ___\\
      //\\]/\\ ___  \\||//  ___ /\\[\\//
      \\\\/[\\//  _)   \\   (_  \\\\/[\\//
       \\___/ _/   o    o   \\_ \\___/
           _/                \\_
          //'VvvvvvvvvvvvvvvV'\\\\
         ( \\.'^^^^^^^^^^^^^^'.\\ )
          \\____   . .. .   ____/
               \\ . .'' . . /
                )________(


        You manage to easily unscrew the ventilation grid, and once he notices the ventilation is now open he extends his hand and you pull him up. 
        He gives you an intimidating stare that unsettles you, then does a big smile that makes you a little less worried.
        Before you can try to communicate he crawls through the ventilation and you just follow him.
        Suddenly, he stops and stare at the top of the ventilation duct you are currently in.
        He starts punching above where you are. He is incredibly strong, and you think how you are lucky to have him on your side.
        With only four punches he opens a hole, stands up and climbs inside the room. Before you could follow him,
        you hear laser beams and a lot of things breaking and falling to the ground.
        You stay hidden and all the noise stopped after about thirty seconds.
        You spy and see the alien you just met is still alive, but doesn't seem to mind your company.
        Were will you go?
        """,
        "choices": [
            {"choice": "Enter the room with him", "destination": "councilRoom"},
            {"choice": "Keep going through the ventilation", "destination": "cryoRoom"},
        ],
    },
    "councilRoom": {
        "story": """
        You enter the room. It has a big conference table in the center and a lot of chairs,
        some of them occupied by dead Balharry. You can also see what looks like tv and radios.
        There is a lot of blue blood, broken tvs and dead aliens all around the room, but your "friend" is still alive and appears to be searching for something.
        He acknowledges you and points to the radio. Suddenly, an alien voice speaks from it in an undistinguishable language.
        You feel that you have to say something, but don't know what to say...
        - All yours leaders are dead, and there is nothing for you in this planet - You say in your deepest voice - leave now, before it's too late.
        Some seconds of silence, then you hear a laugh and a response you cannot comprehend. You look at the alien hoping for a answer,
        and as he nods his head you finally realise it: They are not leaving this easily.
        All the comunication systems turn off, and the alien seems to have found what he wanted.
        He takes some papers and before leaving, gives you one of them: It's a map.
        You're not sure how to read it, but you find out you are in the second floor.
        Across this Council room, there is another lab, and you see the alien going there.
        A few steps away, there is a Tech room, or you could go down the stairs.
        Will you enter the lab with him or will you go another way?
        """,
        "choices": [
            {"choice": "Enter the lab", "destination": "cloneRoom"},
            {"choice": "Go to tech room", "destination": "techRoomAlien"},
            {"choice": "Go downstairs", "destination": "raidDeath"},
        ],
    },
    "raidDeath": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  


        You go downstairs, looking for where to go next.
        Suddenly, a bunch of Balharry burst through a door, and you cannot hide in time.
        You died being shot by the Balharry soldiers' rifles.
        

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "techRoomAlien": {
        "story": """
        You enter the tech room quietly, but the Balharry inside quickly notice you.
        You close the door and run back to the council room, then hides inside the ventilation you came from.
        You hear they coming after you, but before they enter the council room you hear laser beams and screams coming from the lab.
        Too scared to leave the room, your only way is the ventilation ahead of you.
        You keep walking and all the ventilation grids seem too small to fit you, until you find one that you can get in.
        As you get close to it, the cold air coming from the grid gives you shivers, and as you look down to inspect you see what a mess is in there.
        All the aliens are running around, grabbing their guns and leaving the room.
        There are a lot of cryogenic chambers, and inside them you see humans, just like you.
        You feel frightened but is able to pull yourself together. Now there's only one alien in the room reading some documents,
        conveniently positioned below you, and at least 50 humans down there.
        You silently unscrew the grid and jump over the alien. He seems really scared and tries to get you off him.
        He is really strong, but your years of training make you stronger. You don't know what to do to make him stop,
        so you grab a pencil from his desk and stab him until he stops struggling.
        That was brutal... But it's not like you had other choices. Now, you have some blueish liquid sticking to your arms.
        You decide to clean his blood before it can do something to you.
        Now that you are clean, you search for anything that could free these humans.
        You find a switch, pull it without hesitation and all the cryogenic chambers open. The humans start to slowly regain consciousness and stand up.
        - Are we free? - One of them asks.
        - Not yet - you respond - I have to find the navigation room and send them back.
        - We could also grab some guns and kill them ourselves. When the aliens were bringing me here, I could see them coming downstairs with guns.
        - That means - he continues explaining his idea - that there are a lot of guns upstairs that we could use. I know it's dangerous, but what else could we do?
        He has a point, will you consider his idea or just lead them to the exit: The room you killed the first Balharry?
        """,
        "choices": [
            {"choice": "Go upstairs", "destination": "humansUpstairs"},
            {"choice": "Take them to safety", "destination": "exitRoom"},
        ],
    },
    "techRoom": {
        "story": """
        You make your way to the tech room and enter it quietly, but the Balharry inside quickly notice you.  
        You close the door and hide in the ventilation next to the door.  
        You hear they coming after you, but before they look inside the ventilation you hear laser beams and screams coming from the lab.  
        Too scared to leave, your only way is the ventilation ahead of you.  
        You keep walking and all the ventilation grids seem too small to fit you, until you find one that you can get in.  
        It's the cryogenic room, with only one alien in the room reading some documents conveniently positioned below you.  
        You silently unscrew the grid and jump over the alien. He seems really scared and tries to get you off him.  
        He is really strong, but your years of training make you stronger. You don't know what to do to make him stop,  
        so you grab a pencil from his desk and stab him until he stops struggling.  
        That was brutal... But it's not like you had other choices. Now, you have some blueish liquid sticking to your arms.  
        You decide to clean his blood before it can do something to you.  
        Now that you are clean, you search for anything that could free these humans.  
        You find a switch, pull it without hesitation and all the cryogenic chambers open. The humans start to slowly regain consciousness and stand up.  
        - Are we free? - One of them asks.  
        - Not yet - you respond - I have to find the navigation room and send them back.  
        - We could also grab some guns and kill them ourselves. When the aliens were bringing me here, I could see them coming downstairs with guns.  
        - That means - he continues explaining his idea - that there are a lot of guns upstairs that we could use. I know it's dangerous, but what else could we do?  
        He has a point, will you consider his idea or just lead them to the exit: The room you killed the first Balharry?
        """,
        "choices": [
            {"choice": "Go upstairs", "destination": "humansUpstairs"},
            {"choice": "Take them to safety", "destination": "exitRoom"},
        ],
    },
    "techRoomGroup": {
        "story": """
        You enter the room with the group, shooting the Balharry in there. Fortunately, no one in the group was harmed.  
        All you can see are high tech equipments: Protective suits, jetpacks, and bigger guns.  
        There are enought jetpacks for all the group, so everyone takes one. A huge machine gun caught your attention, so you take switch your rifle for it.  
        Now that the group is better equipped, you can leave and look for the navigation room with no fear.  
        On your way out, one of your companions hands you a pendrive that they've found, so you keep it since it can be important later.  
        Back to the corridor, the sirens are on and all the Balharry are coming for you, but you take them down easily.  
        You get to the end of the hallway and see a big door. You open it and is a room filled with smaller spaceships and, of course, Balharry.  
        Your group shoots them all and the conflict is over quick, but few of you perished in the battle.  
        This room is open like a garage and the spaceships can fly out. You could use the spaceships to attack the Balharry outside,  
        But you could make the humans leave the spaceship with jetpacks and go to the navigation room,  
        the left door in the end of the hallway according to the mothership map stuck to the wall.  
        What is your decision?
        """,
        "choices": [
            {"choice": "Enter the spaceships and shoot them", "destination": "spaceshipEnd"},
            {"choice": "Enter the navigation room", "destination": "navigationRoom"},
        ],
    },
    "spaceshipEnd": {
        "story": """
              _,--=--._
            ,'    _    '.
           -    _(_)_o   -
      ____'    /_  _/]    '____
-=====::(+):::::::::::::::::(+)::=====-
        (+).***************,(+)
            .           ,
              '  -=-  '


        You gather the group around the spaceships and assign a pair to each one. You enter yours alone, turn it on and fly into the sky.  
        The city has no humans, they must be hidden in shelters or somewhere else, so you aim at the first Balharry spaceship you see and press one button.  
        Two strong laser beams come from your ship, so you learn how it works and shoot every Balharry you can see, and your group does the same.  
        A strong laser coming from the mothership almost hits you, so you aim at it and shoot.  
        You are not doing much alone, but then all the other ships turn to the mothership and shoot. It doesn't resist for much time,  
        so it explodes and now all the Balharry are dead. The earth is now safe thanks to your teamwork and leadership.  


        Thanks for playing.
        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "navigationRoom": {
        "story": """
        You tell the group they should leave the mothership now, they obey and jump through the opening with their jetpacks.  
        You get out the room with your machine gun, jetpack and the pendrive and quickly enter the navigation room.  
        Before they could notice you, you kill three Balharry in the room and leave only one alive.  
        You point your gun to his head and tell him to make the mothership go away. You hope he understood what you said,  
        because he starts typing on the keyboard and presses a button. You hear the spaceship's engines turning on,  
        the Balharry takes his gun and before you could shoot him, he shoots himself in the head.  
        A metal grid locks the door and the room's light starts flashing red, you see a gas coming from the ceiling and you hold your breath.  
        The computer is still on, and the screen has one button to click. You are getting out of breath and out of options.  
        What will you do?
        """,
        "choices": [
            {"choice": "Plug the pendrive in the computer", "destination": "navigationEnd"},
            {"choice": "Press the button", "destination": "navigationDeath"},
        ],
    },
    "navigationDeath": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  


        You press the button and the computer shuts off.  
        You desperately look for a way to open the door until you can't hold your breath anymore.  
        You died breathing the poisonous gas and bleeding from your nose and mouth until you can't breathe anymore.
              

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "navigationEnd": {
    "story": """
                              .-"L"-.  
      .--""L""---___    J  |  |
      J    J        ""L  L J  J              J----***J**---__
       |    |         J  J  L  L_--""|"--L   |       F      J
        L    L__ ___   L  L |  J     |   J   F      J       F
     \\*******   |   *****-----, L    |   J  J       F      |
      \\          L            L L    |   |  |      J      J      _.---***
       \\         J            | |    |   |  F      F      F     /
        \\         |           J |    |   | J      J      |     /
         \\         L      ___---++...;.++'--__    F     J     /
          \\        J      L**----____ __---**J__--=----_E_   /
           \\        |     J          |       |--__   __--*/ /
      __    \\        L     L         |       F    **F    / /
        ***--__      J     J         |      J      |    / /
               **;    |     L        |      |     J    / /
          __--*** \\    L    J        |      F     F   / /
    __--""         \\   J     L       |     J     |   / /
--**                \\   |    J       |      |    J   / /
                     \\   L    L      |     F    F  / /
                      \\  J    J      |    J    |  / /
                       \\  |    L     |    |   J  / /
                        \\  L   J     |    F   F / /
                         \\ J    L    |   J   | / /
                          \\ |  _J    |   |"-J+' /
                           \\-L"  L   |   F     /
                            \\    J   |  J     /
    '-.                      \\    "-.|+'     /
       '-.                    \\             /                   .
          '-.                  \\           /                 .-'
             '-.             .-'            "-.           .-'
                '-.       .-'        .         "-.     .-'
                   '-. .-'         .' '.          '-.-'
                      '          .'     '.


        You plug the pendrive in the computer, and the smoke immediately stops coming out, the door opens, and the room ventilates again.  
        You press the button in the computer and now the engines start making way more noise, until you feel the mothership shaking and flying away.  
        You run out of the room to take your chance to escape. Five Balharry are running in the navigation room's direction,  
        but you laser them before they could get close. You enter the spaceship room and start turning on your jetpack and running to the opening.  
        The spaceship is pretty high in the sky, and you are really scared to jump, but the longer you take, the worse it'll be.  
        You dive out of the mothership and fly into the sky. You can see the city, the ships following the mothership going away,  
        and the remaining Balharry being killed by the army. You were able to send them back to where they came from and save Earth.  

        Thanks for playing.
        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "cloneRoom": {
        "story": """
        -._    _.--'"''--._    _.--'"''--._    _.--'"''--._    _  
'-:'.'|''|"-:.  '-:'.'|''|"-:.  '-:'.'|''|"-:.  '.' : '.  
'.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '.  '.  
: '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : '.  '.  
'   '.  '.:_.|:.'.' '.  '.:_.|:.'.' '.  '.:_.|:.'.' '.  '.'   '.  
       '-..,..-'       '-..,..-'       '-..,..-'       '         '  


        You decide to follow the alien, and as you've seen he's a threat to the Balharry, you'll probably be safer with him around.  
        This lab is different. It has no flasks or chemicals, only a big chamber in the center connected to a machine.  
        The alien goes to the machine and starts reading the papers he got before. He then presses some buttons and makes a noise looking and waving at you.  
        You approach him, and he gives you his gun and a piece of paper. You cannot read it,  
        but see an image of a lever that looks just like the one this machine has.  
        Then, he gets inside the chamber and closes the door. He signals you a lever motion and you unhesitatingly pull it.  
        The chamber locks and starts glowing a green light from it. It starts making loud noises and you can see a needle stick his skin and take his blood.  
        This tube containing his blood lightens and you can see it goes through another machine and all across the room,  
        arriving at three other chambers in the corner you couldn't see before.  
        Suddenly, the lab door opens and two Balharry are aiming at the chamber. You shoot them both with the gun he gave you and stay vigilant until whatever is happening in this chamber ends.  
        More Balharry appear, and you quickly eliminate them. The spaceship sirens start ringing but the chamber finally stops making noises and its door opens.  
        The alien comes out of it and the other three chambers open, too. Another three aliens identical to this one come out of them.  
        One of the clones goes inside the main chamber, the other pulls the lever and they start cloning themselves again and again.  
        Five minutes have passed and you are now with around sixteen aliens. They all leave the room except for two, that stay cloning themselves.  
        They all enter the tech room. Will you follow them or go downstairs?
        """,
        "choices": [
            {"choice": "Enter the tech room", "destination": "techRoomGroup"},
            {"choice": "Go downstairs", "destination": "raidDeath"},
        ],
    },
    "ventGun": {
        "story": """
        You crawl inside the ventilation system. It is small but big enough to fit a human.  
        Inside, you can only go right and then keep going forward. You can see what's going on under you from the gaps.  
        It looks like a dark hallway, and you haven't found anything that gives you a clue to where the navigation room is.  
        Completely clueless, the ventilation now only goes two ways: to the right, where you can see a red light from a short distance,  
        while to the left you see nothing but pure darkness.  
        Which way are you choosing?
        """,
        "choices": [
            {"choice": "Right", "destination": "prisonCellGun"},
            {"choice": "Left", "destination": "fanDeath"},
        ],
    },
    "fanDeath": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  


        You follow in the darkness and suddenly lose your step.  
        You have quite a long fall to regret your choice before colliding with the high-speed fans from the main ventilation room.  
        You died falling in the ventilation room's fans that tore you apart.
              

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "prisonCellGun": {
        "story": """
                                   ###########                  /
                 \\                  #########                  /
                  \\                                           /
                   \\                                         /
                    \\                                       /
                     \\                                     /
                      \\                                   /
                       \\_________________________________/
                       |                                 |
                       |                                 |
                       |                                 |
                       |            _________            |
                       |           |         |           |
                       |           |   ___   |           |
                       |           I  |___|  |           |
                       |           |         |           |
                       |           |         |           |
                       |           |        _|           |
                       |           |       |#|           |  
               -- ___  |           |         |           |  
                 /   ' |           |         |      _____|    
               */     )|           I         |     \\_____\\    
               /___.,';|           |         |     \\\\     \\     
               |     ; |___________|_________|______\\\\     \\      
               | ._,'  /                             \\\\     \\      
               |,'    /                               \\\\     \\
               ||    /                                 \\\\_____\\
               ||   /                                   \\_____|
               ||  /              ___________                \\


        You follow until you reach the red light you've seen before. You look under you  
        to see a small room with a reinforced door, simple and few furniture and an alien inside it.  
        From your perspective, it looks like a jail cell, and that alien must be the prisoner.  
        This one looks very different from the one that captured you, with different shape, color, size, and features, probably from another planet.  
        He suddenly looks up directly at you and whispers something you cannot comprehend.  
        Now, what will you do?
        """,
        "choices": [
            {"choice": "Throw him the gun", "destination": "giveGun"},
            {"choice": "Ignore him and keep going", "destination": "cryoRoom"},
            {"choice": "Pull him up to the ventilation", "destination": "escapeCell"},
        ],
    },
    "giveGun": {
        "story": """
                     (_)  (_)                  <> \\  / <>
                      .\\::/.                   \\_/\\  \\_/\\
     .:.          _.=._\\\\//_.=._                  \\\\//
..   \\o/   ..      '=' //\\\\ '='             _<>_\\\\_<>/_/_<>_
:o|   |   |o:         '/::\\'                 <> / /<>\\ \\ <>
 ~ '. ' .' ~         (_)  (_)      _    _       _ //\\\\ _
     >O<             '      '     /_/  \\\\_     / /\\  /\\ \\
 _ .' . '. _                        \\\\//       <> /  \\ <>
:o|   |   |o:                   /\\_\\\\><\\\\ \\
     ':'
                                  _//\\\\_
                                  \\\\_/\\_/ 

        You throw the gun between the ventilation grid and he catches it. As he points it to the door and pulls the trigger,  
        the gun does not work. He then grabs the lamp in his cell, rips its wires off, grabs some metal from it, and repairs the gun.  
        He shoots the door, making a hole larger than you were expecting, leaves, and all you can hear are sirens and plenty of laser beams.  
        You should probably keep going now that the chaos is installed in the mothership, and since the only way to keep going is forward, you follow without looking back...  
        You keep walking, and all the ventilation grids seem too small to fit you until you find one that you can get in.  
        As you get close to it, the cold air coming from the grid gives you shivers, and as you look down to inspect you see what a mess is in there.  
        All the aliens are running around, grabbing their guns, and leaving the room. There are a lot of cryogenic chambers, and inside them, you see humans, just like you.  
        You feel frightened but are able to pull yourself together. Now there's only one alien in the room reading some documents, conveniently positioned below you, and at least 50 humans down there.  
        What will you do?
        """,
        "choices": [
            {"choice": "Unscrew the grid and jump over the Balharry", "destination": "cryoRoomEmpty"},
            {"choice": "Keep going through the ventilation", "destination": "electricRoom"},
        ],
    },
    "electricRoom": {
        "story": """
             ___
         .-"'"   '"-.
       .'    .-.    '.
      /     (/^\\)     \\
     /  #   (\\ /)      \\
     | #    .-'-.      |
     |     /(_I_)\\     |
     ;     \\\\) (//     ;
      ;     / Y \\     ;
       \\    \\ | /    /
        \\    \\|/    /
         \\   /|\\   /
          |  \\|/  |
          |__/Y\\__|
          {=======}
          }======={
          {=======}
          }======={
          {=======}
           '""u""'

        You crawl the ventilation and find a grid that takes you to a flashing light room. It is the electricity room of the spaceship.  
        All those buttons and energy generators are a bit overwhelming, and you don't know what to do.  
        Then you come up with a brilliant idea: Destroying all of it! What else could you do that would put the Balharry in more trouble than that?  
        You start pulling all the wires and cables, kicking the generators, and pressing all the buttons until you've made a big mess.  
        The light stops flashing, and you unlock the door from inside, going back to the hallway.  
        You can see nothing; the mothership is now in complete darkness, and you wonder if your decision was brilliant after all.  
        The silence is abruptly disrupted by laser beams and sirens, but you are not the Balharry's target.  
        You run upstairs, but as you are running, you bump into something, and you both fall to the ground.  
        It's an alien, but not a Balharry. He quickly gets up, runs upstairs, and you follow him, since there is no way for you to go and you can't see much in the dark.  
        He enters a room, leaving the door open. You can also see a door with the lights on a few steps away and a ventilation close to it.  
        Where will you go?
        """,
        "choices": [
        {"choice": "Follow him", "destination": "cloneRoom"},
        {"choice": "Follow the lights", "destination": "techRoom"},
        {"choice": "Enter the ventilation", "destination": "warRoom"},
        ],
    },
    "warRoom": {
        "story": """
        You hide inside the ventilation, and crawl looking for a room you can gather your thoughts and make a plan to send them away.
        You see an empty room with a conference table filled with maps and sketches, a big television and enter it. Looks like they are planning something.


        .                                            .
 *   .                  .              .        .   *          .
.         .                     .       .           .      .        .
      o                             .                   .
       .              .                  .           .
        0     .
               .          .                 ,                ,    ,
.       \\          .                         .
  .      \\   ,
.          o     .                 .                   .            .
 .         \\                 ,             .                .
           #\\##\\#      .                              .        .
         #  #O##\\###                .                        .
.        #*#  #\\##\\###                       .                     ,
    .   ##*#  #\\##\\##               .                     .
  .      ##*#  #o##\\#         .                             ,       .
      .     *#  #\\#     .                    .             .          ,
                  \\          .                         .
____^/\\___^--____/\\____O______________/\\/\\---/\\___________---______________
   /\\^   ^  ^    ^                  ^^ ^  '\\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __


        You take a better look and see they plan in invading another planet: Mirkern. It's location is too far for you to comprehend,
        But if the Balharry were able to come to earth, they might be able to come there. So, an idea crosses your mind.
        If you could find the communication room and communicate with these other aliens, maybe they could help defend earth.
        It's not a flawless plan, since they could also be a problem, but as far as you know, the enemy of your enemy is your friend.
        You grab one of the maps, open the room's door and go back to the corridor, you see the lab door open and the room across it also open.
        What will you do?
        """,
        "choices": [
            {"choice": "Enter the lab", "destination": "cloneRoom"},
            {"choice": "Go to the other door", "destination": "startWar"},
        ],
    },
    "startWar": {
        "story": """
        You decide to enter the other door. It has a big conference table in the center and all the Balharry are dead.
        There are three aliens in there, just like the one you saw before, they notice you but do nothing.
        Confused on what to do, you approach one of them and show him the map. He takes a look and points to the radio.
        He walks with you there, presses some buttons and now you have a radio synchronized with Mirkern.
        - Hello - you start your speech - I am from planet Earth. The Balharry invaded us and I just found out you are their next target.
        - Greetings, human - a robotic voice answers - How can we know this is true? And not just another of their stupid plans?
        - I found a room full of maps and plans, they know where you are located and for what I've seen will not be merciful.
        - So tell us their plans, and we will be forever grateful for your help.
        - No. If you want to know their plans, you should come here and see them yourself.
        - Our planet needs help - You continue explaining your plan - So if you come here and help us both of our planets will be safe.
        - Attacking them off guard is a good idea, human. You have my word, as a general, we will not start a war with your kind.
        The alien on your side wants to speak something and you fear he may say something bad.
        What will you do?
        """,
        "choices": [
            {"choice": "Let him say it", "destination": "warEnd"},
            {"choice": "Break the radio", "destination": "warDeath"},
        ],
    },
    "warEnd": {
    "story": """
        .-.                                                               .-.
       /   \\           .-.                                 .-.           /   \\
      /     \\         /   \\       .-.     _     .-.       /   \\         /     \\
    -/-------\\-------/-----\\-----/---\\---/-\\---/---\\-----/-----\\-------/-------\\--
              \\     /       \\   /     '-'   '-'     \\   /       \\     /
               \\   /         '-'                     '-'         \\   /
                '-'                                               '-'


        He speaks something in a language you cannot comprehend, and the general answers him.
        The alien then points his rifle to the room window and shoots until it breaks. He then calls his companions from the lab,
        And as they come the Balharry start shooting them, but there are a lot of these aliens now, and they kill the Balharry with no effort.
        They grab some wires from the equipment, tie and throw them out of the window to jump, and you follow them.
        You are now in the city, out of the spaceship, and you see other ships approaching from the sky.
        They start shooting all of the Balharry spaceships, including the mothership. Some of them land,
        and aliens looking just like the one you met in the ship come out. They shoot all the Balharry and help you defend earth.
        The alien who helped you enters one spaceship and waves at you, disappearing in the sky. The earth is now safe from the Balharry.

        Thanks for playing.
        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "warDeath": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  


        Before he could say anything, you break the radio and leave it unusable.  
        The alien gets very angry and pushes you to the ground, then he starts screaming a lot of things you cannot understand.  
        The other two kneel on the ground and hold their hands together, as if they were praying.  
        A huge laser beam rips through the spaceship and it explodes. At this point, you and all the other things in the ship are already dead.  
        A lot more of these beams come, and then the whole planet is now filled with holes.  
        You died as the mothership explodes, and the whole planet explodes next.
              

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "cryoRoomEmpty": {
        "story": """
        _  
       / |  
       |_|  _                                                   __ _  
       | |_( |_____________ _____________|:::|__________________\_'_|___  
      |' ||=====___________) |___________\___/______________________|(o)||  
      \__|(o)|        ||------------------------------------------------|||  
      |__|___)        ||         _______________________________        |||  
      |               ||        |_______________________________|       ||)  
      |   ____      __||__()__)        /________________________________|||  


        You silently unscrew the grid and jump over the alien. He seems really scared and tries to get you off him.  
        He is really strong, but your years of training make you stronger. You don't know what to do to make him stop,  
        so you grab a pencil from his desk and stab him until he stops struggling.  
        That was brutal... But it's not like you had other choices. Now, you have some blueish liquid sticking to your arms.  
        You decide to clean his blood before it can do something to you. Now that you are clean, you search for anything that could free these humans.  
        You find a switch, pull it without hesitation, and all the cryogenic chambers open. The humans start to slowly regain consciousness and stand up.  
        - Are we free? - One of them asks.  
        - Not yet - you respond - I have to find the navigation room and send them back.  
        - We could also grab some guns and kill them ourselves. When the aliens were bringing me here, I could see them coming downstairs with guns.  
        - That means - he continues explaining his idea - that there are a lot of guns upstairs that we could use. I know it's dangerous, but what else could we do?  
        He has a point, will you consider his idea or just lead them to the exit: The room you killed the first Balharry?
        """,
        "choices": [
            {"choice": "Go upstairs", "destination": "humansUpstairs"},
            {"choice": "Take them to safety", "destination": "exitRoom"},
        ],
    },
    "exitRoom": {
        "story": """
        The humans' safety is your priority, so taking them to the exit would be the best idea.  
        The group grabs the laser rifles remaining, and you lead them to the exit room.  
        No aliens found you on the way, and the exit room is empty. You open the door and can see the city's streets completely empty,  
        aliens walking around and spaceships the size of cars flying around.  
        - Thanks for showing us the way - the humans thank you. What they will do outside the spaceship worries you a little,  
        but stopping them is your job now. You leave the room and follow your way to the stairs, but as you hear aliens coming down from them,  
        you decide that instead of going up, you are going downstairs.  
        On this floor, the lights are weaker and you can hardly see. There are no doors, vents, or anywhere you can go.  
        You walk a little more and see one single big door. You open it, and inside there is a giant room with lots of computers, generators,  
        and a huge reactor in the center. It looks like a reactor room full of Balharry. They notice you, and you quickly take cover as they  
        start shooting in your direction and hit you in the arm.  
        Luckily, you still got your rifle with you, so you shoot them until there are only two left and your gun is not working anymore.  
        With no ideas left, you sprint through the computers and grab the closest Balharry. You punch him, and he shoots your leg as you both  
        fall to the ground. You grab his gun and shoot his head, turn around to see the last Balharry approaching you and shoot him.  
        Now that they are all dead, you explore the room. You try to find something to distract you from your bleeding.  
        And you find it: The reactor's central control panel. You can't understand much, but the big red button in the center is pretty  
        self-explanatory. You look it up in the manual on the panel, and by the images, you think this button will implode the mothership.  
        It would be a heroic decision, but a difficult one. You are bleeding, feeling weak and hopeless, and need to make a decision  
        before your life fades away. Will you sacrifice yourself for the sake of humanity or will you try finding another way?
        """,
        "choices": [
            {"choice": "Press the button", "destination": "reactorEnd"},
            {"choice": "Look for something to stop your bleeding", "destination": "stopBleed"},
        ],
    },
    "reactorEnd": {
        "story": """
                             ____  
                     __,-~~/~    '---.  
                   _/_,---(      ,    )  
               __ /        <    /   )  \\___  
- ------===;;;'====------------------===;;;===----- -  -  
                  \\/  ~"~"~"~"~"~\\~"~)~"/  
                  (_ (   \\  (     >    \\)  
                   \\_( _ <         >_>'  
                      ~ '-i' ::>|--"  
                          I;|.|.|  
                         <|i::|i|'.  
                       ('' ^'"'-' ")  


        You press the button and follow all the implosion procedure in the main computer, hoping it will save earth.  
        The countdown starts, and in your last moments you think about your family and how you want them to live happily in a safe planet.  
        The spaceship implodes. You and all the Balharry inside it are dead. The smaller spaceships retreat and disappear into the blue sky.  
        It doesn't take long for the remaining Balharry to be killed by the army, and the earth is finally safe, thanks to you.  

        Thanks for playing.
        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "stopBleed": {
        "story": """
        You realise there are still ways to save humanity and also keeping you alive.  
        Willing to live, you go around searching the bodies, but find nothing. You are feeling dizzy and fainty,  
        so you walk back to the button before you die in vain. You look inside the drawers of the main computer's desk and find a flask with a red liquid.  

                    ______  
                   (______)  
                    |    |  
                    |    |  
                    |    |  
                    |    |          
                    |    |             
                    |'--'|           
                    |    |           
                    |    |              
                    |    |             
                    |    |         
                    |    |          
                    |    |  
                    |    |  
                    '.__.'  


        Your only choice is to drink it. You do it close to the button in case it does the opposite of healing you.  
        It feels weird, but not in a dying way. You feel a shockwave running through your body and your wounds magically close.  
        You are now feeling better than ever, so you grab a rifle, shoot the generators and walk upstairs.  
        You can see nothing; the mothership is now in complete darkness and you wonder if your decision was brilliant after all.  
        The silence is abruptly disrupted by laser beams and sirens, but you are not the Balharry' target.  
        You run to the second floor, but as you are running, you bump into something and you both fall to the ground.  
        It's an alien, but not a Balharry. He quickly gets up, runs upstairs, and you follow him,  
        since there is no way for you to go and you can't see much in the dark.  
        He enters a room, leaving the door open. You can also see a ventilation in the other side of the corridor.  
        Where will you go?
        """,
        "choices": [
            {"choice": "Follow him", "destination": "cloneRoom"},
            {"choice": "Enter the ventilation", "destination": "warRoom"},
        ],
    },
    "humansUpstairs": {
        "story": """
        You decide that it's a good idea, so you take the guns remaining in the room and follow to the stairs.  
        Now your group consists in approximately 50 people, which 18 of them are armed with rifles, including yourself.  
        You arrive at the stairs and go up, no hostile encounters until now. The second floor looks pretty much the same as the first,  
        but it has lesser doors and these ones are different.  
        Since you don't know which door leads to the Weapon room, you have to decide which way to go before the Balharry finds your group.  
        You can open the closest door to the right or you can keep walking until you find where the room is.  
        Which way is the group following?
        """,
        "choices": [
            {"choice": "Right door", "destination": "techRoomGroup"},
            {"choice": "Walk the hallway", "destination": "groupDeath"},
        ],
    },
    "groupDeath": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_}  

        You keep going through the hallway undisturbed.  
        Suddenly, laser beams start flying through the air, and behind you a group of soldiers is shooting your group.  
        Multiple humans are shot and killed, and one of the laser beams rips through your stomach.  
        You died while trying to hold your insides and watching the Balharry obliterate the humans that are left.
              

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "cryoRoom": {
        "story": """
                     (_)  (_)                  <> \\  / <>
                      .\\::/.                   \\_/\\  \\_/\\
     .:.          _.=._\\\\//_.=._                  \\\\//
..   \\o/   ..      '=' //\\\\ '='             _<>_\\\\_<>/_/_<>_
:o|   |   |o:         '/::\\'                 <> / /<>\\ \\ <>
 ~ '. ' .' ~         (_)  (_)      _    _       _ //\\\\ _
     >O<             '      '     /_/  \\\\_     / /\\  /\\ \\
 _ .' . '. _                        \\\\//       <> /  \\ <>
:o|   |   |o:                   /\\_\\\\><\\\\ \\
     ':'
                                  _//\\\\_
                                  \\\\_/\\_/ 


        You follow your way inside the ventilation, all the grids seem too small to fit you, until you find one that you can get in.  
        As you get close to it, the cold air coming from the grid gives you shivers, and as you look down to inspect you see something that frightens you.  
        There are around 10 aliens in there and a lot of cryogenic chambers that contain humans inside them.  
        All the aliens are wearing lab coats and respirators, they are unarmed except for two in the center of the room.  
        Close to the door there's a desk with lots of guns the size of rifles, and conveniently for you, the door is about five meters from the grid.  
        The room is dark, but not dark enough for them not to see you. If you act quick,  
        you could fall from the ceiling and run to grab a rifle before the two Balharry shoot you.  
        You silently think about your next step.
        """,
        "choices": [
            {"choice": "Unscrew the grid and sprint for the rifles", "destination": "saveHumans"},
            {"choice": "Keep going through the ventilation", "destination": "electricRoom"},
        ],
    },
    "saveHumans": {
        "story": """
        _ 
       / | 
       |_|  _                                                   __ _
       | |_( |_____________ _____________|:::|__________________\\_'_|___
      |' ||=====___________) |___________\\___/______________________|(o)|| 
      \\__|(o)|        ||------------------------------------------------||| 
      |__|___)        ||         _______________________________        ||| 
      |               ||        |_______________________________|       ||) 
      |   ____      __||__()__)        /________________________________||| 
      |  /    )    (           /___ _/ /   |      


        You silently unscrew the grid and go down to the ground. You run as fast as you can in the direction of the door,  
        you feel a laser beam passing close to your ear, so you jump to behind the desk and quickly grab a rifle.  
        They keep shooting at you, so you wait for them to stop shooting you to shoot and kill them both.  
        Now, the sirens are already on and you are left with the other scientists in the room.  
        You point your gun to one of them, and without saying nothing he understands the assignment and pulls a switch.  
        Now that you are clean, you search for anything that could free these humans.  
        All the cryogenic chambers open, and the humans start to slowly regain consciousness and stand up.  
        The scientists are all paralyzed with fear, so now you have to decide what you will do with them...
        """,
        "choices": [
            {"choice": "Kill them", "destination": "killScient"},
            {"choice": "Let them go", "destination": "letScient"},
        ],
    },
    "killScient": {
        "story": """
        Before they could react, you kill all the Balharry. The fear in their faces didn't make you feel good, but you didn't feel bad either...  
        - Are we free? - One of them asks.  
        - Not yet - you respond - I have to find the navigation room and send them back.  
        - We could also grab some guns and kill them ourselves. When the aliens were bringing me here, I could see them coming downstairs with guns.  
        - That means - he continues explaining his idea - that there are a lot of guns upstairs that we could use. I know it's dangerous, but what else could we do?  
        He has a point, will you consider his idea or just lead them to the exit: The room you killed the first Balharry?
        """,
        "choices": [
            {"choice": "Go upstairs", "destination": "humansUpstairs"},
            {"choice": "Take them to safety", "destination": "exitRoom"},
        ],
    },
    "letScient": {
        "story": """
        They seem no harm, so you gather them in the other side of the room, further from the rifle table.  
        - Are we free? - One of them asks.  
        - Not yet - you respond, while pointing your gun at the hostages - I have to find the navigation room and send them back.  
        - We could also grab some guns and kill them ourselves. When the aliens were bringing me here, I could see them coming downstairs with guns.  
        - That means - he continues explaining his idea - that there are a lot of guns upstairs that we could use. I know it's dangerous, but what else could we do?  
        He has a point, will you consider his idea or just lead them to the exit: The room you killed the first Balharry?
        """,
        "choices": [
            {"choice": "Go upstairs", "destination": "humansUpstairs"},
            {"choice": "Take them to safety", "destination": "exitRoom"},
        ],
    },
    "noGun": {
        "story": """
                     o   o                                         
                      )-( 
                     (O O)                                        
                      \\=/ 
                     .-"-. 
                    //\\ /\\ 
                  _// / \\ \\_ 
                 =./ {,-.} \\.= 
                     || || 
                     || ||    
                  _ _|| ||__   
                  '---" '---'


        You slowly open the door to a poorly lit hallway, it is really elongated and full of doors.  
        They look all the same, and you take some time to think about where you should go first.  
        Interrupting your thoughts, you hear two aliens approaching from the end of the hallway and you  
        quickly open the first door you can and hide inside quietly. The room is completely dark, but before  
        looking around you sit in silence waiting for the aliens in the hallway to leave. It doesn't take long,  
        as they walk past you without saying a word to each other. 'Do they even talk?', you wonder as you  
        try to feel the room for something useful.  
        You feel some kind of switch, wondering if you should pull it...
        """,
        "choices": [
            {"choice": "Yes", "destination": "labOn"},
            {"choice": "No", "destination": "labOff"},
        ],
    },
    "labOn": {
        "story": """
                                       ||              []
                                    __ ||              []
                                    || ||              []
                                  .-||-||-.            [] 
                                 _\\_______/_===========[]=(-o)
                                  )\\_____/(            []  
                                 /     ||  \\           []
                                /      ||   \\          []
                               /       ||    \\         []
                              /~~~~~~~~~~~~~~~\\        []
                             /         ::      \\       []
                            (          ::       )      []
                             '-----------------'       []
                                     )                 []
                                   (   )               []
                                     )( . (            []
                                  .) @@)   )           []
                               ' ) @@(@@)@             []
                                 (@@(@@)@              []
                                  @(@.@)@@             []
                                ' (@{__}@)'            []
                                    :__;               []
                ___                  {}+               []
               ( = )             .---''---.            []
                | |_            /          \\   ________[]____
             ___| |_|==========(____________)_/______________\\


        You pull it and the lights turn on to reveal what seems to look like a science lab, full of flasks filled with colorful liquids,  
        weird rocks, plants and etcetera. You take a look around just to find two beds in the corner of the lab and two Balharry sleeping peacefully in it.  
        Fortunately for you, they seem to be in a very heavy sleep completely undisturbed by your presence,  
        but you decide to be more careful to not wake them up. Close to them, you find a table with four flasks containing each a different liquid.  
        Knowing nothing about the alien language in the labels nor chemistry, which one of them will you pick?
        """,
        "choices": [
            {"choice": "Purple Flask", "destination": "flaskGood"},
            {"choice": "Green Flask", "destination": "flaskGood"},
            {"choice": "Orange Flask", "destination": "flaskBad"},
            {"choice": "Blue Flask", "destination": "flaskBad"},
        ],
    },
    "flaskGood": {
        "story": """
        You pick the flask and take another look around to see if there is anything else that can be useful.  
        On one of the top shelves you see what looks like a syringe filled with a bright green liquid.  
        It could be really useful, but to reach it you'll need to stand over the table and climb the shelves, which can be dangerous.

                                    |
                  ,------------=--------|___________|
 -=============%%%|         |  |______|_|___________|
                  | | | | | | ||| | | | |___________|
                  '------------=--------|           |
                                    |

        Will you attempt to reach the syringe?
        """,
        "choices": [
            {"choice": "No, it's too dangerous", "destination": "leaveSyringe"},
            {"choice": "A flask AND a syringe, why not?", "destination": "takeSyringeG"},
        ],
    },
    "takeSyringeG": {
        "story": """
        You balance yourself over the table and start climbing. You firmly grab the bottom shelves and start going up.  
        Suddenly, one of the shelves break and everything else collapses and falls to the ground, including yourself, who fell on the table and broke it.


            .-****-.        .-****-.
           /        \\      /        \\
          /_        _\\    /_        _\\
         // \\      / \\\\  // \\      / \\\\
         |\\__\\    /__/|  |\\__\\    /__/|
          \\    ||    /    \\    ||    /
           \\        /      \\        /
            \\  __  /        \\  __  /
             '.__.'          '.__.'
              |  |            |  |
              |  |            |  |


        You stand up and anxiously look back to the sleeping scientists, thinking that no one could stay sleeping after such a mess.  
        They are, in fact, staring directly at you in a mix of confusion and fear. They appear to be unarmed, and the only gun you see is the one on the table.  
        One of them quickly tries to reach for it, now think fast and act faster!
        """,
        "choices": [
            {"choice": "Throw the flask at them", "destination": "labDeathThrow"},
            {"choice": "Drink the flask", "destination": "drinkFlask"},
        ],
    },
    "labDeathThrow": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_} 


        You aim and throw the flask at them hoping it will melt their skin or something similar, but once the glass breaks and the liquid spills on both  
        they start growing in size, their skin gets tougher and they jump over you faster than you can react.  
        You died while they beheaded you and violently bit through your stomach.
      

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "drinkFlask": {
        "story": """
                                  _.-***- _  
                            _    /      0\\ \\
    _.-***-._           .nNNNNNn:       \#) :  
   /     (#\ \\_.-***-._/NNNNN(#\\N\\         /  
  :       \\#) |.:|||:.|NNNNNNN\#)N"-.___.-"  
   \         /|||||(#\\|\\NNNNNNNNN/  
    "-.___.-"||||||\\#)||"*NNNNN*"  
             \\|||||||||/  
              ':|||:'  
              .-"   "-.  
            .'     (#\ '.  
            :       \#) :  
            '.         .'  
               "-...-"  


        You start getting bigger and bigger, you feel your skin hard like rock and your muscles getting stronger. You feel like you could lift anything.  
        When the scientist grabs the gun and shoots you, the laser beam feels ticklish and does nothing against you. So you take your chance and attack the aliens with your bare hands.  
        You kill them with no effort, but as soon as you get to the lab door,  
        you start feeling an excruciating pain in your stomach, throw up, lay on the ground and feel your body going back to normal.  
        You are ready to leave now, so you open the door and keep walking until you find three doors that catch your attention:  
        The first one is to your left. It has scratches in it, and whoever made them must be really strong and angry...  
        The second one looks normal but as you get closer the air feels really cold. You try opening it out of curiosity but it's locked.  
        The third one has a light flashing, but that's all you can see from under the door, which is also locked.  
        You also see a dim red light coming from inside the ventilation, which you can try crawling inside to make your way to the locked rooms.
        """,
        "choices": [
            {"choice": "First door", "destination": "zooRoom"},
            {"choice": "Second door", "destination": "cryoRoom"},
            {"choice": "Third door", "destination": "electricRoom"},
            {"choice": "Go for the red light", "destination": "prisonCell"}
        ],
    },
    "flaskBad": {
        "story": """
        You pick the flask and take another look around to see if there is anything else that can be useful.  
        On one of the top shelves you see what looks like a syringe filled with a bright green liquid.  
        It could be really useful, but to reach it you'll need to stand over the table and climb the shelves, which can be dangerous.  


                                            |
                      ,------------=--------|___________|
     -=============%%%|         |  |______|_|___________|
                      | | | | | | ||| | | | |___________|
                      '------------=--------|           |
                                            |


        Will you attempt to reach the syringe?
        """,
        "choices": [
            {"choice": "No, it's too dangerous", "destination": "leaveSyringe"},
            {"choice": "A flask AND a syringe, why not?", "destination": "takeSyringeB"},
        ],
    },
    "takeSyringeB": {
        "story": """
        You balance yourself over the table and start climbing. You firmly grab the bottom shelves and start going up.  
        Suddenly, one of the shelves breaks and everything else collapses and falls to the ground, including yourself, who fell on the table and broke it.  


            .-****-.        .-****-.
           /        \\      /        \\
          /_        _\\    /_        _\\
         // \\      / \\\\  // \\      / \\\\
         |\\__\\    /__/|  |\\__\\    /__/|
          \\    ||    /    \\    ||    /
           \\        /      \\        /
            \\  __  /        \\  __  /
             '.__.'          '.__.'
              |  |            |  |
              |  |            |  |


        You stand up and anxiously look back to the sleeping scientists, thinking that no one could stay sleeping after such a mess.  
        They are, in fact, staring directly at you in a mix of confusion and fear. They appear to be unarmed, and the only gun you see is the one on the table.  
        One of them quickly tries to reach for it, now think fast and act faster!
        """,
        "choices": [
            {"choice": "Throw the flask at them", "destination": "throwFlask"},
            {"choice": "Drink the flask", "destination": "labDeathDrink"},
        ],
    },
    "labDeathDrink": {
        "story": """
                _.--\"\"--._ 
               /  _    _  \\ 
            _  ( (_\\  /_) )  _ 
           { \\._\\   /\\   /_./ }
           /_\"=-.}______{.-=\"_\\
            _  _.=(\"\"\"\")=._  _ 
           (_'\"_.-'\"~~\"-.\"'_)
            {_\"            \"_} 


        You quickly open the flask and drink it hoping it will give any superpower, but once the liquid goes down your throat you immediately regret it.  
        Your mouth, throat and esophagus start melting and the last thing you can see is the scientist grabbing the gun and pointing it to your head.  
        You died from a headshot while agonizing in pain from the hyper corrosive liquid.
      

        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end"},
        ],
    },
    "throwFlask": {
        "story": """
                                  _.-***- _  
                            _    /      0\\ \\
    _.-***-._           .nNNNNNn:       \#) :  
   /     (#\ \\_.-***-._/NNNNN(#\\N\\         /  
  :       \\#) |.:|||:.|NNNNNNN\#)N"-.___.-"  
   \         /|||||(#\\|\\NNNNNNNNN/  
    "-.___.-"||||||\\#)||"*NNNNN*"  
             \\|||||||||/  
              ':|||:'  
              .-"   "-.  
            .'     (#\ '.  
            :       \#) :  
            '.         .'  
               "-...-"  


        You throw the flask at them, and before the scientist can reach the gun, its hand starts melting and both of the aliens fall to the ground screaming in pain.  
        Their bodies melt until there's nothing left of them, and you realise you should probably leave now.  
        You open the door and keep walking until you find three doors that catch your attention:  
        The first one is to your left. It has scratches in it, and whoever made them must be really strong and angry...  
        The second one looks normal but as you get closer the air feels really cold. You try opening it out of curiosity but it's locked.  
        The third one has a light flashing, but that's all you can see from under the door, which is also locked.  
        You also see a dim red light coming from inside the ventilation, which you can try crawling inside to make your way to the locked rooms.
        """,
        "choices": [
            {"choice": "First door", "destination": "zooRoom"},
            {"choice": "Second door", "destination": "cryoRoom"},
            {"choice": "Third door", "destination": "electricRoom"},
            {"choice": "Go for the red light", "destination": "prisonCell"},
        ],
    },
    "zooRoom": {
        "story": """
                     _.----~~~~~~-----..__ 
              __..------~~~~-     .._     ~~-.  
 ___.--.--~~~~     --~~~~---~ __  ~~----.__   ~~~~~~~---...._____  
(~~~~_..----~       ~~--=< O >- .----. -< O >=--~~             ..   .)  
 ~-..__..--         ..  ___-----_...__-----___        _.  ~-=___..-~  
         '   _    ..   (     ' :_.}{._; ' '   )      _-     '  
          \   ~~-      '   ' ' __###__  ''    '    -~     .'  
           '-._  ~-.    _'--~~~VvvvvVV~~---'_     ~..    _.  
               -.     '~##\(            )/###~' .     _.~  
                 -    '.###\#    {     #/####.'    _-~  
                  -_    -####    !     #####-  ..  
                    -._  ~.###   }     ###-~ ___.-~  
                       ~-  \##  / '   ##.~ /~  
                         \ |###  '   ###' /  
                          \`/\#######/'\ ;  
                           ~-.^^^^^^^ .-~  
                              ~~~~~~~  


        You open the first door. The room is really dark and filled with Balharry blue blood and corpses. Then, before you can react, something jumps over you.  
        It's an unidentified animal that resembles a panther. Your first reaction is to take the syringe and inject the liquid in it.  
        The creature falls to the ground, you get up and take a look around.  
        A lab filled with animals from earth, but there is something different with them, like if they were experimented on.  
        The panther starts waking up and quickly approaches you, it sniffs you but before you could panic the animal turns around and walks out the door.  
        Since it didn't attack you but attacked the aliens, it may be a good idea to follow the animal.  
        It runs through the hallway and breaks a door: It is the electricity room of the spaceship.  
        It starts destroying all of the wires and generators, making a big mess.  
        You can see nothing, the mothership is now in complete darkness and the panther simply lays on the floor and sleeps. You better let it sleep peacefully.  
        The silence is abruptly disrupted by laser beams and sirens, but you are not the Balharry target.  
        You run upstairs, but as you are running you bump into something and you both fall to the ground.  
        It's an alien, but not a Balharry. He then runs upstairs and you follow him, since there is no way for you to go and you can't see much in the dark.  
        He enters a room, leaving the door open. You can also see a door with the lights on a few steps away, and a ventilation close to it.  
        Where will you go?
        """,
        "choices": [
            {"choice": "Follow him", "destination": "cloneRoom"},
            {"choice": "Follow the lights", "destination": "techRoom"},
            {"choice": "Enter the ventilation", "destination": "warRoom"},
        ],
    },
    "leaveSyringe": {
        "story": """
        You decide that taking the syringe could be dangerous and decide to take only the flask, so you open the door and return to the hallway.  
        All the doors seem to look the same, you walk a little more, finding one with a different color than the others and decide to open it.  
        It looks like a security room, full of screens and cameras. You can see the corridor you were before, the dark room you probably entered before and all kinds of rooms.  
        You search for one that resembles a navigation room but everything looks confusing, although three rooms catch your attention.  
        The first one is a room filled with cryogenic chambers with humans inside of it. You really want to save them before leaving the ship and look around to find any other humans.  
        The second one is a room full of equipment: protective suits, bigger guns and all sorts of technological devices that could really help you right now.  
        The third one is a room with a flashing light, buttons, wires and energy generators, probably an electricity room. Unlike the other two, there are no aliens there.  
        There is also an entry to the ventilation system right behind you that can be useful to get to these rooms, and you can see a dim red light coming from inside it.  
        So which way are you going?
        """,
        "choices": [
            {"choice": "Cryo room", "destination": "cryoRoom"},
            {"choice": "Tech room", "destination": "techRoom"},
            {"choice": "Electricity room", "destination": "electricRoom"},
            {"choice": "Go for the red light", "destination": "prisonCell"},
        ],
    },
    "leaveSyringeGun": {
        "story": """
        You decide that taking the syringe could be dangerous and decide to take only the flask, so you open the door and return to the hallway.  
        All the doors seem to look the same, you walk a little more, finding one with a different color than the others and decide to open it.  
        It looks like a security room, full of screens and cameras. You can see the corridor you were before, the dark room you probably entered before and all kinds of rooms.  
        You search for one that resembles a navigation room but everything looks confusing, although three rooms catch your attention.  
        The first one is a room filled with cryogenic chambers with humans inside of it. You really want to save them before leaving the ship and look around to find any other humans.  
        The second one is a room full of equipment: protective suits, bigger guns, and all sorts of technologic devices that could really help you right now.  
        The third one is a room with a flashing light, buttons, wires, and energy generators, probably an electricity room. Unlike the other two, there are no aliens there.  
        There is also an entry to the ventilation system right behind you that can be useful to get to these rooms, and you can see a dim red light coming from inside it.  
        So which way are you going?
        """,
        "choices": [
            {"choice": "Cryo room", "destination": "cryoRoom"},
            {"choice": "Tech room", "destination": "techRoom"},
            {"choice": "Electricity room", "destination": "electricRoom"},
            {"choice": "Go for the red light", "destination": "prisonCellGun"},
        ],
    },
    "labOff": {
        "story": """
        You decide that whatever is inside that room must be left alone. After waiting a little more, you open the door and return to the hallway.  
        All the doors seem to look the same, you walk a little more, finding one with a different color than the others and decide to open it.  
        It looks like a security room, full of screens and cameras. You can see the corridor you were before, the dark room you probably entered before and all kinds of rooms.  
        You search for one that resembles a navigation room but everything looks confusing, although three rooms catch your attention.  
        The first one is a room filled with cryogenic chambers with humans inside of it. You really want to save them before leaving the ship and look around to find any other humans.  
        The second one is a room full of equipment: protective suits, bigger guns, and all sorts of technologic devices that could really help you right now.  
        The third one is a room with a flashing light, buttons, wires, and energy generators, probably an electricity room. Unlike the other two, there are no aliens there.  
        There is also an entry to the ventilation system right behind you that can be useful to get to some of these rooms, and you can see a dim red light coming from inside it.  
        So which way are you going?
        """,
        "choices": [
            {"choice": "Cryo room", "destination": "cryoRoom"},
            {"choice": "Tech room", "destination": "techRoom"},
            {"choice": "Electricity room", "destination": "electricRoom"},
            {"choice": "Go for the red light", "destination": "prisonCell"},
        ],
    },
}

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_scene(scene_key):
    scene = story[scene_key]
    print(f"\n{scene['story']}")
    for i, choice in enumerate(scene["choices"], 1):
        print(f"[{i}] {choice['choice']}")
    return scene

def handle_choice(scene):
    while True:
        try:
            choice = int(input("\nMake your choice (number): ")) - 1
            if 0 <= choice < len(scene["choices"]):
                return scene["choices"][choice]["destination"]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please, enter a valid number.")

def main():
    current_scene = "begin"
    while True:
        scene = render_scene(current_scene)
        current_scene = handle_choice(scene)
        if current_scene not in story:
            cls()
            print("\nTHANKS FOR PLAYING!")
            break

if __name__ == "__main__":
    main()
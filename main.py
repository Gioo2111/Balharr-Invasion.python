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
            {"choice": "Search the Body", "destination": "get_gun"},
            {"choice": "Leave the room immediately", "destination": "no_gun"},
            {"choice": "Explore the mothership through the ventilation system", "destination": "vent"},
        ],
    },
    "get_gun": {
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
            {"choice": "Leave the room immediately", "destination": "leave_room"},
            {"choice": "Explore the mothership through the ventilation system", "destination": "vent_gun"},
        ],
    },
    "leave_room": {
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
            {"choice": "No", "destination": "end_game"},
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
        """,
        "choices": [
        {"choice": "Try again", "destination": "begin"},
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
        """,
        "choices": [
            {"choice": "Try again", "destination": "begin"}
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
    current_scene = "escapeCell"
    while True:
        scene = render_scene(current_scene)
        current_scene = handle_choice(scene)
        if current_scene not in story:
            cls()
            print("\nTHANKS FOR PLAYING!")
            break

if __name__ == "__main__":
    main()
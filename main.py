import os
story = {
    "game_over": {
        "story": """
        Do you want to play again?
        """,
        "choices": [
            {"choice": "Yes", "destination": "begin"},
            {"choice": "No", "destination": "end_game"},
        ],
    },
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


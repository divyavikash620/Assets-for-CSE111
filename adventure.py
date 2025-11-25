

def get_input(prompt, options):
    """Ask the user for input until a valid option is given."""
    options_lower = [opt.lower() for opt in options]
    while True:
        choice = input(f"{prompt} ({'/'.join(options_lower)}): ").strip().lower()
        if choice in options_lower:
            return choice
        print("Invalid choice. Try again.")

print("Welcome to Hell Land!")
choice = get_input("Do you want to ENTER or RUN?", ["enter", "run"])

if choice == "run":
    print("The gates drag you inside anyway. No escape!")
else:
    print("You step into Hell Land: scorching air and screams everywhere.")

# --- MAIN LOOP (only 3 paths shown at a time) ---
while True:
    path = get_input("Choose a path", ["tunnel", "river", "cliff"])

    # --- DARK TUNNEL ---
    if path == "tunnel":
        print("Whispers call your name...")
        action = get_input("Do you FOLLOW or IGNORE the whispers?", ["follow", "ignore"])

        if action == "follow":
            print("A shadowy demon devours your soul. GAME OVER.")
        else:
            print("You ignored the whispers and reach three sub‑paths:")
            sub = get_input("Choose: STAIRWAY, CAGE, or DOOR", ["stairway", "cage", "door"])

            if sub == "stairway":
                choice2 = get_input("CLIMB quietly or RUN up?", ["climb", "run"])
                if choice2 == "climb": print("You reach a glowing escape portal! YOU WIN!")
                else: print("The stairs crumble beneath you. GAME OVER.")

            elif sub == "cage":
                choice2 = get_input("TOUCH the glowing eye or IGNORE it?", ["touch", "ignore"])
                if choice2 == "ignore": print("A secret tunnel opens leading back to the main paths.")
                else: print("The eye drains your soul. GAME OVER.")

            elif sub == "door":
                choice2 = get_input("SOLVE runes or FORCE door?", ["solve", "force"])
                if choice2 == "solve": print("Runes glow and open a new path to the RIVER!")
                else: print("Flames burst from the door. GAME OVER.")

# --- BLOOD RIVER ---
    elif path == "river":
        print("You reach a river of blood. You see a BOAT, a BRIDGE, or you can SWIM.")
        method = get_input("How do you cross?", ["boat", "bridge", "swim"])

        if method == "bridge":
            print("A demon blocks your way!")
            action = get_input("Do you FIGHT or BEG?", ["fight", "beg"])
            if action == "fight":
                print("You defeat the demon, revealing 3 new routes!")
                sub = get_input("Choose: ISLAND, FERRYWOMAN, or WHIRLPOOL", ["island", "ferrylady", "whirlpool"])

                if sub == "island":
                    c2 = get_input("EXPLORE or REST?", ["explore", "rest"])
                    if c2 == "explore": print("You find an ancient staircase to the CLIFF area!")
                    else: print("Spirits drag you under. GAME OVER.")

                elif sub == "ferrylady":
                    c2 = get_input("PAY with a story or FIGHT her?", ["story", "fight"])
                    if c2 == "story": print("She ferries you to a secret FOREST path!")
                    else: print("She curses you. GAME OVER.")

                elif sub == "whirlpool":
                    c2 = get_input("DIVE deeper or ESCAPE?", ["dive", "escape"])
                    if c2 == "escape": print("You wash up at the TUNNEL entrance!")
                    else: print("You are lost forever. GAME OVER.")

            else:
                print("The demon enslaves your soul. GAME OVER.")
        else:
            print("You are dragged underwater by unseen hands. GAME OVER.")

# --- FIERY CLIFF ---
    elif path == "cliff":
        print("You stand before a FIERY CLIFF. Two paths: ROPE bridge or CLIFF edge.")
        route = get_input("Where do you go?", ["rope", "cliff"])

        if route == "rope":
            print("A fire demon attacks!")
            action = get_input("Do you FIGHT or JUMP off?", ["fight", "jump"])
            if action == "fight":
                print("You defeat the demon. Three new cliff routes appear!")
                sub = get_input("Choose: CAVE, SUMMIT, or LAVA TUNNEL", ["cave", "summit", "lava"])

                if sub == "cave":
                    c2 = get_input("ENTER deeper or RETURN?", ["enter", "return"])
                    if c2 == "enter": print("A hidden elevator lifts you to safety! YOU WIN!")
                    else: print("You return to the RIVER paths.")

                elif sub == "summit":
                    c2 = get_input("CLIMB higher or REST?", ["climb", "rest"])
                    if c2 == "climb": print("You see the exit gates and escape! YOU WIN!")
                    else: print("Rockslide crushes you. GAME OVER.")

                elif sub == "lava":
                    c2 = get_input("CROSS stepping stones or TURN back?", ["cross", "turn"])
                    if c2 == "cross": print("You reach a portal to the TUNNEL! Return begins!")
                    else: print("You retreat to the main 3‑path menu.")

            else:
                print("You fall into lava. GAME OVER.")

        else:
            print("You hide inside a cave and find hidden stairs.")
            print("You escape safely! YOU WIN!")

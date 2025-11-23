# Hell Land — Gore + Dark Fantasy Enhanced (Developer Version)

"""
This file is the current playable Python script for the Hell Land text adventure.
It implements intense gore/body horror and dark fantasy elements (styles 2 + 5)
and expands branching with interlinked paths and many sub-choices.

Design notes for developers:
- The script keeps a single input validator get_input().
- Main loop shows only three choices at a time (tunnel, river, cliff).
- Each main path contains 3 sub-paths, each with further branching.
- Many branches interlink — some send you to other main areas.
- Win/Game Over messages are explicit. You can insert HP/inventory later.
"""


def get_input(prompt, options):
    """Ask the user for input until a valid option is given."""
    options_lower = [opt.lower() for opt in options]
    while True:
        choice = input(f"{prompt} ({'/'.join(options_lower)}): ").strip().lower()
        if choice in options_lower:
            return choice
        print("Invalid choice. Try again.\n")

print("\nWelcome to HELL LAND — a place that devours the living.\n")
print("This experience contains graphic descriptions. Proceed only if ready.")

choice = get_input("Do you want to ENTER or RUN?", ["enter", "run"])
if choice == "run":
    print("The gates SHRIEK and yank you inside by bleeding ropes of flesh. There is no escape.")
else:
    print("You step into Hell Land. The air tastes like iron and old ceremonies.")

# --- MAIN LOOP (3 choices shown at a time) ---
while True:
    print("\n---\nPaths visible: TUNNEL, RIVER, CLIFF (type the keyword)\n---")
    path = get_input("Choose a path", ["tunnel", "river", "cliff"])

    # ------------------------- TUNNEL -------------------------
    if path == "tunnel":
        print("Deep, wet whispers slither through the darkness, speaking your name and your secrets.")
        choice1 = get_input("Do you FOLLOW or IGNORE the whispers?", ["follow", "ignore"]) 

        if choice1 == "follow":
            print("You follow and find a butchered altar. The whispers shove your hands into the open chest — you die as ritual blood seals your throat. GAME OVER.")
            continue

        # IGNORE -> three sub-paths
        print("You choke down your fear. The whispers fade. Three cursed passages reveal themselves: STAIRWAY, CAGE, DOOR.")
        sub = get_input("Choose: STAIRWAY, CAGE, or DOOR", ["stairway", "cage", "door"]) 

        # STAIRWAY branch
        if sub == "stairway":
            print("You climb: the stairs are slick with a viscous black ichor that smells of iron and old bone.")
            s = get_input("CLIMB quietly, RUN up, or PAUSE to listen?", ["climb", "run", "pause"]) 
            if s == "climb":
                print("At the top you find a chamber of mirrors. One mirror shows a SAFE EXIT. Do you TOUCH it or SHATTER it?")
                act = get_input("TOUCH or SHATTER?", ["touch", "shatter"]) 
                if act == "touch":
                    print("Your reflection smiles and pulls you through — you emerge into sunlight. YOU WIN!")
                    break
                else:
                    print("Shards bite your hands; skeletal fingers climb through. GAME OVER.")
                    continue
            elif s == "run":
                print("The stairs collapse. You tumble into a maw that chews memories before flesh. GAME OVER.")
                continue
            else:
                print("You freeze. A wraith slides into your mouth, whispering secrets that rot your mind. GAME OVER.")
                continue

        # CAGE branch
        elif sub == "cage":
            print("A hanging cage pulses, with a single enormous, bloodshot eye inside. Tendrils twitch." )
            s = get_input("TOUCH the eye, OPEN the cage, or STEP back?", ["touch", "open", "back"]) 
            if s == "touch":
                print("The eye lashes with barbed lids and suctions your soul through your fingertips. You go hollow. GAME OVER.")
                continue
            elif s == "open":
                print("The cage creaks open. Inside: a charred map hinting at the RIVER's Ferrylady and the CLIFF's lava tunnel.")
                # interlink: reveal path choice immediately
                link = get_input("Follow MAP to RIVER or CLIFF?", ["river", "cliff"]) 
                if link == "river":
                    print("You follow the map and are carried to the riverbank — continue at the RIVER hub.")
                    path = "river"
                    # jump to river by loop continue; emulate by setting path and using continue to rerun loop body
                    continue
                else:
                    print("You are pulled by the map's ink into the CLIFF area — continue at the CLIFF hub.")
                    path = "cliff"
                    continue
            else:
                print("You step back — a hidden blade snaps your neck from the darkness. GAME OVER.")
                continue

        # DOOR branch
        elif sub == "door":
            print("A towering rune door bleeds smoke and something like prayers.")
            s = get_input("SOLVE the riddle, FORCE the door, or OFFER a drop of your blood?", ["solve", "force", "offer"]) 
            if s == "solve":
                print("You decode the runes. The door opens to a passage leading directly to a secret CLIFF cavern.")
                path = "cliff"
                continue
            elif s == "force":
                print("You force the door; it explodes into a torrent of embers that consume you. GAME OVER.")
                continue
            else:
                print("You slice your palm and let the blood fall. The runes drink, and the door coughs up a small iron KEY.")
                # key leads to Ferrylady dialogue later; for now, allow player to choose RIVER next
                print("Clutching the KEY, the path out points to the RIVER.")
                path = "river"
                continue

    # ------------------------- RIVER -------------------------
    elif path == "river":
        print("You stand at a bank where **boiling blood** hisses against jagged stones. The smell of iron is overwhelming.")
        method = get_input("How do you cross: BOAT, BRIDGE, or SWIM?", ["boat", "bridge", "swim"]) 

        if method == "boat":
            print("The boat is manned by corpses sewn together. Their lips move, but they cannot speak. Do you SIT or LEAP?" )
            b = get_input("SIT or LEAP?", ["sit", "leap"]) 
            if b == "sit":
                print("The corpses stitch you into the boat's hull. You become the rower forever. GAME OVER.")
                continue
            else:
                print("You leap — but unseen hands pull you under. Your scream bubbles in the blood and the surface smooths. GAME OVER.")
                continue

        elif method == "swim":
            print("The blood's current is a throat that gulps. You can DIVE deep toward a faint light or STRUGGLE to shore.")
            s = get_input("DIVE or STRUGGLE?", ["dive", "struggle"]) 
            if s == "dive":
                print("You find an underwater cavern lined with teeth — inside, a narrow tunnel opens to the TUNNEL entrance.")
                path = "tunnel"
                continue
            else:
                print("The current pulls you into a ribcage of stone where the bones click shut. GAME OVER.")
                continue

        # BRIDGE path
        else:
            print("A towering demon of bone and ash rises from the bridge, its hollow eye sockets dripping molten tar.")
            action = get_input("Do you FIGHT or BEG?", ["fight", "beg"]) 
            if action == "beg":
                print("You beg. The demon laughs and eats your voice. You stagger away but are cursed and reappear at the HUB older and hollow. GAME OVER.")
                continue

            # FIGHT
            print("You fight — steel sings against bone. The demon falls but its blood stains the bridge with shouting runes.")
            sub = get_input("Now choose: ISLAND (explore), FERRYLADY, or WHIRLPOOL?", ["island", "ferrylady", "whirlpool"]) 

            # ISLAND
            if sub == "island":
                print("You step onto an island where statues bleed. A carved stair dives into the earth or a well yawns open.")
                i = get_input("STAIR or WELL?", ["stair", "well"]) 
                if i == "stair":
                    print("Stair leads to CLIFF SUMMIT where an exit glows. YOU WIN!")
                    break
                else:
                    print("The well swallows you; hands pull your tongue out to thread a puppet. GAME OVER.")
                    continue

            # FERRYLADY
            elif sub == "ferrylady":
                print("A woman of sea-salt and torn lace offers to ferry you. She asks for a token: STORY, BLOOD, or SILENCE.")
                f = get_input("Choose token: STORY, BLOOD, or SILENCE", ["story", "blood", "silence"]) 
                if f == "story":
                    print("You tell a story of your life. She smiles, ferries you to a hidden FOREST path where a portal sleeps.")
                    path = "tunnel"  # sends to tunnel hub (map interlink)
                    continue
                elif f == "blood":
                    print("You cut your palm. Her eyes flare; she screams and vanishes with the boat, leaving you on a desolate shore. GAME OVER.")
                    continue
                else:
                    print("You keep silent; the Ferrylady takes your silence and gives you a cracked compass. It points to CLIFF LAVA TUNNEL.")
                    path = "cliff"
                    continue

            # WHIRLPOOL
            else:
                print("You edge near the whirlpool. You can THROW a stone to test it or HIDE from its pull.")
                w = get_input("THROW or HIDE?", ["throw", "hide"]) 
                if w == "throw":
                    print("The stone becomes a screaming man and the whirlpool spits you to the RIVER's starting bank. You're trapped. GAME OVER.")
                    continue
                else:
                    print("You hide and the water forgets you — a narrow tunnel opens downstream to the TUNNEL entrance.")
                    path = "tunnel"
                    continue

    # ------------------------- CLIFF -------------------------
    elif path == "cliff":
        print("The FIERY CLIFF roars like a living creature, molten veins crawling across its surface as the air stinks of burning flesh.")
        route = get_input("Take the ROPE bridge or the CLIFF edge?", ["rope", "edge"]) 

        if route == "edge":
            print("You stumble into a suffocating cave where the walls pulse like a beating heart. You can EXPLORE deeper or CLIMB out.")
            e = get_input("EXPLORE or CLIMB?", ["explore", "climb"]) 
            if e == "climb":
                print("You claw your way up and find a plateau leading back to the HUB. You survive but the screams follow. Continue.")
                continue
            else:
                print("Exploring deeper, you find a blood-child curled in a nest. It wakes and devours your eyes. GAME OVER.")
                continue

        # ROPE bridge route
        print("A gigantic fire demon erupts from the flames; its jaws unhinge impossibly wide as it shrieks your name.")
        action = get_input("Do you FIGHT or JUMP?", ["fight", "jump"]) 
        if action == "jump":
            print("You fall into a river of molten flesh. GAME OVER.")
            continue

        # Fight succeeded -> three cliff sub-paths
        print("You strike true. The demon collapses; three new routes open: CAVE, SUMMIT, LAVA.")
        sub = get_input("Choose: CAVE, SUMMIT, or LAVA", ["cave", "summit", "lava"]) 

        if sub == "cave":
            print("The cave drips with coagulated oil; stairs lead down or a grated door squeals open.")
            c = get_input("DOWN or DOOR?", ["down", "door"]) 
            if c == "down":
                print("The elevator of bone lifts you to a desolate temple — an altar sits with an empty chalice. Offer your blood or steal the chalice?")
                c2 = get_input("OFFER or STEAL?", ["offer", "steal"]) 
                if c2 == "offer":
                    print("The altar drinks. The temple coughs up a blazing gate to freedom. YOU WIN!")
                    break
                else:
                    print("The chalice bursts and the temple consumes you. GAME OVER.")
                    continue
            else:
                print("The grated door opens onto a narrow tunnel that vomits you back to the RIVER bank.")
                path = "river"
                continue

        elif sub == "summit":
            print("The summit wind smells of old incense and sharpened bones. You can SIGNAL for help or PRAY at the stone circle.")
            s = get_input("SIGNAL or PRAY?", ["signal", "pray"]) 
            if s == "signal":
                print("A distant hand grasps you and pulls you through a fissure to daylight. YOU WIN!")
                break
            else:
                print("The stones wake. Teeth split the earth and you fall. GAME OVER.")
                continue

        else:  # LAVA
            print("The lava tunnel glows with imprisoned faces. You can CROSS on stones or TURN back.")
            l = get_input("CROSS or TURN?", ["cross", "turn"]) 
            if l == "cross":
                print("As you cross, a face in the lava reaches and latches your ankle — but a hidden portal opens and drags you into the TUNNEL. You survive but are haunted.")
                path = "tunnel"
                continue
            else:
                print("You retreat to the HUB, the cliff's roar following you.")
                continue

# End main loop
print("\nThank you for playing Hell Land. The darkness keeps your name.")

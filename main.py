# MAD LIB 1: BREAKFAST OF CHAMPIONS

i = []

def add(str):
    i.append(input("Enter " + str + ": "))

# Prompts:
add("an interesting adjective") # {i[0]}
add("an adjective for how something smells")
add("one of the people who lives here")
add("a weird food (plural)")
add("someone else in the friend group")
add("an expression someone would yell in all caps")
add("a color")
add("a third friend in the group")
add("a body part")
add("a type of house pet")
add("noun") # {i[10]}
add("someone in the friend group who is very competitive")
add("another competitive friend in the group")
add("a punishment for losing a bet")
add("some words of encouragement (starting with a capital letter)")
add("another friend") # {i[15]}
add("one of the two competitive people you mentioned")
add("the other competitive person you mentioned")
add("a state of emotion (ex: happy, sad, angry, etc.)") # {i[18]}

# Story:
print(f"It was a {i[0]} January day. Everyone woke up to the {i[1]} smell of {i[2]} cooking {i[3]} "
      f"in the kitchen.\n \"Eat up everyone!\" {i[2]} said, serving everyone a big plate. {i[4]} sniffed it, "
      f"then took a giant bite. \"{i[5]}\" {i[4]} yelled,\n immediately throwing up {i[6]} vomit "
      f"all over {i[7]}'s {i[8]}. \"What did you even put in here?\" {i[4]} asked. \"I added {i[9]} food\n with "
      f"some crushed up {i[10]} to really give it that extra kick.\" Everyone looked at each other in shock.\n \"Bro I'll "
      f"make a bet with you that I can eat a plate of this quicker than you can.\" {i[11]} said to {i[12]}.\n \"Alright, "
      f"loser has to {i[13]},\" {i[12]} smirked. \"Deal!\" {i[11]} exclaimed. The two counted down and started scarfing down their food.\n"
      f"{i[3]} was flying left and right throughout the kitchen as they wolfed down their food at supersonic speed.\n"
      f"\"{i[14]}!!!\" yelled {i[15]}. They were both going super hard in the paint but right as they were both about"
      f" to finish,\n {i[16]} pulled ahead and gulped down the last piece. \"Well, a deal is a deal.\" {i[17]} said, "
      f"with a {i[18]} look on their face.\n {i[17]} quickly jumped up and proceeded to {i[13]} as fast as they could. "
      f"\nThey did it better than anyone had ever seen before!\n And from that day on, nobody ever messed with {i[16]} ever "
      f"again. The end.")

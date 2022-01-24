# Kousei Richeson was here

i = []

def add(str):
    i.append(input("Enter " + str + ": "))

# Prompts:
add("an interesting adjective")
add("an adjective for how something smells")
add("one of the people who lives here")
add("a weird food")
add("someone else in the friend group")
add("an expression someone would yell in all caps")
add("a third friend in the group")

# Story:
print(f"It was a {i[0]} January day. Everyone woke up to the {i[1]} smell of {i[2]} cooking {i[3]} in the kitchen. \n \"Eat up everyone!\" {i[2]} said, serving everyone a big plate. {i[4]} sniffed it, then took a giant bite. \"{i[5]}\" {i[4]} yelled, \n immediately throwing up {i[6]} vomit all over {i[2]}'s face.")

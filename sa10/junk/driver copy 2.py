from vertex import Vertex

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):
    vertex_dict = {}
    file = open(filename, "r")

    while True:
        # --- Read name ---
        name = file.readline()
        if name == "":      # end of file
            break
        name = name.strip()
        if name == "":
            continue

        # --- Read description ---
        description_lines = []
        line = file.readline()

        while line != "" and line.strip() != "":
            # remove trailing newline manually
            if line.endswith("\n"):
                line = line[:-1]
            description_lines.append(line)
            line = file.readline()

        # manually build description string
        description = ""
        for d in description_lines:
            description = description + d + "\n"
        # remove final extra newline if any
        if description.endswith("\n"):
            description = description[:-1]

        # --- Read adjacency list ---
        adj_line = file.readline()
        adj_line = adj_line.strip()

        parts = adj_line.split(",")
        adjacent = []

        for p in parts:
            p = p.strip()
            if p != "":
                adjacent.append(p)

        # create the vertex
        v = Vertex(name, adjacent, description)
        vertex_dict[name] = v

    file.close()
    return vertex_dict

def play(story_dict):
    current = story_dict["START"]
    while True:
        print(current.text)
        if not current.adjacent:
            print("THE END")
            break
        for i in range(len(current.adjacent)):
            v = current.adjacent[i]
            option = chr(ord('a') + i)
            print(f"{option}) go to {v}")
        choice = input("Choose: ").strip().lower()
        if not choice:
            continue
        index = ord(choice) - ord('a')
        if index < 0 or index >= len(current.adjacent):
            print("Invalid choice.")
            continue
        next_name = current.adjacent[index]
        current = story_dict[next_name]


story_dict = load_story("story.txt")
play(story_dict)

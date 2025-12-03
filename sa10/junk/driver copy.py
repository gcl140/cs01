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

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            print("vertex " + vertex_name)
            print(" adjacent:  " + str(adjacent_vertices))
            print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
        vertex = Vertex(vertex_name, adjacent_vertices, text)
        vertex_dict[vertex_name] = vertex

    file.close()

    return vertex_dict


def play(story_dict):
    current = story_dict["START"]

    while True:
        print(current.text)

        if not current.adjacent:
            print("THE END")
            break

        # for i, v in enumerate(current.adjacent):
        # for i, v in range(len(current.adjacent)):
        #     option = chr(ord('a') + i)
        #     print(f"{option}) go to {v}")
        for i in range(len(current.adjacent)):
            v = current.adjacent[i]

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

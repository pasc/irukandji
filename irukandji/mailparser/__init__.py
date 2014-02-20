class Node:
    def __init__(self, level, author=None):
        self.level = level
        self.content = ""
        self.author = author


    def append(self, text):
        #text = self.strip_levels(text)
        self.content += text

    def __repr__(self):
        return "Node ([%s] depth = %s, %s)" % (self.author, self.level, self.content)

class Message:
    def __init__(self, author="", subject=""):
        self.author = author
        self.subject = subject
        self.content = []


    def indent_level(self, text):
        level = 0
        for tok in text.split():
            if tok in ['|', '>']:
                level += 1
            else:
                matches = tok.split('>')
                if len(matches) > 1:
                    level += len(matches) - 1
                else:
                    return level
 
        return level

    def strip_levels (self, level, text):
        current = 0
        i = 0

        while current < level and i < len(text):
            if text[i] in ['>', '|']:
                current += 1

            i += 1
        return text[i:]

def parse_author(author_line):
    """This reads in a string and extracts out the possible author name
    
    TODO: lots. like actually implementing a quote line parser. Could possibly
    do with hints as well.
    """
    
    return ' '.join(filter(lambda x: x.istitle(), author_line.split()[1:]))

def generate_message(text, author, subject):
    message = Message(author, subject)
    level = 0
    # Array of authors with depth as index
    message.authors = {}
    n = Node (0)

    content = [n]

    lines = text.splitlines()
    for i, l in enumerate(lines):
        c_level = message.indent_level(l)

        if c_level > level:
            if c_level not in message.authors:
                message.authors[c_level] = parse_author(message.strip_levels(level, lines[i-1]))

        content_line = message.strip_levels(c_level, l).strip()

        if c_level != level:
            n = Node(c_level)
            if c_level in message.authors:
                n.author = message.authors[c_level]
            content.append(n)
            level = c_level
        elif content_line == "":
            n = Node(c_level)
            content.append(n)

        n.append(content_line + " ")

    message.content = content

    return message

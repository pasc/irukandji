def format_mail(mail):
    level = 0

    ret = ""

    for n in mail.content:
        while n.level > level:
            ret += """<span class="label">%s</span>""" % mail.authors[level + 1] if level + 1 in mail.authors else ''
            ret += """<blockquote><div class="quote%s">""" % level
            level += 1

        while n.level < level:
            ret += "</div></blockquote>"
            level -= 1


        ret += "<p>%s</p>" % n.content

        level = n.level

    while level > 0:
        ret += "</div></blockquote>"
        level -= 1
    return ret

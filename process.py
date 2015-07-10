from textinput import fixthis
from wordlists import wordtypes

# python 2.7 builtins
import textwrap
import hashlib
import collections
import sys
import re

fixline_delim = "#"
content_delim = "~"


def tree():
    return collections.defaultdict(tree)


def format(text, indent=2, width=70):
    return "\n".join(textwrap.wrap(text, width=width, initial_indent=" " * indent, subsequent_indent="" * indent))


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


lines = []

# begin basic processing
for line in fixthis.split('\n'):
    if not line.strip():
        # keep the new lines in place for structure
        lines.append('\n')
    else:
        # format the line into 70 character columns, indenting 2 spaces
        res = format(line)
        # take the formatted output and shove it into the array
        for r in res.split('\n'):
            lines.append(r)

docdata = tree()
line_order = []

i = 0
for line in lines:
    try:
        # create a hash of the line so it has a unique identifier.
        # add line counter here because if someone has text like:
        # "no, you"
        # "no, you"
        # there won't hash collisions. At least I hope not.
        line_hash = hashlib.sha1(line + str(i)).hexdigest()
        # get rid of the newlines
        docdata[line_hash]["orig_line"] = line.replace('\n', '')
        # try to save some space, i suppose
        docdata[line_hash]["orig_line_len"] = len(line)
        # create a list populated with zeroes. if something is found, the zero will be
        # changed to a 1
        docdata[line_hash]["fix_line"] = [0] * len(line)
        docdata[line_hash]["fix_reason"] = []
        # there can be multiple fix_reasons, so each byte is given it's own list
        for x in range(0, len(line)):
            docdata[line_hash]["fix_reason"].append([])
        docdata[line_hash]["line_num"] = i
        line_order.append(line_hash)
        i = i + 1
    except Exception, e:
        # this is terribly broad, but i'm not sure what would cause this
        # to be thrown
        print e
        print "Oh, my. Something went horribly awry."
        sys.exit(1)

for doc_hash in docdata.keys():
    for wordlist in wordtypes.keys():
        if wordtypes[wordlist]["enabled"] is True:
            for word in wordtypes[wordlist]["words"]:
                word_len = len(word)
                try:
                    # this does some formatting to make matches better
                    # This will only look for " word " so password won't be triggered
                    # this removes " and ' for the space bit above
                    # this does everything in lower case
                    word_index = docdata[doc_hash]["orig_line"].replace("\"", "").replace("\'", "").lower().index(
                        " " + word.lower() + " ")
                    try:
                        docdata[doc_hash]["words"][wordtypes[wordlist]["tag"]]['pos'].append([word_index + 2, word_len])
                    except:
                        docdata[doc_hash]["words"][wordtypes[wordlist]["tag"]]['pos'] = []
                        docdata[doc_hash]["words"][wordtypes[wordlist]["tag"]]['pos'].append([word_index + 2, word_len])

                    # this adds the words actually found to the data structure.
                    # this isn't currently exposed to the user, though.
                    try:
                        docdata[doc_hash]["words"][wordtypes[wordlist]["tag"]]['found_words'].append(word)
                    except:
                        docdata[doc_hash]["words"][wordtypes[wordlist]["tag"]]['found_words'] = []
                        docdata[doc_hash]["words"][wordtypes[wordlist]["tag"]]['found_words'].append(word)

                except ValueError:
                    pass

for doc_hash in line_order:
    i = 0
    word_found = False
    while (i != docdata[doc_hash]["orig_line_len"]):
        for word_tag in docdata[doc_hash]["words"]:
            for pos in docdata[doc_hash]["words"][word_tag]['pos']:
                word_start = pos[0]
                word_stop = pos[1]

                if word_start == i:
                    docdata[doc_hash]["fix_reason"][i].append(word_tag)

                if word_start <= i and i <= (word_start + word_stop):
                    docdata[doc_hash]["fix_line"][i] = 1

        i = i + 1

# print a header / guide to what the different letter meanings do
print "#0000| %s ) %s" % ("tag", "description")
for list in wordtypes:
    if wordtypes[list]["enabled"] is True:
        print "#0000| %s ) %s" % (wordtypes[list]["tag"], wordtypes[list]["description"])


# now print the content itself
for doc_hash in line_order:
    # this is the original line
    print "%s%04d| %s" % (content_delim, docdata[doc_hash]["line_num"], docdata[doc_hash]["orig_line"])

    if docdata[doc_hash]["orig_line"] != '':
        # this is the line with the carets pointing out what to fix
        sys.stdout.write("%s%04d|" % (fixline_delim, docdata[doc_hash]["line_num"]))
        item_max = len(docdata[doc_hash]["fix_line"])
        # this process isn't perfect, but it's reasonably close
        for index, item in enumerate(docdata[doc_hash]["fix_line"]):
            if item == 1:
                sys.stdout.write("^")
            else:
                sys.stdout.write(" ")

            if (index + 1) == item_max:
                sys.stdout.write("\n")

        # this is the line with the guide
        sys.stdout.write("%s%04d|" % (fixline_delim, docdata[doc_hash]["line_num"]))
        item_max = len(docdata[doc_hash]["fix_reason"])
        # this process isn't perfect, but it's reasonably close
        for index, item in enumerate(docdata[doc_hash]["fix_reason"]):
            tag = None
            item_len = len(item)
            if item_len != 0:
                tag = "".join(item)

            if tag is not None:
                sys.stdout.write(tag)
            else:
                sys.stdout.write(" ")

            if (index + 1) == item_max:
                sys.stdout.write("\n")

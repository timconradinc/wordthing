import collections


def tree():
    return collections.defaultdict(tree)


wordtypes = tree()

########################################################################################################################
wordtypes["custom_template"]["tag"] = "X"
wordtypes["custom_template"]["enabled"] = False
wordtypes["custom_template"]["words"] = ["and", "this", "she", "he"]
wordtypes["custom_template"]["description"] = "This is a custom word list."

########################################################################################################################
wordtypes["custom_list"]["tag"] = "C"
wordtypes["custom_list"]["enabled"] = False
wordtypes["custom_list"]["words"] = ["and", "this", "she", "he"]
wordtypes["custom_list"]["description"] = "Custom test word list, don't use this unless you know what you're doing."

########################################################################################################################
wordtypes["needless_words"]["tag"] = "n"
wordtypes["needless_words"]["enabled"] = True
wordtypes["needless_words"]["words"] = ["then", "almost", "about", "begin", "start", "decided", "planned", "very",
                                        "sat", "truly", "rather", "fairly", "really", "somewhat", "up", "down",
                                        "over", "together", "behind", "out", "in order", "around", "only", "just",
                                        "even"]
wordtypes["needless_words"]["description"] = "Words that can be safely be omitted"

########################################################################################################################
wordtypes["showingvtelling"]["tag"] = "T"
wordtypes["showingvtelling"]["enabled"] = True
wordtypes["showingvtelling"]["words"] = ["was", "were", "when", "as", "the sound of", "could see", "saw", "notice",
                                         "noticed", "noticing", "consider", "considered", "considering", "smell",
                                         "smelled", "heard", "felt", "tasted", "knew", "realize", "realized",
                                         "realizing", "think", "thought", "thinking", "believe", "believed",
                                         "believing", "wonder", "wondered", "wondering", "recognize", "recognized",
                                         "recognizing", "hope", "hoped", "hoping", "supposed", "pray", "prayed",
                                         "praying", "angrily"]
wordtypes["showingvtelling"]["description"] = "Showing vs Telling Words"

########################################################################################################################
wordtypes["passive_words"]["tag"] = "p"
wordtypes["passive_words"]["enabled"] = True
wordtypes["passive_words"]["words"] = ["be", "being", "been", "am", "is", "are", "was", "were", "has", "have", "had",
                                       "do", "did", "does", "can", "could", "shall", "should", "will", "would", "might",
                                       "must", "may"]
wordtypes["passive_words"]["description"] = "Passive Word List"

########################################################################################################################
wordtypes["used_incorrectly"]["tag"] = "i"
wordtypes["used_incorrectly"]["enabled"] = False
wordtypes["used_incorrectly"]["words"] = ["accept", "except", "adverse", "averse", "advice", "advise", "affect",
                                          "effect", "aisle", "isle", "altogether", "all together", "along", "a long",
                                          "aloud", "allowed", "altar", "alter", "amoral", "immoral", "appraise",
                                          "apprise", "assent", "ascent", "aural", "oral", "awhile", "a while",
                                          "balmy", "barmy", "bare", "bear", "bated", "baited", "bazaar", "bizarre",
                                          "birth", "berth", "born", "borne", "bow", "bough", "break", "brake",
                                          "broach", "brooch", "canvas", "canvass", "censure", "censor", "cereal",
                                          "serial", "chord", "cord", "climactic", "climatic", "coarse"]
wordtypes["used_incorrectly"]["description"] = "Words often used incorrectly"

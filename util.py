## This mainly deals with variables, which I'll implement later.

EMOTE_AF = "<:af:795338973102342164>"
EMOTE_MSFROG = "<:msfrog:902580885428269056>"

ERROR_MESSAGE_GENERIC = f"an error occured {EMOTE_MSFROG}"

def parsemessage(args):
    """
    eventually i'll need to be able to parse uservars, so we'll need this for user variables
    """
    ret = []
    for arg in args:
        ret.append(arg)
    return tuple(ret)

markdowns = "*_`"

def escape_markdown(msg):
    """
    escapes markdown for flags etc since discord.py's one adds stuff
    """
    for char in markdowns:
        msg = msg.replace(char, f"\\{char}")
    return msg
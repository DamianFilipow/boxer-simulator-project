#introduction
bobby = "BOBBY"
trainee = "TRAINEE"

prompts = dict(
    bobby_text_1 = """
    {speaker}
    You can't, you can't give up that easily!
    Stand up kid!
    """,
    trainee_text_1 = """
    {speaker}
    It's useless! I am good for nothing!
    I am not talented at all! I can't be like you... nor your previous trainee...
    """,
    bobby_text_2 = """
    {speaker}
    My previous trainee? You mean {current_character} right?
    """,
    trainee_text_2 = """
    {speaker}
    I guess...
    """,

    bobby_text_3 = """
    {speaker}
    Let me tell you something kid...
    He has been as talentless as you...
    He was good for nothing too!
    """,

    trainee_text_3 = """
    {speaker}
    If- if he was like me, how come he became so great?
    I know I can't be like him...
    """,

    bobby_text_4 = """
    {speaker}
    Tell me the numbers!
    """,

    trainee_text_4 = """
    {speaker}
    Wh-at what numbers?
    What are you talking about?
    """,

    bobby_text_5 = """
    {speaker}
    Lottery numbers, you know them, don't you?
    """,

    trainee_text_5 = """
    {speaker}
    Are you mad?!
    Why do you think I know them?
    """,
    bobby_text_6 = """
    {speaker}
    You cleary know the future, otherwise you couldn't tell me what you can't become!
    """,

    trainee_text_6 = """
    {speaker}
    ...
    """,

    bobby_text_7 = """
    {speaker}
    I believe at you kid!
    I know you can do it too!
    You just need to believe at that too!
    That's what in the very moment makes you different from {current_character}
    """,

    bobby_text_8 = """
    {speaker}
    Let me tell you a story, a story how I met {current_character}.
    Haha... I remember that day as it was yesterday.
    """
)

def penis(prompt, **kwargs):
    return prompts[prompt].format(**kwargs)
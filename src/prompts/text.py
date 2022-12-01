#introduction
bobby = "Bobby"
trainee = "Trainee"
def get_text(dict, prompt, **kwargs):
    return dict[prompt].format(**kwargs)

prompts_intro = dict(
    bobby_text_1 = """
    {bobby}
    You can't, you can't give up that easily!
    Stand up kid!
    """,
    trainee_text_1 = """
    {trainee}
    It's useless! I am good for nothing!
    I am not talented at all! I can't be like you... nor your previous trainee...
    """,
    bobby_text_2 = """
    {bobby}
    My previous trainee? You mean {current_character} right?
    """,
    trainee_text_2 = """
    {trainee}
    I guess...
    """,

    bobby_text_3 = """
    {bobby}
    Let me tell you something kid...
    He has been as talentless as you...
    He was good for nothing too!
    """,

    trainee_text_3 = """
    {trainee}
    If- if he was like me, how come he became so great?
    I know I can't be like him...
    """,

    bobby_text_4 = """
    {bobby}
    Tell me the numbers!
    """,

    trainee_text_4 = """
    {trainee}
    Wh-at what numbers?
    What are you talking about?
    """,

    bobby_text_5 = """
    {bobby}
    Lottery numbers, you know them, don't you?
    """,

    trainee_text_5 = """
    {trainee}
    Are you mad?!
    Why do you think I know them?
    """,
    bobby_text_6 = """
    {bobby}
    You cleary know the future, otherwise you couldn't tell me what you can't become!
    """,

    trainee_text_6 = """
    {trainee}
    ...
    """,

    bobby_text_7 = """
    {bobby}
    I believe at you kid!
    I know you can do it too!
    You just need to believe at that too!
    That's what in the very moment makes you different from {current_character}
    """,

    bobby_text_8 = """
    {bobby}
    Let me tell you a story, a story how I met {current_character}.
    Haha... I remember that day as it was yesterday.
    """
)

prompts_prolog = dict(
    bully_text_1 = """
    Bully1
    Stand up you loser!
    """,
    
    bully_text_2 = """
    Bully2
    HAHA, kick his fucking ass!!
    """,
    
    bully_text_3 = """
    Bully3
    Look at him, he is already crying!!!
    HAHAH what a piece of shit!
    """,
    
    bully_text_4 = """
    Bully1
    Crying? Should I let him go guys?
    """,
    
    bully_text_5 = """
    Bully2 & Bully3
    Nooo way, smash his ugly face first!
    """,
    
    mc_text_1 = """
    {current_character}
    Plea- please let me go...
    What- what did I do to you...
    Just let me go please...
    """,
    
    bully_text_6 = """
    Bully1
    Oh it seems you have a tongue in your motherfucking mouth!
    Beg me!
    Beg me, so I will let you go and won't crush your skull...
    HAHA this time HAHA!
    """,
    bobby_text_1 = """
    {bobby}
    Yo! What a shame guys...
    Have you ever thought about an even fight?
    Little boys?
    """,
    
    bully_text_7 = """
    Bully1
    You fucki...
    Do you want your ass beaten too?
    """,
    
    bobby_text_2 = """
    {bobby}
    From an unfair fight to a another one?
    """,
    
    bully_text_8 = """
    Bully1
    Are you scared now? Get him boys!
    """,
    
    bobby_text_3 = """
    {bobby}
    You should be the scared one boy...
    """,
)

commands = """
Here are games commands:
s for status
m for map
i for inventory
"""
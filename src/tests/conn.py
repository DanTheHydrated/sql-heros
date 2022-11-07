import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")

# =========================================================

def select_all():
    query = """
        SELECT * from heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    print(list_of_heroes)
    for record in list_of_heroes:
        print(record[1])


print("----------------------------------------------------START-----------------------------------------------------------")

def at_the_door():
    password = input("Whats your the password?:")

    if password != "PEPE":
        print("""__________████████_____██████\n_________█░░░░░░░░██_██░░░░░░█\n________█░░░░░░░░░░░█░░░░░░░░░█\n_______█░░░░░░░███░░░█░░░░░░░░░█\n_______█░░░░███░░░███░█░░░████░█\n______█░░░██░░░░░░░░███░██░░░░██\n_____█░░░░░░░░░░░░░░░░░█░░░░░░░░███\n____█░░░░░░░░░░░░░██████░░░░░████░░█\n____█░░░░░░░░░█████░░░████░░██░░██░░█\n___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███\n__█░░░░░░░░░░░░░░█████████░░████████\n_█░░░░░░░░░░█████_████___████_█████___█\n_█░░░░░░░░░░█______█_███__█_____███_█___█\n█░░░░░░░░░░░░█___████_████____██_██████\n░░░░░░░░░░░░░█████████░░░████████░░░█\n░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█\n░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██\n░░░░░░░░░░░░░░░░░░██░░░░░░░███████\n░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n░░░░░░░░░░░█████████░░░░░░░░░░░░░░██\n░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█\n░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█\n░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████\n░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█\n░░░░░░░░░░░░░░░░░░██████████████████\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n██░░░░░░░░░░░░░░░░░░░░░░░░░░░██\n▓██░░░░░░░░░░░░░░░░░░░░░░░░██\n▓▓▓███░░░░░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░░░░██\n▓▓▓▓▓▓▓▓▓███████████████▓▓█\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
        Wrong! *Muffled sounds of Helping from behind the door*""")
    if password == "PEPE":
        me = input("Welcome to the House of Pepe, Whats your name?:")
        a = input("Hello! " + me + " My name is Apu Apustaja! \n"  
        "I'm the helper around here! what you you Like to do?\n" 
        "1.) Tour the House? \n" 
        "2.) Meet the House Members?\n"
        "3.)Become a House Member?:")
        if a == '1':
            tour_the_house(me)
        elif a == '2':
            see_members(me)
        elif a == '3':
            become_a_member(me)

def tour_the_house(me):
    name = me
    print("----------------------------------------------------HOUSE TOUR---------------------------------------------------------")
    print("Apu- Follow me! we'll go see the house! But let's keep to the safe side of the house for the moment. \n"  
    "*Apu leeps you through the house giving you info on every littel detail but for some reason you cant get it out of you head that someone somewhere is watching you...*")
    room = input("This is our leaders room! He is amazing, wonderful, confusing, beautiful, powerful, and generally perfect! \n"
    "HE\n" 
    "IS\n" 
    "PEPE!\n" "Do you have any questions? \n" 
    "1.) Can we meet him? \n" 
    "2.) Where did he come from? \n" 
    "3.) No thanks let's keep moving, He sounds a lil intemidating! :")
    if room == '2':
        def call_for_him():
            query = """
                SELECT Pepe.biography from heroes
            """
            print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠠⣀⣠⣤⣤⣤⣤⣤⣄⡠⠤⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠄⠒⠒⠒⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠳⠤⢀⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⡠⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀\n⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀\n⠀⠀⠀⢀⢖⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀\n⠀⠀⠀⢸⡾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀\n⠀⠀⠀⣴⣛⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⢥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀\n⠀⠀⣾⣾⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠽⠿⠿⠿⠿⠿⣧⣄⡈⠛⠛⠛⣛⣛⣳⣶⣶⣦⣄⡀⠀⠀⠀⠀⡎⠀⠀\n⠀⠘⡿⣿⣿⣿⣿⣿⣦⣄⠀⠀⣀⣠⠤⠤⣤⣖⡺⢟⣩⠥⢒⡊⠭⠭⠝⢑⣒⠲⠤⢭⢖⣪⠭⠜⠓⢒⣒⠒⠒⢒⣛⢷⣄⠀⢀⡇⠀⠀\n⠀⢀⣽⣿⣿⣿⣿⣿⣿⣿⣠⠞⠉⢀⣤⣿⡭⠷⡺⠚⠉⢩⣾⣩⡿⠻⣦⡀⠀⠀⠀⠁⠲⡠⠒⠁⠀⣴⣈⡿⠷⣦⠀⠈⠈⠙⠻⣄⠀⠀\n⠀⢸⣿⣿⣿⣿⣿⡭⠟⠉⠁⠀⠀⠘⠓⠒⠲⡉⠀⠀⠀⢸⣿⣬⣷⣶⣿⡇⠀⠀⠀⠀⠈⠀⠀⠀⢸⣿⣧⣿⣶⣿⠇⠀⠀⠀⠀⣸⠀⠀\n⠀⠀⠈⠓⣿⠶⠟⠁⠀⠀⠀⠀⠀⠘⠛⠂⠀⠈⠑⠠⢀⠈⢛⣿⣿⠛⠋⣀⡀⣀⠠⠐⠂⠀⢀⣀⠀⠙⠻⠿⢿⣍⡀⠤⠤⠒⢊⡍⠀⠀\n⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢠⣄⣤⣾⣿⣷⣤⠀⠀⠀⠀⠀⠀⣀⡤⡎⠀⠀⠀\n⠀⠀⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠤⠶⠦⢤⣤⣀⠀⠀⢠⣿⣿⣿⣤⣿⣿⣿⣿⣇⣀⣀⣤⢶⠛⠁⢀⡏⠀⠀⠀\n⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣅⡀⠐⠦⣤⣤⣀⣈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⡿⠉⠀⢀⣀⣠⣤⠴⢻⠀⠀⠀⠀\n⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠶⢤⣄⣉⠉⠛⠛⠛⠻⠻⣿⣿⣿⠿⠿⠿⠛⠛⠋⠉⠁⣀⣴⠏⠀⠀⠀⠀\n⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠒⠦⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠶⠒⠋⠉⡘⠀⠀⠀⠀⠀\n⢀⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡇⠀⠀⠀⠀⠀\n⢸⠀⠙⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠑⠒⠦⢤⣄⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠤⢤⣀⣀⣀⠴⠚⠉⠀⢸⠀⠀⠀⠀⠀\n⢸⠀⠀⠀⠈⠉⠛⠒⠦⠤⢤⣀⣀⣀⣀⣀⣀⣀⣰⠁⠀⠀⠀⠀⠈⠑⡤⠒⠒⢢⠖⣉⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀\n⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠩⠇⠀⠀⠀⠧⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡀⠜⠒⠤⠀⠐⠒⠤⡀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄""")
            print(he)
    if  room == '1':
        query = """
            SELECT name FROM heroes
            where exists(SELECT name FROM heroes)
        """
        print(execute_query(query,()))
        lets_go(me)
        if check == True:
            print("You hear a deep rumble from this universe to the next as the door opens and a blinding light blinds you for only a moment before the door closes. You didn't see anything but you know that you just saw the rarest of them all!")
            lets_go(me)
        if check == False:
            print("you feel a deep rumble, like the worlds are falling apart, your vision blurs as you hear Apu say *Members only I'm afraid.*")
            lets_go(me)
    if room == '3':
        lets_go(me)


def see_members(me):
    print("Apu- let me go get the book really quick!")
    members = """ 
    select * from heroes order by id
    """
    them = execute_query(members,).fetchall()
    print(them)
    helper(me)


    def lets_go(me):
        q = input("Apu- Are you having fun? (yes/no):")
        if q == "no":
            print("*Apu turns to you and helps you have fun* (You are now having fun.)")
        if q == 'yes':
            print("Apu- Great!")
        now = input("Apu- Here we have a frens room Wizard! \n"  
        "He is super powerful and fun! Would you like to meet h--\n"
        "*BOOM*\n" 
        "(The Wizard is blown out of his room through his door by a MASSIVE explosion)\n" 
        "Apu- Are you ok Wizzarding 101 ?!?! \n" 
        "WIzard- F*** THAT HURT!!! but yeah I'm ok, but my toilet will never be the same *Wizard notices you* \n" 
        "LMAO look at this scrub! You don't even have any Magical Robes! \n \n"
        "What will you say back? 1.) Why would you say that... *you start to cry*\n" 
        "2.) Say nothing and try and act tough! \n" 
        "3.) You see his Robes are covered in a massive amount of nestieness and simply laugh at him :")
        if now == '1':
            print("Apu tells Wizard that he is covered in nastieness and then turns and helps you feel better as Wizard quitely walks back into his room")
            helper(me)
        if now == '2':
            print("Wizard locks eyes with you as he stands up and says *ya know your pretty cool! not many others around here can take a joke and not get mad but hurt! then walks back into his room* (You and Wizard are now frens!)")
            helper(me)
            # you become a fren of Wizard ^
        if now == '3':
            print("Wizard gets mad and screams *We are as of now enemys! I will see you in Hell!*")
            helper(me)
            # you become an enemy of Wizard^


def become_a_member(me):
    print("---------------------------------------------------Becoming a memeber-------------------------------------------------------")
    print("Apu- Thats great! we just need to get a little bit more information, so lets get started!")
    about_me = input("Tell me a lil about you fren!:")
    print("Wow if I wasn't a program made to believe you I would think you were lying!")
    biography = input("what is your backstory?:")
    print("weird but ok...")
    ability_types = input("What are your abilities?")
    print("Gross!")
    decision = input("do you want to take base stats or do you want to roll the dice and let fate decide? (Y/N):")
    name = me
    print(me)
    q = """
        INSERT INTO heroes ( name, about_me, biography)VALUES ( %s, %s, %s )
    """
    execute_query(q, (name, about_me, biography))
    print(f"You are now a member {name}! you can now fight in the ariena!")
    hold = input("Now lets go be a fren to all the other members!")
    if hold != None:
        helper(me)


def helper(me):
    print("---------------------------------------------------------------Helper---------------------------------------------------------------")
    name = me
    q = """ 
    Select name from heroes where name = %s
    """
    check_member = execute_query(q, (name,))
    member_options = input(f"Apu- What would you like to do now {me}?\n"
        "1.) Change something about your membership?\n"
        "2.) See member list?\n"
        "3.) Start a fren fight!"
        )
    if member_options == "1":
        changing(me)
    if member_options == "2":
        see_members(me)
    if member_options == "3":
        fight_club(me)


def changing(me):
    name = me
    q = """
    update heroes set about_me = %s where lower(%s) = lower(heroes.name)
    """
    q2 = """
    update heroes set biography = %s where lower(%s) = lower(heroes.name)
    """
    change = input("what would you like to change about yourself?\n"
    "1.) Change about you?\n"
    "2.) Change your bio?\n"
    "3.) Change nothing about yourself because you are perfect the way you are!"
    )
    if change == "1":
        new = input("What would you like it to be?")
        execute_query(q,(new, hero))
    if change == "2":
        new = input("What would you like it to be?")
        execute_query(q2,(new, hero))
    if change == "3":
        print("Apu- Good for you, you are perfect and I love you fren")
    helper(me)

def fight_club(me):
    print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWWWWWWWWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXXXNNNXXXXXXXNXXXXNXXNNNXNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXXXXXXXXNNNNNNXK00OkxddoodddddddddddkO0KXNNNNNXXXXXNNNXXXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXXXXXXXNNXXXXXXXNXXXXXXXXNXXXXXXXXXXXXXXXXNXXXXXNNXXXXXXXXXXXXXXXXXXNNNXXNNNNNXKOxdolc:;;;,,,,;;;;;;;::;;;,;;;:clodxk0KXNNXXNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXXXXNNNNXXXXXXKKKK00O0000000000000000KKXXNNNNXXXXNNNNNNNNNNXXXXXXXNNXXXNNNNKOdlc:;,,;:ccccccccccccccccccccccccccc:;,,,;:lox0XNXXNXXNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXXNNNXXXXXXXNNXXNNNXK0Oxdooolcccccc:::::;;;;;;;;;;::::::;;;::cccldxk0KXNNNXXXNNXXXNNXXXNNXXNNKxl:;,;ccccccccccccccccccccccccccccccccccccccccc:;;:lokKNXXXNXNNNNXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNNXXNXXXNNNXKOxdll:;;,,;;;:ccccccccccccccccccccccccccccccccc::;;,;;:lodxOKNNXXXXNNNXXNXNXko:;:ccccccccccccccccccccccccccccccccccccccccccccccccc:;;:okKNNXNNXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXNNXKOxol:;;;;:ccclcccccccccccccccccccccccccccccccccccccccccccccc::;;;clok0XNNXXNXXXkc;;cccccccccccccccccccccccccccccccccccccccccccccccccccccccc;;:oOXNNNXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNXXNKkol:;;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;:cox0XNKkc;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;cxKNNXNNNNNNNXXXXXNNNNXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNKd:;;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;:loc;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;dKNNNXXNNXNXXXXXNNNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXk:;cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccl:',:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,c0NXXNXNNXXXNXXXXNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXNk;;cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;,;ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,;kNXNNNNXXXNXXNXNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNk;;ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,,:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,,xNNXNNNXXNXNNXNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXNNNXNXl'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,,:lccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;,xXNXXNXXXXNNXNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXNKc,cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;,:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,;ONNXXXXXXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXXNO,;lcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;,;cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'cKNXNNXXXXXXXNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXXXXXXXXXNNXXXXNXl.:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,':ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccl;'xNXNNNXXXXXNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXXXNNNXXXXNXXNNXXNNNNNNXNN0,'lcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,,:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'cXNXNNNNXNXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXXXNNX0kdollclll;..,;,,;,,,,;;;;;;::ccccccccccccccccccccccccccccccccccccccccccccccccccccc:',ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,,kNXNXXNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXX0xoc;,,;;::ccc::::::::;;;,,,,;,,,,,,,,,;;;;;;;;;;,,,,,;,;;;;;;;;;;;;;;::::cccccccccccc:',cccccccccccccccccccccc:::::;;;;;;;;,,,;,,,,;;;;;;,,,,;;:ccccccccccccccccccccccccccccccccclc'cXNXNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXXXXNXNNNNNNN0o;;;cccccccccccccccccccccccccccccccc::::::::::::::::;;;;,,,;;;;;;;;,,,,,,,,,,,,;;:ccccc,':cc:;;;;;;;;;,,,,;,,,,,,,,,,,,,,;;;,,,;;;;;:::::::::;;,,,,,,,,;;;::ccccccccccccccccccccccccc;,kNXXNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXNXXNNXXXXNNKx:;clccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;,,,,,,;,..,;,,,,,;;;;;;;;;:::::ccccccccccccccccccccccccccccccccccccc::;,,,,,,,',;:ccccccccccccccccccccc'lXNNNNNXXNXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNXXXXXNN0oc::ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'';:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;,,:ccccccccccccccccccl';0NNXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXNNNXx;;ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:',cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:''ONXXXXXXNNXXXXXXXXXXXXXXXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXXNNN0l,:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,,:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'.:OKNNXNNNNNNXXXXNNNXXXNNNXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXNNXXXNN0:,:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,,;ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'.;cdOXNNNNNNXXXNNNNXXXNNNNXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXNXXk;,ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;,:ccccccccccccccccccccccccccccccccccc::::::::::::ccc::ccccccccccccccccccccccccccccccccccccccccccccccccc;':c;:coOXNNNNNXXNNXNXXNNNNXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNNXx,,:;;;;::;;;;;;;;;;;::ccccccccccccclccccccccccccccccccccccccccccccccccccccccccccccccccc;,;cccccccccccccccccccccc::;,,'''',:cclooooooooooooooooooolc:;;:cccccccccccccccccccccccccccccccccccccccccc:''ccc:;:lx0XNNNXNXXXXXXNXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXOdl;'',,;,,;,,,;;;;;;;,,,,,;;;,,,,,;;,,,,,,,,,,;:ccccccccccccccccccccccccccccccccccccccccc:,,:ccccccc:::;,,''.........        .,ONWMWMMMMMMMMMMMMMMMMMWNXOdl:;;;ccccccccccccccccccccccccccccccccccccccc;';ccccc:;:lkXNXNNNXXXXNXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNNXXNk,';;:lcccccccccccccccccccccccccccccccc:::;;;;;,,,,,,,,;::ccccccccccccccccccccccccccccccc:;,;clc:;,'....                         ;KMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdolc:;,;;::cccccccccccccccccccccccccccccc,'cccccccc;,l0NNNXXNNNNXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNNXNKc'ccccccccccccccccccccccccccccccccccccccccccccccccc::;,,,,,,,,,,;::ccccccccccccccccccccc;,;:;;'..                                 oWMWMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNK0kxdolc:;,,;;;;;;:cccccccccccccccccc:,;cccccccc:;:OXNXXNNNNXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXXN0;,cccc:;;;;;;;;;;;;;;;;;;;;,,,;;;::::ccccccccccccccccccccccc::;;,,,,,,;::cccccccccccccc;....                          .'cxkc.     ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMWMMWWMNKOl,'',,,;:ccccccccccccccccccc:,;ccccccccc;;dKNNNXXXNNXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNK:';'..                              .....,::;,;;;:cccccccccccccccccc:;,,,,,;ccccccccccc;.                           .l0XWWWk.     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWW0dlc:ccccccccccccccccccccccccccc::ccccccccccc;cONNNXXNNXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNXXNKl:l.                     'll'            ,kK0OOxdolc::;;ccccccccccccccllc:;,,,;:cclcccc,                            ;O0Okoc.      ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:;clcccccccccccccccccccccccccccccccccccccccccc;;kXNNNNXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNNXNXooXK,                    .kKk;            .kMMMMMMMWNX0kdc:;;;;:ccccccccccccc::;,,,,,,'..                             ...          cNMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMWMMWWKl;:ccccccccccccccccccccccccccccccccccccccccccccccc;,kNXNXXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXNXooXMK,                    .'.               lWMMMMMMMMMMMMWX0Okdolcc:;;;;;:::;;;;,,,,:c,               .,:'                        .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXd::cccccccccccccccccccccccccccccccccccccccccccccccccc;,kNNXNXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXNO:kMWK;                                      lWMMMMMMMMMMMMMMMMMMWWNXKOxdoddddddxxkOKXWWOc.             oNMX;             .'.       :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOdc:ccccccccccccccccccccccccccccccccccccccccccccccccccccc,;kNNXXXXXXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXNxc0MMWl          ..                          lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNd,;'          c0Oo.            ;kKk'     'OMMMMMMMMMMMMMMMMMMMMMMMMMMWMWXOdc;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccc;;kNXNNXXXNXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNxc0MMM0,        .kKkko.                     .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXoxXOo,..      ..              .''.    .:OWMMMMMMMMMMMMMMMMMMWMMMMMMN0xoc::cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,;ONXNNNNNXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXN0coWMWW0,       'OWWMNd.                    lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWW0o0WWNK0kdol:::,,''''',''''''''',;:cokKNMMMMMMMMMMMMMMMMMMMMMWNKkxoc;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'cXNNNNNNXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNNXNk:kWWMW0,       'cll:.                    :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMKxkNWWWMMWWWMWWNNWWWNNNNNWWWNNNWWMMMMMMMMMMMMMMMMMMMMMMMWXOdlc:;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;,dNNXNNXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNNXNNklxNMMWKl.                             'oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOxxkXMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkdkOxlc;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,;ONXXNXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXNOccxXWWWXkl;'..                ..,;:okXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXo';xKWMWMMWWMMMMMMMMMMMMMMMMMMMMMMMMWMMMWN0xo:,'..;;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'cKNXXNXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXNXx:,,:dkXWWWWNK0Okxxxollllllllox0XWWWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWKxc;,::;:lodkxdk0XXNNWWWNXNNWWWWWWWWNXXKOxoc:;'..',;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'dNNXNXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNNNNKc'clc:;cokKNWMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdoll:,;:,;clcc:;,,'.,:::clll:;:ccllllllcc::;,,,;::cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,;ONXXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXNN0o:;:clc:;:cldOXWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xoc:;;::clccc:;;;:cccccccclccccccccccccccccccccllcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'lXNXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNKxl:;ccccc:;:coddxkkO0K0KKXNWMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMWWX0Oxdl::::cccccccccccccc:,,;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'dXNXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXN0c,:cccccclc:::;;;::;;;;:cccccllllccccodxxxdxOOOOOOOOOOOOOOkdddolc:;;;:ccccccccccccccccccccc:;;;;;;::cccccccccccccccccccccccccccccccccccccccccccccclccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccl,;0NXXNN\nNNXXXXXXXXXXXXXNNXXXXXXXXXXXXNNNNXXXXXXXXNNNNXXXXXXXXXXXXXXXXXXXXXNNNNKkoc;;;:ccccccccccccccccc:;::::;;;;,,,;;;,,,;;;;;;;;;;;;;;;,;;;:ccccccccccccccccccccccccccccccc:;,,,,,,,,,,,;;;,;;;:::ccccccccccccccccccc:::;;;,,,,,,;cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oXNXNN\nNNXXXXXXXXXXXXNNNNXXXXXXXXXXNNNNNNXXXXNNXXXXNNXXXXXXXXXXXXXXXXXXXXNNXXXNXKOd;,;,,;;;ccccccccccccccccccccccclc;:ccccccccccccccccccccccccccccccccccccccccccccccc:;;;:ccccccccc::;;;;;;;,,,,,,,,,,;;;;;;;;;;;;;,,,,,,,,,,,;;::cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,,0NXXN\nNNXXXXXXXXXXXXNNNNXXXXXXNNXNNXNXXXXNXXNNNNXXXXNXXXXXXXXXXXXXXXXXXXXNXXNNXXNKc;l::;,,,,,,,,,;;:::cccccccccc:;;;:cccccccccccccccccccccccccccccccccccccccccccccccc:;;;;;;;:cccccccccccccccccccccccccccccccccccccccccclcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'dNXNN\nNNXXXXXXXXXXXXNNXNNNXXXXXXXNNNNXNXXNXXXXXXXXXNNNNXXXXXXXXXXXXXXXXNNNNNNNNXNKc,:cccccc:;;;,,,,,,,;;;;;;;,'',:cccccccccccccccccccccccccccccccccccccccccccccccccccccccc:;;;;,,;:clccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,:KNNN\nNNXXXXXXXXXXXXNXXXNNNNXXXXXNXXNXXXNNNXXXXXXXXXNXXXXXXXXXXXXXXXNNXNNNNNNNNOooc,',,;:ccccccccllccccccccc:;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,,,,;;;::cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'dNNN\nNNXXXXXXXXXXXXNNXXNNNNXNXN0dOXNXXNNXXNNNNNKxxXNXNNXXXXXXXXXXXXNNNNNNNXXNO;';;;;,...,;;;;:;;;;;;:;;;;,,,,;;,,,,,;,,,,,,;;,,,,;;,,,,,,;;;:::cccccccccccccccccccccccccccccllccccc:;;,,,;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc':KNN\nNNXXXXXXXXXXXXXXXXXNNNNXNNk:cokKXNNNXNNNKxl;lKNXNNXXXXXXXXXXXXNNXXXXXNNXl':clccccc:;,,;;,,,,,,,,,,,,;;:cccc::::::::::::::::::::;;;,,,;,,,,,,,,;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'xNN\nNNXXXXXXXXXXXXXXXNNNXXNXXN0c:c:coOXXNNXko:c:oKNXNNXXXXXXXXXXXXNNNXXXXNNXo':ccccccccllccccccccccccccccccccccccccccccccccccccccccccccllllllcc::;;,,,,,,;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc':KN\nNNXXXXXXXXXXXXXXNXXNNNNNXNXx:ccc:clkX0o:ccc:oKNXNNNNXXXXNNNXXXXXNNNNNXXNKc'ccccccccccccccccccccccccccccccccccccccccccccccc::;;;;;;;;;;;;;;;;:ccllc::;,,,,,,,,,;;;:::::cc::ccccccccccccccccccc:::;;,,,,;,,;;;,,,;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'xN\nNNXXXXXXXXXXXXXNNKO0KXXNNXNXd:ccccc:cc:cccl:oKNXNXXNNNNXNNNXXXXXNNNNNXXXN0l;;:cccccccccccclccllccccccccllcccccllcc::;;,,,,,,,,,;;;;;;;;;,,,,,,,,,,,;:cllcc:;;;,,,,,,,,,,,,,;;;;;;,;;;;;;;;;;,,,,,,,;;;::;;;;;;;;,,,,;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oN\nNNXXXXXXXXXXXXNXN0occlddxkOK0o:cccccccccccc:lKNXNNXKkkKNNXXXXNNNNNNNNNXNNNX0dl:;,;;;;;;;;,,,;,,;;;;;;;;;,,,,;,,;;,,,,;;;:cclcccccccccccccccccccc:;;,,,,,;;:cllccccclccllcccclcccccccccccccccllclccccccccccccccccccc:;,,:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oN\nNNXXXXXXXXXXXXNXNNX0xoc:::cclc:cccccccccccc:dXKOkxoc:c0NXXXXXNNNNNNXXXXNNNNXNNKOkxddddooc'':::::::::::::::cccccccccllllllccccccccccclcccccccccccccclcc::;,,,,,;:ccccccc:;:cccclccccccccccccccccccccccccccccccccccccclc,.;ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oN\nNNXXXXXXXXXXXXXXNXXNXX0xoc:cccccccccccccccc;colc:ccc:lKNXXXXXNNNNXNXXXXXXNXXXXXXNNNNNNNN0;.clcccccccccccllc::::;;;;;;;;;,,,,,,,,,,,,;;:ccccccccccccccccccccc:;;,,,,,;:c;;:;;:clccccccccccclcccccccccccccccccccccccccccc,.:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oN\nNNXXXXXXXXNXXNNNNNXK0K00Od::ccccccccccccccc::cccccc:cONNNNXXXNNNXXXNXXXXXNNXXNNNNNXNNNXXNOc;;,,;;:::;;,,,,,,,,,,,;;;;;,;;;;;;;;;;;,,,,,,,,,,;:cccccccccccccccccccc:;,,,',cc:;;:cccccccccc:;;ccccccccccccccccccccccccccl;';lccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oN\nNNXXXXXXXNNXNNKkdolcccccc:cccccccccccccccccccccccc:l0NNNNNNNNXXXXXXXXNNNXXNNXXNNNNNNNNNXNNXKOdoooooool;';:clccccccccccccccccccccccccccccc:;;,,,,,,,;:ccccccccccccccclcc;,:cccc;,,;;;;;::;,:;,;:::cccccccccccccccccccccl;';cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:'oN\nNNXXXXXNXXNXXNXK00Okkxdoc::cccccccccccccccccccccc:l0NXXNXNNXXXXXNNNNNNXXXXXNXXXXXXXXNNNXNNXXNNNNNNNNNNXOl;:ccccccccccccccccccccccccccccccccccccc:;,,;;,,,,;;:cccccclcccc;;ccccc:,',,,,,',ccc,.,;;:clccccccccccccccccccl;.;cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,dN\nNNXXXXXNXXNNXXNNXXNNNNNX0kxl:ccccccccccccccccccc::kNXNNNNNXXXXXNNNXNXXXXXNNNXXXXNNNXXXNNNXNXXNXXXXNNXXNNXx::ccccccccccccccccccccccccccccccccccccccccccccc:;,,,,,,,;:cccl:,:cccccc:;;cl:;:ccl;':lccccccccccccccccccccccl,.:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'xW\nNNXXXXXXXXNXXNNNXXNXXNNXXNN0c:ccccccccccccccccccc:cdOXNNXNNXXXXXNNNXXXXNNNNXNNNNNNNNXXXXXXNNXXNNXNXXXNNNNNOc;cccccccccccccccccccccccccccccccccccccccc;,,;::::;;,,,,,,,,,;',cccccccc;;;,:cccc:;:lcccccccccccccccccccccc:',ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,,ON\nNNXXXXXXXXXXXXNXXXNXXNNXNXXNkc:cccccccccccccccccccc::lkKXXNNXXXXNNNXNNNNNXNNXNNNNXXXXXXXXXXXXXNNXNNNNNXNXXNKo;:cccccccccccccccccccccccccccccccccccccc:;:;;,;::;;;::::;;'''.,cccccccc;';cccccc;:llccccccccccccccclccc:,';cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'cXN\nNNXXXXXXXXXXXXNNXNXXXNNNXNXNXo:ccccccccccccccccccccccc::;cx0XXXXNNXXXNNNXXNXXXXNNXXXXXXXXXXXXXNNNNNNNNNXXNXNXkc;:cccccccccccccccccccccccccccccccccccccccc::;;;;:ccccccc::::;;cccccccccccccccc,,;;;,,,,;;;;;;;,,,,,,,,,:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;'xNN\nNNXXXXXXXXXXXXNNNXXXXNNXXXNNNOc:ccccccccccccccccccccc;,'''',lkKXXXNNNNNNXNXXXXXXNXXXXXXXXXXXXXNNXXNNNNNXNNNXXXKd:;ccccccccccccccccccccccccccccccccccccccccccc::;;::cccccccccccccccccccccccccc;',;;;;,,;;;;;,;;;;::ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc,;0NN\nNNXXXXXXXXXXXXXNNXXXXXXXNNXNNXx:ccccccccccccccccccc:,.'''''''';oOXNXXNNXXXXNNXNNXXXXXXXXXXXXXXXXXXXXXNNNNNNXNXXN0d:;ccccccccccccccccccccccccccccccccccccccccccccc;,,;:cccccccccccccccccccccclc:;;;;::cccccclcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,dNNN\nNNXXXXXXXXXXXXXNNXXNXXXNNXXXNNKl:cccccccccccccccc:,''''''''''''',:d0XNNNXXXXXNNXNXXXXXXXXXXXXXXXXXXXXNNNXNXXXNNXNNKdc:;:ccccccccccccccccccccccccccccccccccc::;;:;;:::ccccccccccccccccccccccccccccc::;;:::cclc:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccl:,lKNNN\nNNXXXXXXXXXXXXXNNXXNNXXNXXNXXXNOc:ccccccccccccc:,'''''''''''''''''.,cxKXNNNXNNXXNXXXXXXXXXXXXXXXXNXXXXXXXNNXXXNXNNXNXkoc;;cccccccccccccccccccccccccccc::;;;;;::cccccccccccccccccccccccccccccccccccccccc:;;;;'',,;;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc:,oKNXXN\nNNXXXXXXXXXXXXXXXXXNNXXNNXNXXNNXOc:ccccccccccc;''''''''''''''''''''''';lx0XNXNNNXNXNNNXXXXXNNXXXNNNNXXXXXXXXXXNXNNNXXNNXOdc;;:ccccccccccccccccccccccc;,,,::cccccccccccccccccccccccccccccccccccccccccccccc;'.'''''''',,;;:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;;xXNNNNN\nNNXXXXXXXXXXXXXXXXXXXXXNNXNXXNXNNk:ccccccccc;,,'''''''''''''''''''''''''';lx0XNNNNXXNXXNNNNXXXXXNXXNNNNNNNXXXXXNXXNNNNNXXNXOdl,,;:cccccccccccccccccccc:::;::;::;;:::::ccccccccccccccccccccccccccccccccc;'.'''''''''''''''',;::ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc;;lONNNXNNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXNXx:ccccc:,''''''''''''''''''''''''''''''''';lk0XNXXNXXNXXXXNNNNNXXXNNNNNXXXXXNNNNNNNNNXXNNKOo,..,,;:ccccccccccccccccccccccccc::::;,,,;:ccccccccccccccccccccccccccccc:,.''''''''''''''''''''''',;;:ccccccccccccccccccccccccccccccccccccccccccccccccccccccclccc;,;lOXXXNXXXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXx:cc:,'.'''''''''''''''''''''''''''''''''''';cdkKNXXNXXXXNNNNNXXXXXXXXXXXXXXXNNXXXNNXKko;'.''.',;;,,,;::ccccccccccccccccccc::;;:::cccccccccccccccccccccccccccccc:,''''''''''''''''''''''''''''.',,;;::cccccccccccccccccccccccccccccccccccccccccccccccc::;,,..,:lkKNXXNXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXNXx:,'.''''''''''''''''''''''''''''''''''''''''.':ldOXNNNXXXXXXXXXXXXXXXXXXXXXXXNNX0xl;'.''''''..,:c:;;,,,,;;:cccccccccccc:,,,;:ccccccccccccccccccccccccccccccc:,'''''''''''''''''''''''''''''''''''''',,,;;::ccccccccccccccccccccccccccccccccccc:;,,,,,,;:;..,'.':d0XNXNN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXo'''''''''''''''''''''''''''''''''''''''''''''''..,:ld0XNNXNNXXXNNXNNNXXXXXNNXOdc,..'''''''''''..,;:ccc::;,,,,,;::cccccc:::::;;;:::::;;:ccccccccccccccccccc:,'.''''''''''''''''''''''''''''''''''''''''''''',,,,;:ccccccccccccccccccccc::;,,,,,,,,;:cclc;..'','''.'cx0NN\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNXx;'''''''''''''''''''''''''''''''''''''''''''''''''''';lox0XNNXXNNNNNXXNNNNKx:'..''''''''''''''''..',:ccccccc:;,,,,,;;,;:cccclccccccc::;;:ccccccccccccccc:;''''''''''''''''''''''''''''''''''''''''''''''''''''...',;;;:ccc::;;,,,,,,,,,,,;;:ccccccccc:,..'''''''''.',oK\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXX0o,'''''''''''''''''''''''''''''''''''''''''''''''''''''',cdOXNNXNNNXNNXOl;'.''''''''''''''''''''''..';cccccccccccc:;;,,,,,,,,;;::ccccc:;;:cccccccccccc;'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.''','..',;;::::cccccccccccccc:;'..''''''''''''''',\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXNXXXNNXOc,''''''''''''''''''''''''''''''''''''''''''''''''''''''',:okKXNXNKd:'.''''''''''''''''''''''''''''.',;cccccccccccccccc::;;,,,,,,'.',,,.';ccccccc:;'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,;:cccccccccccc:,,'...''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNXXXNKx;'''''''''''''''''''''''''''''''''''''''''''''''''''''''''';lxkx;''''''''''''''''''''''''''''''''''..',;ccccccccccccccccccccccc:,'',,,,;;:cccc;'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.'',,;;:ccc:,'...''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNXXXXXXNKd;.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..'''''''''''''''''''''''''''''''''''''..',;::ccccccccccccccccccccccclcccc;;;;'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..'..''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXXXXNNNXOl,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''...'',,;:ccccccccccccccccccccccc:,'.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..'''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNNXOo;'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''....'',,;:cccccccccccccccc:,..''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNNXNXXNNXNNXOl,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''......'',;;::cccccccccc:;;;,''.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXNNXXXXNNNNXXXXOdc,'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''......''',,;;::cccllc:;,,'..'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXXXXXNNNNXXNXKkl;''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''........''''',,,;;,'....''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXNX0o,.''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.................''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNXXNNNNXXXNXNNXXXNXkc''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''......'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNNNNXNNKx;''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.....''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNNNXXNXXXNN0l,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.....''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXNXXXXNXx;''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''......''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXNXXNNXNXOc'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''......''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXNNNNXXXXXXNKd,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.....''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNXXXXXXNNXXXNNXNXx;'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.....''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNXXNNXXNNOc'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.....'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXXNXx:,'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXNNNNKd;'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXNNNk,.'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',")
    print("Apu- Listen theres no going back if you go down this route, if you do this we will never be able to see our frens again but at the same time I can't see to begin with so oh well lets go!")
    who = input("These are the members who are willing to tussel\n"
    "1.)PEPE!\n"
    "2.)Wizard apustaja")
    if who == "1":
        q = """ delete from heroes on"""
        execute_query(q,())
        print("As you say I want to fight PEPE! there is a bright flash of light that seems to engulf everything and a voice that say /NAH/ as the light fades to notice everyone even yourself is simply gone")
    if who == "2":
        q = """ delete from heroes where id = 7"""
        execute_query(q,())
        print("The Wizard comes down from his room to meet you in the arena and the battle starts!\n"
        "The battle is a back and forther between the two of you for a few minutes, then hours, then days!\n"
        "you both are so worn out that even breathing seems hard Wizard says\n"
        "STOP! I'm tired of this! I'm tired of you! and I'm tired of this poorly coded world!!!\n"
        "everyone seems confused about that last statment as they watch the wizard run a sql injection and he deletes himself...\n\n"
        "You won!")
    helper(me)
at_the_door()



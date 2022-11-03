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
        SELECT * from heros
    """

    list_of_heroes = execute_query(query).fetchall()
    print(list_of_heroes)
    for record in list_of_heroes:
        print(record[1])


print("----------------------------------------------------START-----------------------------------------------------------")

def at_the_door():
    password = input("Whats your the password?:")

    if password != "PEPE":
        print("Wrong! *Muffled sounds of Helping from behind the door*")
    if password == "PEPE":
        me = input("Welcome to the House of Pepe, Whats your name?:")
        a = input("Hello! " + me + " My name is Apu Apustaja! \n  I'm the helper around here! what you you Like to do?\n 1.) Tour the House? \n 2.) Meet the House Members?\n 3.)Become a House Member?:")
        if a == '1':
            tour_the_house(me)
        elif a == '2':
            select_all()
        elif a == '3':
            become_a_member(me)

def tour_the_house(me):
    me = me
    print("----------------------------------------------------HOUSE TOUR---------------------------------------------------------")
    print("Apu- Follow me! we'll go see the house! But let's keep to the safe side of the house for the moment. \n  *Apu leeps you through the house giving you info on every littel detail but for some reason you cant get it out of you head that someone somewhere is watching you...*")
    room = input("This is our leaders room! He is amazing, wonderful, confusing, beautiful, powerful, and generally perfect! HE\n IS\n PEPE!\n Do you have any questions? \n 1.) Can we meet him? \n 2.) Where did he come from? \n 3.) No thanks let's keep moving, He sounds a lil intemidating! :")
    if room == '2':
        def call_for_him():
            query = """
                SELECT Pepe.biography from heros
            """
            he = execute_query(query)
            print(he)
            lets_go()
    if  room == '1':
        query = """
            SELECT me FROM heros
            where exists(SELECT me FROM heros)
        """
        check = execute_query(query)
        if check == True:
            print("You hear a deep rumble from this universe to the next as the door opens and a blinding light blinds you for only a moment before the door closes. You didn't see anything but you know that you just saw the rarest of them all!")
            lets_go()
        if check == False:
            print("you feel a deep rumble, like the worlds are falling apart, your vision blurs as you hear Apu say *Members only I'm afraid.*.")
            lets_go()
    if room == '3':
        lets_go()

    def lets_go(me):
        q = input("Apu- Are you having fun? (yes/no):")
        if q == "no":
            print("*Apu turns to you and helps you have fun* (You are now having fun.)")
        if q == 'yes':
            print("Apu- Great!")
        now = input("Apu- Here we have a frens room Wizard! \n  He is super powerful and fun! Would you like to meet h--\n*BOOM*\n (The Wizard is blown out of his room through his door by a MASSIVE explosion)\n Apu- Are you ok Wizzarding 101 ?!?! \n WIzard- F*** THAT HURT!!! but yeah I'm ok, but my toilet will never be the same *Wizard notices you* \n LMAO look at this scrub! You don't even have any Magical Robes! \n \nWhat will you say back? 1.) Why would you say that... *you start to cry*\n 2.) Say nothing and try and act tough! \n 3.) You see his Robes are covered in a massive amount of poop and simply laugh at him :")
        if now == '1':
            print("Apu tells Wizard that he is covered in poop and then turns and helps you feel better as Wizard quitely walks back into his room")
            helper(me)
        if now == '2':
            print("Wizard locks eyes with you as he stands up and says *ya know your pretty cool! not many others around here can take a joke and not get mad but hurt! then walks back into his room* (You and Wizard are now frens!)")
            helper(me)
        if now == '3':
            print("Wizard gets mad and screams *We are as of now enemys! I will see you in Hell!*")
            helper(me)

    def helper(me):
        pass


at_the_door()



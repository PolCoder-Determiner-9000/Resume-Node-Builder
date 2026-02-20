import JobLL

from skills import skill
from skills import experience

def fill_information():
    pass


def main():

    print("Program that takes users skills and experience as input and outputs a\nregex string")


    
    loop = True
    while loop:

        # skills and experiences will be made as a class
        # skills: skill name, proficientcy, additional comments
        # experience: experience type, time started, time ended, additional comments
        
        print("options: 1. add skills\n 2. add experience\n")

        user_skills = []
        user_experience = []
        action = str(input("Action: "))

        if action == '1':
            pass
        elif action == '2':
            pass
        

        if action == 'q':
            loop = False


    

    return


if __name__ == '__main__':
    main()


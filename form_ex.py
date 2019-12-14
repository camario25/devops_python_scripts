import re


def form():
    person = {}
    name_exp = r'[^\d\`\~\!\@\#\$\%\^\&\*\(\)|-|_\+\=\{\}\[\]\:\;\'\"\<\,\>\.\?\/\\]+'
    fname = input("Enter first name ").strip()
    while re.fullmatch(name_exp, fname) == None:
        print("This first name your provided is not valid")
        fname = input("Enter first name ").strip()
    person['first-name'] = fname
    print(f"Your first name is {fname}")
    lname = input("Enter last name ").strip()
    while lname.isalpha() == False:
        print("This first name your provided is not valid")
        lname = input("Enter last name ").strip()
    person['last-name'] = lname
    print(f"Your last name is {lname}")
    dob = input("Enter Date of Birth ").strip()
    person['dob'] = dob
    print(f"Your Date of Birth is {dob}")#format date and return age as well
    email = input("Enter email ").strip()
    person['email'] = email
    print(f"Your email is {email}")
    zip_code = input("Enter zip code ").strip()
    while zip_code.isdigit() == False:
        print("This zip code you provided is not valid")
        zip_code = input("Enter zip code ").strip()
    person['zip-code'] = zip_code
    print(f"Your zip code is {zip_code}")#return city and state as well
    race = input("Enter first race or press enter to skip ").strip()
    person['race'] = race
    print(f"Your race is {race}")
    sex = input("Enter gender ").strip()
    person['sex'] = sex
    print(f"Your gender is {sex}")
    print(person)

if __name__ == "__main__":
    form()
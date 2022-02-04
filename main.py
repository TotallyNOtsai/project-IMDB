# Can get apikey at https://imdb-api.com

from imdb import Imdb
from os import system
from slowprint.slowprint import *
import keyboard
import smtplib
from email.message import EmailMessage

# Print Title info
def tt_info(data):
    slowprint(f"Title: {data['fullTitle']}\nGenres: {data['genres']}\nContent Rating: {data['contentRating']}\
\nType: {data['type']}\nRelease date: {data['releaseDate']}\nRuntime: {data['runtimeStr']}\nIMDB Rating: {data['imDbRating']}\
\nAwards: {data['awards']}\nStars: {data['stars']}\n\nPlot:\n{data['plot']}",0.1)

    print("(Press SPACE to continue)")
    keyboard.wait('space')

    # More details
    while 1:
            print("\nMore info\n1.Actors\n2.Writers\n3.Directors\n4.Companies\n5.Boxoffice\n6.More like this\n0.Back")
            try:
                moreinfo = int(input(": "))
            
            # Except user to enter other int
            except ValueError:
                slowprint("Number only!", 1)

            else:
                # Print acotrs that involved
                if moreinfo == 1:
                    print("\n")
                    for actors in data['actorList']:
                        slowprint(f"Name: {actors['name']}(id: {actors['id']})",0.01)

                # Print writers that involved
                elif moreinfo == 2:
                    print("\n")
                    for writers in data['writerList']:
                        slowprint(f"Name: {writers['name']}(id: {writers['id']})",0.05)

                # Print directors that involved 
                elif moreinfo == 3:
                    print("\n")
                    for directors in data['directorList']:
                        slowprint(f"Name: {directors['name']}(id: {directors['id']})",0.05)

                # Print companys that involved
                elif moreinfo == 4:
                    print("\n")
                    for companys in data['companyList']:
                            slowprint(f"Name: {companys['name']}(id: {companys['id']})",0.05)

                # Print Boxoffice data     
                elif moreinfo == 5:
                    print("\n")
                    info = data['boxOffice']
                    slowprint(f"Budget: {info['budget']}\nOpening Weekend USA: {info['openingWeekendUSA']}\nGross USA: {'grossUSA'}\
\nCumulative Worldwide Gross: {info['cumulativeWorldwideGross']}",0.05)

                # Print similar titles       
                elif moreinfo == 6:
                    print("\n")
                    for similars in data['similars']:
                        slowprint(f"Name: {similars['title']}(id: {similars['id']}),Rating: {similars['imDbRating']}",0.01)

                # Exit       
                else:
                    return

# Print Person info
def nm_info(data):
    slowprint(f"Name: {data['name']}\nRole: {data['role']}\nBirthday: {data['birthDate']}\nDeath Date: {data['deathDate']}\
\nAwards: {data['awards']}\n\nSummary: {data['summary']}",0.01)
    
    # More details
    while 1:
        try:
            userchoice = int(input("\nMore info\n1.Known for\n0.Back\n: "))

        # Except user to enter other int
        except ValueError:
            slowprint("Number only!", 1)
        
        # Print well known movies/series that this person involved
        else:
            if userchoice == 1:
                print("\n")
                for results in data['knownFor']:
                    slowprint(f"Title: {results['fullTitle']},Id: {results['id']}\nRole: {results['role']}",0.03)

                print("(Press SPACE to continue)")
                keyboard.wait('space')

            else:
                return

# Print Company info
def co_info(data):
    slowprint(f"{data['name']}",0.3)
    print("\n")
    for item in data['items']:
        print(f"{item['title']}({item['year']}),id: {item['id']},Imdb Rating: {item['imDbRating']} ")

    print("\n(Press SPACE to continue)")
    keyboard.wait('space')

# In Theaters and Coming Soon
def intheaters_comingsoon(data):
    try:
        userchoice = int(input(f"There is {len(data['items'])} movie/series how many of them do u want to see: "))
    
    # Except user to enter other int
    except ValueError:
        slowprint("Number only!", 1)
    
    # Print Data
    else:
        count = 0
        for results in data['items']:
            slowprint(f"\nTitle: {results['fullTitle']}\nid: {results['id']}\nGenres: {results['genres']}\n\
Content Rating: {results['contentRating']}\nRelease date: {results['releaseState']}\nRuntime: {results['runtimeStr']}\n\
Directors: {results['directors']}\nStars: {results['stars']}\n\nPlot:\n{results['plot']}\n",0.01)
            count += 1

            if count == userchoice:
                print("(Press SPACE to continue)")
                keyboard.wait('space')
                return

# Print Top 250
def top250_info(item):
    slowprint(f"{item['rank' ]}.{item['fullTitle']}\nId: {item['id']}\nIMDB Rating: {item['imDbRating']}",0.5)

# Print Weekend Boxoffice 
def weekendboxoffice_info(item):
    slowprint(f"{item['rank']}. Title: {item['title']}\nid: {item['id']}\n\n\
Weeks: {item['weeks']}\nWeekend: {item['weekend']}\nGross: {item['gross']}\n",0.3)

# Print Boxoffice Alltime 
def boxofficealltime_info(item):
    slowprint(f"{item['rank']}. Title: {item['title']}({item['year']})\nid: {item['id']}\n\n\
Worldwide Lifetime Gross: {item['worldwideLifetimeGross']}\nDomestic Lifetime Gross: {item['domesticLifetimeGross']}({item['domestic']})\
\nForeign Lifetime Gross: {item['foreignLifetimeGross']}({item['foreign']})\n", 0.3)

# Function that return info by rank
def rank_info(data, type):
    # Type
    # 1 and 2 print top250
    # 3 and 4 print boxoffice
    system('cls')
    rank = input("Rank: ")
    for item in data['items']:
        if item['rank'] == rank:
            if type == 1 or type == 2:
                top250_info(item)

            if type == 3:
                weekendboxoffice_info(item)

            if type == 4:
                boxofficealltime_info(item)

            print("(Press SPACE to continue)")
            keyboard.wait('space') 
            return
            
    slowprint("\nERROR!Try again", 0.5) 
    print("(Press SPACE to continue)")
    keyboard.wait('space')

# Send title info withh email
def send_email(data):
    preset_content = f"INFO\n----------\nTitle: {data['fullTitle']}\nGenres: {data['genres']}\nContent Rating: {data['contentRating']}\
\nType: {data['type']}\nRelease date: {data['releaseDate']}\nRuntime: {data['runtimeStr']}\nIMDB Rating: {data['imDbRating']}\
\nAwards: {data['awards']}\nStars: {data['stars']}\nIMDB Link: https://www.imdb.com/title/{data['id']}\n\nPlot:\n{data['plot']}"

    msg = EmailMessage()

    email_address = input("Email: ")
    email_password = input("Password: ")
    send_to = input("Send to(email address): ")
    subject = input("Subject(optional): ")
    content = input("Body(optional): ")

    msg['From'] = email_address
    msg['To'] = send_to
    msg['Subject'] = subject
    msg.set_content(f"{content}\n\n{preset_content}")


    with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
        try:
            connection.login(email_address,email_password)
        
        # If user's email address was enter incorrectly
        except TypeError:
            slowprint("ERROR!pls enter your email address correctly",1)
        
        # If user's email password was enter incorrectly
        except smtplib.SMTPAuthenticationError:
            slowprint("ERROR!pls enter your email password correctly", 1)

        else:
            try:
                connection.send_message(msg)
            
            # If receiver's email address was enter incorrectly
            except smtplib.SMTPRecipientsRefused:
                slowprint("ERROR!pls enter the email address that you are going to send email correctly", 1)
            
            else:
                print("\nSuccess\n(Press SPACE to continue)")
                keyboard.wait('space') 
# Main
def main():
    # Can get apikey at https://imdb-api.com/
    apikey = input("Apikey: ")
    imdb = Imdb(apikey)

    # Test if apikey is useable
    data = imdb.searchall("Testing")
    if data['errorMessage'] == "Invalid API Key":
        slowprint(f"\n{data['errorMessage']}!\nCan get apikey at https://imdb-api.com\n", 0.8)
        print("(Press SPACE to continue)")
        keyboard.wait('space')
        return
    
    # Main Loop
    while 1:
        # Home
        system('cls')
        print("HOME\n\n1.Search\n2.Get info(imdb id require)\n3.Top 250\n4.Coming Soon\n5.In Theaters\n6.Weekend boxoffice\
\n7.Boxoffice All time\n8.Send Info About Movie/Series(email)\n0.Exit")
        try:
            userchoice =int(input(": "))

        # Except user to enter other int
        except ValueError:
            slowprint("Number only!", 1)

        else:
            # Exit
            if userchoice == 0:return
                
            # Search
            elif userchoice == 1:
                system('cls')
                search = input("Search: ")
                # If user didnt enter anything,
                # Send back to Home
                if search == "":
                    slowprint("Need to input something!",1)

                else:
                    # Get data
                    data = imdb.searchall(search)

                    system('cls')
                    # Print data
                    for result in data['results']:                  
                        slowprint(f"{result['title']}{result['description']},IMDB id: {result['id']}", 0.03)

                    print("(Press SPACE to continue)")
                    keyboard.wait('space')

            # Get detail information of an id
            elif userchoice == 2:
                system('cls')
                id = input("Enter imdb id to get info: " )
                data = imdb.getinfo_id(id)

                if data:
                    # tt = Title(movies/series),nm = Name,co = Company
                    # Check what kind of data needed to print
                    if data['id'][:2] == 'tt':
                        tt_info(data)
                    
                    elif data['id'][:2] == 'nm':
                        nm_info(data)
                    
                    elif data['id'][:2] == 'co':
                        co_info(data)

                # If id is doesn't start with "tt","nm" and "co"
                else:
                    slowprint("ERROR!Try again", 0.5)
                    print("(Press SPACE to continue)")
                    keyboard.wait('space')

            #Top 250 movies/series  
            elif userchoice == 3:
                run = True
                while run:
                    system('cls')
                    print("Top 250\n")
                    try:
                        type = int(input("1.Movies\n2.Series\n0.Back\n: "))
                        
                    # Except user to enter other int
                    except ValueError:
                        slowprint("Number only!", 1)
                    
                    else:
                        # If user input is 3 or 4 code will print out boxoffice
                        if type != 1 and type != 2 and type != 0:
                            slowprint("ERROR!1,2 and 0 only!", 1)

                        # Send back to Home
                        elif type == 0:run = False

                        # Print data
                        else:
                            data = imdb.get_info(type)
                            if data:
                                rank_info(data, type)

            # Coming Soon
            elif userchoice == 4:
                system('cls')
                print("Coming Soon\n")
                data = imdb.get_info(3)
                if data:
                    intheaters_comingsoon(data)
            
            # In Theaters
            elif userchoice == 5:
                system('cls')
                print("In Theaters\n")
                data = imdb.get_info(4)
                if data:
                    intheaters_comingsoon(data)

            # Weekend Boxoffice
            elif userchoice == 6:
                system('cls')
                print("Weekend Boxoffice\n")
                data = imdb.get_info(5)
                if data:
                    rank_info(data, 3)
            
            # Boxoffice Alltime
            elif userchoice == 7:
                system('cls')
                print("Boxoffice Alltime\n")
                data = imdb.get_info(6)
                if data:
                    rank_info(data, 4)

            # Send Email
            # Can only send title info 
            elif userchoice == 8:
                system('cls')
                print("Send Email\n")
                id = input("Movie/Series Imdb id: ")
                # Check if id is title's id
                if id[:2] != "tt":
                    slowprint("Movies and Series Only!!",1)

                else:
                    data = imdb.getinfo_id(id)
                    send_email(data)
            
if __name__ == '__main__':
    main()

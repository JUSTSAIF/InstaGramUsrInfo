########################
# Coded By Me ==> SAIF #
#     2020/June/8      #
########################
import urllib.request, json ,time, os.path, re, random, string, requests

########################### START ASCII ###########################
print('''
          ▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
       ▄▄██▌█ Insta: @qq_iq    
       ▌▐██▌█ GitHub: JUSTSAIF 
    ███████▌█ Tool : Get Insta Acc Info
    ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
    ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀(@)
''')
########################### END ASCII ###########################

UsrFile = input('Users File : ')
CKFile = os.path.exists(UsrFile)
if CKFile == False:
    print('File Not Found !!')
    exit()
# Read Users File
usr = open(UsrFile ,'r')
usr = usr.readlines()

for usrs in usr:
        try:
            with urllib.request.urlopen("https://www.instagram.com/" + usrs.replace('\n', '').replace(' ', '') + "/?__a=1") as url:
                data = json.loads(url.read().decode())
                username      =  str(data['graphql']['user']['username'])                              # Get Username
                FullName      =  str(data['graphql']['user']['full_name'])                             # Get Full Name
                Followers     =  str(data['graphql']['user']['edge_followed_by'])                      # Get Followers
                Following     =  str(data['graphql']['user']['edge_follow'])                           # Get Following
                POSTS         =  str(data['graphql']['user']['edge_owner_to_timeline_media']['count']) # Get Num of POSTs
                Profile_Pic   =  str(data['graphql']['user']['profile_pic_url_hd'])                    # Profile Pic
                Bio           =  str(data['graphql']['user']['biography'])                             # Get Bio
                Website_Link  =  str(data['graphql']['user']['external_url'])                          # Get Website Link
                Private_Not   =  str(data['graphql']['user']['is_private'])                            # Acc Private Or Not
                ############## Some Edit ##############
                #Followers
                Followers = re.search("{'count':(.*)}", Followers)
                Followers = Followers.group(1)
                #Following
                Following = re.search("{'count':(.*)}", Following)
                Following = Following.group(1)
                if Private_Not == "True":
                    Private_Not = "Yes is Private"
                elif Private_Not == "False":
                    Private_Not = "Not Private (PUBLIC)"
                # ======= ShortCut Photo URL =======
                website = 'https://v.ht/processreq.php'
                # Random Str Function 
                def randomString(stringLength=8):
                    letters = "1234567890QAZWSXEDCRFVTGBYHNUJMIKqazwsxedcrfvtgbyhnujmikolp"
                    return ''.join(random.choice(letters) for i in range(stringLength)) + "Mr28"
                MyRanURL    = randomString(4)
                Photo_Url   = {'txt_url': Profile_Pic,'txt_name':MyRanURL}
                GetUrl = requests.post(website, data=Photo_Url)
                Profile_Pic = "https://v.ht/" + MyRanURL
                #######################################
                line_F = "================================================================================="
                print(line_F)
                AllData = 'Username : ' + username + '\n' + 'Full Name : ' + FullName + '\n' + 'Followers : ' + Followers + '\n' + 'Following : ' + Following + '\n' + 'POSTS Num : ' + POSTS + '\n' + 'Bio : ' + Bio + '\n' + 'Website Link : ' + Website_Link + '\n' + "profile Photo :" + Profile_Pic + '\n' + 'Private Or Not : ' + Private_Not
                print(AllData)
                print(line_F)
                print('\n\n')
                # Save Users File 
                NewUsr = open('NewUSR.txt','a', encoding="utf-8")
                NewUsr.write(line_F + '\n' + AllData + '\n' + line_F + "\n\n\n\n\n")
                NewUsr.close()
                time.sleep(1)
        except:
            print("=================================================================================")
            print('Not Found :: User')
            print("=================================================================================")
            print('\n\n')
            time.sleep(1)
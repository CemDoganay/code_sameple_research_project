import requests
import os
import csv

csv_androidx_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\\wip-jetpack-code\\3_Get_list_of_androidX_apps\\get_list_of_androidx_apps.csv'
csv_google_play_existance_location = 'C:\\Users\\dogan\Desktop\\tru_repo\\wip-jetpack-code\\6_Play_Store_Availability\\google_play_existance.csv'


# opens the cvs files:
with open(csv_androidx_location, 'r') as csv_androidx, \
        open(csv_google_play_existance_location, 'w', newline='') as csv_google_play_existance:

    # creates a reader or a writer for each csv file:
    csv_androidx_reader = csv.reader(csv_androidx)
    csv_google_play_existance_writer = csv.writer(
        csv_google_play_existance, delimiter=',')

    # for each line of the androidx csv, saves the information into variables.
    for line in csv_androidx_reader:

        # name of the app:
        app_name = line[0]

        # if AndroidX or else:
        android_x = line[1]

        # create the app url:
        app_url = 'https://play.google.com/store/apps/details?id=' + app_name

        # Check if website exist and record:
        if android_x == 'AndroidX':
            request = requests.get(app_url)
            if request.status_code == 200:
                print('Web site exists')
                csv_google_play_existance_writer.writerow(
                    [app_name, "exist"])
            else:
                print('Web site does not exist')
                csv_google_play_existance_writer.writerow(
                    [app_name, "dont exist"])

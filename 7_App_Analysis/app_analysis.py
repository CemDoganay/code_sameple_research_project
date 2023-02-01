import requests
import os
import csv
from bs4 import BeautifulSoup

# beautifulsoup and lxml packages needs to be installed


csv_google_play_existance_with_Androidx_location = 'C:\\Users\\dogan\Desktop\\tru_repo\\wip-jetpack-code\\6_Play_Store_Availability\\google_play_existance_with_Androidx.csv'
csv_app_analysis_location = 'C:\\Users\\dogan\Desktop\\tru_repo\\wip-jetpack-code\\7_App_Analysis\\app_analysis.csv'
with open(csv_google_play_existance_with_Androidx_location, 'r') as csv_google_play_existance, \
        open(csv_app_analysis_location, 'w', newline='') as csv_app_analysis:

    # creates a reader or a writer for each csv file:
    csv_google_play_existance_reader = csv.reader(csv_google_play_existance)
    csv_app_analysis_writer = csv.writer(
        csv_app_analysis, delimiter=',')

    # for each line of the androidx csv, saves the information into variables.
    for line in csv_google_play_existance_reader:

        # name of the app:
        app_name = line[0]

        # if exist on google play:
        existance = line[1]

        if existance == "exist":
            existance = "Yes"
        else:
            existance = "No"

        # if AndroidX or else:
        android_x = line[2]

        if android_x == "androix":
            android_x = "Yes"
        else:
            android_x = "No"

        # if it exist on google play store:
        if existance == "Yes":

            # create the app url:
            app_url = 'https://play.google.com/store/apps/details?id=' + app_name

            # get the page as html text:
            html_text = requests.get(app_url).text

            # run the beautifulsoup:
            soup = BeautifulSoup(html_text, 'lxml')

            # find the class that has rating variable in it:
            rating = soup.find('div', class_='LvvOW')

            # transform into string
            rating_string = str(rating)

            # filtering and trimming operation:
            rating_string_start = r'aria-label="Rated '
            rating_string_end = r' stars out of five stars"'
            filtered_rating_string = rating_string[rating_string.find(
                rating_string_start)+len(rating_string_start):rating_string.rfind(rating_string_end)]

            # if empty, mark it as N/A:
            if not filtered_rating_string:
                filtered_rating_string = "N/A"

            # find the class that has downloads variable in it:
            downloads = soup.find_all('div', class_='hAyfc')

            # transform into string
            downloads_string = str(downloads)

            # filtering and trimming operation:
            downloads_string_start = r'Installs</div><span class="htlgb"><div class="IQ1z0d"><span class="htlgb">'
            downloads_string_end = r'</span></div></span></div>, <div class="hAyfc"><div class="BgcNfc">Current Version'
            filtered_downloads_string = downloads_string[downloads_string.find(
                downloads_string_start)+len(downloads_string_start):downloads_string.rfind(downloads_string_end)]

            # if empty, mark it as N/A:
            if not filtered_downloads_string:
                filtered_downloads_string = "N/A"

            # find the class that has genre variable in it:
            category = soup.find_all('a', itemprop="genre")

            # transform into string
            category_string = str(category)

            # filtering and trimming operation:
            category_string_start = r'/store/apps/category/'
            category_string_end = r'" itemprop="genre"'
            filtered_category_string = category_string[category_string.find(
                category_string_start)+len(category_string_start):category_string.rfind(category_string_end)]
            filtered_category_string = filtered_category_string.split("_")[0]

            # if empty, mark it as N/A:
            if not filtered_category_string:
                filtered_category_string = "N/A"

        # if it doesnt exist on google play store, mark as N/A:
        else:
            filtered_rating_string = "N/A"
            filtered_downloads_string = "N/A"
            filtered_category_string = "N/A"

        # write the values into csv file:
        csv_app_analysis_writer.writerow(
            [app_name, android_x, existance, filtered_downloads_string, filtered_rating_string, filtered_category_string])

        # print the values:
        print(app_name + " " + android_x + " " + existance + " " + filtered_downloads_string
              + " " + filtered_rating_string + " " + filtered_category_string)

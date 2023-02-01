import os
import csv

# file locations
csv_write_location = 'C:\\Users\\dogan\Desktop\\tru_repo\wip-jetpack-code\\3_Get_list_of_androidX_apps\\get_list_of_androidx_apps.csv'
repo_location = 'C:\\Users\\dogan\\Desktop\\f-droid_cloned_repos'

# opens the csv file:
with open(csv_write_location, 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')

    # gets app folder names and iterates:
    for app_name in os.listdir(repo_location):

        # gets the app folder location:
        app_location = repo_location + '\\' + app_name

        # Checks if file exist:
        if os.path.exists(app_location + '\\gradle.properties') == True:

            # reads the file:
            with open(app_location + '\\gradle.properties') as f:

                # adds the app into the csv file and marks as 'AndroidX':
                if 'android.useAndroidX=true' and 'android.enableJetifier=true' in f.read():
                    csv_writer.writerow([app_name, 'AndroidX'])

                # adds the app into the csv file and marks as 'NOT AndroidX':
                else:
                    csv_writer.writerow([app_name, 'NOT AndroidX'])

         # adds the app into the csv file and marks as 'gradle.properties NOT FOUND':
        else:
            csv_writer.writerow([app_name, 'gradle.properties NOT FOUND'])

print("completed")

import os
import csv

# file locations:
csv_androidx_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\\wip-jetpack-code\\3_Get_list_of_androidX_apps\\get_list_of_androidx_apps.csv'
csv_androidx_and_java_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\\wip-jetpack-code\\8_get_list_of_androidx_and_java\\list_of_androidx_and_java.csv'
repo_location = 'C:\\Users\\dogan\\Desktop\\f-droid_cloned_repos'


def kotlin_finder(app_location):
    app_language = "Java"
    # recursive directory walk:
    for root, dirs, files in os.walk(app_location):
        for file in files:

            # if file extention is '.kt'.
            if file.endswith(".kt"):
                app_language = "Kotlin"
                return app_language

    return app_language


# opens the cvs files:
with open(csv_androidx_location, 'r') as csv_androidx, \
        open(csv_androidx_and_java_location, 'w', newline='') as csv_androidx_and_java:

    # creates a reader or a writer for each csv file:
    csv_androidx_reader = csv.reader(csv_androidx)
    csv_androidx_and_java_writer = csv.writer(
        csv_androidx_and_java, delimiter=',')

    # for each line of the androidx csv, saves the information into variables.
    for line_ in csv_androidx_reader:

        # name of the app:
        app_name = line_[0]

        # if AndroidX or else:
        android_x = line_[1]

        # app location:
        app_location = repo_location + "\\" + app_name

        # checks if app uses AndroidX and file path exist:
        if android_x == 'AndroidX' and os.path.isdir(app_location):
            app_language = kotlin_finder(app_location)

            csv_androidx_and_java_writer.writerow(
                [app_name, app_language])

            print('Completed for ' + app_name)

        # give error if app folder is missing:
        elif android_x == 'AndroidX':
            print('ERROR: directory of ' + android_x + ' is missing!')
            csv_androidx_and_java_writer.writerow(
                [app_name, "ERROR, DIRECTORY IS MISSING!"])

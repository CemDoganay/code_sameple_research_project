import os
import csv

# file locations:
csv_androidx_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\\wip-jetpack-code\\3_Get_list_of_androidX_apps\\get_list_of_androidx_apps.csv'
csv_used_libraries_location = 'C:\\Users\\dogan\Desktop\\tru_repo\\wip-jetpack-code\\4_Identify_Used_Libraries\\used_libraries.csv'
csv_used_classes_location = 'C:\\Users\\dogan\Desktop\\tru_repo\\wip-jetpack-code\\4_Identify_Used_Libraries\\used_classes.csv'
csv_project_summary_location = 'C:\\Users\\dogan\Desktop\\tru_repo\\wip-jetpack-code\\4_Identify_Used_Libraries\\project_summary.csv'
repo_location = 'C:\\Users\\dogan\\Desktop\\f-droid_cloned_repos'

# opens the cvs files:
with open(csv_androidx_location, 'r') as csv_androidx, \
        open(csv_used_libraries_location, 'w', newline='') as csv_used_libraries, \
        open(csv_used_classes_location, 'w', newline='') as csv_used_classes, \
        open(csv_project_summary_location, 'w', newline='') as csv_project_summary:

    # creates a reader or a writer for each csv file:
    csv_androidx_reader = csv.reader(csv_androidx)
    csv_used_libraries_writer = csv.writer(csv_used_libraries, delimiter=',')
    csv_used_classes_writer = csv.writer(csv_used_classes, delimiter=',')
    csv_project_summary_writer = csv.writer(csv_project_summary, delimiter=',')

    # allocates the first row of the summary csv for headers:
    csv_project_summary_writer.writerow(
        ['PROJECT_NAME', 'USED_LIBRARIES', 'USED_CLASSES'])

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

            # creates sets for classes and libraries:
            all_libraries = set()
            all_class_identifiers = set()

            # recursive directory walk:
            for root, dirs, files in os.walk(app_location):
                for file in files:

                    # open the file if file extention is '.java'.
                    if file.endswith(".java"):
                        with open(os.path.join(root, file), encoding="utf8") as f:

                            # checks if any of the lines in the file starts with following:
                            for line in f:
                                if line.startswith('import androidx') or line.startswith('import static androidx'):

                                    # remove 'import ' from the string:
                                    package = line.removeprefix('import ')

                                    # remove 'static' from the string:
                                    if(package.startswith('static')):
                                        package = package.removeprefix(
                                            'static ')

                                    # remove ';\n' from the string:
                                    package = package.replace(';\n', '')

                                    # trim everything after second '.':
                                    library = ".".join(
                                        package.split(".", 2)[:2])

                                    # add the library into the set (allows only unique):
                                    all_libraries.add(library)

                                    # add the class identifier into the set (allows only unique):
                                    all_class_identifiers.add(package)

                                else:
                                    continue
            if len(all_libraries) == 0:
                csv_used_libraries_writer.writerow([app_name, ""])
                csv_used_classes_writer.writerow([app_name, ""])
            # Record used libraries in the apps:
            for i in all_libraries:
                csv_used_libraries_writer.writerow([app_name, i])

            # Record used classes in the apps:
            for i in all_class_identifiers:
                csv_used_classes_writer.writerow([app_name, i])

            # Record the summary of the app:
            csv_project_summary_writer.writerow(
                [app_name, len(all_libraries), len(all_class_identifiers)])

            print('Completed for ' + app_name)

        # give error if app folder is missing:
        elif android_x == 'AndroidX':
            print('ERROR: directory of ' + android_x + ' is missing!')

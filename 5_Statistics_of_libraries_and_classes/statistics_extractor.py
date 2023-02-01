import csv

# existing csv locations:
csv_used_libraries_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\\wip-jetpack-code\\4_Identify_Used_Libraries\\used_libraries.csv'
csv_used_classes_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\\wip-jetpack-code\\4_Identify_Used_Libraries\\used_classes.csv'
csv_library_statistics_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\wip-jetpack-code\\5_Statistics_of_libraries_and_classes\\library_statistics.csv'
csv_class_statistics_location = 'C:\\Users\\dogan\\Desktop\\tru_repo\wip-jetpack-code\\5_Statistics_of_libraries_and_classes\\class_statistics.csv'

# opens the csv files:
with open(csv_used_libraries_location, 'r') as csv_used_libraries, \
        open(csv_used_classes_location, 'r') as csv_used_classes, \
        open(csv_library_statistics_location, 'w', newline='') as csv_library_statistics, \
        open(csv_class_statistics_location, 'w', newline='') as csv_class_statistics:

    # creates a reader or a writer for each csv file:
    csv_used_libraries_reader = csv.reader(csv_used_libraries)
    csv_used_classes_reader = csv.reader(csv_used_classes)
    csv_library_statistics_writer = csv.writer(
        csv_library_statistics, delimiter=',')
    csv_class_statistics_writer = csv.writer(
        csv_class_statistics, delimiter=',')

    # creates a list that will contain all libraries:
    all_libraries = []

    # adds all unique libraries into the list (all_libraries):
    for line in csv_used_libraries_reader:
        if line[1] not in all_libraries and line[1]:
            all_libraries.append(line[1])
        else:
            continue

    # for each element (library) in the list (all_libraries):
    for library in all_libraries:

        # Sets counter to 0:
        library_used_count = 0

        # Resets the file seeker:
        csv_used_libraries.seek(0)

        # for each line in the csv file:
        for line in csv_used_libraries_reader:

            # if second cell (library cell) from csv file matches with the library name from the all_libraries list:
            if line[1] == library:

                library_used_count += 1

        # record the total count:
        csv_library_statistics_writer.writerow([library, library_used_count])

    print('library statistics has been created')

    # creates a list that will contain all classes:
    all_clases = []

    # adds all unique classes into the list (all_classes):
    for line in csv_used_classes_reader:
        if line[1] not in all_clases and line[1]:
            all_clases.append(line[1])
        else:
            continue

    # for each element (class) in the list (all_clases):
    for class_ in all_clases:

        # Sets counter to 0:
        class_used_count = 0

        # Resets the file seeker:
        csv_used_classes.seek(0)

        # for each line in the csv file:
        for line in csv_used_classes_reader:

            # if second cell (class cell) from csv file matches with the library name from the all_clases list
            if line[1] == class_:
                class_used_count += 1

        # record the total count:
        csv_class_statistics_writer.writerow([class_, class_used_count])

    print('Class statistics has been created')

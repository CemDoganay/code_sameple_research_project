from git import Repo
import csv

# file locations:
csv_read_location = 'C:\\Users\\dogan\\Desktop\\python\\Success_Packages_Repositories_WithoutHeader.csv'
csv_write_location = 'C:\\Users\\dogan\\Desktop\\python\\cloned_repos.csv'
repo_save_location = 'C:\\Users\dogan\Desktop\\f-droid_cloned_repos\\'

# opens the csv file:
with open(csv_read_location, 'r') as csv_file:

    # creates a reader for the csv file:
    csv_reader = csv.reader(csv_file)

    # opens the csv file:
    with open(csv_write_location, 'w', newline='') as new_file:

        # creates a writer for the csv file:
        csv_writer = csv.writer(new_file, delimiter=',')

        # counts the total apps
        line_count = sum(1 for row in csv_file)
        csv_file.seek(0)

        count_total = 0
        count_fail = 0
        count_succes = 0

        # for every line in the csv file:
        for line in csv_reader:

            # amount of repos will be downloaded:
            if count_total >= line_count:
                break

            else:
                # saves the repo url:
                repo_url = line[1]

                # saves the package name:
                repo_package_name = line[0]

                # saves the repo directory:
                repo_dir = repo_save_location + repo_package_name

                print("\nWorking on repository number " + str((count_total + 1)) +
                      ". Package name: " + repo_package_name, end="")

            # try cloning:
            try:
                Repo.clone_from(repo_url, repo_dir)

            # report and record if failed:
            except:
                count_fail += 1
                print(" Status: fail")
                line.append("Fail")

            # report and record if succeed:
            else:
                count_succes += 1
                print(" Status: success")
                line.append("Success")

            # record to the csv file:
            csv_writer.writerow(line)
            count_total += 1

print("Total success: " + str(count_succes) + " Total fail: " + str(count_fail))

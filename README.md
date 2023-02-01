This project contains code for the Jetpack project.

## 1) Git the list of F-Droid apps

Input: FDroid website 

Script: Different scripts to get the repos URL and the package names.

Output: 

 - The F-Droid website lists 3,432 apps. The file “Fdroid_App_Categories” has the statistics about the number of apps in each category. The file “FDroid_Package_Names” has the apps URL and their package names. Not that there are some apps that belong to multiple categories that is the reason for having 3984 apps in the “Fdroid_App_Categories” sheet. 

  - Then, we try to see the F-Droid webpage for each apps. So, the file “Success_Packages_Repositories_WithoutHeader” has the apps that I could parse their URLs (3,404 apps). 
 


## 2) Download the FDroid apps

Input:  CSV file “Success_Packages_Repositories_WithoutHeader" with 3,404 apps + GitHub website and desired save location.

Script: 
- First install python library 
- Run the repo_downloader.py
- Install GitPython: https://gitpython.readthedocs.io/en/stable/intro.html

Output: 
  - CSV file "cloned_repos" with cloning status of each app. In total we could clone *"X"* apps.


## 3) Identify Projects with Jetpack apps

Input: 
  - The actual source code of x apps stored in the folder
  - CSV file "cloned_repos"
  - Repo location

Script:
  - Run get_list_of_androidx_apps.py

Output:
  - CSV file "get_list_of_androidx_apps" with if app has "androidX" or "not androidX" or "gradle.properties not found"

## 4) Identify the used libraries in each project 

Input:
  - The actual source code of x apps stored in the folder
  - CSV file "get_list_of_androidx_apps".
  - Repo location

Script:
  - Run androidx_extractor.py

Output:
  - project_summary.csv with total classes and libraries used in an app
  - used_classes.csv with used androidx libraries in an app
  - used_libraries.csv with used androidx libraries in an app

## 5) Statistics of libraries and classes

Input:
  - CSV files "used_classes.csv" and "used_libraries.csv".

Script:
  - Run statistics_extractor.py

Output:
  - class_statistics.csv  with amount usage of classes
  - library_statistics.csv with amount usage of libraries

## 6) Play Store Availability & Play Store availability with android x

Input:
  - CSV files "get_list_of_androidx_apps".

Script:
  - Run Play_Store_Availability_Checker.py OR
  - Play_Store_Availability_Checker_with_androidx.py(useful for step 7)

Output:
  - google_play_existance.csv with app's play store availability information OR
  - google_play_existance_with_androidx.csv with app's play store availability information and if the app is android x.

## 7) App analysis

Input: 
  - CSV file "google_play_existance_with_androidx.csv"

Script:
  - Run app_analysis.py

Output:
  - CSV file "app_analysis.csv" with if app's package name, if android x, if exist in google play, amount of downloads, rating, category






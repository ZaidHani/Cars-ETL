# this file contains the code to setup the data for this project
import requests
import kaggle

# setting up the main cars dataset
# kaggle.api.authenticate()
# kaggle.api.dataset_download_files(dataset='ananaymital/us-used-cars-dataset', path='./data', unzip=True)

# setting up the colors dataset
csv_content = requests.get('https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv').content
csv_file = open('data/colors.csv','wb')
csv_file.write(csv_content)
csv_file.close()

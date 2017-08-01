import pandas
import xlrd
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from operator import itemgetter # to sort the list of dicts


book = xlrd.open_workbook("Swiss Food Database.xlsx")

sheet = book.sheet_by_index(0)

total_rows = sheet.nrows
total_cols = sheet.ncols

table = list()
record = list()


for x in range(total_rows):
    for y in range(total_cols):
        record.append(sheet.cell(x,y).value)
    table.append(record)
    record = []
    x += 1


upnames = list()

for i in table:
    upnames.append(i[1])

lownames = [element.lower() for element in upnames]
    
#print(lownames)




simulated_database = {'Banana': 'foodvalues', 'apple' : 'foodvalues', 'pizza' : 'foodValues'}

test_url = 'http://lebensmittel-warenkunde.de/assets/images/bananen.jpg'
#test_url = 'http://images.eatsmarter.de/sites/default/files/styles/576x432/public/images/cholesterinsenker-341x256.jpg'
#test_url = "http://www.cicis.com/media/1243/pizza_adven_zestypepperoni.png"
#test_url = "https://www.quia.com/files/quia/users/carladefaveri/Pausenbrot/Birne"
#test_url = "https://www.kochschule.de/sites/default/files/images/kochwissen/457/grapefruit.jpg"


visual_recognition = VisualRecognitionV3('2016-05-20', api_key='156f02f7a2afd0e4c1c50197db1f66a6e1fd6229')


# threshold gibt nur Werte, die grösser sind als diese Zahl
url_result = visual_recognition.classify(images_url=test_url, threshold=0.6)
# score_results is a list of dicts
score_results = url_result["images"][0]["classifiers"][0]["classes"]
sorted_score_results = sorted(score_results, key = itemgetter('score'), reverse=True)

#print("the result")
print(json.dumps(sorted_score_results, indent = 4))

#print("test of the result")
print(json.dumps(sorted_score_results[0], indent = 4))

# prints foodname
#print(sorted_score_results[0]['class'])

search = sorted_score_results[1]['class']
#print(search)


#print(next((item for item in sorted_score_results if item["class"] == "banana")))



myVal = next((item for item in sorted_score_results if item["class"] in str(lownames)), None)

if myVal is None:
    print("type of myVal is None")
else:
    search = myVal['class']
    print(search)



def searcher(tab, x):
    
    for i in tab:
        h = 3
        if i[1].lower() == x.lower():
            print("ID:", int(i[0]), "\n" "Name:", i[1], "\n" "Category:", i[2], "\n" "\n" "Nutrition facts per 100g:", "\n" "Kcal:", i[3], "\n" "Protein:", i[4], "\n" "Fat:", i[5], "\n" "Carbohydrate:", i[5],)
            break
            

searcher(table, search)

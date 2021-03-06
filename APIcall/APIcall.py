import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from operator import itemgetter # to sort the list of dicts


simulated_database = {'Banana': 'foodvalues', 'apple' : 'foodvalues', 'pizza' : 'foodValues'}

#test_url = 'http://lebensmittel-warenkunde.de/assets/images/bananen.jpg'
test_url = 'http://images.eatsmarter.de/sites/default/files/styles/576x432/public/images/cholesterinsenker-341x256.jpg'
#test_url = "http://www.cicis.com/media/1243/pizza_adven_zestypepperoni.png"


visual_recognition = VisualRecognitionV3('2016-05-20', api_key='156f02f7a2afd0e4c1c50197db1f66a6e1fd6229')


# threshold gibt nur Werte, die grösser sind als diese Zahl
url_result = visual_recognition.classify(images_url=test_url, threshold=0.6)
# score_results is a list of dicts
score_results = url_result["images"][0]["classifiers"][0]["classes"]
sorted_score_results = sorted(score_results, key = itemgetter('score'), reverse=True)

print("the result")
print(json.dumps(sorted_score_results, indent = 4))

print("test of the result")
print(json.dumps(sorted_score_results[0], indent = 4))

# prints foodname
print(sorted_score_results[0]['class'])

search = sorted_score_results[1]['class']
print(search)


print(next((item for item in sorted_score_results if item["class"] == "ban"), None))



myVal = next((item for item in sorted_score_results if item["class"] == "baana"), None)



if myVal is None:
    print("type of myVal is None")
else:
    print(myVal['class'])


          
"""
names = [{'name':'Tom', 'age': 10}, {'name': 'Mark', 'age': 5}, {'name': 'Pam', 'age': 7}]
resultlist = [d    for d in names     if d.get('name', '') == 'Pam']
first_result = resultlist[0]
"""

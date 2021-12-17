import random

from flask import jsonify, request
from flask_cors import cross_origin
from app import app
from app.algorithm.ml import ml
from app.info import features, questions, answers, questionWithComplete

@app.route('/api/questions/', methods = ['POST'])
@cross_origin()
def getQuestions():
    availableFeatures = features[:]
    characterMatch = None

    if 'alreadyFeatures' in request.json:
        availableFeatures = set(availableFeatures) - set(request.json['alreadyFeatures'])
        characterMatch = ml(request.json['alreadyFeatures'], request.json['params'], request.json['answers'])
        characterMatch = characterMatch.to_dict()

        #print("#######",availableFeatures)
        #exit

        #featuresThatCharacterIsTrue = []

        
        #print("$$$$$$$$",characterMatch)
        #exit()

        characterMatchId = 0
        for id in characterMatch['name']:
            characterMatchId = id
            #print("^^^^^^^^^",characterMatchId)
            #exit()

        print("--------------------------------")
        #print(characterMatch)
        print(characterMatch['name'][characterMatchId])
        print("--------------------------------")

        #for i in range(len(availableFeatures)):
            #print(i)
            #exit()
            #availableFeature = availableFeatures[i]
           #if(characterMatch[availableFeature][characterMatchId]):
                #featuresThatCharacterIsTrue.append(availableFeature)
                #print("*****************", featuresThatCharacterIsTrue)
                #exit()

        #if(len(featuresThatCharacterIsTrue)):
          # availableFeatures = featuresThatCharacterIsTrue
          # print("@@@@@@@@@@@@", availableFeatures)
                #exit()


        characterMatch = {
          "name": characterMatch['name'][characterMatchId],
          "image": characterMatch['image'][characterMatchId],
        }
        print("@@@@@@@@@@@@", characterMatch['image'])
    else:
        availableFeatures = set(availableFeatures) - set(questionWithComplete)

    availableFeatures = list(availableFeatures)

    if(not len(availableFeatures)): 
       return jsonify(
        characterMatch = characterMatch
    )

    feature = random.choice(availableFeatures)
    param = feature
    question = questions[feature]


    if feature in questionWithComplete:
        question += characterMatch[feature] + '?'
        param = 'هل_' + characterMatch[feature]



    return jsonify(
      feature = feature,
      param = param,
      question = question,
      answers = answers[feature],
      characterMatch = characterMatch
    )
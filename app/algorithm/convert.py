import pandas
import datetime

now = datetime.datetime.now()

pandas.options.mode.chained_assignment = None

data = pandas.read_json('all.json')
#print(data)
#data = data.drop(columns = ['stableRelease'])

#data = data.assign(isOld=0, isNew=0, isPopular=0)

#for i in range(len(data)):
    #differenceInYears = now.year - data['firstAppeared'][i]

    #data['isOld'][i] = 1 if differenceInYears >= 30 else 0
    ##data['isNew'][i] = 1 if differenceInYears < 20 else 0
    #data['isPopular'][i] = 1 if data['tiobeIndex'][i] <= 20 else 0

#data = data.drop(columns = ['tiobeIndex', 'firstAppeared', 'stableReleaseYear'])

data.to_csv(r'../../all.csv')

#data.to_csv(r'C:/Users/VIP\Desktop/New folder (2)/programming-language-akinator-masternew/all.csv')
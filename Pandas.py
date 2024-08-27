import pandas as pd
import numpy as np
import matplotlib
#------Basic Dataframes -------#
df = pd.read_csv("London_weather.csv") # or use df = pd.dataframe(dictionary you have created)
print(df)
print(df.shape) # df.head(2:5) df.tail(4)
print(df.columns)
print(df.sunshine) # or print("df[sunshine]")
print(df[['sunshine','pressure']])
print(df['max_temp'].max())
print(df.describe())
print(df[df.max_temp>=35])
print(df[['date','max_temp']][df.max_temp == df.max_temp.max()])
print(df.set_index('date',inplace = True))
print(df)
print(df.loc[20201227])
print(df.reset_index(inplace=True))
print(df)
df = pd.read_csv("london_weather.csv", skiprows = 1) #it removes first row    index = false removes index
df = pd.read_csv("london_weather.csv", skiprows = None,) #names[x,y,z]) it assigns new headers.
df = pd.read_csv("london_weather.csv", na_values = ["not available","n.a"])
df = pd.read_csv("london_weather.csv", na_values = {
                                                    'eps' : ["not available","n.a"],
                                                    'revenue' : ["not available", "n.a", "-1"]
                                                                                             })
df.to_csv ("new csv", columns=["sunshine","pressure"], header=False)

new_df = df.fillna("Del")
print(new_df)
new_df = df.fillna({ 
  "snow_depth": "Good"
})
print(new_df)
new_df = df.fillna(method ="ffill", limit = 1 )
print(new_df)
new_df= df.interpolate()
print(new_df)
new_df = df.dropna(how = "all") # or thresh = 1 removes rows which dont have at least one value
print(new_df)
print(df)
new_df = df.replace(-4.1,np.nan)
print(new_df)
new_df = df.replace({
                      "global_radiation": 52.0,
                      "max_temp": 2.3
}, np.nan)
print(new_df)
df = pd.DataFrame({ "students": ['priya', 'tulasi','meghana','robert','jason'],
                    "marks": [45,67,98,76,33]
})
print(df)
print('\n')
df = df.replace([45,67,98,76,33],[50,90,66,69,61])
print(df)

g = df.groupby('students')
print(g)

for students, students_df in g:
    print(students)
    print(students_df)

g = g.get_group('priya')
print(g)

india_weather = pd.DataFrame({
                             'cities': ['hyderabad','bangaliore','chennai','coaimbatore'],
                             'temprature': [30,26,29,26],
                             'humidity': [78,69,80,80]
})

britain_weather = pd.DataFrame({
                                'cities': ['glassgow','cardiff','manchester','birmingham'],
                                'temprature':[18,20,10,15],
                                'humidity' : [70,78,80,79]
})
a = pd.concat([india_weather,britain_weather], keys = ['india','britain'] )  # axis = 1 appends data frame as coloum
print(a)

temp_df = pd.DataFrame({
                       'cities':['birmingham','new york','melbourne'],
                       'temprature': [18,25,16]
}, index=[1,2,3])

windspeed_df = pd.DataFrame({
                            'cities':['birmingham','new york','melbourne'],
                           'wind speed':[10,12,9]
},index=[1,3,2])
a = pd.concat([temp_df,windspeed_df], axis =1, )
print(a)
s = pd.Series(['damp','cold','warm'],index =[1,2,3], name= 'event')
b = pd.concat([a,s], axis=1)
print(b)
a = pd.merge(temp_df,windspeed_df,on = 'cities')
a.index=[1,2,3]
print(a)
temp_df = pd.DataFrame({
                       'cities':['birmingham','new york','melbourne'],
                       'temprature': [18,25,16]
}, index=[1,2,3])

windspeed_df = pd.DataFrame({
                            'cities':['birmingham','new york','sydney'],
                           'wind speed':[10,12,9]
},index=[1,3,2])
a = pd.merge(temp_df,windspeed_df,on = 'cities', how = 'right', indicator=True, suffixes=('_left','_right'))
print(a)
weather = pd.DataFrame({
    'dates': ['5/1/19','5/2/19','5/3/19','5/4/19','5/1/19','5/2/19','5/3/19','5/4/19'],
    'cities':['kashmir','kashmir','kashmir','kashmir','ladakh','ladakh','ladakh','ladakh'],
    'temprature':[15,10,10,12,3,4,2,1],
    'humidity' : [70,74,72,69,60,66,62,69]
}, index=[1,2,3,4,5,6,7,8])
print(weather)
a=weather.pivot(index='dates', columns='cities')
print(a)
weather = pd.DataFrame({
    'dates': ['5/1/19','5/1/19','5/2/19','5/2/19','5/1/19','5/1/19','5/2/19','5/2/19'],
    'cities':['kashmir','kashmir','kashmir','kashmir','ladakh','ladakh','ladakh','ladakh'],
    'temprature':[15,10,10,12,3,4,2,1],
    'humidity' : [70,74,72,69,60,66,62,69]
}, index=[1,2,3,4,5,6,7,8])
a = weather.pivot_table(index = 'dates', columns='cities')
print(a)
weather = pd.DataFrame({
    'dates': ['5/1/19','5/2/19','5/3/19','5/4/19','5/1/19','5/2/19','5/3/19','5/4/19'],
    'cities':['kashmir','kashmir','kashmir','kashmir','ladakh','ladakh','ladakh','ladakh'],
    'temprature':[15,10,10,12,3,4,2,1],
    'humidity' : [70,74,72,69,60,66,62,69]
}, index=[1,2,3,4,5,6,7,8])
weather['dates'] = pd.to_datetime(weather['dates'])
a = weather.pivot_table(index= pd.Grouper(freq='ME', key='dates'),columns='cities')
print(a)

data = pd.DataFrame({ 
                     'name':['a','b','c','d'],
                    'nation': ['india','england','france','germany'],
                    'hand': ['r','l','l','r'],
                    'sex':['m','m','f','f'],
                    'age':[23,43,21,12]
}, index=[1,2,3,4])              
#print(data)    
a = pd.crosstab([data.sex, data.nation ],data.hand,margins = True)
#print(a)
b = pd.crosstab([data.sex],[data.hand], normalize=True)
#print(b)
b = pd.crosstab([data.sex],[data.hand], values=data.age, aggfunc=np.average)
print(b)
df = pd.read_csv('stock data.csv')
print(type(df.head(3)))
print(df.index)
print(df.get('Date'))
print(df['Volume'])
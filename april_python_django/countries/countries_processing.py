from json import *
with open("countries.json",encoding="utf-8") as f:
    data=load(f)
print(len(data))
print(data[0])
#print capital of china
capital=[country.get("capital") for country in data if country["name"]=="China"]
print(capital)
#Population of china
pop=[population.get("population") for population in data if population["name"]=="China"]
print(pop)
#Currency of ukraine
currency=[country.get("currencies")[0]["name"] for country in data if country["name"]=="Ukraine"]
print(currency.pop())#.pop to remove the list
#languages of India
language=[country.get("languages") for country in data if country["name"]=="India"].pop()
lang=[lan["name"] for lan in language if lan["name"]!="A"]
print(lang)
#borders of ukraine
border=[country.get("borders") for country in data if country["name"].lower()=="ukraine"].pop()
print(border)
alpha3cod=[country["name"]for country in data if country["alpha3Code"]in border]
print(alpha3cod)

#highest populated country
high_pop=[country.get("population") for country in data if country["population"]!=0]
high_pop_data=(max(high_pop))
high_pop=[country.get("name") for country in data if country["population"]==high_pop_data]
print(high_pop)

#countries with language English

eng_languages= [country["name"] for country in data for lan in country["languages"] if lan["name"].lower()=="english"]
print(eng_languages)
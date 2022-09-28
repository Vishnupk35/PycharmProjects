# Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal
city=input("Please enter the city name:")
if(city=="Delhi")or(city=="delhi"):
    print("Monument of Delhi is Red fort")
elif(city=="Agra")or(city=="agra"):
    print("Monument of Agra is Taj Mahal")
elif(city=="Jaipur")or(city=="jaipur"):
    print("Monument of Jaipur is Jal Mahal")
else:
    print("Selected city is invalid")

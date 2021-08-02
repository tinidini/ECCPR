import sys

MAX=999999

print("Ora la care ajungeti la cinema: ")
hour=input()
hour=hour.split(':')
my_hour=int(hour[0])+int(hour[1])
print("\nNr de oferte disponibile: ")
n=int(input())
i=0
movies=[]
noOfMovies=0
print("\nFilmele din oferta cinematografului: (ora, pret, nume)")
while i<n:
    print("\nVarianta "+ str(i+1))
    movie=input()    #film="ora pret nume"
    movie=movie.split() #film=['ora', 'pret', 'nume']
    #hour.clear()
    hour=movie[0]
    hour=hour.split(':')
    movie_hour=int(hour[0])+int(hour[1])
    if movie_hour>my_hour:
        noOfMovies+=1
        movie[0]=movie_hour
        movies.append(movie)
    else: print("-----Ai ajuns prea tarziu pentru a viziona acest film!-----")
    i+=1

if noOfMovies==0:
    sys.exit("\n\n§§§§§§ Ai venit degeaba §§§§§§")
        

i=0
hours=[]

while i<noOfMovies:
    hours.append(movies[i][0])
    i+=1
MinH=min(hours)
movie_of_choice='none'
pret=MAX
i=0
while i<noOfMovies:
    if int(movies[i][0])==int(MinH) and int(movies[i][1])<int(pret):
        pret=movies[i][1]
        movie_of_choice=movies[i][2]
    #else: print(filmales)
    i+=1
    
print("\nCea mai buna varianta ar fi ", movie_of_choice, "\n")
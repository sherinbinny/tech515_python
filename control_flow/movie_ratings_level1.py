# ----------------------------
# Movie Ratings Level 1
# ----------------------------

# Change the beginning so that it asks the user for the movie rating. Make sure you list the acceptable options on the screen.
# If the user enters an invalid option, continually prompt them until again they enter a valid option

valid_ratings = ["universal", "pg", "12", "12a", "15", "18"]

print("Choose a movie rating from the following options:")
print("universal, pg, 12, 12a, 15, 18")

while True:
    film_rating = input("Enter a movie rating: ").lower()
    if film_rating in valid_ratings:
        break
    else:
        print("Invalid rating. Please choose from: universal, pg, 12, 12a, 15, 18")

if film_rating == "universal":
    print("all age groups can watch this film")
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
elif film_rating == "12" or film_rating == "12a":
    print(
        "Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

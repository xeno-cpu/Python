def get_movie_details():

    movies = {}
    count = 1
    
    while True:  
        print(f"\n--- Movie {count} ---")
        
        title = input("Enter movie title: ")
        director = input("Enter director name: ")
        release_year = input("Enter release year: ")
        rating = input("Enter rating (0-10): ")
        
        movies[title] = {
            "director": director,
            "release_year": release_year,
            "rating": rating
        }
        

        another = input("\nDo you want to add another movie? (yes/no): ").lower()
        
        if another != "yes" and another != "y":
            break  
        
        count += 1
    
    return movies


def display_movies(movies):
    

    print("\n" + "="*70)
    print("MOVIE DETAILS".center(70))
    print("="*70)
    
    index = 1
    for title, details in movies.items():
        print(f"\nMovie {index}:")
        print(f"  Title:        {title}")
        print(f"  Director:     {details['director']}")
        print(f"  Release Year: {details['release_year']}")
        print(f"  Rating:       {details['rating']}/10")
        print("-" * 70)
        index += 1
    
    print("="*70 + "\n")



if __name__ == "__main__":
    print("MOVIE INFORMATION SYSTEM")
    print("=" * 70)

    movie_dictionary = get_movie_details()

    display_movies(movie_dictionary)

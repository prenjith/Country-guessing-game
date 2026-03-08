import random

# Dictionary of countries and their corresponding descriptions
country_data = {
    "Argentina": "This country is known for its tango, delicious beef, and beautiful landscapes.",
    "Australia": "This country is famous for its unique wildlife, such as kangaroos and koalas.",
    "Brazil": "This country is home to the Amazon rainforest and the samba dance.",
    "Canada": "This country is known for its stunning landscapes, maple syrup, and ice hockey.",
    "China": "This country is the most populous in the world and is famous for the Great Wall and Chinese cuisine.",
    "Egypt": "This country is renowned for its ancient pyramids and the Nile River.",
    "France": "This country is known for its art, culture, cuisine, and the Eiffel Tower.",
    "Germany": "This country is famous for its engineering, beer, and the Autobahn.",
    "India": "This country is diverse, with a rich history, spicy cuisine, and the Taj Mahal.",
    "Italy": "This country is renowned for its delicious food, historical landmarks, and art.",
    "Japan": "This country is known for its advanced technology, sushi, and cherry blossoms.",
    "Mexico": "This country is famous for its vibrant culture, mariachi music, and tasty tacos.",
    "Russia": "This country spans across Europe and Asia, known for its vast landscapes and the Kremlin.",
    "South Africa": "This country is known for its wildlife safaris, diverse cultures, and beautiful beaches.",
    "Spain": "This country is famous for its flamenco dance, sunny beaches, and delicious paella.",
    "United Kingdom": "This country includes England, Scotland, Wales, and Northern Ireland, with iconic landmarks like Big Ben and the Tower of London.",
    "United States": "This country is diverse, with famous cities like New York and Los Angeles, and landmarks such as the Statue of Liberty."
}

def play_country_guessing_game():
    print("Welcome to the Country Guessing Game!")
    print("I have chosen a random country, and you have to guess which one it is.")
    
    # Randomly select a country from the dictionary
    selected_country = random.choice(list(country_data.keys()))
    country_description = country_data[selected_country]
    
    attempts = 3
    while attempts > 0:
        print("\nYou have", attempts, "attempts left.")
        print("Here's a hint: ", country_description)
        guess = input("Enter your guess: ").strip().capitalize()
        
        if guess == selected_country:
            print("Congratulations! You guessed it right. The country is", selected_country)
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect guess. Try again.")
            else:
                print("Sorry, you've run out of attempts. The correct country was", selected_country)

if __name__ == "__main__":
    play_country_guessing_game()




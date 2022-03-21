# My Crazy Date
# randomly select a date from a contact list, pick a random outfit
# and random restaurant, watch a random movie, and go to a random place after dinner
# see how crazy my date turns out to be!

import random
date_contact_list_m = ['Frodo', 'Sheldon Cooper', 'Gandalf', 'Thor', 'Capitan America', 'Iron Man', 'Dumbledore',
                     'Voldemort', 'John Wick', 'Spider Man', 'Hulk', 'Aqua man', 'Professor Xavier',
                      'Doctor Strange', 'Wolverine', 'Bumblebee', 'Deadpool', 'Fantastic Four',
                     'Tom and Jerry', 'Mickey Mouse', 'Goofy', 'Shrek', 'Genie of Aladdin', 'Donald Duck']

friend_list_f = ['Elsa from Frozen', 'Anna from Frozen', 'Wonder woman', 'Black widow', 'Black Phoenix', 'Cat woman',
                 'Storm', 'Katniss Everdeen', 'Harley Quinn', 'little mermaid', 'Cinderella', 'Mulan', 'Angelina Jolie',
                 "snow white's step mother", 'Princess Leia', 'the Dragon mom', 'Mary Poppins']

output_top = ['an orange shirt with purple tie', 'pink glittering overall with a purple wig',
              'a leopard print poncho']

shoes = ['shinny green sneakers', 'dutch orange wooden shoes', 'toddler-size pink crocs',
         'big red glittering dancing shoes', 'golden glittering Jimmy Choo 4-inch high heels',

         ]
movies = ['Suicide Squad', 'Frozen', 'The Lord of the Rings', 'Harry Potter the Half Blood Prince', 'X Men',
          'Avenger', 'John Wick', 'Transformers', 'Fantastic Four', 'Wolverine', 'Tom and Jerry',
          'Mama Mia', 'Fast and Furious', 'Despicable Me', 'My Fair Lady', 'Percy Jackson', 'God Father 1']

restaurants_type = ['Chinese DimSim', 'Indian Curry', 'French Cuisine', 'Japanese Omakase', 'Italian Pasta',
                   'Canadian Poutine', 'English Fish and Chips', 'Korean BBQ', 'Spanish Seafood',
                    'Turkish Lamb Kebab', 'Thailand Yum Goong']

restaurant_locations = ['Shanghai, China', 'Kyoto, Japan', 'Toronto, Canada', 'San Fransisco, USA', 'New York City, USA',
                        'Paris, France', 'Lucerne, Switzerland', 'Madrid, Spain', 'London, UK',
                        'Frankfurt, Germany', 'Boston, USA', 'Los Angeles, USA', 'Montreal, Canada',
                        'Milan, Italy', 'Sicily, Italy', 'Manchester, UK', 'Bangkok, Thailand',
                        'Tokyo, Japan', 'Venice, Italy', 'Las Vegas, USA']

when = ['Halloween night', 'Valentine Day', "April Fool's Day", 'St. Patrick Day',
        'Thanksgiving day', 'The Day I got a bad flu', 'Prom night', 'First day of work', 'Last weekend',
        'One hot summer day', 'thunderstorm night', 'The day of biggest snow storm',
        'On my Commencement day', 'On my birthday']

pets = ['Lucy the Lion', 'Kody the Cockapoo', 'Penny the Python', 'Leonard the Leopard', 'Tony the Tiger',
        'Ella the elephant', 'Wayne the Whale']

transportation = ['by bike', 'by subway', 'by plane', 'walking', 'by scooter', 'by car', 'by Uber']

after_dinner_places = ['Wonderland', 'Pet store', 'Hogwarts', 'Laundry shop', 'Nail Salon', 'Hollywood',
                       'Bellagio', 'Apple store', 'parking lot', 'Cineplex', 'Night Club', 'Ikea']

events = ['solved a puzzle', "couldn't find his car", 'bought some Disney toys', 'went swimming in the bath tub',
          'watched hockey', 'had an argument with the bartender', 'dropped his ice cream',
          "bought an iPad", 'threw up in my drinks', 'adopted a kitty']

print(random.choice(when) + ', ' + random.choice(date_contact_list_m) + ' and I had a double date with ' +
      random.choice(friend_list_f) + ' and her partner ' + random.choice(date_contact_list_m) + '.' + '\n'
      'My date showed up wearing ' + random.choice(output_top) + ' and ' + random.choice(shoes) + ' and his pet ' +
      random.choice(pets) + '.' + '\n'
      'He suggested watching movies ' + random.choice(movies) + ', then have dinner for ' + random.choice(restaurants_type)
       + ' at ' + random.choice(restaurant_locations) + ' ' + random.choice(transportation) + '.' + '\n'
      'After dinner, he ' + random.choice(events) + ' at ' + random.choice(after_dinner_places) + '.' + '\n'
      'It was a CRAZY date :-) !')

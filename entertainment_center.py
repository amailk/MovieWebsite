import fresh_tomatoes
import media
harrypotter= media.Movie("Harry Potter",
                         "Daniel Radcliffe, Emma Watson and Rupert Grint",
                         "A story about the boy who lived",
                         "http://www.tribute.ca/harrypotter/images/HP1/harry_potter_and_the_sorcerers_stone_poster5.jpg",
                         "https://www.youtube.com/watch?v=VyHV0BRtdxo")
spy = media.Movie("Spy","Jude Law, Raad Rawi and Melissa McCarthy",
                "A desk-bound CIA analyst volunteers to go undercover to infiltrate the world of a deadly arms dealer, and prevent diabolical global disaster.",
                "http://ia.media-imdb.com/images/M/MV5BNjI5OTQ0MDQxM15BMl5BanBnXkFtZTgwMzcwNjMyNTE@._V1_SX214_AL_.jpg",
                "https://www.youtube.com/watch?v=ltijEmlyqlg")
blackmass = media.Movie("Blackmass",
                        "Johnny Depp, Joel Edgerton and Benedict Cumberbatch",
                      "The true story of Whitey Bulger, the brother of a state senator and the most infamous violent criminal in the history of South Boston, who became an FBI informant to take down a Mafia family invading his turf.",
                      "http://ia.media-imdb.com/images/M/MV5BNzg0ODI3NDQxNF5BMl5BanBnXkFtZTgwMzgzNDA0NjE@._V1_SX214_AL_.jpg",
                      "https://www.youtube.com/watch?v=CE3e3hGF2jc")
colonia = media.Movie("Colonia",
                      "Emma Watson, Daniel Bruhl and Michael Nyqvist",
                      "A young woman's desperate search for her abducted boyfriend that draws her into the infamous Colonia Dignidad, a sect nobody ever escaped from.",
                      "http://www.fashiongonerogue.com/wp-content/uploads/2015/09/Colonia-Emma-Watson-Movie-Poster.jpg",
                      "https://www.youtube.com/watch?v=SiVAGDTmlpY")
amelie= media.Movie("Amelie",
                    "Audrey Tautou, Mathieu Kassovitz and Rufus",
                    "Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
                    "http://ia.media-imdb.com/images/M/MV5BMTYzNjkxMTczOF5BMl5BanBnXkFtZTgwODg5NDc2MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=2UT5xaAfxWU")
danishgirl = media.Movie("Danish Girl",
                         "Eddie Redmayne, Alicia Vikander and Amber Heard",
                         "The remarkable love story inspired by the lives of artists Lili Elbe and Gerda Wegener. Lili and Gerda's marriage and work evolve as they navigate Lili's groundbreaking journey as a transgender pioneer.",
                         "http://ia.media-imdb.com/images/M/MV5BMjA0NjA4NjE2Nl5BMl5BanBnXkFtZTgwNzIxNTY2NjE@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=d88APYIGkjk")
pitchperfect = media.Movie("Pitch Perfect",
                           "Anna Kendrick, Rebel Wilson and Skylar Astin",
                           "Beca, a freshman at Barden University, is cajoled into joining The Bellas, her school's all-girls singing group. Injecting some much needed energy into their repertoire, The Bellas take on their male rivals in a campus competition.",
                           "http://ia.media-imdb.com/images/M/MV5BMTcyMTMzNzE5N15BMl5BanBnXkFtZTcwNzg5NjM5Nw@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=F03N-ApQdmw")
shestheman = media.Movie("She's the Man",
                         "Amanda Bynes, Channing Tatum and Laura Ramsey",
                         "When her brother decides to ditch for a couple weeks in London, Viola heads over to his elite boarding school, disguises herself as him, and proceeds to fall for one of her soccer teammates. Little does she realize she's not the only one with romantic troubles, as she, as he, gets in the middle of a series of intermingled love affairs.",
                         "http://ia.media-imdb.com/images/M/MV5BMjEyMzAzMDk1Ml5BMl5BanBnXkFtZTcwNjg0OTEzMQ@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=_UiPki2uxM8")
fastfive = media.Movie("Fast Five",
                       "Paul Walker, Vin Diesel and Jordana Brewster",
                       "Dominic Toretto and his crew of street racers plan a massive heist to buy their freedom while in the sights of a powerful Brazilian drug lord and a dangerous federal agent.",
                       "http://ia.media-imdb.com/images/M/MV5BMTUxNTk5MTE0OF5BMl5BanBnXkFtZTcwMjA2NzY3NA@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=mw2AqdB5EVA")
movies = [harrypotter, spy, blackmass, colonia, amelie, danishgirl, pitchperfect, shestheman, fastfive]

fresh_tomatoes.open_movies_page(movies)


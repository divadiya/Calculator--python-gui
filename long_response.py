import random

R_EATING = "I dont like eating anything because I am a bot obivously!"

def unknown():
  response = ['could you please re-phrase that?',
             ".....",
             "sounds about right",
             "what does that mean?"][random.randrange(4)]
  return response
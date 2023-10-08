# Osasere Ikponmwosa
# for exceeding requirements i added a get function to get an adjective and add to my get_prepositional_phrase function 
import random


def main():
    # these are the two arguments that will be used in the program
    quantity = random.choice([1,2])
    tense = random.choice(['present', 'past', 'future'])
    i = 0    
   
    while i < 6:
        # this is to make it print 6 sentences
        i += 1
        sentence = make_sentence(quantity=quantity, tense=tense)
        print(sentence)
    
def make_sentence(quantity, tense):
    if quantity == 1:
        sentence = f'{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(quantity=1, tense=tense)} {get_prepositional_phrase(1)}.'
    elif quantity == 2:
        sentence = f'{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(quantity=1, tense=tense)} {get_prepositional_phrase(2)}.'
    return sentence
        
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word


def get_noun(quantity):
    words_singular = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    words_plural = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    if quantity == 1:
        word = words_singular
    else:
        word = words_plural
    word = random.choice(word)
    return word


def get_verb(quantity, tense):
    past_tense = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    singular_present_tense = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    plural_present_tense = [ "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_tense = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    if tense == 'past':
        word = past_tense
    elif tense == 'present':
        if quantity == 1:
            word = singular_present_tense
        else:
            word = plural_present_tense
    elif tense == 'future':
        word = future_tense
    word = random.choice(word)
    return word        


def get_preposition():
    preposition = [ "about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    word = random.choice(preposition)
    return word
def get_adjective():
    adjectives = random.choice(["enthusiastic","serene","jubilant","mysterious","radiant","lively","tranquil","playful","resilient","majestic",
    "vibrant","whimsical","eloquent","tenacious","harmonious"])
    return adjectives


def get_prepositional_phrase(quantity):
    if quantity == 1:
        prepositional_phrase = f'{get_preposition()} {get_determiner(1)} {get_adjective()} {get_noun(1)}'
    else:
        prepositional_phrase = f'{get_preposition()} {get_determiner(2)} {get_adjective()} {get_noun(2)}'
    return prepositional_phrase


main()
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['full_text']
    word_list = full_text.replace('-', ' ').replace('—', ' ').split()
    word_dictionary = {}

    for word in word_list:
        word = word.lower().strip(",.")
        if word in word_dictionary:
            #Increase
            word_dictionary[word] += 1
        else:
            #Add to the dictionary
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)


    #for word in word_list:

    return render(request, 'count.html', {'full_text': full_text, 'count':len(word_list), 'sorted_words': sorted_words})

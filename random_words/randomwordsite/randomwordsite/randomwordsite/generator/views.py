from django.http import HttpResponse
from faker import Faker

def generate_word(request):
    fake = Faker()
    word = fake.word()
    return HttpResponse(request, 'generator/word.html', {'word': word})

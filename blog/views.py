from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_all_post(request):

    messages = [
        {
            'id': 1,
            'title': "Article 1",
            'desc': "Ceci est notre article 1"
        },
        {
            'id': 2,
            'title': "Article 2",
            'desc': "Ceci est notre article 2"
        },
        {
            'id': 3,
            'title': "Article 3",
            'desc': "Ceci est notre article 3"
        }
    ]

    context = {
        'messages': messages,
    }

    return render(request, 'blog/get_all_post.html', context)

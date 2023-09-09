from django.shortcuts import render
<<<<<<< HEAD
from datetime import datetime

articles = [
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

=======

articles = [
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

>>>>>>> 61f7d0af4c23b0027b96892cbecf7e58753c088d

def get_all_post(request):

    context = {
        'messages': articles,
    }

    return render(request, 'blog/get_all_post.html', context)


def post(request, pk):

    article = articles[pk - 1]

    context = {
        'article': article,
<<<<<<< HEAD
        'ma_date': datetime.now(),
        'testVar': "Test Valeur"
=======
>>>>>>> 61f7d0af4c23b0027b96892cbecf7e58753c088d
    }

    return render(request, 'blog/post.html', context)

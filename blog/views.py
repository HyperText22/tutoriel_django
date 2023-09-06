from django.shortcuts import render

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


def get_all_post(request):

    context = {
        'messages': articles,
    }

    return render(request, 'blog/get_all_post.html', context)


def post(request, pk):

    article = articles[pk - 1]

    context = {
        'article': article,
    }

    return render(request, 'blog/post.html', context)

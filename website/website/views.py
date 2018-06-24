from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from website import TextSummarization, ArticleClassifier

@csrf_exempt
def summarization(request):
    if request.method == 'POST':
        urlAddress = request.POST.get('urlAddress')
        numberOfSentence = request.POST.get('numberOfSentence')
        articleContent=request.POST.get('articleContent')
        articleTitle=request.POST.get('articleTitle')

        if articleContent and articleTitle:
            summarization = TextSummarization.summarize(articleContent, numberOfSentence)
            title=articleTitle;

        elif urlAddress:
            text = TextSummarization.getTextFromWebsite(urlAddress)
            summarization = TextSummarization.summarize(text, numberOfSentence)
            title=TextSummarization.getTitle(urlAddress)

        context = {
            'summarization': summarization,
            'title':title,
        }

        template = loader.get_template('showSummarization.html')

        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('shortenArticle.html')
        return HttpResponse(template.render())


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def classifier(request):
    template = loader.get_template('articleClassifier.html')
    return HttpResponse(template.render())


@csrf_exempt
def classification_result(request):
    articleContent = request.POST.get('articleContent')

    label = ArticleClassifier.classify(articleContent)

    # adding the values in a context variable
    context = {
        'label': label
    }

    template = loader.get_template('classificationResult.html')
    return HttpResponse(template.render(context, request))

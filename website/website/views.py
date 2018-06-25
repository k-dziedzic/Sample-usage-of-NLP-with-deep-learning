from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from website import TextSummarization, ArticleClassifier
from website import SpamFilter


@csrf_exempt
def summarization(request):
    url_address = request.POST.get('urlAddress')
    number_of_sentence = request.POST.get('numberOfSentence')
    article_content = request.POST.get('articleContent')
    article_title = request.POST.get('articleTitle')

    if article_content and article_title:
        summarization = TextSummarization.summarize(article_content, number_of_sentence)
        title = article_title

    elif url_address:
        text = TextSummarization.get_text_from_website(urlAddress)
        summarization = TextSummarization.summarize(text, numberOfSentence)
        title = TextSummarization.get_title(urlAddress)

    context = {
        'summarization': summarization,
        'title': title,
    }

    template = loader.get_template('showSummarization.html')

    return HttpResponse(template.render(context, request))


def shorten_article(request):
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
    article_content = request.POST.get('articleContent')
    article_title = request.POST.get('articleTitle')
    label = ArticleClassifier.classify(article_content)

    context = {
        'label': label,
        'title': article_title,
        'content': article_content
    }

    template = loader.get_template('classificationResult.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
def spam_classifier(request):
    template = loader.get_template('spamClassifier.html')
    return HttpResponse(template.render())


@csrf_exempt
def classification_spam(request):
    mail_content = request.POST.get('mailContent')

    is_spam = SpamFilter.spam_filter(mail_content)

    # adding the values in a context variable
    context = {
        'isSpam': is_spam,
        'mailContent': mail_content,
    }

    template = loader.get_template('classificationSpam.html')
    return HttpResponse(template.render(context, request))

# importing required packages
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# disabling csrf (cross site request forgery)
from website import TextSummarization


@csrf_exempt
def index(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        address = request.POST.get('address')
        numberOfSentence = request.POST.get('numberOfSentence')

        TextSummarization.articleURL = address
        TextSummarization.numberOfSentence = numberOfSentence
        text = TextSummarization.getTextWaPo(address)
        summarization = TextSummarization.summarize(text, numberOfSentence)
        title=TextSummarization.getTitle(address)

        # adding the values in a context variable
        context = {
            'summarization': summarization,
            'title':title,
        }

        # getting our showdata template
        template = loader.get_template('showSummarization.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:

        # if post request is not true
        # returing the form template
        template = loader.get_template('shortenArticle.html')
        return HttpResponse(template.render())


def mainPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

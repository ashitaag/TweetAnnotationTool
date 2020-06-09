from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Tweet
from django.views.decorators.csrf import csrf_exempt
import csv
import json


# Create your views here.

def index(request):
    tweets = Tweet.objects.all()
    annotated_tweets = Tweet.objects.filter(is_annotated=True).count()
    colors = {
        True: 'light-green',
        False: 'light-red'
    }
    context = {
        "tweets": tweets,
        "count": len(tweets),
        "annotated_tweets_count": annotated_tweets,
        'colors' : colors,
    }

    return render(request, template_name='homepage.html', context=context)


@csrf_exempt
def upload_tweets_from_csv(request):

    csv_file = request.FILES["csv_file"]
    with open('current_json_file.json', 'wb+') as destination:
        for chunk in csv_file.chunks():
            destination.write(chunk)

    with open('current_json_file.json') as json_file:
        data = json.load(json_file)

    for tweet in data['all_tweets']:
        try:
            current_object = Tweet.objects.get(text = tweet)
        except:
            tweet_object = Tweet(text=tweet)
            tweet_object.save()


    return redirect("/")


def test(request):
    tweets = Tweet.objects.all()
    for tweet in tweets:
        tweet.key_term_injured = ""
        tweet.key_term_killed = ""
        tweet.key_term_num_vehicles = ""
        tweet.save()

    return_obj = {
        "msg": len(tweets)
    }

    return JsonResponse(return_obj)


def annotate(request):
    try:
        tweet = Tweet.objects.filter(is_annotated=False)[:1].get()
    except:
        tweet = None

    context = {"tweet": tweet}
    return render(request, 'annotate.html', context= context)


@csrf_exempt
def annotate_tweet(request):
    tweet = Tweet.objects.get(id = request.POST.get('id'))

    tweet.key_term_injured = str(request.POST.get('key_term_injured'))
    tweet.key_term_killed = str(request.POST.get('key_term_killed'))
    tweet.key_term_num_vehicles = str(request.POST.get('key_term_num_vehicles'))
    tweet.num_killed = int(request.POST.get('num_killed'))
    tweet.num_injured = int(request.POST.get('num_injured'))
    tweet.num_vehicles = int(request.POST.get('num_vehicles'))
    tweet.informative = bool(request.POST.get('informative'))
    tweet.accident_related = bool(request.POST.get('accident_related'))
    tweet.severity = bool(request.POST.get('severity'))
    tweet.is_annotated = True

    tweet.save()

    return redirect('/annotate')

def export_json(request):
    tweets_list = []
    all_tweets = Tweet.objects.filter(is_annotated=True)
    for tweet in all_tweets:
        obj = {
            'text': tweet.text,
            'annotation': {
                'key_term_injured': tweet.key_term_injured,
                'key_term_killed': tweet.key_term_killed,
                'accident_related': tweet.accident_related,
                'informative': tweet.informative,
                'num_killed': tweet.num_killed,
                'num_vehicles': tweet.num_vehicles,
                'key_term_num_vehicles': tweet.key_term_num_vehicles,
                'num_injured': tweet.num_injured,
                'severity': tweet.severity
            },
            'id': tweet.id,
            'is_annotated': tweet.is_annotated
        }

        tweets_list.append(obj)

    with open('Tool/static/annotated_tweets_data.json', 'w') as fp:
        json.dump(tweets_list, fp)

    return redirect('/static/annotated_tweets_data.json')



def delete_tweet(request,tweet_id):
    tweet = Tweet.objects.get(id = tweet_id)
    tweet.delete()
    return redirect('/')


def delete_tweet_and_annotate(request,tweet_id):
    tweet = Tweet.objects.get(id = tweet_id)
    tweet.delete()
    return redirect('/annotate')


from django.shortcuts import render

import requests
import json
# Create your views here.
def home(request):

    if request.method == "POST":
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        api_request = requests.get(api_url, headers={'X-Api-Key': '4bbYf2+UgdQXQza7XobhDA==3np7e0Szyi625T7P'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "error!"
            print(e)
        return render(request, 'home.html', {'api' :api})

    else:
        return render(request, 'home.html', {'query': 'INVALID try again'})

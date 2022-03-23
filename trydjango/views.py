"""
-> The main purpose of the views.py is render the HTML pages.

"""

from django.http import HttpResponse
import random


def home_view (request):
  """
  - Take in a request (Django sends the request)
  - Return the response as a HTML pages (We get the response)
  """
  name = "sam"
  number = random.randint(1,1000)    # Some API call to rest in python 

  # Django Templets really gives the better HTML representation
  HTML_STRING = f"""
  <h1> Hello {name}, You balance is: {number} /- !!! </h1>
  """
  return HttpResponse(HTML_STRING)
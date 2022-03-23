"""
-> The main purpose of the views.py is render the HTML pages.

"""

from django.http import HttpResponse



def home_view (request):
  """
  - Take in a request (Django sends the request)
  - Return the response as a HTML pages (We get the response)
  """
  HTML_STRING = """
  <h1> Hello World !!! </h1>
  """
  return HttpResponse(HTML_STRING)
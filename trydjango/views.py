"""
-> The main purpose of the views.py is render the HTML pages.

"""

from django.http import HttpResponse
import random

from articles.models import Article


def home_view (request):
  """
  - Take in a request (Django sends the request)
  - Return the response as a HTML pages (We get the response)
  - Need to get the data from the article app
  - article_name and article_content from database
  """
  name = "sam"
  number = random.randint(1,1000)    # Some API call to rest in python 

  article_obj = Article.objects.get(id = 2)
  
  HTML_STRING = f"""
  <h1> Hello {name}, You balance is: {number} /- !!! </h1>
  <h1> {article_obj.title} (id: {article_obj.id}) </h1>
  <p>{article_obj.content}</p>
  """
  return HttpResponse(HTML_STRING)


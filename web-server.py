from flask import Flask, request, render_template, redirect
import string
import random

# Create an empty dictionary where we store the stories of one page
def create_page_dict(sent):
  page_dict = {
    "top_sent": None,
    "left_sent": None,
    "center_sent": sent,
    "right_sent": None,
    "bottom_sent": None
  }
  return page_dict

# Generate a random id for each page; Returns random alphanumeric characters (EX: page_id_2A5DST)
def get_page_id():
    page_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return ("page_id_" + page_id)

# Returns a the sentence 
def get_user_input(page_id):
  if(page_id != None):
    return dictionary_of_pages[page_id]["center_sent"]

# Create a new id and dictionary for a new page and link them to the dictionary of pages
def add_page(current_page_id, position, sent):
  page_id = get_page_id()
  new_page_dict = create_page_dict(sent)
  dictionary_of_pages[page_id] = new_page_dict
  dictionary_of_pages[current_page_id][position] = page_id

# Create empty dictionary and add the index page sentence to it
dictionary_of_pages = {}
dictionary_of_pages["index"] = create_page_dict("Once upon a time there was a big bad wolf.")

# Create an instance of Flask and set up POST and GET methods for the web app
app = Flask(__name__)

@app.route('/new_page', methods=['POST'])
def new_page():
    current_page_id = request.form["current_page_id"]
    position = request.form["position"]
    new_sent = request.form["new_sent"]
    add_page(current_page_id, position, new_sent)
    return redirect("/" + current_page_id)

@app.route('/<page_id>')
def display_page(page_id):
    current_story_dict = dictionary_of_pages.get(page_id)

    top_sent = get_user_input(current_story_dict["top_sent"])
    left_sent = get_user_input(current_story_dict["left_sent"])
    right_sent = get_user_input(current_story_dict["right_sent"])
    bottom_sent = get_user_input(current_story_dict["bottom_sent"])

    return render_template(
      "webpage.html", 
      center_sent=current_story_dict["center_sent"],
      top_page_id=current_story_dict["top_sent"],
      left_page_id=current_story_dict["left_sent"],
      right_page_id=current_story_dict["right_sent"],
      bottom_page_id=current_story_dict["bottom_sent"],
      top_sent=top_sent,
      left_sent=left_sent,
      right_sent=right_sent,
      bottom_sent=bottom_sent,
      current_page_id=page_id)

if __name__ == '__main__':
    app.run(port=4000, debug=True)

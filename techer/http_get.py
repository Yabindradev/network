#
# http_get.py
#
import requests

html = requests.get(
    "https://shikoku-u.manaba.jp/ct/course_325292_topics_5_tflat")
# print(html.text)


# Open a file in write mode
with open('manaba.html', 'w') as f:
  # Write the contents of the response to the file
  f.write(html.text)

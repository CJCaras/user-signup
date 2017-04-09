#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Create an account</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Account Registration</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

#Sign-in page form data
form = """

<form action="/success" method="post">
    <label>Create a user name you would like to use with our site:
    <br />
    <input type="text" name="user_name" value="%(user_name)s">
    </label>
    <br />
    <label>Enter your e-mail address for verification:
    <br />
    <input type="text" name="user_email" value="%(user_email)s">
    </label>
    <br />
    <label>Password (5-10 characters without spaces):
    <br />
    <input type="password" name="user_password" value="">
    </label>
    <br />
    <label>Re-type Password:
    <br />
    <input type="password" name="password2" value="">
    </label>
    <br />
    <input type="submit">
</form>
"""



#error_name = "User name should be 3-10 characters and have no spaces or symbols"
#error_password = "User passwords should match"
#error_email = "User did not enter a valid e-mail address. Try again."

#def escape_html(s):
#    return cgi.escape(s, quote = True)


class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
    """

    def get(self):

        error = self.request.get("error")
        if error:
            error_esc = cgi.escape(error, quote=True)
            error_message = '<p class="error">' + error_esc + '</p>'
        else:
            error_message = ''


        self.response.write(page_header + form + error_message + page_footer)

class SuccessfulRegistration(webapp2.RequestHandler):
    def post(self):

        user_name = self.request.get('user_name')
        user_email = self.request.get('user_email')
        user_password = self.request.get('user_password')

        #if len(user_name) < 3 or len(user_name) > 10:
            #self.redirect("/?error=Your login name must be 3-10 characters in length. Please choose another.)
        # TODO 2
        # if the user typed nothing at all, redirect and yell at them
        if user_name == '' or user_email == '' or user_password == '':
            self.redirect("/?error=One or more fields were left blank. Please complete the form before submission.")

        self.response.write(page_header + "Congratulation on a successful submission!" + page_footer)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/success', SuccessfulRegistration)
], debug=True)

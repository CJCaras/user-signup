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
form_opener = """<table>
<form action="/success" method="post">"""

name = ''
user_email = ''

name_form = """<tr>
    <td>Create a user name you would like to use with our site:
    </td>
    <td>
    <input type="text" name="user_name" value="{0}">
    </td>
    <td class="error">
    """.format(name)

form_end = """</td></tr>"""

email_form = """
<tr><td>Enter a valid e-mail address (optional):</td>
<td>
<input type="text" name="user_email" value="{0}">
</td>
<td class="error">
""".format(user_email)

password_form = """<tr>
<td>Password (5-10 characters without spaces):</td>
<td><input type="password" name="user_password" value="">
</td>
</tr>
<td class="error">
"""

password2_form = """
<tr><td>Re-type Password:</td>
<td><input type="password" name="password2" value="">
</td>
<td class="error">
"""

form_closer = """<tr><td></td>
<td><input type="submit"></td>
</form></table>
"""

def valid_password(password):
    USER_PW = re.compile(r"^.{3,20}$")
    return USER_PW.match(password)

def valid_email(email):
    USER_EM = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return USER_EM.match(email)

def escape_html(s):
    return cgi.escape(s, quote = True)

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
    """

    def get(self):

        error = self.request.get("error")
        if error:
            error_message = '<p class="error">' + error + '</p>'
        else:
            error_message = ''

        name_error = self.request.get("name_error")
        if name_error:
            name_error_message = '<p class="error">' + name_error + '</p>'
        else:
            name_error_message = ''

        pass_error = self.request.get("pass_error")
        if pass_error:
            #name = self.request.get(cgi.escape('user_name'))
            pass_error_message = '<p class="error">' + pass_error + '</p>'
        else:
            pass_error_message = ''

        self.response.write(page_header + form_opener + name_form +
        name_error_message + form_end + email_form + error_message + form_end + password_form + form_end + password2_form + pass_error_message + form_end + form_closer + page_footer)

class SuccessfulRegistration(webapp2.RequestHandler):

    def post(self):

        user_name = self.request.get(cgi.escape('user_name'))
        user_email = self.request.get('user_email')
        user_password = self.request.get('user_password')
        password2 = self.request.get('password2')

        #name = user_name

        if len(user_name) < 3 or len(user_name) > 20:
            self.redirect("/?name_error=User name must be 3-20 characters in length. Please choose another.")

        if valid_email(user_email) != '' and user_email != '':
            self.redirect("/?error=Please enter a valid e-mail address.")

        #if valid_username(user_name) != '':
            #self.redirect("/?name_error=User name should not contain spaces or special characters.")

        if user_name == '' or user_password == '':
            self.redirect("/?error=One or more fields were left blank. Please complete the form before submission.")

        if user_password != password2:
            self.redirect("/?pass_error=Your passwords do not match. Try again.")

        self.response.write(page_header + "Welcome " + user_name + "! Thank you for registering. Stay tuned for updates!" + page_footer)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/success', SuccessfulRegistration)
], debug=True)

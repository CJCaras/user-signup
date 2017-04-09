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


form = """

<form method="post" action="/success">
    <label>User name (3-10 characters, no spaces or symbols):
    <input type="text" name="user_name" value="%(user_name)s">
    </label>

    <label>User E-mail:
    <input type="text" name="user_email" value="%(user_email)s">
    </label>

    <label>Password (3-10 characters without spaces):
    <input type="password" name="user_password" value="">
    </label>

    <label>Re-type Password:
    <input type="password" name="password2" value="">
    </label>
    <div style="color:red">%(error)s</div>
    <input type="submit">

</form>
"""

error = "User name should not contain any spaces"
"User passwords should match"
"User did not enter a valid e-mail address. Try again."

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.write(form % {"error": error})


    def get(self):
        user_name = self.request.get('user_name')
        user_email = self.request.get('user_email')
        user_password = self.request.get('user_password') if password == password2


        self.response.write(form)

    def post(self):
        self.response.write


class TestHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        self.response.write("Congratulation on a successful submission!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/success', TestHandler)
], debug=True)

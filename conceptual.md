### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Both of the languages are high-level languages, pyhton is very versatile and commonly used for web development, AI, scientific computing where as JS is used alot for client-side web development, enabling interactive features and user interfaces. Regarding formatting, python uses indentation to define blocks of code, and variables can be declaired without var, let or const. Whereas JS uses {} to define their blocks of code. On tope of these differences it is also important to note python comes with a sturdy library where JS has fewer built in fucntionalities.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  I could either use 'get()' method with a default value, so it will return a key if the value is not found, another way you could do it could be a 'try'-'except' block to catch the KeyError when trying to find something that may not be present.

- What is a unit test? 
A unit test tests if an individual component works, like a function of some sort. It promotes modular code and typically tests one function/method.

- What is an integration test?
An integration test tests if all of your parts ( functions/methods) work properly together.

- What is the role of web application framework, like Flask? 
The purpose of flask is to provide a structured and efficient way to build web apps. Flask allows for routing and URL mapping, HTTP request handling, template rendering, session management, error handling, security features and many forms of testing and debugging.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  As a parameter, it is easier to read for the user/ all is in english for the most part. it is very simple and you can access thewm directly in the view functionn using route(). It is alos important to note that using a parameter based search there is a more limited to the ammount of data you can pass through them. Where as in using a query parameter, they allow passinng more data and they are not restricted by the URL path length. Query parameters are ideal for optional filters or search criteria as well as many of the forms of data being base through can be coded in a way that interface users cannot break them down to english.

- How do you collect data from a URL placeholder parameter using Flask?
You can collect data from a URL placeholder parameter using the route decorator, allowing you to define patterns with placeholders. The placeholders are enclosed within < and > and are passed as arguements to the view function when matchiong URL is requested.

- How do you collect data from the query string using Flask?
To collect data from the query string using flask you can use the request objects which helps handle incoming requested data. You can use request.args whichh provides a dictionary-like object containing the query parameters.

- How do you collect data from the body of the request using Flask?
To collect data from the body you can use request methods such as POST, PUT or patch while using the request objects.

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data that a server sends to a users web browser and is then stored on the users device, it is not stored on the server side. It is important to note that cookies are stored in a session based storage. Cookies are many times used for user authentication, security, personalization and many other uses.

- What is the session object in Flask?
A session object is a built-in feature in flask that allows you to store and send data across multiple requests from the same user. They are commonly used to impliment features like user authentication, and what we just spoke about above. The data stored inn the session remains on the server side, and only the session ID is sent back and forth between the server ans the client in the form of a cookie.

- What does Flask's `jsonify()` do?
jsonify() is a helper function that creates a JSON response from a Python dictionary or list. It is primarily useful when you want to return JSON data as a response from your Flask routes.
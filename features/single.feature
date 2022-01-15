Feature: Google\'s Search Functionality
    Scenario: can find search results
        When visit url "https://bstackdemo.com/"
        When field with name "q" is given "BrowserStack"
      
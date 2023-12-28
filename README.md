The python function will accept a url as string (by default: "https://httpbin.org")

It will fetch all the links it that url and store it in the list.

Then the random function will fetch n random links from that list and store them in a new list

After that it will return a dictionary in which the key will be the status code of each url and values will be a list of urls that gives that status code.

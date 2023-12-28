import requests
import re
import random

def answer(input_url: str = 'https://httpbin.org'):
    get_object = requests.get(input_url)
    total_urls = re.findall('["\'](https?://\S+["\'])', get_object.text)
    if not total_urls:
        return "No links present"
    no_of_random_urls = random.randint(len(total_urls)//2,len(total_urls))

    random_url_list = random.choices(total_urls, k=no_of_random_urls)
    ans = {}
    for j in random_url_list:
        i = j[:-1]
        current_object = requests.get(i)
        current_status_code = current_object.status_code
        if current_status_code in ans:
            ans[current_status_code].append(i)
        else:
            ans[current_status_code] = [i]
    return ans

if __name__ == "__main__":
    print(answer())

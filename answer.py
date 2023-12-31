import requests
import re
import random
def answer(n: int=1, url: str='https://httpbin.org'):
    get_object = requests.get('https://httpbin.org')
    total_urls = re.findall('["\'](https?://\S+)["\']', get_object.text)
    if not total_urls:
        return "No url found"
    current_urls = total_urls.copy()
    for _ in range(n):
        iterator_urls = []
        for i in current_urls:
            temp_object = requests.get(i)
            temp_urls = re.findall('["\'](https?://\S+)["\']', temp_object.text)
            iterator_urls = iterator_urls + temp_urls
        total_urls += iterator_urls
    
    number_of_random_urls = random.randint(len(total_urls)//2, len(total_urls))

    random_urls = random.choices(total_urls, k=number_of_random_urls)

    ans = {}
    for i in random_urls:
        try:
            r = requests.get(i)
        except Exception as e:
            print("Unable to establish new connection")
        if r.status_code in ans:
            ans[r.status_code].append(i)
        else:
            ans[r.status_code] = [i]
    
    return ans

if __name__ == "__main__":
    print(answer())

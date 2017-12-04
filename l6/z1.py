import urllib.request
import html.parser
import time
import threading

print("Usage: site max_recursion_level query")

input_string = input().split()
start_site = input_string[0]
max_level = int(input_string[1])
query = input_string[2]

sites = []
answer = []
site_dict = {}
site_set = {start_site}
site_list = [(start_site, 0)]
recursion_level = 0
temp_dicts = []


def eat_one_website(site, index):
    try:
        site_code = str(urllib.request.urlopen(site).read())
    except:
        pass
    else:
        parser = Parser(site, index)
        parser.feed(site_code)


class Parser(html.parser.HTMLParser):
    def __init__(self, parent_site, index):
        self.index = index
        self.parent_site = parent_site
        html.parser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (atr, val) in attrs:
                if atr == 'href':
                    if val and len(val) == 0:
                        continue
                    if len(val) >= 4 and val[0:2] == r"\'" and val[-2:] == r"\'":
                        val = val[2:-2]
                    if len(val) > 0 and val[-1] == '/':
                        val = val[:len(val) - 1]
                    if len(val) == 0:
                        continue
                    if len(val) < 7 or len(val) >= 7 and val[:7] != 'http://':
                        if len(val) > 0 and val[0] == '/':
                            val = val[1:len(val)]
                        if len(val) == 0:
                            continue
                        val = self.parent_site + '/' + val
                    if len(val) >= 4 and val[:4] == 'http' and val not in site_set:
                        lock = threading.Lock()
                        lock.acquire()

                        site_list.append((val, recursion_level + 1))
                        site_set.add(val)

                        lock.release()

    def handle_data(self, data):
        global temp_dicts

        for word in data.split():
            lock = threading.Lock()
            lock.acquire()

            if word in temp_dicts[self.index].keys():
                temp_dicts[self.index][word] += 1
            else:
                temp_dicts[self.index][word] = 1

            lock.release()


def eat_websites():
    global temp_dicts, sites, site_dict, recursion_level
    threads = []
    threads_quantity = 0
    to_join = 0
    index = 0

    lock = threading.Lock()

    lock.acquire()
    for (site, level) in site_list:
        lock.release()
        index += 1

        if level >= max_level:
            lock.acquire()
            break
        if level > recursion_level:
            for i in range(threads_quantity):
                threads[i].join()
            for i in range(threads_quantity):
                site_dict[sites[i]] = (temp_dicts[i])

            sites = []
            temp_dicts = []
            threads_quantity = 0
            threads = []

            recursion_level = level

        print(site)
        temp_dicts.append({})
        sites.append(site)
        threads.append(threading.Thread(
            target=eat_one_website, args=(site, threads_quantity)))
        threads_quantity += 1
        threads[-1].start()

        lock.acquire()
        while index == len(site_list) and to_join < threads_quantity:
            lock.release()
            threads[to_join].join()
            to_join += 1
            lock.acquire()

        lock.release()
        lock.acquire()

    lock.release()

    for i in range(threads_quantity):
        threads[i].join()
    for i in range(threads_quantity):
        site_dict[sites[i]] = (temp_dicts[i])


def find_and_sort_answer():
    global site_list, site_dict, answer
    for site, level in site_list:
        if site in site_dict and query in site_dict[site]:
            answer.append((-site_dict[site][query], site))
    answer.sort()


def return_answer():
    global answer
    ind = 1
    for num, site in answer:
        print ("{}: {} ({} occurences)".format(ind, site, -num))
        ind += 1
        if ind > 10:
            break


eat_websites()
find_and_sort_answer()
return_answer()

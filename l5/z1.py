import urllib.request
import html.parser

print("Usage: site max_recursion_level query")

input_string = input().split()
start_site = input_string[0]
max_level = int(input_string[1])
query = input_string[2]

site_dict = {}
site_set = {start_site}
site_list = [(start_site, 0)]
recursion_level = 0
parent_site = ""


class Parser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (atr, val) in attrs:
                if atr == 'href':
                    if len(val) == 0:
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
                        val = parent_site + '/' + val
                    if len(val) >= 4 and val[:4] == 'http' and val not in site_set:
                        site_list.append((val, recursion_level + 1))
                        site_set.add(val)

    def handle_data(self, data):
        for word in data.split():
            if word in temp_dict.keys():
                temp_dict[word] += 1
            else:
                temp_dict[word] = 1


parser = Parser()
for (site, level) in site_list:
    if level >= max_level:
        break
    if level > recursion_level:
        recursion_level = level
    try:
        site_code = str(urllib.request.urlopen(site).read())
    except:
        pass
    else:
        parent_site = site
        global temp_dict
        temp_dict = {}
        print(site)
        parser.feed(site_code)
        site_dict[site] = temp_dict

answer = []
for site, level in site_list:
    if site in site_dict and query in site_dict[site]:
        answer.append((-site_dict[site][query], site))

answer.sort()
ind = 1
for num, site in answer:
    print ("{}: {} ({} occurences)".format(ind, site, -num))
    ind += 1
    if ind > 10:
        break

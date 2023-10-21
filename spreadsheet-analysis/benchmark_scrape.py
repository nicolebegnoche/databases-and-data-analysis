import requests, re
from bs4 import BeautifulSoup
from csv import DictReader

base_url = "https://www.cpubenchmark.net/cpu.php?cpu="
in_file = "processors_list.csv"
out_file = "benchmarks.txt"
errors = []


def main():
    output = ""

    # create list of dictionaries of processors from csv file
    with open(in_file, 'r') as file:
        processors = list(DictReader(file))
        
    # for each processor...
    for cpu in processors:
        if not cpu: continue

        # query web
        url = cpu['url'] = get_url(cpu)
        request = query_web(url)
        
        # on successful query, get benchmark and clockspeed
        if request:
            soup = BeautifulSoup(request, 'html.parser')
            cpu['speed'] = get_speed(soup)
            cpu['benchmark'] = get_benchmark(soup)

            # note errors
            if not cpu['speed']: error('clockspeed', cpu)
            if not cpu['benchmark']: error('benchmark', cpu)


        # # add to output
        row = ','.join(cpu.values())
        print(row)
        output += row + '\n'

    # save output to file
    with open(out_file, 'w') as file:
        file.write(output)

    # report results
    if len(errors):
        print("\nErrors during process:")
        for x in errors:
            print(x)
    else:
        print("\nProcess finished without errors.")


def get_url(cpu):
    format = lambda x: x.replace(' ','+').lower().strip()
    attributes = [cpu['brand'], cpu['make'], cpu['model']]    
    query = '+'.join([format(x) for x in attributes if x])
    return base_url + query


def query_web(url):
    try:
        r = requests.get(url)
        if (r.status_code == 200): return r.content
        else: raise Exception()

    except Exception as e:
        msg = f"{url}\tCode: {r.status_code}\n"
        if str(e): msg += f"Exception: {e}\n"
        errors.append(msg)
        return None


def get_benchmark(soup):
    divs = soup.find("div", class_="right-desc")
    spans = divs.find_all("span")
    benchmark = [x.string.strip() for x in spans if x.string.strip().isnumeric()]
    return benchmark[0] if benchmark else None


def get_speed(soup):
    divs = soup.find('div', class_='left-desc-cpu')
    speed = [x.text for x in divs if "Clockspeed" in x.text]
    if speed:
        pattern = r'(?:speed:\s*)(.+)(\s*GHz)'
        matches = re.search(pattern, speed[0])
        if matches:
            return matches.group(1).strip()
    return None


def error(attribute, cpu):
    msg = f">>> Couldn't get {attribute} for {cpu['brand']} {cpu['make']} {cpu['model']} ({cpu['url']})"
    print(msg)
    errors.append(msg)


if __name__ == "__main__":
    main()
    print('done')
#!usr/bin/python3

try:
    import requests
    import argparse
    import json
except Exception as e:
    print(f'{e}, please install the mentioned module.')

def req (domain):
    crtReq = requests.get(fr"https://crt.sh/?q="+domain+r"&output=json")
    return crtReq.text

def pars(data):
    domainsSet = set()
    Jsoned = json.loads(data)
    for link in Jsoned:
        print(link['name_value'])
        domainsSet.add(link['name_value'])
    return domainsSet

def output(setArray, fileName = "crtScrap-domains"):
    file = open(fileName, 'a')
    for link in setArray :
        file.write(link+"\n")
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage="python3 crtScrap.py <domain name>",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="a scraper to scrap crt.sh domains",
        epilog="""\
        Examples:
            python3 crtScrap.py google.com -o domains-google 
        """
        )
    parser.add_argument('-o', '--output', required=False, help="outputs the results in file")
    parser.add_argument('-d', '--domain', required=False, help='domain you want to quary on')
    
    arg = parser.parse_args()
    if arg.domain:
        parsedArray = pars(req(arg.domain))
        pass
    else:
        parser.print_help()
    if arg.output:
        output(parsedArray,arg.output)








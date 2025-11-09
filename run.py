import requests
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("repo", help="Repository name")
parser.add_argument("-d", "--defaults", action="store_true", help="Use default values (os:linux, arch:amd64)")
parser.add_argument("-n", "--by-name",  action="store_true", help="Order by name instead of date")
parser.add_argument("-p",   metavar="5",            help="Number of pages to be parsed (default:5)", type=int)
parser.add_argument("-fe",  metavar="foo,bar",      help="Exclude repos contains the filter")
parser.add_argument("-fi",  metavar="foo,bar",      help="Show only repos contains the filters")
parser.add_argument("-o",   metavar="linux",        help="Show only given os related versions")
parser.add_argument("-a",   metavar="amd64",        help="Show only given architecture related versions")
args = parser.parse_args()

REPO_NAME       = args.repo if "/" in args.repo else "library/" + args.repo
API_URL         = f"https://registry.hub.docker.com/v2/repositories/{REPO_NAME}/tags/?page="
FILTER_NAMES_EX = args.fe.split(",") if args.fe else None
FILTER_NAMES_IN = args.fi.split(",") if args.fi else None
FILTER_OS       = args.o if args.o else "linux" if args.defaults else None
FILTER_ARCH     = args.a if args.a else "amd64" if args.defaults else None
TOTAL_PAGE      = args.p if args.p else 5
ORDER_BY_NAME   = args.by_name
total_images    = 0
parsed_page     = 0

table = []
for i in range(1, TOTAL_PAGE + 1):
    r = requests.get(API_URL + str(i))
    
    if not r.json().get("results"):
        break

    total_images = r.json().get("count")
    parsed_page  = i
    
    for item in r.json().get("results"):
        
        if FILTER_NAMES_EX and any(k in item.get("name") for k in FILTER_NAMES_EX):
            continue

        if FILTER_NAMES_IN and not any(k in item.get("name") for k in FILTER_NAMES_IN):
            continue

        if FILTER_OS and not any(k["os"] == FILTER_OS for k in item.get("images")):
            continue

        if FILTER_ARCH and not any(k["architecture"] == FILTER_ARCH for k in item.get("images")):
            continue
        
        table.append([
            item.get("last_updated")[:10],
            item.get("name"),
            ",".join({k.get("os") for k in item.get("images")}),
            ",".join({k.get("architecture") for k in item.get("images")}),
        ])
    
if ORDER_BY_NAME:
    table.sort(key=lambda x: x[1], reverse=False)
else:
    table.sort(key=lambda x: x[0], reverse=False)
    
print(tabulate(table, headers=["UPDATE DATE", "NAME", "OS", "ARCH"]))
print(f"""
REPO NAME    : {REPO_NAME}
TOTAL PARSED : {len(table)} images found. (Total : {total_images})
PARSED PAGES : {parsed_page}/{int(total_images / 10) + 1} page parsed
NAME FILTERS : {",".join(FILTER_NAMES_EX) if FILTER_NAMES_EX else None}
OS FILTER    : {FILTER_OS}
ARCH FILTER  : {FILTER_ARCH}""".replace("None", "-"))

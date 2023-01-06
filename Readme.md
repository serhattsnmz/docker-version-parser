# DOCKER VERSION PARSER

This is a python script file which basically list all existing versions of a repository on Docker Hub.

![](https://img.shields.io/static/v1?style=flat-square&label=Licence&message=GPL%20v3&color=blue)
[![](https://img.shields.io/static/v1?style=flat-square&label=Stable%20Version&message=1.0&color=green)](https://github.com/serhattsnmz/rabbitgram/releases)
[![](https://img.shields.io/static/v1?style=flat-square&label=Docker%20Hub&message=Passed&color=green)](https://hub.docker.com/repository/docker/serhattsnmz/rabbitgram)

## Requirements

1. [Python 3.6+](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone this repo,
2. Install required libraries with pip,
3. Run `run.py` file with Python3. 

```bash
$ git clone https://github.com/serhattsnmz/docker-version-parser.git
$ cd docker-version-parser/
$ python3 -m pip install -r requirements.txt
$ python3 run.py nginx
```

## Usage Examples

```
$ python3 run.py nginx

UPDATE DATE    NAME                     OS     ARCH
-------------  -----------------------  -----  --------------------------------------------------
2022-12-21     10.13-slim               linux  386,arm64,amd64,arm
2022-12-21     10.13                    linux  386,arm64,amd64,arm
2022-12-21     10-slim                  linux  386,arm64,amd64,arm
2022-12-21     10                       linux  386,arm64,amd64,arm
...

REPO NAME    : library/debian
TOTAL PARSED : 50 images found. (Total : 1580)
PARSED PAGES : 5/159 page parsed
NAME FILTERS : -
OS FILTER    : -
ARCH FILTER  : -
```

```
$ python3 run.py portainer/portainer-ce

UPDATE DATE    NAME                          OS             ARCH
-------------  ----------------------------  -------------  -----------------------------
2022-11-21     windows1909-amd64             windows        amd64
2022-11-21     linux-s390x                   linux          s390x
2022-11-21     linux-ppc64le                 linux          ppc64le
2022-11-21     alpine                        linux          amd64,arm,arm64
2022-11-21     2.16.2-alpine                 linux          amd64,arm,arm64
2022-11-21     linux-amd64-2.16.2-alpine     linux          amd64
...

REPO NAME    : portainer/portainer-ce
TOTAL PARSED : 50 images found. (Total : 391)
PARSED PAGES : 5/40 page parsed
NAME FILTERS : -
OS FILTER    : -
ARCH FILTER  : -
```

```
$ python3 run.py portainer/portainer-ce -fi 2.16 -fe linux,windows -o linux -a amd64

UPDATE DATE    NAME           OS             ARCH
-------------  -------------  -------------  -----------------------------
2022-10-30     2.16.0-alpine  linux          amd64,arm,arm64
2022-10-30     2.16.0         windows,linux  s390x,arm,ppc64le,amd64,arm64
2022-11-09     2.16.1-alpine  linux          amd64,arm,arm64
2022-11-09     2.16.1         windows,linux  s390x,arm,ppc64le,amd64,arm64
2022-11-21     2.16.2-alpine  linux          amd64,arm,arm64
2022-11-21     2.16.2         windows,linux  s390x,arm,ppc64le,amd64,arm64

REPO NAME    : portainer/portainer-ce
TOTAL PARSED : 6 images found. (Total : 391)
PARSED PAGES : 5/40 page parsed
NAME FILTERS : linux,windows
OS FILTER    : linux
ARCH FILTER  : amd64
```

## Advanced Usage

```
usage: run.py [-h] [-d] [-n] [-p 5] [-fe foo,bar] [-fi foo,bar] [-o linux] [-a amd64] repo

positional arguments:
  repo            Repository name

optional arguments:
  -h, --help      show this help message and exit
  -d, --defaults  Use default values (os:linux, arch:amd64)
  -n, --by-name   Order by name instead of date
  -p 5            Number of pages to be parsed (default:5)
  -fe foo,bar     Exclude repos contains the filter
  -fi foo,bar     Show only repos contains the filters
  -o linux        Show only given os related versions
  -a amd64        Show only given architecture related versions
```
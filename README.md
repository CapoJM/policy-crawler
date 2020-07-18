# Web crawler para el Periódico Oficial del Estado de Jalisco

## Prerequisites

It is necessary to have Scrapy installed in your system. To install it, simply use `pip` as

```
pip install Scrapy
```

## Running the crawler

Having Scrapy installed, you need to fetch the repository in order to run the crawler locally. Once fetched, open the command line interface and go to the outermost POJalisco directory. There use the command

```
scrapy crawl periodico
```



## Personal notes:

Scrapy project is created using

```
scrapy startproject POJalisco
```

This will create all the folders and _backbone_ of the crawler. Then you move to the project crawler and run

```
scrapy genspider periodico periodicooficial.jalisco.gob.mx
```

which creates a spider for the crawler. This can be found in the `spiders` folder. Inside `periodico.py` is the information relevant to the crawler. We modified the `start_urls` parameter to describe which is the first URL the crawler must _crawl_.

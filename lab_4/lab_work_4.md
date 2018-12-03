# Лабораторная работа №4

## Дано

1. Набор заданных английских текстов большого размера.
    Набор таких файлов можно скачать и положить в папку `lab_4`:

    * [5_7.txt](https://www.dropbox.com/s/ch486h1avdjaifg/5_7.txt?dl=1)
    * [15_2.txt](https://www.dropbox.com/s/kkz12uriw6gj6qx/15_2.txt?dl=1)
    * [10547_3.txt](https://www.dropbox.com/s/75yzydzwxgud1j1/10547_3.txt?dl=1)
    * [12230_7.txt](https://www.dropbox.com/s/tzm7iylvkptw1kr/12230_7.txt?dl=1)

Таким образом, повторить структуру:

```bash
|-- 2018-2-level-labs
  |-- lab_4
    |-- 5_7.txt
    |-- 15_2.txt
    |-- 10547_3.txt
    |-- 12230_7.txt
```

Каждый текст - это отдельный текстовый файл.

Если интересно, то весь набор текстов можно скачать 
[по ссылке](http://ai.stanford.edu/~amaas/data/sentiment/).

## Что надо сделать

### Шаг 0.1 Подготовка (проделать вместе с преподавателем на практике)

1. В имеющемся форке репозитория, обновить содержимое до последнего доступного
состояния в родительском репозитории.
2. Изменить файл `main.py`
3. Закоммитить изменения и создать pull request

### Шаг 0.2 Прочитать содержимое документов

Необходимо считать все документы в список из строк. 

> **Внимание**: этот код уже написан в `main.py`. Если у вас больше файлов, убедитесь, что
> все файлы указаны в этом списке.

## Шаг 1. Создание класса расчета TF-IDF

### Шаг 1.1 Объявление полей класса

Создаем класс `TfIdfCalculator`. Внутри него задаем поля `word_frequency`, `word_tfidf`.

### Шаг 1.2 Заполнение класса 


### Шаг ОПА. Расчет TF-IDF

Итак, для каждого слова из каждого документа нужно уметь рассчитать TF-IDF показатель.

А именно, он состоит из двух частей. Первая часть - это TF (term frequency) - обычная частота
слова в рамках заданного документа. Формула рассчета такова:
<img src="https://latex.codecogs.com/gif.latex?tf(t,d)&space;=&space;\frac{n_{t}}{\sum_{k}{n_{k}}}" title="tf(t,d) = \frac{n_{t}}{\sum_{k}{n_{k}}}" />

Здесь <img src="https://latex.codecogs.com/gif.latex?n_{t}" title="n_{t}" />
это количество раз слово <img src="https://latex.codecogs.com/gif.latex?t" title="t" />
встречается в документе <img src="https://latex.codecogs.com/gif.latex?d" title="d" />.

Вторая часть - это IDF (inversed document frequency):
<img src="https://latex.codecogs.com/gif.latex?idf(t,D)&space;=&space;log(\frac{|D|}{|\{d_{i}&space;\epsilon&space;D&space;|&space;t&space;\epsilon&space;d_{i}\}|})" title="idf(t,D) = log(\frac{|D|}{|\{d_{i} \epsilon D | t \epsilon d_{i}\}|})" />

Здесь:


## Ссылки

В данной работе предполагается использовать избранные тексты из

@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
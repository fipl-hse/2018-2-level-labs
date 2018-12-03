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

### Шаг 1. Закодировать все предложения 

Для этого воспользуемся кодом из Лабораторной работы №3. То есть каждый текст превращаем
в двумерный список. Подробнее в лабораторной работе №2.

## Шаг 1. Создание класса расчета TF-IDF

### Шаг 1.1 Объявление полей класса

Создаем класс `TfIdfCalculator`. Внутри него задаем поля `word_frequency`, 
`word_tfidf`, `corpus`.

### Шаг 1.2 Заполнение класса 

### Шаг 1.2 Заполнение класса 

### Шаг ОПА. Расчет TF

Итак, для каждого слова из каждого документа нужно уметь рассчитать TF-IDF показатель.

А именно, он состоит из двух частей. Первая часть - это TF (term frequency) - обычная частота
слова в рамках заданного документа. Формула рассчета такова:
<img src="https://latex.codecogs.com/gif.latex?tf(t,d)&space;=&space;\frac{n_{t}}{\sum_{k}{n_{k}}}" title="tf(t,d) = \frac{n_{t}}{\sum_{k}{n_{k}}}" />

Здесь <img src="https://latex.codecogs.com/gif.latex?n_{t}" title="n_{t}" />
это количество раз слово <img src="https://latex.codecogs.com/gif.latex?t" title="t" />
встречается в документе <img src="https://latex.codecogs.com/gif.latex?d" title="d" />.

**TF** тем больше чем чаще слово встречается в заданном документе и тем меньше чем реже
встречается заданное слово. Получается, мы получаем важность слова в данном тексте.

Внутри класса необходимо реализовать метод `calculate_tf(self)`:

```python
class TfIdfCalculator:
  ...
  def calculate_tf(self):
    pass
```

Данный метод для каждого текста из корпуса, который уже хранится в классе,
рассчитывает значение **TF** для каждого слова в этом документе. В результате, для
одного текста получается словарь, который содержит структуру:

```json
{
  "word1": 0.17,
  "word2": 0.45
}
```

А так как таких текстов у нас 
<img src="https://latex.codecogs.com/gif.latex?|D|" title="|D|" />, то и 
в результате работы функции получается список из 
<img src="https://latex.codecogs.com/gif.latex?|D|" title="|D|" /> элементов.

Каждый элемент списка - словарь с **TF** для каждого слова.

Полученный список метод `calculate_tf(self)` сохраняет в собственное поле 
`self.tf_values`.

### Шаг ОПА. Расчет IDF

Вторая часть - это IDF (inversed document frequency):
<img src="https://latex.codecogs.com/gif.latex?idf(t,D)&space;=&space;log(\frac{|D|}{|\{d_{i}&space;\epsilon&space;D&space;|&space;t&space;\epsilon&space;d_{i}\}|})" title="idf(t,D) = log(\frac{|D|}{|\{d_{i} \epsilon D | t \epsilon d_{i}\}|})" />

**IDF** тем больше чем реже слово встречается в корпусе и тем меньше чем чаще
встречается заданное слово.

Здесь: <img src="https://latex.codecogs.com/gif.latex?|D|" title="|D|" /> - это 
количество документов в корпусе, а 
<img src="https://latex.codecogs.com/gif.latex?|\{d_{i}&space;\epsilon&space;D&space;|&space;t&space;\epsilon&space;d_{i}\}|" title="|\{d_{i} \epsilon D | t \epsilon d_{i}\}|" /> 
- это количество документов, в которых присутствовало слово 
<img src="https://latex.codecogs.com/gif.latex?t" title="t" />.

Внутри класса необходимо реализовать метод `calculate_idf(self)`:

```python
class TfIdfCalculator:
  ...
  def calculate_idf(self):
    pass
```

Данный метод для каждого текста из корпуса, который уже хранится в классе,
рассчитывает значение **IDF** для каждого слова, которое встречается хотя бы в одном
документе. В результате, получается словарь, который содержит структуру:

```json
{
  "word1": 0.33,
  "word2": 0.21
}
```

Ключ - слово, значение - **IDF** для данного слова.

Полученный список метод `calculate_idf(self)` сохраняет в собственное поле 
`self.idf_values`.

### Шаг ОПА. Расчет TF-IDF

Теперь можем расчитать общую метрику **TF-IDF**:
<img src="https://latex.codecogs.com/gif.latex?\operatorname&space;{tf-idf}(t,d,D)=\operatorname&space;{tf}(t,d)\times&space;\operatorname&space;{idf}(t,D)" title="\operatorname {tf-idf}(t,d,D)=\operatorname {tf}(t,d)\times \operatorname {idf}(t,D)" />

Внутри класса необходимо реализовать метод `calculate(self)`:

```python
class TfIdfCalculator:
  ...
  def calculate(self):
    pass
```

Данный метод для каждого текста из корпуса, который уже хранится в классе,
рассчитывает значение **TF-IDF** для каждого слова, которое встречается хотя бы в одном
документе. В результате, получается словарь, который содержит структуру:

```json
{
  "word1": 0.33,
  "word2": 0.21
}
```

Ключ - слово, значение - **TF-IDF** для данного слова.

Полученный список метод `calculate(self)` сохраняет в собственное поле 
`self.tf_idf_values`.

### Шаг ОПА. Получение отчета для данного слова

Теперь, когда были произведены расчеты **TF-IDF** для каждого слова, мы можем начать
анализировать результаты, например, сравнивать значения метрики для нескольких слов.

Для этого, требуется реализовать метод `report_on_word(self, word)`:

```python
class TfIdfCalculator:
  ...
  def report_on_word(self, word):
    pass
```

Данный метод возвращает значение IDF для заданного слова, если оно встречалось в тексте 
и `None` иначе. 

### Шаг ОПА. Сохранение отчета в Excel-приемлемом формате

Требуется сохранить содержимое наших расчетов в `.csv` файл. Особенность такого файла
заключается в том, что все строки - это наборы значений, разделенных запятой.

Например, есть таблица:

| Слово | TF (text a) | TF (text b) | IDF | TF-IDF (text a) | TF-IDF (text b) |
| bag   | 0.142        | 0        | 0.3           | 0.043 | 0 |

Превращается в текстовый файл (**не бинарный**) `.csv`, с содержимым:

```sh
bag,0.142,0,0.3,0.043,0
```

Вам необходимо обеспечить сохранение в такой файл расчетов по заданному корпусу.

Для этого, требуется реализовать метод `dump_report_csv(self)`:

```python
class TfIdfCalculator:
  ...
  def dump_report_csv(self):
    pass
```

Этот метод создает файл `report.csv` в той же директории, что и сам `main.py` для
Лабораторной работы №4. Если расчеты не производились, то создается пустой файл
(без строк).


## Ссылки

В данной работе предполагается использовать избранные тексты из

```json
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
```

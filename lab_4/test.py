from lab_4.main import TfIdfCalculator


clean_texts = [
        ['this', 'is', 'an', 'example', 'of', 'test', 'text', 'it', 'contains', 'two', 'sentences'],
        ['das', 'ist', 'ein', 'testtext', 'es', 'ist', 'auf', 'deutsch', 'geschrieben']
    ]
tf_instance = TfIdfCalculator(clean_texts)
tf_instance.tf_idf_values = [
        {
            'this': 10,
            'that': 9,
            'another': 5
        }
    ]

tf_instance.calculate()

res = tf_instance.report_on('this', 0)
print(res)


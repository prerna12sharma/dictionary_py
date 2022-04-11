d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
dic=dict()
# result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), d.items()))
# print(result)
for x in d.items():
        if x[1][0]>6.0:
            if x[1][1]>70:
                dict(x)
            print(x)


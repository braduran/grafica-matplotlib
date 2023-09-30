import matplotlib.pyplot as plt
import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
	
def choose_continent():
    print('-- Choose a continent --')
    print('1. Africa')
    print('2. Asia')
    print('3. North America')
    print('4. South America')
    print('5. Europe')
    print('6. Oceania')
    
    switch_continent = {
        1: 'Africa',
        2: 'Asia',
        3: 'North America',
        4: 'South America',
        5: 'Europe',
        6: 'Oceania'
    }

    continent = int(input('=> '))
    return switch_continent.get(continent)

def run():
    data = read_csv('./data.csv')
    continent = choose_continent()

    data = list(filter(lambda x: x['Continent'] == continent, data))
    countries = list(map(lambda item: item['Country'], data))
    growth_rate_population = list(map(lambda item: float(item['Growth Rate']), data))

    generate_pie_chart(countries, growth_rate_population)


if __name__ == '__main__':
    run()
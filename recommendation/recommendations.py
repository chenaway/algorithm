#encoding=utf8
# 计算两个人的相似度

from math import sqrt


def sim_distance(prefs, person1, person2):

    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = prefs[person2]

    if len(si) == 0: return 0
    
    p1, p2 = prefs[person1], prefs[person2]

    square = sum([pow(p1[item]-p2[item], 2) for item in si])
    distance = 1/(1+sqrt(square))
    return distance


def data():
    return {
        'Nico': { 'Python': 4.5, 'Ruby': 3.0, 'C++': 3.4, 'Java': 2.5 },
        'Yann': { 'Python': 3.0, 'Ruby': 4.5, 'C++': 3.4, 'Java': 1.5 },
        'Josh': { 'Python': 0.5, 'Ruby': 0.0, 'C++': 1.0, 'Java': 5.0 },
        'Kerstin': { 'Chocolate': 5.0 },
    }


def main():
    prefs = data()
    print sim_distance(prefs,
                 'Nico',
                 'Yann',
                 )
    print sim_distance(prefs,
                 'Josh',
                 'Yann',
                 )
    print sim_distance(prefs,
                 'Nico',
                 'Kerstin'
                 )


if __name__ == '__main__':
    main()

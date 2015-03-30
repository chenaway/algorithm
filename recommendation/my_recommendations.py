#encoding=utf8
# 计算两个人的相似度

from math import sqrt


def sim_distance(prefs, person1, person2):
    
    pref_seq = [(person1[pref], person2[pref]) for pref in prefs]
    square = sum([pow(x-y, 2) for x,y in pref_seq])
    distance = 1/(1+sqrt(square))
    return distance


def data():
    return {
        'Nico': { 'Python': 4.5, 'Ruby': 3.0, 'C++': 3.4, 'Java': 2.5 },
        'Yann': { 'Python': 3.0, 'Ruby': 4.5, 'C++': 3.4, 'Java': 1.5 },
        'Josh': { 'Python': 0.5, 'Ruby': 0.0, 'C++': 1.0, 'Java': 5.0 },
    }


def main():
    persons = data()
    print sim_distance(['Python', 'Ruby', 'Java'],
                 persons['Nico'],
                 persons['Yann'],
                 )
    print sim_distance(['Python', 'Ruby', 'Java'],
                 persons['Nico'],
                 persons['Josh'],
                 )
    print sim_distance(['Python', 'Ruby', 'Java'],
                 persons['Yann'],
                 persons['Josh'],
                 )


if __name__ == '__main__':
    main()

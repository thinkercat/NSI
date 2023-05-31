import csv

def main():

    with open('iris.csv') as f:
        iris = list(csv.DictReader(f,delimiter=','))

    def distance(u:tuple,v:tuple):
        '''
        Renvoie la distance entre les points u(x,y) et v(x',y')
        '''
        x1 = u[0]
        y1 = u[1]

        x2 = v[0]
        y2 = v[1]
        
        return ((x1-x2)**2+(y1-y2)**2)**0.5

    def plus_proches(data,u:tuple,k:int):
        '''
        Renvoie les k points de data les plus proches du point u
        '''

        for valeur in data:

            v = (float(valeur['petal length (cm)']),float(valeur['petal width (cm)']))
            d = distance(u,v)

            valeur['distance'] = d


        def key_sort(t):
            return t['distance']

        sort_data = sorted(data, key=key_sort)
        

        mins = []
        for i in range(k):
            mins.append(sort_data[i])
        return mins

    def i_max(values:list):
        '''
        Renvoie l'indice de la valeur max
        '''
        im = 0
        m = 0
        for i in range(len(values)-1):
            if values[i] > m:
                m = values[i]
                im = i
        return im

    def flower_type(values:list):
        '''
        Renvoie le type de fleur 0,1 ou 2
        '''
        c = [0,0,0]

        for v in values:
            c[int(v['target'])] += 1
        return i_max(c)

            
    def f_calc(flower_values:tuple,k)->int:
        p_proches = plus_proches(iris,flower_values,k)
        f_type = flower_type(p_proches)
        return f_type




    print(f_calc((1,5),5))
if __name__ == '__main__':
    main()

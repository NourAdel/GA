#include <iostream>
#include <cstdlib>
#include <ctime>
#include <time.h>
#include <utility>
#include <process.h>
using namespace std;
static int MAXW,sz,pn,pairsn;


class Gen
{
public:

    int weight;
    double  value;
    Gen ()
    {
        weight=-1;
        value=-1;
    }
    void setGen(int x, int y)
    {
        this->weight=x;
        this->value=y;
    }
};
static Gen* original;


class chromosome
{
public:
    int* bits;
    double fit;
    int w;
    void setch (int x)
    {


        bits=new int[x];
        fit=0;
        for (int i=0; i<x; i++)
        {

            int y= 0 + rand() % (( 1 + 1 ) - 0);;
            if (y>0.5)
                bits[i]=1;
            else
                bits[i]=0;


        }
    }

};
static chromosome* population;

void buildPop (int s)
{


    population= new chromosome[s] ();
    for (int i=0; i<s; i++)
    {
        population[i].setch(s/4);
    }
}

void fitness(chromosome* x)
{
    double tempv=0;
    int tempw=0;
    for(int i=0; i<sz; i++)
    {
        if(x->bits[i]==1)
        {
            tempv+=original[i].value;
            tempw+=original[i].weight;
        }

    }

    if (tempw>MAXW)
        tempv=1/tempv;
    x->fit=tempv;
    x->w=tempw;


}


pair <int, int>* selection (chromosome*p)
{
    double cummf=0,p1,p2;
    double cumRange[pn+1];
    cumRange[0]=0;
    pairsn=pn/2;
    for (int i=0; i<pn; i++)
    {
        cummf+=p[i].fit;
        cumRange[i+1]=p[i].fit+cumRange[i];

    }

    if (pn%2 !=0)
        pairsn+=1;
    pair <int, int>* pa= new pair<int, int> [pairsn];


    for(int i=0; i<pairsn; i++)
    {

        p1=  ((double) rand()*(cummf-0)/(double)RAND_MAX-0);
        p2=((double) rand()*(cummf-0)/(double)RAND_MAX-0);
        pair<int, int> p;
        for (int i=0; i<pn+1; i++)
        {
            if(p1>=cumRange[i]&& p1<cumRange[i+1])
            {
                p.first=i;
                break;
            }
        }
        for (int i=0; i<pn+1; i++)
        {
            if(p2>=cumRange[i]&& p2<cumRange[i+1])
            {
                p.second=i;
                break;
            }
        }
        pa [i].first=p.first;
        pa[i].second=p.second;
    }
    return pa;
}

void crossover (pair <int, int>* x, chromosome* p)
{
    chromosome p1,p2,c1,c2;
    p1.setch(sz);
    p2.setch(sz);
    c1.setch(sz);
    c2.setch(sz);

    double pc=0.6, r;
    int l,counter=0, j=0;

    for (int i=0; i<pairsn; i++)
    {
        for (int k=0; k<sz; k++)
        {
            p1.bits[k]=p[x[i].first].bits[k];
            p2.bits[k]=p[x[i].second].bits[k];
        }

        r=((double) rand()*(1-0)/(double)RAND_MAX-0);
        if (r<=pc)
        {
            l=( rand()*(sz-1)/RAND_MAX-1);
            for ( j; j<l; j++)
            {
                c1.bits[j]=p2.bits[j];
                c2.bits[j]=p1.bits[j];
            }
            for (j; j<sz; j++)
            {
                c1.bits[j]=p1.bits[j];
                c2.bits[j]=p2.bits[j];
            }
        }
        else
        {
            for (int k=0; k<sz; k++)
            {
                c1.bits[k]=p1.bits[k];
                c2.bits[k]=p2.bits[k];
            }
        }

            for (int y=0; y<sz; y++)
            {
                p[counter].bits[y]=c1.bits[y];
            }
            for (int y=0; y<sz; y++)
            {
                p[counter+1].bits[y]=c2.bits[y];
            }
        counter+2;
        j=0;
    }
}

void mutation (chromosome* p)
{
    double pm= 0.00001,r;

    for (int i=0; i<pn; i++)
    {
        for (int j=0; j<sz; j++)
        {
            r=((double) rand()*(1-0)/(double)RAND_MAX-0);
            if (r<=pm)
                p[i].bits[j]=!p[i].bits[j];
        }
    }
}

int findop (chromosome* p)
{
    for(int i=0; i<pn; i++)
    {
        fitness(&p[i]);
    }
    int mx=-1;

    for (int i=0; i<pn; i++)
    {
        if(p[i].fit<1)
            continue;
        if(p[i].fit>mx)
        {
            mx=p[i].fit;

        }
    }

    return mx;
}

int testcase ()
{

    cin>>sz>>MAXW;
    pn=sz*4;
    buildPop(pn);
    original=new Gen[sz];
    int y,l;
    Gen m;
    for (int i=0; i<sz; i++)
    {
        cin>>y>>l;
        m.setGen(y,l);
        original[i]=m;
    }
    for(int i=0; i<pn; i++)
    {

        fitness(&population[i]);

    }
    pair <int, int> * parents;
    for(int i=0; i<sz*20; i++)
    {

        parents=selection(population);
        crossover(parents, population);
        mutation(population);
    }

    int r=findop(population);
    return r;
}

int main()

{

    srand(time(NULL));
    int cases;
    cin>>cases;
    int answers [cases];

    for( int i=0; i<cases; i++)
    {
        answers[i]= testcase();

    }
    for (int i=0; i<cases; i++ )
    {
        cout<<"case "<<i+1<<" : "<<answers[i]<<endl;
    }
    system("pause");
    return 0;
}

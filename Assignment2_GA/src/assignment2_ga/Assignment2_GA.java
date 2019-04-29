import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;
import static java.lang.Math.pow;
import java.util.ArrayList;

class Chromosome {
    double error;
    ArrayList<Double> genes = new ArrayList<Double>();
}

class Points {
    double x;
    double y;
    public Points(double X, double Y)
    {
        x = X;
        y = Y;
    }
}

class Sortbenefits implements Comparator<Chromosome> {

    @Override
    public int compare(Chromosome x,Chromosome y) {
        if(x.error<y.error)
            return -1;
        else if(x.error>y.error)
            return 1;
        else
            return 0;
    }
}

public class Assignment2_GA{
    static ArrayList<Points> points = new ArrayList<>();
    static int numberofiterations = 100;
    static int numoftestcases;
    static int noofpoints;
    static int degree;

    public static ArrayList<Chromosome> createPopulation(int degreee) {
        int numOfPopoulation = 1000;
        ArrayList<Chromosome> population = new ArrayList<>();

        for (int i = 0; i < numOfPopoulation; i++) {
            Chromosome chromosome = new Chromosome();
            for (int j = 0; j < degreee; j++) {
                double randnum = (-10) + (Math.random()) * 10;
                chromosome.genes.add(randnum);
            }
            population.add(chromosome);
        }
        return population;
    }

    public static ArrayList<Chromosome> fitness(ArrayList<Chromosome> p, ArrayList<Points> s) {
        for (int i = 0; i < p.size(); i++) {
            double mean = 0;
            for (int j = 0; j < s.size(); j++) {
                double ycalc = 0.0;
                for (int k = 0; k < p.get(i).genes.size(); k++) {
                    ycalc += (p.get(i).genes.get(k) * pow(s.get(j).x, k));
                }
                mean += pow((ycalc - s.get(j).y), 2);
            }
            p.get(i).error = (mean / s.size());
        }
        return p;
    }

    public static ArrayList<Chromosome> selectNewGeneration(double totalerrors, ArrayList<Chromosome> pop) {
        ArrayList<Chromosome> newPop = new ArrayList<>();
        for (int j = 0; j < pop.size(); j++) {
            double rand = (Math.random()) * totalerrors;
            //System.out.println("the random "+randomnumber);
            double combenefit = 0;
            for (int i = 0; i < pop.size(); i++) {
                combenefit += (1.0 / pop.get(i).error);
                if (combenefit >= rand) {
                    Chromosome newChromosome = new Chromosome();
                    newChromosome.genes = pop.get(i).genes;
                    newChromosome.error = pop.get(i).error;
                    newPop.add(newChromosome);
                    break;
                }
            }
        }
        return newPop;
    }

    public static ArrayList<Chromosome> crossOver(ArrayList<Chromosome> newPopulation,int currentgeneration) {
        ArrayList<Chromosome> oldgeneration = newPopulation;
        ArrayList<Chromosome> newgeneration = new ArrayList<>();
        for (int i = 0; i < oldgeneration.size() - 1; i += 2) {
            Chromosome c1 = new Chromosome(), c2 = new Chromosome();
            double randomnumber = 0 + (Math.random()) * 1;
            if (randomnumber < 0.7) {
                int crossoverpoint = 1 + (int) (Math.random()) * (degree);
                for (int m = 0; m <= crossoverpoint; m++) {
                    c1.genes.add(oldgeneration.get(i).genes.get(m));
                    c2.genes.add(oldgeneration.get(i + 1).genes.get(m));
                }
                for (int j = crossoverpoint + 1; j < degree+1; j++) {
                    c1.genes.add(oldgeneration.get(i + 1).genes.get(j));
                    c2.genes.add(oldgeneration.get(i).genes.get(j));
                }
                newgeneration.add(c1);
                newgeneration.add(c2);
            } else {
                newgeneration.add(oldgeneration.get(i));
                newgeneration.add(oldgeneration.get(i + 1));
            }
        }
        newgeneration = Mutation(newgeneration,currentgeneration);
        newgeneration = fitness(newgeneration, points);
        ArrayList<Chromosome> oldnew = new ArrayList<>();
        oldnew.addAll(oldgeneration);
        oldnew.addAll(newgeneration);
        ArrayList<Chromosome> returngeneration = replacement(oldnew, 100);
        return returngeneration;
    }

    public static ArrayList<Chromosome> Mutation(ArrayList<Chromosome> population, int curit) {
        ArrayList<Chromosome> newgenration = new ArrayList<>();
        for (int i = 0; i < population.size(); i++) {
            for (int j = 0; j < population.get(i).genes.size(); j++) {
                double rand = 0 + (Math.random()) * 1;
                if (rand < 0.01) {
                    double randomnum = 0 + (Math.random()) * 1;
                    if (randomnum < 0.5) {
                        double y = population.get(i).genes.get(j) + 10;
                        randomnum = 0 + (Math.random()) * 1;
                        double am = y * (1 - pow(randomnum, (1 - (curit / numberofiterations))));
                        population.get(i).genes.set(j, (population.get(i).genes.get(j) - am));
                    } else {
                        double y = 10 - population.get(i).genes.get(j);
                        randomnum = 0 + (Math.random()) * 1;
                        double am = y * (1 - pow(randomnum, (1 - (curit / numberofiterations))));
                        population.get(i).genes.set(j, (population.get(i).genes.get(j) + am));
                    }
                }
            }
            newgenration.add( population.get(i));
        }
        return newgenration;
    }


    public static ArrayList<Chromosome> replacement(ArrayList<Chromosome> population,int numOfPop){
            Collections.sort(population,new Sortbenefits());
            ArrayList<Chromosome> oldnew=new ArrayList<>();
            for(int i=0;i<numOfPop;i++){
                oldnew.add(population.get(i));
            }
            return  oldnew;
    }
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("C:\\Users\\Belal\\Desktop\\input.txt");
        Scanner scanner = new Scanner(file);
        ArrayList<Chromosome> pop = new ArrayList<>();
        numoftestcases = scanner.nextInt();
        double x, y;
        while (numoftestcases > 0) {
            noofpoints = scanner.nextInt();
            degree = scanner.nextInt();
            points=new ArrayList<>();
            for (int i = 0; i < noofpoints; i++) {
                //create pair and push them
                x = scanner.nextDouble();
                y = scanner.nextDouble();
                Points p = new Points(x, y);
                points.add(p);
            }
            pop = createPopulation(degree+1);
            int cot =1;
            while(cot <= numberofiterations){
                pop = fitness(pop,points);
                double totalerror=0;
                for(int i=0;i<pop.size();i++){
                    totalerror+= (1.0/pop.get(i).error);
                }
                int currentgeneration;
                pop = selectNewGeneration(totalerror,pop);
                pop = crossOver(pop,cot);
                cot ++;
            }
            System.out.println(pop.get(0).genes+" Error "+pop.get(0).error);  
            numoftestcases --;
          
        }
    }
}

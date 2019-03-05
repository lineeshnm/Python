import java.util.*;

 // A directed graph using
// adjacency list representation
class Graph {

    // No. of vertices in graph
    private int v;

    // adjacency list
    private ArrayList<Integer>[] adjList;

    //Constructor
    public Graph(int vertices) {

        //initialise vertex count
        this.v = vertices;

        // initialise adjacency list
        initAdjList();
    }

    // utility method to initialise
    // adjacency list
    @SuppressWarnings("unchecked")
    private void initAdjList() {
        adjList = new ArrayList[v];

        for (int i = 0; i < v; i++) {
            adjList[i] = new ArrayList<>();
        }
    }

    // add edge from u to v
    public void addEdge(int u, int v) {
        // Add v to u's list.
        adjList[u].add(v);
    }

    public ArrayList<Integer> getAdjList(int u) {
        return adjList[u];
    }

    // Prints all paths from
    // 's' to 'd'
    public List<List<Integer>> printAllPaths(int s, int d) {
        boolean[] isVisited = new boolean[v];
        List<Integer> pathList = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();

        //add source to path[]
        pathList.add(s);

        //Call recursive utility
        printAllPathsUtil(s, d, isVisited, pathList,result);
        return result;
    }

    // A recursive function to print
    // all paths from 'u' to 'd'.
    // isVisited[] keeps track of
    // vertices in current path.
    // localPathList<> stores actual
    // vertices in the current path
    private void printAllPathsUtil(Integer u, Integer d,
                                   boolean[] isVisited,
                                   List<Integer> localPathList, List<List<Integer>> result) {

        // Mark the current node
        isVisited[u] = true;

        if (u.equals(d)) {
            //System.out.println(localPathList);
            result.add(new ArrayList<Integer>(){{addAll(localPathList);}});
        }

        // Recur for all the vertices
        // adjacent to current vertex
        for (Integer i : adjList[u]) {
            if (!isVisited[i]) {
                // store current node
                // in path[]
                localPathList.add(i);
                printAllPathsUtil(i, d, isVisited, localPathList, result);

                // remove current node
                // in path[]
                localPathList.remove(i);
            }
        }

        // Mark the current node
        isVisited[u] = false;
    }
}


class Tree {

    private int i;
    private Point p;
    private int m;
    private int t;
    private double w;

    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }

    public double getW() {
        return w;
    }

    public void setW(double w) {
        this.w = w;
    }

    public Point getP() {
        return p;
    }

    public void setP(Point p) {
        this.p = p;
    }

    public int getM() {
        return m;
    }

    public void setM(int m) {
        this.m = m;
    }

    public int getT() {
        return t;
    }

    public void setT(int t) {
        this.t = t;
    }

    public Tree(long x, long y, int m, int t, int i) {
        this.p = new Point (x, y);
        this.m = m;
        this.t = t;
        this.i=i;
    }

    @Override
    public String toString() {
        return "Tree{" +
                "i=" + i +
                ", p=" + p +
                ", m=" + m +
                ", t=" + t +
                ", w=" + w +
                '}';
    }
}

class Point {
    private long x;
    private long y;

    public Point(long x, long y) {
        this.x = x;
        this.y = y;
    }

    public long getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public long getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    Double distFrom(Point p) {
        return Math.sqrt((this.getX()-p.getX())*(this.getX()-p.getX()) + (this.getY()-p.getY())*(this.getY()-p.getY()));
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}

class Dinic {
    private  int N;
    private int INF = 1 << 29;
    private int[] eadj, eprev, elast;
    private int eidx;
    private int[] flow, capa, now;

    public void init(int _N, int M) {
        N = _N;
        eadj = new int[M];
        eprev = new int[M];
        elast = new int[N];
        flow = new int[M];
        capa = new int[M];
        now = new int[N];
        level = new int[N];
        eidx = 0;
        Arrays.fill(elast, -1);
    }

    public void add_edge(int a, int b, int c, int c2) {
        //System.out.print(eidx+ " ");
        eadj[eidx] = b; flow[eidx] = 0; capa[eidx] = c; eprev[eidx] = elast[a]; elast[a] = eidx++;
        eadj[eidx] = a; flow[eidx] = 0; capa[eidx] = c2; eprev[eidx] = elast[b]; elast[b] = eidx++;
    }

    public int dinic(int source, int sink) {
        int res, flow = 0;
        while (bfs(source, sink)) { // see if there is an augmenting path
            System.arraycopy(elast, 0, now, 0, N);
            while ((res = dfs(source, INF, sink)) > 0)
                // push all possible flow through
                flow += res;
        }
        return flow;
    }

    private int[] level;

    private boolean bfs(int source, int sink) {
        Arrays.fill(level, -1);
        int front = 0, back = 0;
        int[] queue = new int[N];
        level[source] = 0;
        queue[back++] = source;
        while (front < back && level[sink] == -1) {
            int node = queue[front++];
            for (int e = elast[node]; e != -1; e = eprev[e]) {
                int to = eadj[e];
                if (level[to] == -1 && flow[e] < capa[e]) {
                    level[to] = level[node] + 1;
                    queue[back++] = to;
                }
            }
        }

        return level[sink] != -1;
    }

    private int dfs(int cur, int curflow, int goal) {
        if (cur == goal)
            return curflow;

        for (int e = now[cur]; e != -1; now[cur] = e = eprev[e]) {
            if (level[eadj[e]] > level[cur] && flow[e] < capa[e]) {
                int res = dfs(eadj[e], Math.min(curflow, capa[e] - flow[e]), goal);
                if (res > 0) {
                    flow[e] += res;
                    flow[e ^ 1] -= res;
                    return res;
                }
            }
        }
        return 0;
    }
}

public class CandidateCode {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 1<=N<=200
        Double C = sc.nextDouble(); // 0 <=C<=100000
        List<Tree> trees = new ArrayList<>();
        int no_solution=0;
        int total_monkeys=0;
        int weak_tree=-1;
        for (int i = 0; i < N; i++) {
            long x=sc.nextLong(),y=sc.nextLong();
            int m=sc.nextInt(),t=sc.nextInt();
            trees.add(new Tree (x,y,m,t,i));
            total_monkeys=total_monkeys+m;
            if(t < m) {no_solution++;weak_tree=i;}
        }
        if(no_solution>1) {System.out.println("-1");return;}

        int M=0;
        Graph g = new Graph(N);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(Double.compare(trees.get(i).getP().distFrom(trees.get(j).getP()) , C)<=0) {
                    if(i != j) g.addEdge(i,j);
                    M++;
                }
            }

        }

        // for each tree as a destination, find if there is atleast one path between source and destination
        // if not, then print -1 and return

       //for (int i = 0; i < N; i++) {
       //     for (int j = 0; j < N && j!=i; j++) {
       //         if(g.printAllPaths(i,j).isEmpty()) {
       //             System.out.println("-1"); return;
       //         }
       //     }
       // }

        List<Integer> result = new ArrayList<>();

        for(Tree t : trees) {
            if(no_solution == 1 && t.getI() != weak_tree){
                continue;
            }
            Set<String> s = new HashSet<>();
            Dinic d = new Dinic();
            d.init(N+1,2*(M + N-1));

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N && j != i ; j++) {
                    if(s.contains(i+" "+j)) {
                        //System.out.println("skipping i j "+ i + " "+j);
                        continue;
                    }

                    if(Double.compare(trees.get(i).getP().distFrom(trees.get(j).getP()), C)<=0) {

                        d.add_edge(i,j, trees.get(i).getT(), trees.get(j).getT());
                        s.add(i+" "+j);
                        //System.out.println("adding i j "+ i + " "+j);
                    } else if(g.printAllPaths(i,j).isEmpty() && trees.get(i).getM() > 0 && trees.get(j).getM() > 0) {
                        System.out.println("-1");return;
                    }
                }
            }


            //Imaginary Source
            for (int i = 0; i < N; i++) {
                if (t.getI() != i) d.add_edge(N, i, 1<<9, 0);
            }
            int dMaxFlow = d.dinic(N,t.getI());
            //System.out.println("For tree ="+t.getI()+" dinic="+dMaxFlow);

            if(dMaxFlow+t.getM() >= total_monkeys) {
                result.add(t.getI());
            }
        }

        if(result.isEmpty()) {
            System.out.println("-1");
            return;
        }
        else {
            StringBuffer sb =new StringBuffer();
            for (int i:result) {
                sb.append(i);
                sb.append(" ");
            }
            System.out.println(sb.toString().trim());
        }
    }
}


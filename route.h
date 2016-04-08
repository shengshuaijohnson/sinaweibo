
#ifndef __ROUTE_H__
#define __ROUTE_H__
typedef struct mnode node;
typedef struct QueueRecord *Queue;
    void MakeEmpty(Queue Q);
    int Succ(int val,int cap);
    void Enqueue(int X,Queue Q);
    int Dequeue(Queue Q);
//void search_route(char *graph[5000], int edge_num, char *condition);
int read_file_topo(char *filename,node*graph);
bool check_route(int begin,int end,node *graph,int *v);
int make_random(node *graph,int pos);
int cost(int begin,int end,node* graph,int*route);
#endif

//队列相关操作
struct QueueRecord
{
    int Capacity;
    int Front;
    int Rear;
    int Size;
    int EleArray[300];
};

void MakeEmpty(Queue Q){
    Q->Capacity=200;
    Q->Size=0;
    Q->Front=1;
    Q->Rear=0;
}
int Succ(int val,int cap)
{
    if (++val==cap)  val=0;
    return val;
}
void Enqueue(int X,Queue Q){
    Q->Size++;
    Q->Rear=Succ(Q->Rear,Q->Capacity);
    Q->EleArray[Q->Rear]=X;
    return;
}
int Dequeue(Queue Q){
    int x=Q->EleArray[Q->Front];
    Q->Size--;
    Q->Front=Succ(Q->Front,Q->Capacity);
    return x;
}


//图节点
struct  mnode
{
    int out_num=0;//储存出点的数量
    int in_num=0;//储存入点数量
    int to_point[8];//储存目标端点
    int from_point[20];//储存前驱顶点
    int line[8];//储存边
    float cost[8];
    int weight=100; //权重
    int kind=0;//1表示为A或B类
};



int read_file_topo(const char * const filename,node graph[600])
{
    FILE* fp;
    int num;
    int cnt=0;
    int index,from,to,cost,out;
    char c1,c2,c3;
    fp=fopen(filename,"r");
    num=0;
    while(!feof(fp))
    {
    fscanf(fp,"%d %c %d %c %d %c %d",&index,&c1,&from,&c2,&to,&c3,&cost);//第一个是边的index,第二个是起点，第三个是终点，第四个是路径花费
    if(from>num)  num=from;
    if(to>num)    num=to;
    out=graph[from].out_num;
    graph[from].to_point[out]=to;
    graph[to].from_point[graph[to].in_num++]=from;
    graph[from].line[out]=index;
    graph[from].cost[out]=cost;
    graph[from].out_num++;
    graph[to].weight+=(20-cost);//初步加权
    cnt++;
    }
    graph[555].weight=num+1;
    fclose(fp);
    return cnt;
}
//随机函数
static unsigned long Seed =1;
#define A 48271L
#define M 2147483647L
#define Q (M/A)
#define R (M%A)
double Random(void)
{
    long TmpSeed;
    TmpSeed=A*(Seed%Q)-R*(Seed/Q);
    if(TmpSeed>=0)
        Seed = TmpSeed;
    else
        Seed = TmpSeed+M;
return (double) Seed/M;
}
//加权随机，具体权重变化在寻址过程中还需更多考虑
int make_random(node *graph,int pos)
{
    int sum,tmp;
    int i,x;
    x=graph[pos].out_num;
    if(x==1) return graph[pos].to_point[0];
    for(i=0,sum=0;i<x;i++)
    {

        sum+=graph[graph[pos].to_point[i]].weight;
    }
    tmp=(int)((double)sum*(Random()));
    for(i=0,sum=0;i<x;i++)
    {
        sum+=graph[graph[pos].to_point[i]].weight;
        if(sum>=tmp) break;   
    }

    return graph[pos].to_point[i];
}
//下面是对V'中的点分三类，(算上AB是四类)
void check_a(node* graph,int * type,int begin,int *v)
{
    Queue q;
    int i,j,to,p;
    int flag[600];
    for(i=0;i<600;i++) flag[i]=0;
    q=(Queue)malloc(sizeof(struct QueueRecord));
    MakeEmpty(q);
    Enqueue(begin,q);
    flag[begin]=55;
    while(q->Size!=0)
    {
        p=Dequeue(q);
        for(i=0;i<graph[p].out_num;i++){

            to=graph[p].to_point[i];
            if(flag[to]==55) continue;
            for(j=0;j<v[55];j++)
            {
                if(v[j]==to) {type[type[55]++]=to;flag[to]=55;graph[to].kind=1;break;}
            }
            if(j==v[55]) {Enqueue(to,q);flag[to]=55;}
        }
    
    }

    return;

}
void check_b(node* graph,int *type,int end,int *v)
{   
    Queue q;
    int flag[600];
    int i,j,from,p;
    for(i=0;i<600;i++) flag[i]=0;
    q=(Queue)malloc(sizeof(struct QueueRecord));
    MakeEmpty(q);
    Enqueue(end,q);
    flag[end]=55;//55代表走过?

    while(q->Size!=0)
    {
        p=Dequeue(q);
        for(i=0;i<graph[p].in_num;i++){
            from=graph[p].from_point[i];
            if (flag[from]==55) {continue;}
            for(j=0;j<v[55];j++)
            {
                if(v[j]==from) {type[type[55]++]=from;flag[from]=55;graph[from].kind=1;break;}
            }
            if(j==v[55]) {Enqueue(from,q);flag[from]=55;}
           

        }
    }
    return;
}
//
bool check_route(int begin,int end,int *route,int *v,node* graph)
{
    int i,j,tmp;
    i=50;
    j=v[55];
    if (graph[begin].kind>0)   j--;
    tmp=begin;
    while(i--)
    {
        tmp=route[tmp];
        if (graph[tmp].kind>0)  j--;
        if (tmp==end&&(j==0)) return true;
        if(tmp==end&&(j!=0))  return false;
    }
    return false;
}
int cost(int begin,int end,node* graph,int*route)
{
    int tmp,i,j;
    int val=0;
    for(i=begin;i!=end;i=route[i])
    {
        j=route[i];
        for(tmp=0;tmp<graph[i].out_num;tmp++)
        {
            if (graph[i].to_point[tmp]==j)
            {   

                val+=graph[i].cost[tmp];
            }
        }
    }
    return val;
}
//在两点间路径合法的情况下，计算返回cost值